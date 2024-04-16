# Import the required packages
from selenium import webdriver

def get_chrome_title():
    # Initialize Chrome WebDriver
    driver = webdriver.Chrome()

    # Open the specified URL
    driver.get("https://ecommerce-playground.lambdatest.io/")
    
    return driver.title

def get_edge_title():
    # Initialize Chrome WebDriver
    driver = webdriver.Edge()

    # Open the specified URL
    driver.get("https://ecommerce-playground.lambdatest.io/")
    
    return driver.title