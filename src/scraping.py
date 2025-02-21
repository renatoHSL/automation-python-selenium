import json
import time
import random
import urllib.parse
import pandas as pd
from seleniumbase import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from seleniumbase.common.exceptions import NoSuchElementException


# Nota: Existe a possibilidade de pegar os dados diretamente via API do Indeed (XHR request no DevTools),
# mas por enquanto estou mantendo o scraping simples com Selenium para entrega do projeto.
# Futuramente, irei explorar essa abordagem para otimizar a extração.


posicao = "Desenvolvedor Junior"
local = "São Paulo"

vaga_formatada = urllib.parse.quote(posicao)
cidade_formatada = urllib.parse.quote(local)
url = f"https://br.indeed.com/jobs?q={vaga_formatada}&l={cidade_formatada}"

driver = Driver(uc=True, headless=False)
driver.uc_open_with_reconnect(url, reconnect_time=6)

try:
    driver.uc_gui_click_captcha()

    print("Captcha concluido")

except NoSuchElementException:
    print("Erro no captcha")

try:
    myElem = WebDriverWait(driver, 4).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='jobsearch']/div/div[2]/button")))
    print("Page is ready!")
except TimeoutException:
    print("Loading took too much time!")

driver.implicitly_wait(3)

jobs = driver.find_elements(by=By.CLASS_NAME, value="slider_container")

vagas = {}
vaga_id = 1

for job in jobs:
    time.sleep(random.uniform(2, 5))

    vaga = {
        "title": "",
        "employer": "",
        "location": "",
        "description": ""
    }

    try:
        title = job.find_element(By.XPATH, ".//h2[contains(@class,'jobTitle')]/a/span").text
    except NoSuchElementException:
        title = "Título não disponível"
    vaga["title"] = title

    try:
        employer = job.find_element(By.XPATH, ".//span[@data-testid='company-name']").text
    except NoSuchElementException:
        employer = "Empresa não informada"
    vaga["employer"] = employer

    try:
        location = job.find_element(By.XPATH, ".//div[@data-testid='text-location']").text
    except NoSuchElementException:
        location = "Local não informado"
    vaga["location"] = location

    try:
        description = job.find_element(By.XPATH, ".//div[@data-testid='jobsnippet_footer']//ul/li").text
    except NoSuchElementException:
        description = "Descrição não disponível"
    vaga["description"] = description

    vagas[f"vaga_{vaga_id}"] = vaga
    vaga_id += 1

print(json.dumps(vagas, indent=4, ensure_ascii=False))

dataframe = pd.DataFrame.from_dict(vagas, orient="index")
dataframe.to_csv("out.csv", encoding='utf-8-sig', header=True, index=False, sep=",")

print(dataframe.head())

driver.quit()
