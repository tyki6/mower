from src.field import Field


def test_init():
    field = Field(0, 0)
    assert field.height == 0
    assert field.width == 0


def test_is_valid_coord():
    field = Field(5, 5)
    assert field.is_valid_coord((1, 1))
    assert not field.is_valid_coord((6, 1))
