from seleniumbase import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import pandas as pd

# from bs4 import BeautifulSoup

# Nota: Existe a possibilidade de pegar os dados diretamente via API do Indeed (XHR request no DevTools),
# mas por enquanto estou mantendo o scraping simples com Selenium para entrega do projeto.
# Futuramente, irei explorar essa abordagem para otimizar a extração.


driver = Driver(uc=True, headless=False)

url = "https://www.indeed.com/jobs?q=Desenvolvedor+Junior&l=Rio+de+Janeiro%2C+RJ&from=searchOnHP&vjk=20790cd4b63c0a9e"

# open URL using UC mode with 6 second reconnect time to bypass initial detection
driver.uc_open_with_reconnect(url, reconnect_time=6)

# attempt to click the CAPTCHA checkbox if present
driver.uc_gui_click_captcha()

driver.implicitly_wait(10)

try:
    myElem = WebDriverWait(driver, 4).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='jobsearch']/div/div[2]/button")))
    print("Page is ready!")
except TimeoutException:
    print("Loading took too much time!")

titles = []
companies = []
locations = []
links = []
reviews = []
salaries = []
descriptions = []

driver.implicitly_wait(10)

job_title = driver.find_element(By.XPATH, "//h2[@data-testid='jobsearch-JobInfoHeader-title']/span")
employer = driver.find_element(By.XPATH,
                               "//*[@id='jobsearch-ViewjobPaneWrapper']/div/div[2]/div[2]/div[1]/div/div[1]/div[2]/div/div/div/div[1]/div/span/a")

job_title2 = job_title.text.split("\n")[0]

jobs = driver.find_elements(by=By.CLASS_NAME, value="slider_container")

# job_location = driver.find_element(By.XPATH, "//*[@id='jobLocationText']/div/span")
#
# job_url = driver.find_element(By.XPATH, "//*[@id='applyButtonLinkContainer']/div/button/span")
#
# job_description = driver.find_element(By.XPATH, "//*[@id='jobDescriptionText']")

# optional

# salary = driver.find_element(By.XPATH, "//*[@id='salaryInfoAndJobType']/span")
#
# job_type = driver.find_element(By.XPATH, "//*[@id='jobDetailsSection']/div/div[1]/div[
# 2]/div/div/div/ul/li/div/div/div/div/span")
#
# benefits = driver.find_element(By.XPATH, "//*[@id='benefits']/div[1]/div/span")


for job in jobs:
    print("Empres: ", job.text)

driver.quit()

# author = driver.find_elements(by=By.CLASS_NAME, value="author")
# tags = driver.find_elements(by=By.CLASS_NAME, value="tag")
#
#
# scraping = []
#
# for e in range(len(text_citation)):
#     e_dicionary = {
#         "author": author[e].text,
#         "citação": text_citation[e].text,
#     }
#     scraping.append(e_dicionary)
#     # print(f"{author[e].text} uma vez disse: {text_citation[e].text}")
#
#
# dataframe = pd.DataFrame(scraping)
# # dataframe.replace()
# dataframe.to_csv("out.csv", encoding='utf-8-sig', header=True, index=False, sep=",")
#
# print("scrapping", scraping)
# print("dataframe", dataframe)


# test = driver.find_element(by=By.XPATH, value="//*[@id='jobsearch-JapanPage']/div/div[5]/div/div[1]/div[3]/span")

# Exibe o código fonte da página (para verificar se o bloqueio foi contornado)
# print(driver.page_source)
# print("Nome do emprego: ", job_title2)
# print("Empres: ", employer.text)

# input_job_name = driver.find_element(By.XPATH, "//*[@id='text-input-what']")
# input_job_name.clear()
# input_location = driver.find_element(By.XPATH, "//*[@id='text-input-where']")
# input_location.clear()
# input_search = driver.find_element(By.XPATH, "//*[@id='jobsearch']/div/div[2]/button")

# job_name = "Desenvolvedor Junior"
# location = "Rio de Janeiro, RJ"
#
# input_job_name.send_keys(job_name)
# input_location.send_keys(location)
# input_search.click()
