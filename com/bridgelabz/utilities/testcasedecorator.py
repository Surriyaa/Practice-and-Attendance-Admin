# com/bridgelabz/utilities/testcasedecorator.py
import functools
import logging

def test_case(test_case_id):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            logger = logging.getLogger(func.__module__)
            logger.info(f"Executing Test Case ID: {test_case_id} - {func.__name__}")
            print(f"Executing Test Case ID: {test_case_id} - {func.__name__}")  # Optional: For console
            return func(*args, **kwargs)
        return wrapper
    return decorator
