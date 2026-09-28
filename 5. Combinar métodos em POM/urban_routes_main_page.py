from selenium.webdriver.common.by import By


# Definição da classe da página, dos localizadores e do método na classe
class UrbanRoutesPage:
    # Localizadores como atributos de classe
    FROM_LOCATOR = (By.ID, 'from')
    TO_LOCATOR = (By.ID, 'to')
    PERSONAL_OPTION_LOCATOR = (By.XPATH, '//div[text()="Personal"]')
    SCOOTER_ICON_LOCATOR = (By.XPATH, '//img[@src="/static/media/scooter.cf9bb57e.svg"]')
    CARSHARING_ICON_LOCATOR = (By.XPATH, '//img[@src="/static/media/drive.05beabd2.svg"]')
    BOOK_BUTTON_LOCATOR = (By.XPATH, '//button[@class="button round"]')
    CAMPING_LOCATOR = (By.XPATH, '//div[text()="Camping"]')
    AUDI_TEXT_LOCATOR = (By.XPATH, '//div[contains(text(),"Audi A3 Sedã")]')
    ADD_DRIVER_LICENSE_LOCATOR = (By.XPATH, '//div[@class="np-text" and contains(text(),"Adicionar carteira de motorista")]')
    FIRST_NAME_LOCATOR = (By.ID, 'firstName')
    LAST_NAME_LOCATOR = (By.ID, 'lastName')
    DATE_OF_BIRTH_LOCATOR = (By.ID, 'birthDate')
    NUMBER_LOCATOR = (By.XPATH, '//input[@id="number" and @placeholder="01 01 123456"]')
    ADD_BUTTON_LOCATOR = (By.XPATH, '//button[@type="submit" and not(@disabled) and contains(@class,"button")]')
    ADD_DRIVER_LICENSE_TITLE_LOCATOR = (By.XPATH, '//div[@class="head" and contains(text(),"Adicionar carteira de motorista")]')
    VERIFICATION_TEXT_LOCATOR = (By.XPATH, '//*[contains(text(),"Obrigado!")]')
    DURATION_TEXT_LOCATOR = (By.XPATH, '//div[contains(text(),"Duração")]')

    def __init__(self, driver):
        self.driver = driver  # Inicializar o driver

    def enter_from_location(self, from_text):
        # Inserir De
        self.driver.find_element(*self.FROM_LOCATOR).send_keys(from_text)

    def enter_to_location(self, to_text):
        # Inserir Para
        self.driver.find_element(*self.TO_LOCATOR).send_keys(to_text)

    def click_personal_option(self):
        # Clicar Personal
        self.driver.find_element(*self.PERSONAL_OPTION_LOCATOR).click()

    def click_carsharing_icon(self):
        # Clique no ícone Carsharing
        self.driver.find_element(*self.CARSHARING_ICON_LOCATOR).click()

    def click_scooter_icon(self):
        self.driver.find_element(*self.SCOOTER_ICON_LOCATOR).click()

    def click_book_button(self):
        # Clique no botão Reservar
        self.driver.find_element(*self.BOOK_BUTTON_LOCATOR).click()

    def click_camping(self):
        # Clique em Camping
        self.driver.find_element(*self.CAMPING_LOCATOR).click()

    def get_audi_text(self):
         # Retornar o texto "Audi"
        return self.driver.find_element(*self.AUDI_TEXT_LOCATOR).text

    def click_add_driver_license(self):
        # Clicar em Adicionar carteira de motorista
        self.driver.find_element(*self.ADD_DRIVER_LICENSE_LOCATOR).click()

    def enter_first_name(self, first_name):
        # Digitar Nome
        self.driver.find_element(*self.FIRST_NAME_LOCATOR).send_keys(first_name)

    def enter_last_name(self, last_name):
        # Digitar Sobrenome
        self.driver.find_element(*self.LAST_NAME_LOCATOR).send_keys(last_name)

    def enter_date_of_birth(self, date_of_birth):
        # Inserir Data de nascimento
        self.driver.find_element(*self.DATE_OF_BIRTH_LOCATOR).send_keys(date_of_birth)

    def enter_number(self, number):
        # Digitar Número
        self.driver.find_element(*self.NUMBER_LOCATOR).send_keys(number)

    def click_title(self):
        # Clicar Adicionar um título de carteira de motorista
        self.driver.find_element(*self.ADD_DRIVER_LICENSE_TITLE_LOCATOR).click()

    def click_add_button(self):
        # Clicar no botão Adicionar
        self.driver.find_element(*self.ADD_BUTTON_LOCATOR).click()

    def get_verification_text(self):
        # Retornar o texto de verificação
        for element in self.driver.find_elements(*self.VERIFICATION_TEXT_LOCATOR):
            text = (element.text or element.get_attribute('textContent') or '').strip()
            if text:
                return text
        return ''

    def get_duration_text(self):
        return self.driver.find_element(*self.DURATION_TEXT_LOCATOR).text

    def enter_locations(self, from_text, to_text):
        self.enter_from_location(from_text)
        self.enter_to_location(to_text)

    # Etapa para inserir "De", "Para" e clicar em "personal_option", "carsharing_icon", "book_button" e "camping"
    def choose_camping_car(self, from_text, to_text):
        self.enter_locations(from_text, to_text)
        self.click_personal_option()
        self.click_carsharing_icon()
        self.click_book_button()
        self.click_camping()

    # Etapa para clicar em "add_driver_license"; para digitar "first_name", "last_name", "date_of_birth", "number"; e
    # para clicar em "title" e "add_button"
    def adding_driver_license(self, first_name, last_name, date_of_birth, number):
        self.click_add_driver_license()
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_date_of_birth(date_of_birth)
        self.enter_number(number)
        self.click_title()
        self.click_add_button()
