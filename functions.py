from urllib.request import urlopen
import json


class Query:

    def __init__(self, mode, users_count, user_id, country):
        self.mode = mode
        self.users_count = users_count
        self.user_id = user_id
        self.country = country

    def get_json(self):

        with open('lib/temp.json') as infile:
            data = json.load(infile)

            cursor = 0
            for p in data['leaderboard']:
                if cursor != self.users_count:  # NEEDS REWRITING FOR MORE THAN 20 USERS
                    cursor += 1

                    print('name: ' + p['name'])
                    print('country: ' + p['country'])
                    print('match_type: ' + str(p['match_type']))
                    print('rating: ' + p['rating'])
                    print('rank_tier: ' + str(p['rank_tier']))
                    print('rank_position: ' + str(p['rank_position']))
                    print('match_count: ' + str(p['match_count']))
                    print('match_wins: ' + str(p['match_wins']) + '\n')

    def parse(self, url):
        info = urlopen(url)
        result = json.loads(info.read())

        # write data into file
        with open('lib/temp.json', 'w') as outfile:
            json.dump(result, outfile)

        # print edited data
        self.get_json()
