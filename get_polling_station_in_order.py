
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
m=0
# Save non-duplicate output content
output_set = set()
#  Locate the dropdown select box
select_box = Select(driver.find_element("id", "CountyCombo"))
select_options = len(select_box.options)

for i in range(1, select_options):
    select_box.select_by_index(i)
    time.sleep(1) # Wait for the page to fully load after going back

    select_box1 = Select(driver.find_element("id", "drpCity"))
    select_options1 = len(select_box1.options)

    for j in range(1, select_options1):
        select_box1.select_by_index(j)
        time.sleep(1)
        
        if j >= 2:
            select_box.select_by_index(i)

        time.sleep(1)
        select_box2 = Select(driver.find_element("id", "drpStreetName"))
        select_options2 = len(select_box2.options)
        time.sleep(1)

        for k in range(1, select_options2):
            if k>=2:
                select_box = Select(driver.find_element("id", "CountyCombo"))
                select_options = len(select_box.options)
                select_box.select_by_index(i)
                time.sleep(1)
                select_box1 = Select(driver.find_element("id", "drpCity"))
                select_options1 = len(select_box1.options)
                select_box1.select_by_index(j)
                time.sleep(1)
                select_box2 = Select(driver.find_element("id", "drpStreetName"))
                select_options2 = len(select_box2.options)
            select_box2.select_by_index(k)
            time.sleep(1)


            # Generate a random number and input it into the input box
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
            
            num_range = end_num - start_num + 1
            repeated_results = 0
            n_reached = False
            n=0
            while repeated_results < 30 and not n_reached:
                for n in range(num_range):
                    if n>=1:
                        select_box = Select(driver.find_element("id", "CountyCombo"))
                        select_options = len(select_box.options)
                        select_box.select_by_index(i)
                        time.sleep(1)
                        select_box1 = Select(driver.find_element("id", "drpCity"))
                        select_options1 = len(select_box1.options)
                        select_box1.select_by_index(j)
                        time.sleep(1)
                        select_box2 = Select(driver.find_element("id", "drpStreetName"))
                        select_options2 = len(select_box2.options)
                        select_box2.select_by_index(k)
                        time.sleep(1)
                    num = start_num + n
                    if num_range > 100:
                        num = start_num + 10 * n
                    if num_range > 50 and num_range <= 100:
                        num = start_num + 5 * n
                    house_number_input = driver.find_element("id", "ctl00_ContentPlaceHolder1_txtHouseNumber")
                    
                    house_number_input.send_keys(num)
                    time.sleep(1)

                    search_button = driver.find_element("id", "ctl00_ContentPlaceHolder1_SearchButton")
                    search_button.click()
                    time.sleep(2)

                    # Data not found, perform repeated clicking
                    if "Unable to locate polling place information." in driver.page_source:
                        driver.back()
                        time.sleep(2)
                        n_reached= True
                        break

                    address_label = driver.find_element("id", "ctl00_ContentPlaceHolder1_lblAddress").text
                    street_label = driver.find_element("id", "ctl00_ContentPlaceHolder1_lblStreet1").text
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
                        with open("data5.txt", "a") as file:
                            file.write(output + "\n")

                        # Checks a counter for consecutive identical results
                        if len(output_set) == 1:
                            repeated_results += 1
                        else:
                            repeated_results = 0

                    # Determine whether to achieve the same result 30 times in a row
                    if repeated_results == 30:
                        break
                
                    
                    driver.back()
                    time.sleep(2)
                if n == num_range - 1:
                    n_reached = True
                if repeated_results == 30 or n_reached:
                    break
            
driver.quit()
