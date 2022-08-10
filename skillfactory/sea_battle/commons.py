from enum import IntEnum, Enum


class ShotResult(IntEnum):
    PAST = 0
    WOUNDED = 1
    KILLED = 2


class Orientation(IntEnum):
    HORIZONTAL = 0
    VERTICAL = 1


class Values(Enum):
    SPACE = " "
    SHIP = "■"
    CONTOUR = "·"
    DROP = "X"
    PAST = "T"
