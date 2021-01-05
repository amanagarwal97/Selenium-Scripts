from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import re
import time
import os
from selenium.webdriver.firefox.options import Options

REGEX_LINK = re.compile(r'(https?:\S+)')
EXTENSION_FOLDER = "extensions"
BINARY_FOLDER = "binaries"
ADLINKS_FILE = "adlinks.txt"
OUTPUT_FILE = "megalinks.txt"
CLOUD_PROVIDER_LIST = ["mega", "google"]
FIREFOX_BINARY_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), BINARY_FOLDER, "geckodriver.exe")
ADBLOCKER_PATH = os.path.join(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                           EXTENSION_FOLDER, "uBlock0_1.32.5b4.firefox.signed.xpi"))


def get_link(driver, url):
    try:
        driver.get(url)
        element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'skip_button')))
        element.click()
        time.sleep(1)
        return driver.current_url if any(provider in driver.current_url for provider in CLOUD_PROVIDER_LIST) else None
    except TimeoutException:
        return None


def get_all_links(urls):
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Firefox(executable_path=FIREFOX_BINARY_PATH, options=options)
    driver.install_addon(ADBLOCKER_PATH, temporary=None)
    driver.set_page_load_timeout(60)
    ads_removed_links = []
    for url in urls:
        print('Getting URL {}'.format(url), end=" ")
        ad_removed_link = get_link(driver, url)
        while not ad_removed_link:
            ad_removed_link = get_link(driver, url)
        print(ad_removed_link)
        ads_removed_links.append(ad_removed_link)

    driver.quit()
    return ads_removed_links


def main():
    start_time = time.time()
    adfile = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), ADLINKS_FILE))
    print("Fetching adlinks from {}".format(adfile.name))
    links = adfile.read()
    new_links = re.findall(REGEX_LINK, links)
    megafile = open(OUTPUT_FILE, 'a')
    print("Found {} episodes".format(len(new_links)))
    mega_list = get_all_links(new_links)
    print('MEGA LINKS:')
    for item in mega_list:
        print(item)
        megafile.write('\n{}'.format(item))
        megafile.flush()
    print(time.time()-start_time)


if __name__ == '__main__':
    main()
