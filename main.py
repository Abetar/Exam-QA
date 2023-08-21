from distutils.util import strtobool
from inspect import isframe
from itertools import count
from os import link
from shelve import Shelf
from threading import local
from turtle import st
from typing import Counter
from attr import attr
import re
from numpy import save
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from lxml import etree
import time
from lxml import html
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from openpyxl import load_workbook

PATH = './chromedriver'
driver = webdriver.Chrome(PATH)


def escenario1(product):
    # In this section we entered to the page, clear the search bar in case have content, and search "Playstation"
    driver.get("https://www.liverpool.com.mx/tienda/home")
    searchBar = driver.find_element(By.XPATH, "//div[@class = 'm-header__searchBar']//input[@id = 'mainSearchbar']")
    searchBar.clear()
    searchBar.send_keys(product)
    searchButton = driver.find_element(By.XPATH, "//div[@class = 'm-header__searchBar']//div[@class = 'input-group-append']//button[@class = 'input-group-text']")
    searchButton.click()

    time.sleep(5)

    # Select the the first 
    playResults = driver.find_elements(By.XPATH, "//div[@class = 'o-listing__products']//ul[@class = 'm-product__listingPlp']//li")

    playResultName = playResults[0].find_element(By.XPATH, "//figure//figcaption//article")
    playResultPrice = playResults[0].find_element(By.XPATH, "//figure//figcaption//div[@class = 'o-card__image__container']//p[@class = 'a-card-discount']")
    playResultPriceCents = playResults[0].find_element(By.XPATH, "//figure//figcaption//div[@class = 'o-card__image__container']//p[@class = 'a-card-discount']//sup[@class = 'undefined']")

    if(playResultPrice.text.find(playResultPriceCents.text) != -1):
        playResultPrice = playResultPrice.text.replace(playResultPriceCents.text, "")
    else:
        print("Hola")
        pass
    
    print("Product Name: " + playResultName.text)
    print("Price: " + playResultPrice + "." + playResultPriceCents.text)

def escenario2(product):
    # In this section we entered to the page, clear the search bar in case have content, and search "smart TV"
    driver.get("https://www.liverpool.com.mx/tienda/home")
    searchBar = driver.find_element(By.XPATH, "//div[@class = 'm-header__searchBar']//input[@id = 'mainSearchbar']")
    searchBar.clear()
    searchBar.send_keys(product)
    searchButton = driver.find_element(By.XPATH, "//div[@class = 'm-header__searchBar']//div[@class = 'input-group-append']//button[@class = 'input-group-text']")
    searchButton.click()
    time.sleep(5)

    # Filtering the results
    print("Selecting the price")
    filterPrice = driver.find_element(By.ID, "variants.prices.sortPrice-10000-700000")
    filterPrice.click()
    time.sleep(2)

    print("Selecting the Brand")
    filterBrandBtn = driver.find_element(By.ID, "Marcas")
    filterBrandBtn.click()

    filterBrand = driver.find_element(By.ID, "brand-SONY")
    filterBrand.click()
    time.sleep(2)

    print("Selecting the Size")
    btnShowMore = driver.find_element(By.XPATH, "//a[@id = 'Tamao']")
    btnShowMore.click()

    filterSize = driver.find_element(By.ID, "variants.normalizedSize-55 pulgadas")
    filterSize.click()
    time.sleep(2)

    totalProducts = driver.find_element(By.XPATH, "//p[@class = 'a-plp-results-title']")
    totalProductsAux =  re.sub('[^0-9]','',totalProducts.text)


    print("This is the total product count: " + totalProductsAux)

def escenario3():
    driver.get("https://www.liverpool.com.mx/tienda/home")

    time.sleep(5)

    action = ActionChains(driver)
    dropdownCategories = driver.find_element(By.XPATH, "//span[@class = 'a-header__strongLink nav-desktop-menu-action pr-3 pb-3']")
    action.move_to_element(dropdownCategories).perform()

    print("Selecting Belleza from Mega Menu")

    selectOptions = driver.find_elements(By.XPATH, "//ul[@role = 'menu']//div[@class = 'm-megamenu__category_menu-item']")

    bellezaOption = selectOptions[5]

    action.move_to_element(bellezaOption).perform()

    print("Selecting Perfumes Hombre")

    driver.get("https://www.liverpool.com.mx/tienda/perfumes-hombre/catst44258581")


    showMoreBrands = driver.find_element(By.XPATH, "//a[@id = 'Marcas']")
    showMoreBrands.click()
    
    time.sleep(2)

    diorOption = driver.find_element(By.XPATH, "//input[@id = 'brand-DIOR']")
    diorOption.click()

    time.sleep(3)

    totalProducts = driver.find_element(By.XPATH, "//p[@class = 'a-plp-results-title']")
    totalProductsAux =  re.sub('[^0-9]','',totalProducts.text)


    print("This is the total product count: " + totalProductsAux)




print("----- 1st Test Case Begins -----")
escenario1("playstation")
print("----- 1st Test Case Ends -----")
print("----- 2nd Test Case Begins -----")
escenario2("smart TV")
print("----- 2nd Test Case Ends -----")
print("----- 3rd Test Case Begins -----")
escenario3()
print("----- 3rd Test Case Ends -----")

driver.quit()
