import sys

import os
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options


chrome_options = Options()  
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1200x600")
#chrome_options.add_argument("--use-spdy")
chrome_options.add_argument("--disable-http2")
chrome_options.add_argument("--disable-http-cache")
chrome_options.add_argument("--ignore-certificate-errors")

chrome_options.binary_location = '/Applications/Google Chrome Canary.app/Contents/MacOS/Google Chrome Canary'    

driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver"),   chrome_options=chrome_options)  
driver.get(sys.argv[1])
driver.get_screenshot_as_file('test.png')

navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
responseStart = driver.execute_script("return window.performance.timing.responseStart")
domComplete = driver.execute_script("return window.performance.timing.domComplete")
loadeventEnd= driver.execute_script("return window.performance.timing.loadEventEnd")
        
backendPerformance = responseStart - navigationStart
frontendPerformance = domComplete - responseStart
plt = loadeventEnd - navigationStart
    
print "Back End: %s" % backendPerformance
print "Front End: %s" % frontendPerformance
print "Page load time: %s" % plt

driver.close()
