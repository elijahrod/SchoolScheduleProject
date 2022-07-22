from asyncio.windows_events import NULL
from selenium import webdriver
import course 
import time
import bs4 as bs
import pandas as pd

def login(uName, pWord):
    path = "C:\Windows\chromedriver.exe"
    driver = webdriver.Chrome(path)
    driver.get("https://login.uconn.edu/cas/login?service=https://student.studentadmin.uconn.edu/psp/CSPR/?cmd=start")
    username = driver.find_element_by_id("username") #finds username element on login page
    username.clear()
    username.send_keys(uName) #inserts username
    password = driver.find_element_by_id("password") #finds password element on login page
    password.clear()
    password.send_keys(pWord) #inserts password
    driver.find_element_by_id("button").click() #clicks login
    driver.get("https://student.studentadmin.uconn.edu/psc/CSPR_newwin/EMPLOYEE/SA/c/SSR_STUDENT_FL.SSR_COMPONENT_FL.GBL")
    driver.find_element_by_id("DERIVED_SSR_FL_SSR_DROPPED").click()
    time.sleep(2)

def scanForCourses():
    print("oogabooga")
    ##scan over possible courses and store each class in dictonary by keyword day


def main():
    userName = input("Enter your NETID: ")
    password = input("Enter your password: ")
    login(userName, password)
    scanForCourses()

main()