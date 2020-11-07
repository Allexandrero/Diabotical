import sys
import argparse

from app import functions
from app.functions import Query as q
import lib.config as cfg


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--mode', nargs='?', type=str)
    parser.add_argument('-c', '--count', nargs='?', type=int)
    parser.add_argument('-u', '--user_id', nargs='?', type=str)
    parser.add_argument('-y', '--country', nargs='?', type=str)
    return parser


if __name__ == '__main__':

    print(str(create_parser()) + 'OLOLOLOLOLOLOLOLOLOLO')

    parser = create_parser()
    my = parser.parse_args(sys.argv[1:])

    # Set counters back to zero
    cfg.basic_counter = 0
    cfg.message = False
    cfg.temp_url = ''

    # Creating request
    query = q(my.mode, my.count, my.user_id, my.country, cfg.basic_offset, cfg.basic_counter)

    # Creating URL. Depends on input arguments
    if my.user_id is not None:
        cfg.temp_url = cfg.url_user_id + query.user_id
        q.parse(query, cfg.temp_url)

    elif my.country is not None:
        cfg.temp_url = cfg.url_country + 'mode=' + str(functions.define_gamemode(query.mode)) + '&offset='
        q.parse(query, cfg.temp_url + str(query.offset))

    elif my.mode is not None:
        cfg.temp_url = cfg.url_leaderboard + 'mode=' + str(functions.define_gamemode(query.mode)) + '&offset='
        q.parse(query, cfg.temp_url + str(query.offset))
    else:
        print(cfg.err_no_attr)




