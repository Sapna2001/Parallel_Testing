# Import the functions for retrieving the title and its length from parallel_testing module
from parallel_testing import get_title, get_title_length


# Test function to verify the web page title retrieved from browser
def test_title():
    title = get_title()
    assert title == "Your Store", "Test not passed for title"


# Test function to verify the length of the web page title retrieved from browser
def test_title_length():
    title_length = get_title_length()
    assert title_length == 10, "Test not passed for title length"