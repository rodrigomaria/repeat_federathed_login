from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from automation import auto_login_federathed

count = 0
chrome_driver = ChromeDriverManager().install()

for each in range(0, 100):
    print(f"Execution number: {count}")
    # chrome driver
    driver = webdriver.Chrome(chrome_driver)
    result = auto_login_federathed(driver)
    if result:
        count += 1
    else:
        print(f"ERROR: Execution with success: {count}")
        break
