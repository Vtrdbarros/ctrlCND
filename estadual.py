from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time



def open_efisco_website_in_subprocess():
    # Set up the webdriver
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")

    # set up the driver
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://efisco.sefaz.pe.gov.br/")

    try:
        # Clique no botão "Estadual" usando o XPath fornecido
        estadual_button = driver.find_element(By.XPATH, '//*[@id="aay-28"]')
        estadual_button.click()

        # Se você precisar realizar mais ações após clicar no botão, adicione-as aqui

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

    time.sleep(3600) # mantenha o navegador aberto por 1 hora