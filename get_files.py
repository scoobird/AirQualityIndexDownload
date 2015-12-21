import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException #unused?
from selenium.webdriver.common.keys import Keys

baseurl = 'http://www3.epa.gov/airdata/ad_rep_aqi.html'
mydriver = webdriver.Firefox() #initialize a browser
mydriver.implicitly_wait(500) #sets default timeout for all requests
mydriver.get(baseurl)

#must select a year before other form elements appear
mydriver.find_element_by_xpath('//*[@id="year"]/option[text()="2015"]').click()
mydriver.find_element_by_xpath('//*[@id="cbsa"]').click() #click the drop-down box to get elements
selection = Select(mydriver.find_element_by_xpath('//*[@id="cbsa"]'))
for CBSA in [option.text for option in selection.options]:
    if CBSA == 'Select a City (defined as CBSA) ...':
        print CBSA #generate report button does not appear until the second element is selected
    else: #assumes all counties have a report
        print CBSA
        selection.select_by_visible_text(CBSA)
        reportbutton = mydriver.find_element_by_id('launch')
        reportbutton.click()# Generate Report
        download = mydriver.find_element_by_link_text('Download CSV (spreadsheet)')
        download.click() # download csv


mydriver.find_element_by_xpath('//*[@id="year"]/option[text()="2015"]').click()
mydriver.find_element_by_xpath('//*[@id="county"]').click()
selection = Select(mydriver.find_element_by_xpath('//*[@id="county"]'))
for County in [option.text for option in selection.options]:
    if County == 'Select a County ...':
        print County #generate report button does not appear until the second element is selected
    else: #assumes all counties have a report
        print County
        selection.select_by_visible_text(County)
        reportbutton = mydriver.find_element_by_id('launch')
        reportbutton.click()# Generate Report
        download = mydriver.find_element_by_link_text('Download CSV (spreadsheet)')
        download.click() # download csv

mydriver.close()
