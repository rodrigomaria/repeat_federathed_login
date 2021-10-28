from time import sleep

from selenium.webdriver.common.by import By

from credentials import PASSWORD, USER

MANAGER_ADDRESS = "https://stage-manager.azion.com/"
URL_EXPECTED = "https://stage-sso.azion.com/account/switch#brands"


def auto_login_federathed(driver):
    driver.maximize_window()

    # access login
    driver.get(MANAGER_ADDRESS)
    sleep(1)

    # input email on RTM
    usuario_input = driver.find_element(By.ID, "field-email")
    usuario_input.send_keys(USER)
    driver.find_element(By.ID, "button-proceed").click()
    sleep(5)

    # input password on Azure
    federathed_password = driver.find_element(By.NAME, "passwd")
    federathed_password.send_keys(PASSWORD)
    driver.find_element(By.ID, "idSIButton9").click()
    sleep(3)

    # Set option on Azure
    driver.find_element(
        By.XPATH, '//a[text()="Skip for now (14 days until this is required)"]'
    ).click()
    driver.find_element(By.ID, "idBtn_Back").click()
    sleep(3)

    if driver.current_url == URL_EXPECTED:
        is_url_expected = True
    else:
        is_url_expected = False

    driver.quit()
    return is_url_expected
