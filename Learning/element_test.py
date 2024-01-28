from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.get('https://www.jotform.com/build/240275247417456?s=templates#preview')

driver.find_element(By.ID, 'first_3').send_keys('<first_name>')
time.sleep(2)
driver.find_element(By.ID, 'last_3').send_keys('<last_name>')
time.sleep(2)
driver.find_element(By.ID, 'dragger-item').click()
time.sleep(2)