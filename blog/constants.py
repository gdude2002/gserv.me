from enum import Enum


class BlockType(Enum):
    HEADER = 0
    PARAGRAPH = 1
    LIST = 2
    IMAGE = 3
    FRAME = 4
    MEDIA = 5
