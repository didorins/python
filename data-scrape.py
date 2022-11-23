# Data scrape static value from website using Selenium driver. Before the code can work on your local machine, you need to install the driver ("pip.exe install selenium")
# You also need to install your browser driver. For Chrome ("https://chromedriver.chromium.org/")


from selenium import webdriver
from selenium.webdriver.chrome.service import Service

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
    driver.get("https://whatismyipaddress.com/")
    return driver

def main():
    driver = get_driver()  # Link output of get_driver()
    element = driver.find_element(by="xpath", value="/html/body/div[2]/div/div/div/div/article/div/div/div[1]/div/div[2]/div/div/div/div/div/div[2]/div[1]/div[1]/p[2]/span[2]/a")
    # Fetch element by xpath. To find the xpath, use browser console, right click on element and 'inspect' it. Right click on the object and Copy full xpath
    return element.text

print(main())

