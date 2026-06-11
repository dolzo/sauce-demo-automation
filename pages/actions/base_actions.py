from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

#TODO: Quitar esta importacion, ahora esta activa solo como guia para el intellisense
from selenium.webdriver.chrome.webdriver import WebDriver

class BaseActions:

    def __init__(self, driver:WebDriver):
        self.driver = driver

    # Cargar pagina web
    def load(self, url):
        self.driver.get(url)

    # Handler para esperar por un elemento de la pagina
    def _wait_for_element(self, by_locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(by_locator)
            )
            return self.driver.find_element(*by_locator)
        
        except TimeoutException:
            print("El elemento no fue encontrado")
            return None
        
    # Hacer clic en un elemento
    def click_on_element(self, by_locator):
        element = self._wait_for_element(by_locator)
        
        if not element:
            raise Exception("No se puede clicar en el elemento")
        
        element.click()

    # Escribir en un elemento                
    def type_info(self, by_locator, text_to_type):
        element = self._wait_for_element(by_locator)

        if not element:
            raise Exception("No se puede escribir en el elemento")
        
        element.send_keys(text_to_type)

    # Seleccionar elemento de un dropdown
    def select_from_dropdown(self, by_locator, value):
        element = self._wait_for_element(by_locator)

        if not element:
            raise Exception("No se puede seleccionar el item del dropdown")
        
        dropdown = Select(element)
        dropdown.select_by_value(value)
    
    # Verificar si un elemento esta presente
    def is_displayed(self, by_locator) -> bool:
        element = self._wait_for_element(by_locator)

        if not element:
            return False
        
        return element.is_displayed()

    # Verificar si el elemento esta habilitado
    def is_enabled(self, by_locator) -> bool:
        element = self._wait_for_element(by_locator)
        
        if not element:
            return False
        
        return element.is_enabled()
        