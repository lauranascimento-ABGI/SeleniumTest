from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))  # Configura o driver do Chrome

driver.get("https://fapesp.br/chamadas-html")
open1 = driver.find_element(By.XPATH, '/html/body/main/div/div[1]/div/div[1]/div[1]/b[2]').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="DescProp"]/h3[1]/a').click()
time.sleep(2)