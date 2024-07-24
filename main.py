from selenium import webdriver
from selenium.webdriver.common.by import By

def get_driver():
    
    """get_diver code"""

    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")  # Corregido el error tipográfico
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled") 
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.pythonanywhere.com/")
    return driver

def main():
    driver = get_driver()
    element = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div")  # Usando By.XPATH
    return element.text  # Devuelve el texto del elemento

print(main())
