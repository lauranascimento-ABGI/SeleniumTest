# Canal: Automation Step by Step
# Aula 01
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))  # Configura o driver do Chrome

driver.get("https://google.com")
search = driver.find_element(By.ID, "APjFqb")
search.send_keys("Fapesp")
search.send_keys(Keys.ENTER)
# driver.find_element(By.NAME, "btnK").click()

time.sleep(2)  # Quantos segundos fica aberto o site
driver.close()  # Fecha a aba
# driver.quit()  # Fecha a janela inteira
print("Done!")
