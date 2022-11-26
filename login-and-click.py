# Simple program to select a login form, input hardcoded values and then enter. In next page, it will click on an object and copy the URL. Then fetch a value and format it in text

# Before the code can work on your local machine, you need to install the driver ("pip.exe install selenium")
# You also need to install your browser driver. For Chrome ("https://chromedriver.chromium.org/")


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

import time

service = Service('F:\\Work.b\\py\\chromedriver.exe')

def get_driver():
    # Set options to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")                                      # Disable that display information like out of memory etc. Preferrably disable to avoid cursor interference
    options.add_argument("start-maximized")                                       # Start the browser as maximized
    options.add_argument("disable-dev-shm-usage")                                 # Avoid issues on systems running Linux
    options.add_argument("no-sandbox")                                            # Disable browser security feature called "Sandbox" to leverage our script privileges 
    options.add_experimental_option("excludeSwitches", ["enable-automation"])     # Help Selenium avoid detection to bypass script disabling features of browser
    options.add_argument("disable-blink-features=AutomationControlled")           

    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://automated.pythonanywhere.com/login/?next=/dashboard/")
    return driver

def clean_up(text):
    format_split = float(text.split(": ")[1])               # Format float to split object in elements and fetch the 2nd element 
    output = f"The temperature now is : {format_split}"     # Format text 
    return output   

def main():
    driver = get_driver()
    element = driver.find_element(by = "id", value = "id_username").send_keys("automated")                          # Find element by ID for more rebustness and use send_keys function
    time.sleep(1)                                                                                                   # Good idea to place some timer to simulate user experience

    element = driver.find_element(by = "id", value = "id_password").send_keys("automatedautomated" + Keys.RETURN)   # Enter value in pw field and use Keys to press "enter" to complete login
    print("Link after login :" + driver.current_url)                                                                # Print current URL
    time.sleep(2)
    
    driver.find_element(by = "xpath", value = "/html/body/nav/div/a").click()                                       # Find an element and Click 
    time.sleep(2)
    print("Link when you click HOME button :" + driver.current_url)

    text = element = driver.find_element(by = "xpath", value = "/html/body/div[1]/div/h1[2]").text                  # Scrape text in element by xpath

    return clean_up(text)
    
print(main())

