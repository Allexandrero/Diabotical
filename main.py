import sys
import argparse

from functions import Query as q
import lib.config as cfg


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--mode', nargs='?', type=str)
    parser.add_argument('-c', '--count', nargs='?', type=int)
    parser.add_argument('-u', '--user_id', nargs='?', type=str)
    parser.add_argument('-y', '--country', nargs='?', type=str)

    return parser


if __name__ == '__main__':

    parser = create_parser()
    my = parser.parse_args(sys.argv[1:])

    # print(namespace.user_id)
    query = q(my.mode, my.count, my.user_id, my.country, cfg.basic_offset)

    if my.user_id is not None:
        q.parse(query, cfg.url_user_id + query.user_id)
    elif my.country is not None:
        q.parse(query, cfg.url_country + str(query.offset))
    elif my.mode is not None:
        q.parse(query, cfg.url_leaderboard + str(query.offset))
    else:
        print(cfg.err_no_attr)

    """for param in sys.argv:
        print(param)
"""
    """user_query = input('>> ')

    temp = f.Query('leaderboard', 10, 'Jamaco225', 'USA')

    temp.parse(cfg.url_leaderboard + user_query)"""


