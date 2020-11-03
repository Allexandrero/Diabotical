from urllib.request import urlopen
import json

import lib.config as cfg


class Query:

    def __init__(self, mode, users_count, user_id, country, offset):
        self.mode = mode
        self.users_count = users_count
        self.user_id = user_id
        self.country = country
        self.offset = offset

    def get_json(self):

        with open('lib/temp.json') as infile:
            data = json.load(infile)

            # getting certain leaderboard parameters
            cursor = 0
            for p in data['leaderboard']:
                if cursor < self.users_count:

                    cursor += 1

                    print('name: ' + p['name'])
                    print('country: ' + p['country'])
                    print('match_type: ' + str(p['match_type']))
                    print('rating: ' + p['rating'])
                    print('rank_tier: ' + str(p['rank_tier']))
                    print('rank_position: ' + str(p['rank_position']))
                    print('match_count: ' + str(p['match_count']))
                    print('match_wins: ' + str(p['match_wins']) + '\n')

            if self.users_count > 20:
                self.offset += 20
                self.users_count -= 20
                self.parse(cfg.url_leaderboard + str(self.offset))

    def parse(self, url):

        info = urlopen(url)
        result = json.loads(info.read())

        # write data into file
        with open('lib/temp.json', 'w') as outfile:
            json.dump(result, outfile)

        # print edited data
        self.get_json()
