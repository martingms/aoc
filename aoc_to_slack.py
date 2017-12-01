#!/usr/bin/env python3

from operator import itemgetter
import sys

import requests
from slackclient import SlackClient

def get_aoc_stats(leaderboard_id, session_cookie):
    url = 'http://adventofcode.com/2017/leaderboard/private/view/{}.json'\
            .format(leaderboard_id)

    r = requests.get(url, cookies={
        'session': session_cookie
    })
    r.raise_for_status()

    return r.json()


def format_message(stats):
    lines = ['*:santa: Advent of Code 2017 :santa: - Blank leaderboard*\n']

    members = sorted(stats['members'].values(), key=itemgetter('local_score'),
            reverse=True)

    for i, member in enumerate(members):
        lines.append('*{pos}*  {name}: {score} ({stars} stars)'.format(
            pos=i + 1,
            name=member['name'] or 'ANON',
            score=member['local_score'] or 0,
            stars=member['stars']
        ))

    return '\n'.join(lines)


def post_to_slack(api_token, channel, msg):
    sc = SlackClient(api_token)

    sc.api_call(
        'chat.postMessage',
        channel=channel,
        text=msg
    )

usage_str = '''
usage: ./aoc_to_slack.py SLACK_API_TOKEN SLACK_CHANNEL AOC_ID AOC_COOKIE'
'''

if len(sys.argv) != 5:
    print(usage_str, file=sys.stderr)
    sys.exit(1)

msg = format_message(get_aoc_stats(sys.argv[3], sys.argv[4]))
post_to_slack(sys.argv[1], sys.argv[2], msg)
