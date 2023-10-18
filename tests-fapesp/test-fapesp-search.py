# Canal: Automation Step by Step
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))  # Configura o driver do Chrome

driver.get("https://fapesp.br/chamadas-html")
search = driver.find_element(By.ID, "search-input")
search.send_keys("Fapesp")
# button = driver.find_element(By.CLASS_NAME, "text-center")
search.send_keys(Keys.ENTER)
time.sleep(2)  # Quantos segundos fica aberto esperando o próximo comando
driver.close()  # Fecha a aba
print("Done 1!")

driver.get("https://fapesp.br/chamadas-html")
driver.find_element(By.XPATH, "/html/body/main/div/div[1]/div/div[1]/div[1]/b[2]").click()
