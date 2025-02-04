from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from utils.config import BASE_URL

class FormPage:
    def __init__(self,driver):
        self.driver=driver
        self.url=BASE_URL
    
    First_name =(By.ID,"firstName")
    last_name =(By.ID,"lastName")
    email=(By.ID,"userEmail")
    gender=(By.XPATH,"//label[contains(.,'Male')]")
    mobile_number=(By.ID,"userNumber")
    DOB=(By.ID,"dateOfBirthInput")
    subjects=(By.ID,"subjectsContainer")
    hobbies=(By.XPATH, "//label[@for='hobbies-checkbox-1']") 
    current_address=(By.ID,"currentAddress")
    STATE_INPUT = (By.XPATH, "//div[contains(text(),'Select State')]")
    STATE_OPTION = (By.XPATH, "//div[text()='NCR']")
    CITY_DROPDOWN = (By.XPATH, "//div[contains(text(),'Select City')]")
    CITY_OPTION = (By.XPATH, "//div[text()='Delhi']")
    submit=(By.ID,"submit")
    submission_confirmation=(By.CLASS_NAME,"modal-title")

    def open(self):
        self.driver.get(self.url)

    def fill_form(self,Firstname,lastname,email,mobile,address):
        # text_field
        self.driver.find_element(*self.First_name).send_keys(Firstname)
        self.driver.find_element(*self.last_name).send_keys(lastname)
        self.driver.find_element(*self.email).send_keys(email)
        self.driver.find_element(*self.mobile_number).send_keys(mobile)
        self.driver.find_element(*self.current_address).send_keys(address)
        #radio button
        self.driver.find_element(*self.gender).click()
        #checkbox
        self.driver.find_element(*self.hobbies).click()
        # Dateofbirth
        # self.driver.find_element(*self.DOB).send_keys(date)
        # Handle State Dropdown
        self.driver.find_element(*self.STATE_INPUT).click()
        self.driver.find_element(*self.STATE_OPTION).click()

        # Handle City Dropdown
        self.driver.find_element(*self.CITY_DROPDOWN).click()
        self.driver.find_element(*self.CITY_OPTION).click()

    # In FormPage class
    def set_date_of_birth(self, date):
        self.driver.find_element(*self.DOB).send_keys(date)
    
    def submission(self):
        self.driver.find_element(*self.submit).click()

    def is_submitted(self):
        return self.driver.find_element(*self.submission_confirmation).is_displayed()
