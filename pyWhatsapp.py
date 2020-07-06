from selenium import webdriver

driver = webdriver.Chrome("/Users/valenti/Documents/chromedriver")
driver.get("https://web.whatsapp.com/")
#driver.execute_script("window.open('https://www.google.com');")

driver.maximize_window()

name = input("Enter name or group name:")
msg = input("Enter your msg:")
count = int(input("Enter count:"))
input("Press enter to continue...")

#Entrar al xat
user = driver.find_element_by_xpath("//span[@title='{}']".format(name))
user.click()

#Trobar el msg box del xat
msg_box = driver.find_element_by_xpath(
    "//*[@id='main']/footer/div[1]/div[2]/div/div[2]")

#Enviar X missatges 
for index in range(count):
    msg_box.send_keys(msg)
    driver.find_element_by_xpath(
        "//*[@id='main']/footer/div[1]/div[3]/button").click()

print("Success :)")*/
