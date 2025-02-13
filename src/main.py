import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
# options.add_argument("window-size=1400,1400")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

for i in range(0, 50, 10):
    driver.get('https://www.indeed.com/jobs?q=chemical%20engineer&l=united%20states&start=' + str(i))
    driver.implicitly_wait(5)

    jobtitles = []
    companies = []
    locations = []
    descriptions = []

    jobs = driver.find_elements(By.CLASS_NAME, "slider_container")

    for job in jobs:

        jobtitle = job.find_element(By.CLASS_NAME, "jobTitle").text.replace("new", "").strip()
        jobtitles.append(jobtitle)

        company = job.find_element(By.CLASS_NAME, "companyName").text.replace("new", "").strip()
        companies.append(company)

        location = job.find_element(By.CLASS_NAME, "companyLocation").text.replace("new", "").strip()
        locations.append(location)

        description = job.find_element(By.CLASS_NAME, "job-snippet").text.replace("new", "").strip()
        descriptions.append(description)
        try:
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "button.popover-x-button-close.icl-CloseButton"))).click()
        except:
            pass

    df_da = pd.DataFrame()
    df_da['JobTitle'] = jobtitles
    df_da['Company'] = companies
    df_da['Location'] = locations
    df_da['Description'] = descriptions
    print(df_da)
    df_da.to_csv('C:/Users/Dan/Desktop/AZNext/file_name1.csv')
