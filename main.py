import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
from time import sleep
import sys

N_EXPANSIONS = 2
EXPANSIONS = ["Alchemy", "Dominion II", "Dark Ages", "Intrigue", "Nocturne", "Prosperity", "Renaissance"]

OPTIONS = {
    "Require +2 Action": False,
    "Require Drawer": False,
    "Require Buy": False,
    "Allow Attacks": True,
    "Require Reaction": False,
    "Require Trashing": False,
    "Distribute Cost": False,
    "3+ Alchemy Cards": False,
}
DEFAULT_SELECTIONS = {
    "Require +2 Action": True,
    "Require Drawer": False,
    "Require Buy": False,
    "Allow Attacks": True,
    "Require Reaction": False,
    "Require Trashing": False,
    "Distribute Cost": False,
    "3+ Alchemy Cards": True,
}
SORT = "Cost" # either "Cost", "Set", or "Alphabetical"
driver = webdriver.Firefox()
driver.get("https://dominionrandomizer.com")

sets = random.sample(EXPANSIONS, N_EXPANSIONS)
boxes = driver.find_elements(by=By.CLASS_NAME, value="checkbox")
for i in boxes[:18]:
    if i.text == "Dominion II" or i.text == "Allow Attacks" or i.text == "Require +2 Action" or i.text == "3+ Alchemy Cards":
        i.click()
    if i.text == sets[0] or i.text == sets[1]:
        i.click()
boxes = driver.find_elements(by=By.CLASS_NAME, value="checkbox")
for i in boxes[18:]:
    if i.text == SORT:
        i.click()
    if (i.text in OPTIONS.keys() and OPTIONS[i.text] != DEFAULT_SELECTIONS[i.text]):
        i.click()
        
driver.find_element(By.CLASS_NAME, "standard-button").click()

input("")
driver.close()
