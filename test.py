from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import re

REGEX_LINK = re.compile(r'Episode\s+\d+\s+-\s+(\S+)')
links = ''' Episode 01 - http://destyy.com/wpt4kJ
Episode 02 - http://destyy.com/wpt4kC
Episode 03 - http://destyy.com/wpt4k1
Episode 04 - http://destyy.com/wpt4k6
Episode 05 - http://destyy.com/wpt4lq
Episode 06 - http://destyy.com/wpt4ly
Episode 07 - http://destyy.com/wpt4la
Episode 08 - http://destyy.com/wpt4lh
Episode 09 - http://destyy.com/wpt4lx
Episode 10 - http://destyy.com/wpt4lm
Episode 11 - http://destyy.com/wpt4lT
Episode 12 - http://destyy.com/wpt4lP
Episode 13 - http://destyy.com/wpt4lZ
Episode 14 - http://destyy.com/wpt4lN
Episode 15 - http://destyy.com/wpt4l4
Episode 16 - http://destyy.com/wpt4l9
Episode 17 - http://destyy.com/wpt4zr
Episode 18 - http://destyy.com/wpt4zf
Episode 19 - http://destyy.com/wpt4zl
Episode 20 - http://destyy.com/wpt4zb
Episode 21 - http://destyy.com/wpt4DT
Episode 22 - http://destyy.com/wpt4DP
Episode 23 - http://destyy.com/wpt4DG
Episode 24 - http://destyy.com/wpt4DZ'''


def get_links(url):
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Firefox(firefox_options=options)
    driver.install_addon('C:\\Users\\Aman Agarwal\\PycharmProjects\\selenium\\uBlock0.xpi', temporary=None)
    print("Firefox Headless Browser Invoked")
    driver.get(url)
    try:
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'skip_button')))
        element.click()
    except TimeoutException:
        print('Timeout')

    finally:
        print(driver.current_url)
        driver.quit()


def main():
    new_links = re.findall(REGEX_LINK, links)
    mega_links = []
    for item in new_links:
        get_links(item)

    print(mega_links)


main()
