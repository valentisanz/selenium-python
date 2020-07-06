from selenium import webdriver

driver = webdriver.Chrome("/Users/valenti/Documents/chromedriver")
driver.get("https://www.instagram.com/")
# driver.execute_script("window.open('https://www.google.com');")
driver.maximize_window()

username = input("Enter username:")
password = input("Enter password:")

# Guardar els inputs i el boto de login
username_box = driver.find_element_by_xpath(
    "//*[@id='react-root']/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input")
password_box = driver.find_element_by_xpath(
    "//*[@id='react-root']/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input")
btn = driver.find_element_by_xpath(
    "//*[@id='react-root']/section/main/article/div[2]/div[1]/div/form/div[4]/button")

# Introduir credencials i fer click
username_box.send_keys(username)
password_box.send_keys(password)
btn.click()

print("Success :)")
