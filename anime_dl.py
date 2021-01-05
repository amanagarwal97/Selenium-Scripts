from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

import re
import time
import os
from selenium.webdriver.firefox.options import Options

REGEX_LINK = re.compile(r'(https?:\S+)')
binary = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'geckodriver.exe')


mega_list = []
adblocker_path = os.path.join(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'uBlock1.xpi'))


def get_link(url):

    options = Options()
    options.add_argument('--headless')
    # options.set_preference("dom.webnotifications.enabled", False)
    driver = webdriver.Firefox(executable_path=binary, options=options)
    driver.install_addon(adblocker_path, temporary=None)
    driver.set_page_load_timeout(60)

    try:
        print('Getting URL')
        driver.get(url)
        element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'skip_button')))
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
    adfile = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'adlinks.txt'))
    print("Fetching adlinks from {}".format(adfile))
    links = adfile.read()

    new_links = re.findall(REGEX_LINK, links)
    megafile = open('megalinks.txt', 'a')
    print("Found {} episodes".format(len(new_links)))

    for num, item in enumerate(new_links, 1):
        link = get_link(item)
        while not link:
            print('Failed. Trying Again')
            link = get_link(item)

        print(num, link)
        mega_list.append(link)
        megafile.write('\n{}'.format(link))
        megafile.flush()

    print('MEGA LINKS:')
    for item in mega_list:
        print(item)

    print(time.time()-start)


if __name__ == '__main__':
    main()
