from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import re
import time
from selenium.webdriver.firefox.options import Options

REGEX_LINK = re.compile(r'(https?:\S+)')
links = '''
Episode 01 - http://corneey.com/wUDtQf
Episode 02 - http://corneey.com/wUDtQl
Episode 03 - http://corneey.com/wUDtQE
Episode 04 - http://corneey.com/wUDtQI
Episode 05 - http://corneey.com/wUDtQD
Episode 06 - http://corneey.com/wUDtQK
Episode 07 - http://corneey.com/wUDtQV
Episode 08 - http://corneey.com/wUDtQ2
Episode 09 - http://corneey.com/wUDtQ7
Episode 10 - http://corneey.com/wUDtWw
Episode 11 - http://corneey.com/wUDtWu
Episode 12 - http://corneey.com/wUDtWs
Episode 01 - http://ceesty.com/wuXQzw
Episode 02 - http://ceesty.com/wuXQzu
Episode 03 - http://ceesty.com/wuXQzs
Episode 04 - http://ceesty.com/wuXQzj
Episode 05 - http://ceesty.com/wuXQzc
Episode 06 - http://ceesty.com/wuXQzQ
Episode 07 - http://ceesty.com/wuXQzA
Episode 08 - http://ceesty.com/wuXQzX
Episode 09 - http://ceesty.com/wuXQzM
Episode 10 - http://ceesty.com/wuXQx0
Episode 11 - http://ceesty.com/wuXQxt
Episode 12 - http://ceesty.com/wuXQxp
Episode 13 - http://ceesty.com/wuXQxg
Episode 14 - http://ceesty.com/wuXQxn
Episode 15 - http://ceesty.com/wuXQxR
Episode 16 - http://ceesty.com/wuXQxO
Episode 17 - http://ceesty.com/wuXQxF
Episode 18 - http://ceesty.com/wuXQxL
Episode 19 - http://ceesty.com/wuXQxB
Episode 20 - http://ceesty.com/wuXQx3
Episode 21 - http://ceesty.com/wuXQXd
Episode 22 - http://ceesty.com/wuXQXk
Episode 23 - http://ceesty.com/wuXQXW
Episode 24 - http://ceesty.com/wuXQXU
Episode 25 - http://ceesty.com/wuXQXS
'''

mega_list = []


def get_link(url):

    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Firefox(firefox_options=options)
    driver.install_addon('C:\\Users\\Aman Agarwal\\PycharmProjects\\selenium\\uBlock0.xpi', temporary=None)
    driver.set_page_load_timeout(60)
    try:
        print('Getting URL')
        driver.get(url)
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'skip_button')))
        element.click()
        if 'mega' in driver.current_url:
            return driver.current_url
        else:
            return False
    except TimeoutException:
        return False
    finally:
        driver.quit()


def main():
    start = time.time()
    new_links = re.findall(REGEX_LINK, links)

    for item in new_links:
        link = get_link(item)
        while not link:
            print('Failed. Trying Again')
            link = get_link(item)

        print(link)
        mega_list.append(link)

    print('MEGA LINKS:')
    for item in mega_list:
        print(item)
    print(time.time()-start)


if __name__=='__main__':
    main()
