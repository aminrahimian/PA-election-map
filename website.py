import time
import random
import re
from selenium import webdriver
from selenium.webdriver.support.ui import Select
# Create a browser driver program, for example, Chrome
driver = webdriver.Chrome("yourfilepath")#download your version in https://sites.google.com/chromium.org/driver/?pli=1
# Open the webpage
url = 'https://www.pavoterservices.pa.gov/Pages/PollingPlaceInfo.aspx'
driver.get(url)
driver.implicitly_wait(10)
# Save non-duplicate output content
output_set = set()
first_loop = True
while True:
    if not first_loop:
        driver.back()
        time.sleep(2)  # # Wait for the page to fully load after going back
    #  Locate the dropdown select box
    select_box = Select(driver.find_element("id", "CountyCombo"))
    #  Get the total number of dropdown options
    select_options = len(select_box.options)
    #Generate a random number and select a dropdown option
    random_option = random.randint(1, select_options - 1)
    select_box.select_by_index(random_option)
    time.sleep(1)
    select_box1 = Select(driver.find_element("id", "drpCity"))
    select_options1 = len(select_box1.options)
    random_option1 = random.randint(1, select_options1 - 1)
    select_box1.select_by_index(random_option1)
    time.sleep(1)
    select_box2 = Select(driver.find_element("id", "drpStreetName"))
    select_options2 = len(select_box2.options)
    random_option2 = random.randint(1, select_options2 - 1)
    select_box2.select_by_index(random_option2)
    time.sleep(1)
    #Generate a random number and input it into the input box
    house_number_input = driver.find_element("id", "ctl00_ContentPlaceHolder1_txtHouseNumber")
    label_element = driver.find_element("id", "ctl00_ContentPlaceHolder1_lblHouseNumber")
    label_text = label_element.text
    #  Use regular expressions to extract the number range
    match = re.search(r'(\d+) - (\d+)', label_text)
    if match:
        start_num = int(match.group(1))
        end_num = int(match.group(2))
    else:
        clear_button = driver.find_element("id", "ctl00_ContentPlaceHolder1_ResetButton")
        clear_button.click()
        time.sleep(2)
        continue
    for num in range(start_num, end_num+1):
        random_num = random.randint(start_num, end_num)
        house_number_input.clear()
        house_number_input.send_keys(random_num)
        time.sleep(1)
        search_button = driver.find_element("id", "ctl00_ContentPlaceHolder1_SearchButton")
        search_button.click()
        time.sleep(2)
        #Data not found, perform repeated clicking
        if "Unable to locate polling place information." in driver.page_source:
            break
        
        address_label = driver.find_element("id", "ctl00_ContentPlaceHolder1_lblAddress").text
        street_label = driver.find_element("id", "ctl00_ContentPlaceHolder1_lblStreet1").text
        city_label = driver.find_element("id", "ctl00_ContentPlaceHolder1_lblCity").text
        city_label = driver.find_element("id", "ctl00_ContentPlaceHolder1_lblCity").text
        state_label = driver.find_element("id", "ctl00_ContentPlaceHolder1_lblState").text
        zipcode_label = driver.find_element("id", "ctl00_ContentPlaceHolder1_lblZipCode").text
        # Check if the output already exists in the set, if not, save and print the output
        output = f"{address_label},{street_label},{city_label.strip().replace(',', '')},{state_label},{zipcode_label}"
        if output not in output_set:
            output_set.add(output)
            print("Address:", address_label)
            print("Street:", street_label)
            print("City:", city_label)
            print("State:", state_label)
            print("Zip Code:", zipcode_label)
            # Save to a text file
            with open("data.txt", "a") as file:
                file.write(output + "\n")
        break
    first_loop = False