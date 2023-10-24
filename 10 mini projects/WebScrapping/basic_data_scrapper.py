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
from tqdm import tqdm
import uuid

def scrape_data(search_parameter):
    options = Options()
    options.add_experimental_option("detach", True)
    options.add_argument("--headless")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install(), options=options))

    driver.get("https://amazon.in")
    driver.maximize_window()
    pbar.update(5)

    # search buttons and text inputs
    input_field = driver.find_element(By.ID, "twotabsearchtextbox")
    search_button = driver.find_element(By.ID, "nav-search-submit-button")

    input_field.send_keys(search_parameter)
    sleep(1)
    search_button.click()
    pbar.update(5)

    products = []
    for i in range(10):
        product_class = "a-size-medium a-color-base a-text-normal"
        product = driver.find_elements(By.XPATH, f"//span[@class='{product_class}']")
        for item in product:
            products.append(item.text)
        next_button = driver.find_element(By.XPATH, f"//a[@class='s-pagination-item s-pagination-next s-pagination-button s-pagination-separator']")
        next_button.click()
        sleep(3)
        pbar.update(9)


    driver.quit()
    return products


def creating_csv(data, product_name):
    # file_name = "products-" + str(uuid.uuid4()) + ".csv"
    product_name = product_name.replace("_", " ")
    file_name = f"products-({product_name}).csv"
    pbar.update(50)
    
    df = pd.DataFrame({ "product_name" : data })
    df.to_csv(file_name, index=False)
    pbar.update(50)


if __name__ == "__main__":
    product_name = input("Enter the name of the product you want to scrape the data of : ")

    data = None
    with tqdm(total=100, desc='Scrapping the data...') as pbar:
        data = scrape_data(product_name)  
        print("Data scrapped")

    with tqdm(total=100, desc="Creating file...") as pbar:
        creating_csv(data, product_name)
        print("File created")