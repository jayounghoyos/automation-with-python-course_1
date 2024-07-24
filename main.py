from selenium import webdriver

driver = webdriver.Chrome()  # Asegúrate de que el binario esté en el PATH o especifica la ruta completa

driver.get('https://www.example.com')
print(driver.title)

driver.quit()