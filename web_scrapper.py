from selenium import webdriver
from bs4 import BeautifulSoup

URL = 'https://www.homes.com/brooklyn-ny/homes-for-sale/'

driver = webdriver.Firefox()
driver.get(URL)
driver.implicitly_wait(1000)
soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()

for listing in soup.find_all('div', class_='card-wrapper card-wrapper--property grid-cell'):
    address = listing.find('h2', class_='property-card-content__address').text
    price = listing.find('span', class_='details__price-val').text
    print(address + ' @ ' + price)
