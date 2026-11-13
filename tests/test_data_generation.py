from collections.abc import Callable
import random
import pytest

RANDOM_SEED = 1
RANDOM_INSTANCE = random.Random().seed(RANDOM_SEED)