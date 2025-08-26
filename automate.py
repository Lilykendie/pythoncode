from selenium import webdriver
from selenium.webdriver.chrome.service import Service

website = "https://ww1.goojara.to/watch-series"
path = r"C:\chromedriver\chromedriver.exe"
 # raw string fixes unicode error

service = Service(path)
driver = webdriver.Chrome(service=service)
driver.get(website)



