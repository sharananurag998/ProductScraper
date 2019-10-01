from selenium import webdriver
from bs4 import BeautifulSoup as bs
import pandas as pd
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome("chromedriver.exe", options=chrome_options)

products = []
prices = []
ratings = []

driver.get("https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniqBStoreParam1=val1&wid=11.productCard.PMU_V2")

content = driver.page_source

soup = bs(content, "html.parser")

for a in soup.findAll('a', href=True, attrs={'class': '_31qSD5'}):
    name = a.find('div', attrs={'class': '_3wU53n'})
    price = a.find('div', attrs={'class': '_1vC4OE _2rQ-NK'})
    rating = a.find('div', attrs={'class': 'hGSR34'})
    products.append(name.text)
    prices.append(price.text)
    ratings.append(rating.text)

df = pd.DataFrame({'Product Name': products, 'Price': prices, 'Rating': ratings})
df.to_csv('products.csv', index='False', encoding='utf-8-sig')

readDf = pd.read_csv(filepath_or_buffer='products.csv', skiprows=1)
print(readDf.head(5))




