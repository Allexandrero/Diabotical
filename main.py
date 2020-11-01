import sys

import functions as f
import lib.config as cfg


if __name__ == '__main__':
    for param in sys.argv:
        print(param)

    user_query = input('>> ')

    temp = f.Query('leaderboard', 10, 'Jamaco225', 'USA')

    temp.parse(cfg.url_leaderboard + user_query)


