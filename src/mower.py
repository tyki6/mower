"""Mower file"""
from src.constant import orientation
from src.field import Field


class Mower:
    def __init__(
        self,
        field: Field,
        coord=(0, 0),
        orientation=0,
        list_movement=None,
        name="Mower",
    ):
        """
        Instantiate Mower Object
        :param field: Field object linked with mower.
        :param coord: initial coord
        :param orientation: initial orientation
        :param list_movement: list of mower movement
        :param name: mower's name
        """
        if list_movement is None:
            list_movement = []
        self.coord = coord
        self.orientation = orientation
        self.field = field
        self.list_movement = list_movement
        self.name = name

    def __str__(self) -> str:
        return f"{self.name} pos: {self.coord[0]}:{self.coord[1]}:{orientation[self.orientation]}"

    def is_finish(self) -> bool:
        """
        Return true if mower have no next movement else False.
        :return: true if mower have no next movement else False.
        """
        return len(self.list_movement) == 0

    def play_turn(self) -> None:
        """
        Play a movement.After that consume first movement in list_movement
        """
        if self.is_finish():
            return
        start = str(self)
        movement = self.list_movement[0]
        self.move(self.list_movement[0])
        self.list_movement.pop(0)
        print(start, movement, self)

    def move(self, movement: str) -> None:
        """
        Change orientation and coord.
        :param movement: Movement (Need to be in Orientation list)
        """
        if movement == "L":
            self.orientation = (self.orientation - 1) % 4
        elif movement == "R":
            self.orientation = (self.orientation + 1) % 4
        elif movement == "F":
            self.forward()

    def forward(self) -> None:
        """
        Forward mower depending on her orientation.Modifying coord
        :return:
        """
        x = self.coord[0]
        y = self.coord[1]
        if self.orientation == 0:
            x = self.coord[0]
            y = self.coord[1] + 1
        elif self.orientation == 1:
            x = self.coord[0] + 1
            y = self.coord[1]
        elif self.orientation == 2:
            x = self.coord[0]
            y = self.coord[1] - 1
        elif self.orientation == 3:
            x = self.coord[0] - 1
            y = self.coord[1]
        if self.field.is_valid_coord((x, y)):
            self.coord = (x, y)
