from enum import Enum


class ChopFoodStates(Enum):
    FRESH = "Fresh"
    CHOPPED = "Chopped"


class BlenderFoodStates(Enum):
    FRESH = "Fresh"
    IN_PROGRESS = "InProgress"
    MASHED = "Well-Cooked"
    OVERCOOKED = "Overcooked"


ONION_INIT_STATE = ChopFoodStates.FRESH
TOMATO_INIT_STATE = ChopFoodStates.FRESH
LETTUCE_INIT_STATE = ChopFoodStates.FRESH
