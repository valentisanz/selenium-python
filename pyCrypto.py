from selenium import webdriver

data = []
chromeDriverUrl = "./chromedriver"
cryptoWebUrl = "https://preciohoy.com/prevision-"
driver = webdriver.Chrome(chromeDriverUrl)

#get bitcoin value from website
def getBTC():
    print('Getting Bitcoin value...')

    driver.get(f'{cryptoWebUrl}bitcoin')
    elements = driver.find_elements_by_tag_name("b")

    data.append({
        'BTC':   '{} {}'.format(elements[0].text, elements[1].text)
    })
    getLTC()

#get litecoin value from website
def getLTC():
    print('Getting Litecoin value...')

    driver.get(f'{cryptoWebUrl}litecoin')
    elements = driver.find_elements_by_tag_name("b")

    data.append({
        'LTC':   '{} {}'.format(elements[0].text, elements[1].text)
    })
    getETH()

#get ethereum value from website
def getETH():
    print('Getting Ethereum value...')

    driver.get(f'{cryptoWebUrl}ethereum')
    elements = driver.find_elements_by_tag_name("b")

    data.append({
        'ETH':   '{} {}'.format(elements[0].text, elements[1].text)
    })
    driver.quit()

getBTC()

#print the value of cryptocurrencies searched
print(data)
