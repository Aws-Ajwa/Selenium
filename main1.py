import datetime

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys

now = datetime.datetime.now()

def submit():
    submit = driver.find_element_by_link_text("Submit attendance")
    submit.click()
    saveC = driver.find_element_by_id("id_submitbutton") #test on all courses
    saveC.click()

PATH = "C:\Program Files\Google\Chrome\Application\chrome.exe"


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://s1.ebalqa.courses/ncentermoodle/login/index.php")#the link of the website

#driver.implicitly_wait(5) #wait 5 sec before stating

username = driver.find_element("id","username") #declare the username by the ID
username.send_keys("your username") #entering the username

password = driver.find_element("id","password") #declare the password by the ID
password.send_keys("your password") #entering the password
username.send_keys(Keys.RETURN) #pressing enter


if now.hour == 18:
    #activate at (6:30)
    software = driver.find_element_by_partial_link_text("subject1")
    software.click() 
    #submit attendance the normal way
    attendance = driver.find_element_by_partial_link_text("Attendance") 
    attendance.click() 
    submit()

if now.hour == 15:
    #activate at (3:00)
    CS2 = driver.find_element_by_partial_link_text("subject2")
    CS2.click() 
    attendanceCS = driver.find_element_by_link_text("Attendance") 
    attendanceCS.click() 

    #submit attendance if the normal way doesn't work(by ID)
    submit = driver.find_element_by_link_text("Submit attendance")
    submit.click()
    present = driver.find_element_by_id("id_status_27729") 
    present.click()
    saveC = driver.find_element_by_link_text("Save changes")
                          

if now.hour ==17:
    #activate at (5:00)
    E = driver.find_element_by_partial_link_text("subject3")
    E.click() 
    attendance = driver.find_element_by_partial_link_text("Attendance") 
    attendance.click()  
    submit()

quit()
