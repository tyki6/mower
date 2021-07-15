from src.field import Field
from src.mower import Mower


def test_init():
    mower = Mower(field=Field(5, 5))
    assert type(mower.field) == Field
    assert mower.orientation == 0
    assert mower.coord == (0, 0)


def test_str():
    mower = Mower(field=Field(5, 5))
    assert "pos" in str(mower)
    assert mower.name in str(mower)


def test_is_finish():
    mower = Mower(field=Field(5, 5), coord=(0, 0), list_movement=[])
    assert mower.is_finish()
    mower = Mower(field=Field(5, 5), coord=(0, 0), list_movement=[1, 2])
    assert not mower.is_finish()


def test_play_turn():
    mower = Mower(field=Field(5, 5), coord=(0, 0), list_movement=[])
    mower.play_turn()
    assert mower.coord == (0, 0)
    assert mower.orientation == 0
    assert mower.list_movement == []

    mower = Mower(field=Field(5, 5), coord=(0, 0), list_movement=["F"])
    mower.play_turn()
    assert mower.coord == (0, 1)
    assert mower.orientation == 0
    assert mower.list_movement == []


def test_move():
    mower = Mower(field=Field(5, 5), coord=(0, 0), orientation=0)
    mower.move("L")
    assert mower.coord == (0, 0)
    assert mower.orientation == 3

    mower = Mower(field=Field(5, 5), coord=(0, 0), orientation=0)
    mower.move("R")
    assert mower.coord == (0, 0)
    assert mower.orientation == 1

    mower = Mower(field=Field(5, 5), coord=(0, 0), orientation=0)
    mower.move("F")
    assert mower.coord == (0, 1)
    assert mower.orientation == 0


def test_forward():
    mower = Mower(field=Field(5, 5), coord=(0, 0), orientation=0)
    mower.forward()
    assert mower.coord == (0, 1)
    assert mower.orientation == 0

    mower = Mower(field=Field(5, 5), coord=(0, 0), orientation=1)
    mower.forward()
    assert mower.coord == (1, 0)

    mower = Mower(field=Field(5, 5), coord=(0, 1), orientation=2)
    mower.forward()
    assert mower.coord == (0, 0)

    mower = Mower(field=Field(5, 5), coord=(1, 0), orientation=3)
    mower.forward()
    assert mower.coord == (0, 0)

    mower = Mower(field=Field(5, 5), coord=(5, 5), orientation=0)
    mower.forward()
    assert mower.coord == (5, 5)
