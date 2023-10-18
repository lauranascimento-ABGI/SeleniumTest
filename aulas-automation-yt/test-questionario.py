# Canal: Automation Step by Step
# Aula 02
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))  # Configura o driver do Chrome

# DEMO SITE - NÃO FUNCIONA
driver.get("https://trytestingthis.netlify.app/")
campo1 = driver.find_element(By.ID, "fname")
campo1.send_keys("Laura")
time.sleep(2)
campo2 = driver.find_element(By.ID, "lname")
campo2.send_keys("Nascimento")
time.sleep(2)
# Para botões sem nome/id fácil de identificação
# Clica com direito em cima do código > copy > copy xpath
driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/form/fieldset/button')  # forma 1
driver.find_element(By.XPATH, "//button[@class'nome-da-classe']").click()  # forma 2

# driver.find_element(By.NAME, "btnK").click()

time.sleep(2)  # Quantos segundos fica aberto esperando o próximo passo
driver.close()  # Fecha a aba
# driver.quit()  # Fecha a janela inteira
print("Done!")
