from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")
driver.get("https://web.whatsapp.com/")
driver.maximize_window()

name = input("Enter name or group name:")
msg = input("Enter your msg:")
count = int(input("Enter count:"))
input("Press enter to continue...")

try:
    # Select a user to send the messages
    user = driver.find_element_by_xpath(f"//span[@title='{name}']")
    user.click()

    # Get msg box
    msg_box = driver.find_element_by_xpath(
        "//*[@id='main']/footer/div[1]/div[2]/div/div[2]")

    # Send messages
    for i in range(count):
        msg_box.send_keys(msg)
        driver.find_element_by_xpath(
            "//*[@id='main']/footer/div[1]/div[3]/button").click()
except:
    print("Something went wrong")
    driver.quit()


print("Done :)")
