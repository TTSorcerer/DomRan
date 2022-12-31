from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random

N_EXPANSIONS = 7 # max 7 (changes with extra expansions)
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
DEFAULT_OPTIONS = {
    "Require +2 Action": True,
    "Require Drawer": False,
    "Require Buy": False,
    "Allow Attacks": True,
    "Require Reaction": False,
    "Require Trashing": False,
    "Distribute Cost": False,
    "3+ Alchemy Cards": True,
}
DEFAULT_EXPANSIONS = {
    "Alchemy": False,
    "Dominion II": True,
    "Dark Ages": False,
    "Intrigue": False,
    "Nocturne": False,
    "Prosperity": False,
    "Renaissance": False
}
SORT = "Cost" # either "Cost", "Set", or "Alphabetical"
driver = webdriver.Firefox()
driver.get("https://dominionrandomizer.com")

sets = random.sample(EXPANSIONS, N_EXPANSIONS)
boxes = driver.find_elements(by=By.CLASS_NAME, value="checkbox")
for i in boxes[:18]:
    if i.text in DEFAULT_OPTIONS.keys() and DEFAULT_OPTIONS[i.text] != OPTIONS[i.text]:
        i.click()
    if i.text in sets and not DEFAULT_EXPANSIONS[i.text]:
        i.click()
boxes = driver.find_elements(by=By.CLASS_NAME, value="checkbox")
for i in boxes[18:]:
    if i.text == SORT:
        i.click()
    if (i.text in OPTIONS.keys() and OPTIONS[i.text] != DEFAULT_OPTIONS[i.text]):
        i.click()
        
driver.find_element(By.CLASS_NAME, "standard-button").click()

input("")
driver.close()
