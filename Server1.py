# -*- coding: utf-8 -*-
"""
Created on Sat May  8 17:24:43 2021

@author: Akshat Jain
"""
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
import sys
import requests
url="www.google.com"
timeout=10
try:
    request=requests.get('http://www.google.com/').status_code
    print("Mit dem Internet verbunden")
except:
    print("Keine Internetverbindung \nWieder herstellen und erneut starten")
    sys.exit(0)
    
print("\n\nTo Stop Program Press Ctrl+C.\nUm das Programm zu stoppen, drücken Sie Strg+C.\n\n")

print("Initialisieren des Servers\n")


WINDOW_SIZE="1,1"
chrome_options = Options()
chrome_options.add_argument("--headless")
##chrome_options.add_argument("--window-size=%s" %WINDOW_SIZE)

down_loc=input("\nSpeicherort, an dem Sie die Datei speichern möchten : ")
params = {'behavior': 'allow', 'downloadPath': down_loc}




driver = webdriver.Chrome(options=chrome_options)

driver.execute_cdp_cmd('Page.setDownloadBehavior', params)

driver.minimize_window()

print("ServerInitialisiert\n")

while(True):
    val= input("Drücken Sie 1, um ein Bild zu verarbeiten, und alles andere, um es zu beenden : ")
    if(val=="1"):
        driver.get("https://www.experte.com/background-remover")
        ##upload=driver.find_element_by_xpath("/html/body/cms/div[1]/main/page/content/page/lazy-loader/remove-bg/div/div/div/div[1]/div[1]")
        ##upload.click()
        
        s=driver.find_element_by_xpath("/html/body/cms/div[1]/main/page/content/page/lazy-loader/remove-bg/div/div/div/div[1]/input")
        while(True):
            try:
                file_loc=input("Vollständige Bildposition mit seinem Format : ")
                s.send_keys(file_loc)
                break
            except:
                print("Datei nicht gefunden")
                
        time.sleep(2)
        
        
        
        print("Verarbeitungsbild")
        
        while(True):
                try:
                    download=driver.find_element_by_xpath("/html/body/cms/div[1]/main/page/content/page/lazy-loader/remove-bg/div/div/div/a")
                    download.click()
                    break
                except:
                    time.sleep(5)
        print("Bild verarbeitet")  
    else :
        print("Auf Wiedersehen")
        driver.close()        
        sys.exit(0)
         
        
        
    
    
    
