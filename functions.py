from urllib.request import urlopen
import json

import lib.config as cfg
import decorators as now


class Query:

    def __init__(self, mode, count, user_id, country, offset, counter):
        self.mode = mode
        self.count = count
        self.user_id = user_id
        self.country = country
        self.offset = offset
        self.counter = counter

    @now.sleep(1)  # needed in case of avoiding Too_Much_Requests error
    def get_json(self):

        with open('lib/temp.json') as infile:
            data = json.load(infile)

            # getting certain leaderboard parameters
            cursor = 0

            if not cfg.message:  # Just annotation that module has started his job
                cfg.message = True
                print('\nParsing leaderboard for ' + self.mode + ' mode. Please wait...\n')

            for p in data['leaderboard']:
                if cursor < self.count:
                    cursor += 1

                    print('name: ' + p['name'])
                    print('country: ' + p['country'])
                    print('match_type: ' + str(p['match_type']))
                    print('rating: ' + p['rating'])
                    print('rank_tier: ' + str(p['rank_tier']))
                    print('rank_position: ' + str(p['rank_position']))
                    print('match_count: ' + str(p['match_count']))
                    print('match_wins: ' + str(p['match_wins']) + '\n')

            if self.count > 20:
                self.offset += 20
                self.count -= 20
                self.parse(cfg.url_leaderboard + str(self.offset))

    @now.sleep(1)  # needed in case of avoiding Too_Much_Requests error
    def get_json_by_user_id(self):

        with open('lib/temp.json') as infile:
            data = {'user_id': [json.load(infile)]}

            # getting parameters about user by user_id
            cursor = 0
            for p in data['user_id']:
                if cursor < self.count:
                    cursor += 1

                    print('\nInformation about user ' + self.user_id + ':\n')
                    print('name: ' + p['name'])
                    print('country: ' + p['country'])
                    print('avatar: ' + p['avatar'])
                    print('customizations: ' + str(p['customizations']))
                    print('level: ' + str(p['level']))
                    print('active_battlepass_id: ' + p['active_battlepass_id'])
                    print('battlepass_owned: ' + str(p['battlepass_owned']))
                    print('battlepass_xp: ' + str(p['battlepass_xp']))
                    print('battlepass_level: ' + str(p['battlepass_level']) + '\n')

    @now.sleep(1)  # needed in case of avoiding Too_Much_Requests error
    def get_json_by_country(self, counter):

        with open('lib/temp.json') as infile:
            data = json.load(infile)

            if str(data['leaderboard']) == '[]':
                print('Finished. The amount of ' + str(self.country) + ' users is ' + str(counter))
                return
            else:
                if not cfg.message:  # Just annotation that module has started his job
                    cfg.message = True
                    print('Counting ' + str(self.country) + ' users. Please wait...')

                cursor = 0
                for p in data['leaderboard']:
                    if self.country == p['country']:
                        cursor += 1
                        counter += 1

                # Keeps parsing until there is no more data
                self.offset += 20
                cfg.basic_counter = counter
                self.parse(cfg.url_country + str(self.offset))

    def define_gamemode(self, mode):
        if mode == 'mcguffin':
            return
        elif mode == 'ffa':
            return
        elif mode == 'ca':
            return
        elif mode == 'rocket_arena':
            return
        elif mode == 'shaft_arena':
            return
        elif mode == 'wipeout':
            return
        else:
            print('ERROR. Game mode incorrect')

    def parse(self, url):

        info = urlopen(url)
        result = json.loads(info.read())

        # write data into file
        with open('lib/temp.json', 'w') as outfile:
            json.dump(result, outfile)

        if self.count is None:
            self.count = cfg.basic_count

        # print edited data
        if self.user_id is not None:
            self.get_json_by_user_id()
        elif self.country is not None:
            self.get_json_by_country(cfg.basic_counter)
        elif self.mode == 'macguffin' or 'ffa' or 'ca' or 'rocket_arena' or 'shaft_arena' or 'wipeout':
            self.get_json()
        else:
            print('[ERROR] Game mode incorrect')
