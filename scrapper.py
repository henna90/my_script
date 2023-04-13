from selenium import webdriver
import time
import pandas as pd

# Launch Chrome browser
driver = webdriver.Chrome()
driver.get("https://www.zillow.com/homes/for_sale/")

# Wait for page to load
time.sleep(5)

# Apply filters
beds_input = driver.find_element_by_xpath("//input[@id='beds-0']")
beds_input.clear()
beds_input.send_keys("3+")

baths_input = driver.find_element_by_xpath("//input[@id='baths-0']")
baths_input.clear()
baths_input.send_keys("2.5+")

sqft_input = driver.find_element_by_xpath("//input[@id='sqft-0']")
sqft_input.clear()
sqft_input.send_keys("1700+")

year_built_input = driver.find_element_by_xpath("//input[@id='year-built-0']")
year_built_input.clear()
year_built_input.send_keys("2019+")

apply_filters_button = driver.find_element_by_xpath("//button[@id='apply-search-options']")
apply_filters_button.click()

# Wait for page to load
time.sleep(5)

# Find all the listings on the page
listings = driver.find_elements_by_xpath("//article[@class='list-card']")

# Extract the relevant information from each listing
data = []
for listing in listings:
    address = listing.find_element_by_xpath(".//address").text
    price = listing.find_element_by_xpath(".//div[contains(@class, 'list-card-price')]").text
    bedrooms = listing.find_element_by_xpath(".//ul/li[1]").text
    bathrooms = listing.find_element_by_xpath(".//ul/li[2]").text
    sqft = listing.find_element_by_xpath(".//ul/li[3]").text
    year_built = listing.find_element_by_xpath(".//ul/li[4]").text
    
    # Get estimated rent
    listing_id = listing.get_attribute("id")
    rent_url = f'https://www.zillow.com/homedetails/{listing_id}_zpid/'
    driver.get(rent_url)
    time.sleep(2)
    try:
        rent = driver.find_element_by_xpath("//div[contains(@class, 'ds-bed-bath-living-area-rental')]//span[contains(@class, 'ds-body ds-home-fact-value')]").text
    except:
        rent = None
    
    data.append({
        "address": address,
        "price": price,
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "sqft":

        
        # https://chat.openai.com/chat/8ce17672-6960-4c86-b02d-fd7e023a7968
