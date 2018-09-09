#import libraries

#import libraries for selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#Imports for beautiful Soup
from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup

#Imports for Excel Datasets
from datetime import datetime
import pyrebase
import pandas as pd
import csv

#create chrome window to handle all the web urls
CHROME_PATH = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
CHROMEDRIVER_PATH = r"C:\Users\lawalo\Desktop\chromedriver_win32\chromedriver.exe"
WINDOW_SIZE = "1920,1080"

#Custom option to stop chrome window from opening
chrome_options = Options()  
chrome_options.add_argument("--headless")  
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
chrome_options.binary_location = CHROME_PATH

driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH) #, chrome_options=chrome_options)

page_url = "https://namemc.com/name/"

known_names = []
known_reason = []

def scrape_with_Xpath(name_path):
	the_name = driver.find_element_by_xpath(name_path)

	return the_name.text


#open excel file and push all image data to database. 
with open("known_Rayers.csv") as csvDataFile:
	csvReader = csv.reader(csvDataFile)
	for data in csvReader:
		data = list(csv.reader(csvDataFile))
		x = 0

		for x in range(len(data)):
			known_names.append(data[x][0])
			known_reason.append(data[x][1])


config = {"apiKey": "AIzaSyCKQl74vgI56uxAGqVWYwAO_YmR6XoFwGo",  
"authDomain": "images-5a37d.firebaseapp.com",  
"databaseURL": "https://images-5a37d.firebaseio.com",  
"storageBucket": "images-5a37d.appspot.com",  
"serviceAccount": "serviceAccountCredentials.json"
}

firebase = pyrebase.initialize_app(config)

auth = firebase.auth() 
#authenticate a user
user = auth.sign_in_with_email_and_password("olawal196@gmail.com", "JimmyCarter123")

user['idToken']

#open firebase database
db = firebase.database()

#Push image data to database.
def input_image_data(name, reason):
	data = {"name": name, "reason": reason}
	db.child("image_refrences").push(data, user['idToken'])

def main(): 
	x = 0
	name_xPath = """/html/body/main/div[3]/div[1]/div[1]/div/a/div/div[1]/h3"""
	for x in range(len(known_names)):
		if (x % 22 == 0):
			time.sleep(2)
		else:
			driver.get(page_url + known_names[x])
			known_names[x] = scrape_with_Xpath(name_xPath)

			input_image_data(known_names[x], known_reason[x])
		print(x)

	print(done)




if __name__ == "__main__":
	main()