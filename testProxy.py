from browsermobproxy import Server
import psutil
import time
import json
from selenium import webdriver
def writeToJSONFile(path, fileName, data):
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)

for proc in psutil.process_iter():
    if proc.name() == "browsermob-proxy":
        proc.kill()

dict = {'port': 8090}
server = Server(path="C:/Users/SUPAWATSIRINTRANON/Desktop/browsermob-proxy-2.1.4/bin/browsermob-proxy", options=dict)

server.start()
time.sleep(1)
proxy = server.create_proxy()
time.sleep(1)

profile = webdriver.FirefoxProfile()
selenium_proxy = proxy.selenium_proxy()
profile.set_proxy(selenium_proxy)
driver = webdriver.Firefox(firefox_profile=profile)


proxy.new_har("google")
driver.get("http://localhost/football%20boot/cart/")
driver.get("http://4bearz.com/test.php")

path = './'
fileName = 'trafficCapture'

writeToJSONFile(path, fileName, proxy.har)

server.stop()
driver.quit()