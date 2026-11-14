import random
from generate_data import generate_random, generate_nearly_sorted, generate_sorted, generate_reverse_sorted

RANDOM_SEED = 1

def test_random():
    random_instance = random.Random()
    random_instance.seed(RANDOM_SEED)
    assert generate_random(10, random_instance) == [137, 582, 867, 821, 782, 64, 261, 120, 507, 779]

def test_sorted():
    assert generate_sorted(5) == [0, 1, 2, 3, 4]

def test_reverse_sorted():
    assert generate_reverse_sorted(5) == [4, 3, 2, 1, 0]

def test_nearly_sorted():
    random_instance = random.Random()
    random_instance.seed(RANDOM_SEED)
    assert generate_nearly_sorted(15, random_instance) == [0, 13, 9, 3, 4, 5, 6, 7, 8, 2, 10, 11, 1, 12, 14]