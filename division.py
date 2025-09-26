"""
This module provides a function for performing division operations.
"""
def divide(a, b):
    """
    This function divides two numbers and returns the result.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
