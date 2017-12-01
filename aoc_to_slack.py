#!/usr/bin/env python3

from datetime import date, datetime
from operator import itemgetter
import sys

import pytz
import requests
from slackclient import SlackClient


def _parse_ts(ts):
    return datetime.strptime(ts, '%Y-%m-%dT%H:%M:%S%z').astimezone(local_tz)


def get_aoc_stats(leaderboard_id, session_cookie):
    url = 'http://adventofcode.com/2017/leaderboard/private/view/{}.json'\
            .format(leaderboard_id)

    r = requests.get(url, cookies={
        'session': session_cookie
    })
    r.raise_for_status()

    return r.json()


def format_message(stats):
    lines = ['*:santa: Advent of Code 2017 :santa:*\n']

    members = sorted(stats['members'].values(), key=itemgetter('local_score'),
            reverse=True)

    today = date.today().day
    early_bird = None

    for i, member in enumerate(members):
        name = member['name'] or 'ANON #{}'.format(member['id'])
        lines.append('*{pos}*  {name}: {score} (:star: x {stars})'.format(
            pos=i + 1,
            name=name,
            score=member['local_score'] or 0,
            stars=member['stars']
        ))

        last_star_ts = _parse_ts(member['last_star_ts'])

        try:
            member_today = member['completion_day_level'][str(today)]
            first_star_ts = _parse_ts(member_today['1']['get_star_ts'])
        except KeyError:
            continue

        if early_bird is None or first_star_ts < early_bird[1]:
            early_bird = (name, first_star_ts)

    if early_bird is not None:
        lines.append(
            '\nTodays first :star::  :crown: *{name}* :crown:, at {time}!'.format(
                name=early_bird[0],
                time=early_bird[1].time().isoformat()
            )
        )
    else:
        lines.append('No :star: earned so far today :face_with_rolling_eyes:')

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
