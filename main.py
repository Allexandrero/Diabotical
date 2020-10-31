from urllib.request import urlopen
import json
import functions as f


def fetch(url):
    info = urlopen(url)
    result = json.loads(info.read())


def parse(url):
    info = urlopen(url)
    result = json.loads(info.read())

    # write data into file
    with open('temp.json', 'w') as outfile:
        json.dump(result, outfile)

    # print edited data
    f.getJson()


if __name__ == '__main__':
    print('Enter the amount of users you would like to know about: ')

    f.parse('https://www.diabotical.com/api/v0/stats/leaderboard?mode=r_macguffin&offset=0')
    f.parse('https://www.diabotical.com/api/v0/stats/leaderboard?mode=r_macguffin&offset=19')

    # print("OZOZO" + f.fetchWebData('https://www.diabotical.com/api/v0/stats/leaderboard?mode=r_macguffin&offset=0'))

# curl -X GET "https://www.diabotical.com/api/v0/stats/leaderboard?mode=r_macguffin&offset=0" -H  "accept: */*"
# curl -X GET "https://www.diabotical.com/api/v0/users/9a1c62de13ef40d69442a891b55a21fb/leaderboard" -H  "accept: */*"
#
