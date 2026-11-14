from collections.abc import Callable
import random
from generate_data import generate_random, generate_nearly_sorted, generate_sorted
import pytest

RANDOM_SEED = 1
random_instance = random.Random()
random_instance.seed(RANDOM_SEED)
# Generate_random with random seed of 1 returns [137, 582, 857, 821, 782, 64, 261, 120, 507, 779] 
# Generate nearly sorted w/ 15 returns [0, 13, 9, 3, 4, 5, 6, 7, 8, 2, 10, 11, 1, 12, 14]

def test_random():
    assert generate_random(10, random_instance) == [137, 582, 867, 821, 782, 64, 261, 120, 507, 779]