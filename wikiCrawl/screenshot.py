#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.by import By
from fpdf import FPDF
import glob
import os


def takescreenshot(list_link):
    """
    Create PDF from a given list of URLs

    Input
    list_link : type=list description: List of URLs
    # """
    # executablepath = "/home/jcschec/wikiCrawl/chromedriver"
    #setup chrome headless for retrieving screenshot
    options = webdriver.ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
    driver.set_window_size(1280,1900) # Manual adjustment of size is possible

    dirname = os.path.dirname(__file__)

    for i in range(len(list_link)):
        url = list_link[i]
        driver.get(url)
        path = str(i)+"_image.png"
        driver.find_element(By.TAG_NAME,'body').screenshot(path)
    
    driver.quit()

    # Create FPDF object for creating the PDF
    pdf = FPDF()

    pdf.add_page() # Start by adding a page to PDF
    for filename in glob.glob(dirname + f'/*.png'):
        pdf.image(filename,w=200)

    pdf.output("output.pdf",'F')


# Testing
url = ["https://stackoverflow.com/questions/66311997/why-do-i-get-cannot-save-mode-rgba-error-when-using-pil", "https://datatofish.com/images-to-pdf-python/", "https://stackoverflow.com/questions/72773206/selenium-python-attributeerror-webdriver-object-has-no-attribute-find-el"]
takescreenshot(url)