from urllib.request import urlopen
import json


# Reformat Json info for comfortable reading
def getJson():
    with open('temp.json') as infile:
        data = json.load(infile)
        for p in data['leaderboard']:
            print('name: ' + p['name'])
            print('country: ' + p['country'])
            print('match_type: ' + str(p['match_type']))
            print('rating: ' + p['rating'])
            print('rank_tier: ' + str(p['rank_tier']))
            print('rank_position: ' + str(p['rank_position']))
            print('match_count: ' + str(p['match_count']))
            print('match_wins: ' + str(p['match_wins']) + '\n')


def parse(url):
    info = urlopen(url)
    result = json.loads(info.read())

    # write data into file
    with open('temp.json', 'w') as outfile:
        json.dump(result, outfile)

    # print edited data
    getJson()


# def fetchWebData(url):
    # info = urlopen(url)
    # result = json.loads(info.read())

    # return json.loads(urlopen(url).read())
