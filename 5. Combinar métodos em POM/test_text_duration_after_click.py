import time

from selenium import webdriver

from urban_routes_main_page import UrbanRoutesPage


def test_duration_personal_scooter_option():
    driver = webdriver.Chrome()
    try:
        driver.get(
            'https://cnt-1210bfdf-9609-4ca2-83a8-857200b3bd53.containerhub.tripleten-services.com/?lng=pt'
        )
        driver.implicitly_wait(3)
        time.sleep(2)

        urban_routes_page = UrbanRoutesPage(driver)
        urban_routes_page.enter_locations('East 2nd Street, 601', '1300 1st St')
        urban_routes_page.click_personal_option()
        time.sleep(2)
        urban_routes_page.click_scooter_icon()
        time.sleep(2)

        actual_value = urban_routes_page.get_duration_text()
        expected_value = 'Duração'
        assert expected_value in actual_value, (
            f"Esperado '{expected_value}', mas recebeu '{actual_value}'"
        )
    finally:
        driver.quit()
