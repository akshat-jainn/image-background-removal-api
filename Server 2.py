# -*- coding: utf-8 -*-
"""
Created on Sun May  9 11:32:54 2021

@author: Akshat Jain
"""
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import requests
import sys
from selenium.webdriver.chrome.options import Options
print("\n\nEntwickelt von Akshat Jain\nServer 2.0\n")
url="www.google.com"
timeout=10
try:
    request=requests.get('http://www.google.com/').status_code
    print("Mit dem Internet verbunden")
except:
    print("Keine Internetverbindung \nWieder herstellen und erneut starten")
    sys.exit(0)

WINDOW_SIZE="1,1"
chrome_options = Options()
chrome_options.add_argument("--headless")
##chrome_options.add_argument("--window-size=%s" %WINDOW_SIZE)

down_loc=input("\nSpeicherort, an dem Sie die Datei speichern möchten : ")
params = {'behavior': 'allow', 'downloadPath': down_loc}




driver = webdriver.Chrome(options=chrome_options)

driver.execute_cdp_cmd('Page.setDownloadBehavior', params)

driver.minimize_window()








##driver = webdriver.Chrome()
##driver.maximize_window()
driver.get("https://photoshop.adobe.com")









##signup

while(True):
    try:
        time.sleep(5)
        signup=driver.find_element_by_xpath("//*[@id='navbar-container']/div/div/div[2]/div[2]/button")
        signup.click()
        print("Anmeldung")
        break
    except:
        time.sleep(5)
while(True):
    try:
        time.sleep(5)
        email=driver.find_element_by_xpath("//*[@id='EmailPage-EmailField']")
        email.send_keys("hgentfern@protonmail.com")
        email.send_keys(Keys.ENTER)
        print("E-Mail verifiziert")
        break
    except:
        time.sleep(5)
while(True):
    try:
        time.sleep(5)
        passw=driver.find_element_by_xpath("//*[@id='PasswordPage-PasswordField']")
        passw.send_keys("Autom@ted")
        passw.send_keys(Keys.ENTER)
        print("Passwort verifiziert")
        break
    except:
        time.sleep(5)
for i in range(3):
    try:
        m_no=driver.find_element_by_xpath("//*[@id='App']/div/div/section/div/div/section/div/section/div/div/section/section[2]/form/section[2]/button[1]/span")
        m_no.click()
        print("Server-Start")
        break
    except:
        time.sleep(3)

for i in range(3):
    try:
        m_noo=driver.find_element_by_xpath("//*[@id='App']/div/div/section/div/div/section/div/section/div/div/section/footer/div/button/span")
        m_noo.click()
        print("Server-Start")
        break
    except:
        time.sleep(3)      
        
        
time.sleep(5)        
        
##uploading imaages---------------------------------------------------------------------------------------   


##print("searching place to input files")


while(True):
    val= input("Drücken Sie 1, um ein Bild zu verarbeiten, und alles andere, um es zu beenden : ")
    if(val=="1"):
        uploadd=driver.find_element_by_xpath("//*[@id='file-upload']")
        while(True):
            try:
                file_loc=input("Vollständige Bildposition mit seinem Format : ")
                uploadd.send_keys(file_loc)
                break
            except:
                print("Datei nicht gefunden")
        ##upload=driver.find_element_by_xpath("//*[@id='app-container']/div[1]/div/div/button")
        ##upload.click()
        while(True):
            try:
                rem_img=driver.find_element_by_xpath("//*[@id='react-spectrum-7']")
                rem_img.click()
                print("Bildverarbeitung jetzt gestartet")
                break
            except:
                time.sleep(3)
        
##while(True):
##    try:
##        print("proc filter")
##        sel_tfilter=driver.find_element_by_xpath("//*[@id='react-spectrum-79']/div[1]/div[1]/div")
##        sel_tfilter.click()
##        print("filter selected")
##        break
##    except:
##        time.sleep(5)

        while(True):
            try:
                print("Verarbeitung")
                applyt=driver.find_element_by_xpath("//*[@id='editor-container']/div/div/div[2]/button[2]")
                applyt.click()
                print("Verarbeitet")
                break
            except:
                time.sleep(5)
        for i in range(2):
            try:
                print("Rendern von Schatten")
                popup0=driver.find_element_by_xpath("//*[@id='react-spectrum-32']/div/button[1]")
                popup0.click()
                print("Schatten gerendert")
                break
            except:
                time.sleep(1)
        
        for i in range(2):
            try:
                print("Entfernen von Schatten")
                popup=driver.find_element_by_xpath("//*[@id='react-spectrum-31']/div[3]/button[3]")        
                popup.click()
                print("Schatten entfernt")
                break
            except:
                time.sleep(2)

        for i in range(2):
            try:
                print("Bildqualitätsprüfung")
                popup0=driver.find_element_by_xpath("//*[@id='react-spectrum-32']/div/button[1]")
                popup0.click()
                print("Zufriedenstellend")
                break
            except:
                time.sleep(1)
        
        for i in range(2):
            try:
                print("Anwenden des Filters")
                down_timg=driver.find_element_by_xpath("//*[@id='actions-container']/div/button[3]/span")
                down_timg.click()
                print("Filter angewendet")
            except:
                time.sleep(5)
        while(True):
            try:
                print("Herunterladen in Bearbeitung")
                f_down=driver.find_element_by_xpath("//*[@id='react-spectrum-32']/div[2]/div/div[2]/section/div[4]/button[2]")
                f_down.click()
                print("Heruntergeladen")
                break
            except:
                time.sleep(10)
        time.sleep(20)
        print("Bild verarbeitet")
        time.sleep(5)
        driver.get("https://photoshop.adobe.com")
    else:
        print("Auf Wiedersehen")
        sys.exit(0)     
        driver.close()
