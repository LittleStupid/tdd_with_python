# from selenium import webdriver
#
# browser = webdriver.Firefox()
# browser.get('http://localhost:8000')

# assert 'Django' in browser.title

from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary('/Applications/Firefox.app/Contents/MacOS/firefox-bin')
browser = webdriver.Firefox(firefox_binary=binary)
browser.get('http://localhost:8000')
assert 'Django' in browser.title
