from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

LINKS = ['https://mega.nz/#!oXxnXI5I!WVH-2jSYeNgkPLBEqWpn_0U9C3vXSgaeVo3wRq6uVQY',
         'https://mega.nz/#!hCBnUJDL!umiTNBpAKuGGK4TQh8aYPBRyu5mBinyyf8Kg_OhYzBM',
         'https://mega.nz/#!wGB3wbDD!XKld36Exg-LVpOHzNPzBSLODyQ6d5DW9HppDUQ20MYA',
         'https://mega.nz/#!tTBlnIaI!1yCAb57fy1S4z6n9__PU1Y10N5gOtHD3bXN3THA6Ry8']


def add_to_mega(links):
    driver = webdriver.Firefox()
    for link in links:
        print(link)
        try:
            driver.get(link)
            element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                    '.video-mode-wrapper > div:nth-child(2) > div:nth-child(2)')))
            element.click()
        except TimeoutException:
            print('Timeout')

        finally:
            driver.quit()


def main():
    add_to_mega(LINKS)


main()
