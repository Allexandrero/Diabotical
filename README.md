# Diabotical Parser

This console application was created as a simple interest in parsing web data from "Diabotical" game.


## Quick start

This app achieves in three tasks:

> Show leaderboards on any game mode (modes list is relevant on November 3, 2020)

```terminal
python main.py --mode macguffin --count 25
```

> Find information about current user ID
```shell
python main.py --mode ffa --user_id 9a1c62de13ef40d69442a891b55a21fb
```

> Count all players of the concrete country
```shell
python main.py --mode rocket_arena --country ru
```

## Usage

1. Download the project
2. Extract the project into preferred directory
3. `cd` (move) into extracted folder via terminal/console
4. write request, dedicated to `main.py` file (as in examples above)

There are 4 different arguments you can choose to customise your requests:
- `--mode` or `-m` to search leaderboards of the chosen game mode;
```shell
python main.py --mode <mode>
```

- `--count` or `-c` to show only amount of users that you need (basic request shows 20 users);
```shell
python main.py --mode <mode> --count N
```

- `--user_id` or `-u` to find information about certain user (you need to have ID of user you want to find);
```shell
python main.py --mode <mode> --count N --user_id <user_id>
```

- `--country` or `-y` to count all users of the chosen country;
```shell
python main.py --mode <mode> --count N --country ru
```

## Attention! 

Parser might  work slowly, because the website, which it takes data from, is limited to the amount of requests!

Also, `count` parameter is unnecessary. you may not use it.
