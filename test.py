from parallel_testing import get_chrome_title, get_edge_title
 
def test_get_chrome_title():
    title = get_chrome_title()
    assert title == "Your Store", "Test not passed for chrome"
 
def test_get_edge_title():
    title = get_edge_title()
    assert title == "Your Store", "Test not passed for edge"