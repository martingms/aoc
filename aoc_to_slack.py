#!/usr/bin/env python3

from datetime import date, datetime
from operator import itemgetter
import sys

import pytz
import requests
from slackclient import SlackClient


def parse_ts(ts):
    return datetime.fromtimestamp(int(ts), tz=local_tz)


def get_aoc_stats(leaderboard_id, session_cookie):
    url = 'http://adventofcode.com/2018/leaderboard/private/view/{}.json'\
            .format(leaderboard_id)

    r = requests.get(url, cookies={
        'session': session_cookie
    })
    r.raise_for_status()

    return r.json()


def format_message(stats):
    today = date.today().day

    members = []
    for member in stats['members'].values():
        member = {
            **member,
            'name': member['name'] or 'ANON #{}'.format(member['id']),
            'star_ts': { '1': None, '2':None }
        }
        try:
            completion_today = member['completion_day_level'][str(today)]
        except KeyError:
            pass
        else:
            for star in ('1', '2'):
                member['star_ts'][star] = parse_ts(
                    completion_today[star]['get_star_ts']
                )

        members.append(member)


    lines = [
        '*:santa: Advent of Code {} :santa:*\n'.format(stats['event']),
        '*Leaderboard:*',
    ]

    # Score
    for i, member in enumerate(sorted(members, key=itemgetter('local_score'), reverse=True)):
        lines.append('*{pos}*  {name}: {score} (:star: x {stars})'.format(
            pos=i + 1,
            name=member['name'],
            score=member['local_score'] or 0,
            stars=member['stars']
        ))

    lines.append('\n')

    # Star top threes
    for star in ('1', '2'):

        top = sorted(
            (m for m in members if m['star_ts'][star] is not None),
            key=lambda m: m['star_ts'][star],
        )[:3]

        if not top:
            lines.append(f'*No one has finished :star: #{star} today :face_with_rolling_eyes:*')
            continue

        lines.append(f'*Todays top {len(top)} for :star: #{star}:*')

        for i, member in enumerate(top):
            lines.append('*{pos}*  {name}: {ts}'.format(
                pos=i + 1,
                name=member['name'],
                ts=member['star_ts'][star],
            ))

        lines.append('\n')

    return '\n'.join(lines)


def post_to_slack(api_token, channel, msg):
    sc = SlackClient(api_token)

    sc.api_call(
        'chat.postMessage',
        channel=channel,
        text=msg
    )

usage_str = '''\
usage: ./aoc_to_slack.py SLACK_API_TOKEN SLACK_CHANNEL AOC_ID AOC_COOKIE TZ'\
'''

if len(sys.argv) != 6:
    print(usage_str, file=sys.stderr)
    sys.exit(1)

local_tz = pytz.timezone(sys.argv[5])

msg = format_message(get_aoc_stats(sys.argv[3], sys.argv[4]))
post_to_slack(sys.argv[1], sys.argv[2], msg)
