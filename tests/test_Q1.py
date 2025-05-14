import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from practical_codes.Q1_code import dfa_accepts_101

def test_accepts_101_true():
    assert dfa_accepts_101("1101") == True

def test_accepts_101_false():
    assert dfa_accepts_101("1111") == False

def test_accepts_101_invalid():
    assert dfa_accepts_101("10a1") == "Error: Please enter a valid binary string (only 0 and 1)."

