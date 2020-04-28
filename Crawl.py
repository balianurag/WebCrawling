from selenium.webdriver.edge.options import Options

from selenium import webdriver

driver = webdriver.Edge()

driver.get("'https://www.indiatoday.in/india-sitemap.xml'")

# Extract lists of "urls" based on xpath.

urls = driver.find_elements_by_xpath('//url/loc')

# Print out all of the buyers and prices on page:

num_page_items = len(urls)

for i in range(num_page_items):

    print(urls[i].text)

# Clean up (close browser once completed task).

driver.close()
