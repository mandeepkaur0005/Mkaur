from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.maximize_window()
driver.get("https://www.linkedin.com/home")

email = "mandeepdhiman065@gmail.com"
password = "Mohit1016"

email_element = driver.find_element('xpath', '/html/body/main/section[1]/div/div/form[1]/div[1]/div[1]/div/div/input')
email_element.send_keys(email)

password_element = driver.find_element('xpath', '/html/body/main/section[1]/div/div/form[1]/div[1]/div[2]/div/div/input')
password_element.send_keys(password)

login_btn = driver.find_element('xpath', '/html/body/main/section[1]/div/div/form[1]/div[2]/button')
login_btn.click()

# Test 1: Verify if the user profile dropdown is displayed
profile_dropdown = driver.find_element('xpath', '/html/body/div[5]/header/div/nav/ul/li[6]/div/button"]')
if profile_dropdown.is_displayed():
    print("Profile dropdown is displayed")
else:
    print("Profile dropdown is not displayed")

# Test 2: Verify if the user's full name is displayed
full_name = driver.find_element('xpath', '//*[@id="nav-settings__dropdown-options"]/li[1]/div/div[1]/div/span')
if full_name.text:
    print("Full name is displayed: ", full_name.text)
else:
    print("Full name is not displayed")

# Test 3: Verify if the user's network tab is displayed
network_tab = driver.find_element('xpath', '//*[@id="ember23"]')
if network_tab.is_displayed():
    print("Network tab is displayed")
else:
    print("Network tab is not displayed")

# Test 4: Verify if the search bar is displayed
search_bar = driver.find_element('xpath', '//*[@id="global-nav-typeahead"]/input')
if search_bar.is_displayed():
    print("Search bar is displayed")
else:
    print("Search bar is not displayed")

driver.quit()
