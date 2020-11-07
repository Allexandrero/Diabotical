import pytest

import main
import functions
import decorators

from lib import test_config


# Tests for main.py
def test_parser_works():
    assert str(main.create_parser()) == test_config.arg_parser, 'Parser error'


# Tests for functions.py
# Testing query initialization
def test_query():
    with pytest.raises(TypeError):
        functions.Query.__init__()


# Checking game modes
def test_macguffin():
    assert functions.define_gamemode('r_macguffin')


def test_ffa():
    assert functions.define_gamemode('ffa') == 'r_ca_1'


def test_ca():
    assert functions.define_gamemode('ca') == 'r_ca_2'


def test_rocket_arena():
    assert functions.define_gamemode('rocket_arena') == 'r_rocket_arena_2'


def test_shaft_arena():
    assert functions.define_gamemode('shaft_arena') == 'r_shaft_arena_1'


def test_wipeout():
    assert functions.define_gamemode('wipeout') == 'r_wo'


def test_wrond_gamemode():
    assert functions.define_gamemode('') == '[ERROR] Incorrect game mode'


# Tests for decorators.py
def test_sleep_works():
    assert decorators.sleep(0)



