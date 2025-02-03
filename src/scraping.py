from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

from bs4 import BeautifulSoup

driver = webdriver.Chrome()

driver.get("https://quotes.toscrape.com/")

text_citation = driver.find_elements(by=By.CLASS_NAME, value="text")
author = driver.find_elements(by=By.CLASS_NAME, value="author")
tags = driver.find_elements(by=By.CLASS_NAME, value="tag")


scraping = []

for e in range(len(text_citation)):
    e_dicionary = {
        "author": author[e].text,
        "citação": text_citation[e].text,
    }
    scraping.append(e_dicionary)
    # print(f"{author[e].text} uma vez disse: {text_citation[e].text}")


dataframe = pd.DataFrame(scraping)
# dataframe.replace()
dataframe.to_csv("out.csv", encoding='utf-8-sig', header=True, index=False, sep=",")

print("scrapping", scraping)
print("dataframe", dataframe)
driver.quit()