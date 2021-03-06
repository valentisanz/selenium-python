from selenium import webdriver
import time
username = input("Enter username:")
password = input("Enter password:")
userToSearch = input("Enter the user to search:")

driver = webdriver.Chrome("./chromedriver")
driver.get("https://www.instagram.com/")
driver.maximize_window()


def login():
    try:
        # Save the elements with which we are going to interact
        username_box = driver.find_element_by_xpath(
            "//*[@id='react-root']/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input")
        password_box = driver.find_element_by_xpath(
            "//*[@id='react-root']/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input")
        btn = driver.find_element_by_xpath(
            "//*[@id='react-root']/section/main/article/div[2]/div[1]/div/form/div[4]/button")

        # Enter username and password given by the user and sign in
        username_box.send_keys(username)
        password_box.send_keys(password)
        btn.click()
        time.sleep(6)
        searchUser()
    except:
        print("Something went wrong loging in, try again. *Could be a problem with wait time between actions.")
        driver.quit()


def searchUser():
    try:
        # Search for the entered user
        search_bar = driver.find_element_by_xpath(
            "//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/input")
        search_bar.send_keys(userToSearch)
        print("Searching user...")
        time.sleep(6)

        # Click the first result of the users list
        first_result = driver.find_element_by_xpath(
            "//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a[1]")
        first_result.click()
        print("User found, press enter to end program.")
    except:
        print("Something went wrong searching the user, try again. *Could be a problem with wait time between actions.")
        driver.quit()

login()
input()
driver.quit()
