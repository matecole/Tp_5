import enum


class GameState(enum.Enum):
    GAME_NOT_STARTED = 1
    ROUND_ACTIVE = 2
    ROUND_DONE = 3
    GAME_OVER = 4
