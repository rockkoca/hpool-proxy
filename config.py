from selenium import webdriver
import requests
import zipfile


def main():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://bhd.hpool.com/download/')
    for a in driver.find_elements_by_tag_name('a'):
        text = a.text.strip()
        if text.startswith('x-proxy') and text.endswith('linux'):
            url = a.get_attribute('href')
            print(url)
            download = requests.get(url, allow_redirects=True)
            with open('x-proxy.zip', 'wb') as file:
                file.write(download.content)
            zip_ref = zipfile.ZipFile('x-proxy.zip', 'r')
            zip_ref.extractall('app')
            zip_ref.close()
            break


if __name__ == '__main__':
    main()
