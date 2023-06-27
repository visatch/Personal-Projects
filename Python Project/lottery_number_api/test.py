from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

html = '<span>6</span><span>28</span><span>39</span><span>43</span><span>54</span><span>12</span><span class="sr-only">Superball</span>'

# Set up the driver options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode

# Set up the Chrome driver
driver = webdriver.Chrome(service=Service(executable_path='path/to/chromedriver'), options=chrome_options)

# Load the HTML content
driver.get("data:text/html;charset=utf-8," + html)

# Find all the span elements and extract the text
elements = driver.find_elements(By.TAG_NAME, "span")
text_values = [element.text for element in elements]

# Close the browser instance
driver.quit()

print(text_values)
