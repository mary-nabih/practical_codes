import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from practical_codes.Q3_code import binary_divisible_by_3

def test_divisible_by_3_true():
    assert binary_divisible_by_3("110") == True  # 6

def test_divisible_by_3_false():
    assert binary_divisible_by_3("100") == False  # 4

def test_divisible_by_3_invalid():
    assert binary_divisible_by_3("10b0") == "Error: Please enter a valid binary number (only 0 and 1)."


