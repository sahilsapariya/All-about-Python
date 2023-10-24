from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.chrome.options import Options 
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import pandas as pd


options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install(), options=options))


driver.get("https://amazon.in")
driver.maximize_window()


# search buttons and text inputs
input_field = driver.find_element(By.ID, "twotabsearchtextbox")
search_button = driver.find_element(By.ID, "nav-search-submit-button")



input_field.send_keys("Smartphones under 20000")
sleep(1)
search_button.click()


products = []
for i in range(5):
    print("Scraping times : ", i + 1)
    product_class = "a-size-medium a-color-base a-text-normal"
    product = driver.find_elements(By.XPATH, f"//span[@class='{product_class}']")
    for item in product:
        products.append(item.text)
    next_button = driver.find_element(By.XPATH, f"//a[@class='s-pagination-item s-pagination-next s-pagination-button s-pagination-separator']")
    next_button.click()
    sleep(3)


df = pd.DataFrame({ "product_name" : products })

df.to_csv("products.csv", index=False)

print("csv file created")

driver.quit()