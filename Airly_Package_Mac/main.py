from selenium import webdriver
from datetime import datetime
import requests
import time
import getpass
import os
username = getpass.getuser()
cwd = os.getcwd()
chrome_driver = f"/Users/{username}/Desktop/Airly_Package/ChromeDriver/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver)
driver.get("https://airly.org/map/en/#33.89255,-84.835544,i90171")

button = driver.find_element_by_css_selector("div .sc-pFZIQ")
button.click()
time.sleep(12)
AQ1 = driver.find_elements_by_css_selector("div .sc-licaXj")
particles = driver.find_elements_by_css_selector("div .sc-dwqbIM")

sheetyAPI = "https://api.sheety.co/ec2268bc28d37608590b3b795cf24e1e/airQuality/sheet1"
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
basicHeader = {
    "Authorization": "Basic bHVmZnk6Y29jb2E="
}
AQ = []
def data():
    global pm10, pm25, pm1
    for number, particle in zip(AQ1, particles):
         n = number.text
         AQ.append(n)
    pm10 = AQ[0]
    pm25 = AQ[1]
    pm1 = AQ[2]
data()
if data == None:
    data()
else:
    sheet = {
        "sheet1": {
            "date": today_date,
            "time": now_time,
            "pm10": pm10,
            "pm2":  pm25,
            "pm1":  pm1
        }
    }
    g = requests.post(url=sheetyAPI, json=sheet, headers=basicHeader)
driver.close()