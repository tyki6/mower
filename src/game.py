"""Game file"""
import re
from os import path

from src.constant import orientation
from src.field import Field
from src.mower import Mower


class Game:
    def __init__(self, filename: str) -> None:
        """
        Instantiate Game Object
        :param filename: file name with setup text.
        """
        self.filename = filename
        self.field = None
        if not self.is_legal_file():
            raise Exception("Error during loading")

    def is_finish(self) -> bool:
        """
        Determine if all mowers have finished.
        :return:  If all mowers have finish their movements return True else False.
        :rtype: bool
        """
        finish = True
        for mower in self.field.list_mower:
            finish = finish and mower.is_finish()
        return finish

    def play_turn(self) -> None:
        """
        Play a Turn
        """
        for mower in self.field.list_mower:
            mower.play_turn()

    def print_result(self) -> None:
        """
        Print End result.
        """
        for mower in self.field.list_mower:
            print(
                mower.coord[0],
                mower.coord[1],
                orientation[mower.orientation],
            )

    def is_legal_file(self) -> bool:
        """
        Determine if setup file is correct.
        :return: return true if setup file is correct.
        :rtype: bool
        """
        if not path.exists(self.filename):
            return False
        with open(self.filename, "r") as file:
            lines = file.readlines()
        if len(lines) % 2 != 1:
            return False
        header = re.match("^(\d+)\s(\d+)$", lines[0])
        if not header:
            return False
        field = Field(
            height=int(header.groups()[0]),
            width=int(header.groups()[1]),
        )
        del lines[0]
        list_mower = []
        for index in range(0, len(lines), 2):
            mower_orientation = re.match(
                "^(\d)\s(\d)\s([NWSE])$",
                lines[index],
            )
            if not mower_orientation:
                return False
            mower_movement = re.search("^([LFR]*)$", lines[index + 1])
            if not mower_movement:
                return False
            group = mower_orientation.groups()
            list_mower.append(
                Mower(
                    name=f"Mower{int(index / 2 + 1)}",
                    field=field,
                    coord=(int(group[0]), int(group[1])),
                    orientation=orientation.index(group[2]),
                    list_movement=list(mower_movement.groups()[0]),
                ),
            )
        self.field = field
        self.field.list_mower = list_mower
        return True
