"""File for define Field"""


class Field:
    def __init__(self, height: int, width: int) -> None:
        """
        Instance field Object.
        :param height: height of field.
        :param width: width of field.
        """
        self.height = height
        self.width = width
        self.list_mower = []

    def is_valid_coord(self, pos: tuple) -> bool:
        """
        Define if given coord is valid or not.
        :param pos: coord format: (x, y)
        :return: return true if given coord is valid else False.
        :rtype: bool
        """
        same_coord = False
        for mower in self.list_mower:
            same_coord = same_coord or mower.coord == pos
        return (
            (self.width >= pos[0] >= 0)
            and (self.height >= pos[1] >= 0)
            and not same_coord
        )
