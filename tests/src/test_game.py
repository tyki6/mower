import pytest

from src.game import Game


def test_init():
    game = Game("test.txt")
    assert game.filename == "test.txt"

    with pytest.raises(Exception):
        Game("unknown.txt")


def test_is_finish():
    game = Game("test.txt")
    assert not game.is_finish()


def test_play_turn():
    pass
