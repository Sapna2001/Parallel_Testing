# Import the required packages
from selenium import webdriver

# Function to retrieve the title of the web page
def get_title(): 
    # Configure Chrome WebDriver options
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    
    # Initialize Chrome WebDriver
    driver = webdriver.Chrome(options=options)
     
    # Open the specified URL
    driver.get("https://ecommerce-playground.lambdatest.io/")
    
    # Return the title of the web page
    return driver.title

# Function to retrieve the length of the title of the web page
def get_title_length(): 
    # Configure Chrome WebDriver options
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    
    # Initialize Chrome WebDriver
    driver = webdriver.Chrome(options=options) 
    
    # Open the specified URL
    driver.get("https://ecommerce-playground.lambdatest.io/")
    
    # Return the length of the title of the web page
    return len(driver.title)

