import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the web driver (make sure you have the appropriate web driver executable in your system PATH)
driver = webdriver.Chrome()

# Navigate to the website
driver.get("https://ceoelection.maharashtra.gov.in/searchlist/")

# Wait for the page to load
wait = WebDriverWait(driver, 200)
district_dropdown = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#district")))




# Select the district based on user input (replace 'your_district' with the actual input)
district_select = driver.find_element(By.ID, "district")
district_select.send_keys("your_district")

# Wait for the assembly constituency options to load
wait.until(EC.presence_of_element_located((By.ID, "assembly_constituency")))

# Get the list of assembly constituencies
assembly_constituencies = driver.find_elements(By.CSS_SELECTOR, "#assembly_constituency option")

# Iterate through the assembly constituencies
for assembly_constituency in assembly_constituencies:
    # Select the assembly constituency
    assembly_constituency_select = driver.find_element(By.ID, "assembly_constituency")
    assembly_constituency_select.send_keys(assembly_constituency.get_attribute("value"))

    # Wait for the part options to load
    wait.until(EC.presence_of_element_located((By.ID, "part")))

    # Get the list of parts
    parts = driver.find_elements(By.CSS_SELECTOR, "#part option")

    # Iterate through the parts
    for part in parts:
        # Select the part
        part_select = driver.find_element(By.ID, "part")
        part_select.send_keys(part.get_attribute("value"))

        # Wait for the captcha to load (you'll need to implement captcha handling here)
        time.sleep(5)  # Replace this with your captcha handling code

        # Click on the 'Open PDF' button
        open_pdf_button = driver.find_element(By.ID, "open_pdf")
        open_pdf_button.click()

        # Wait for the PDF to be downloaded (you'll need to handle the file download here)
        time.sleep(5)  # Replace this with your file download handling code

        # Go back to the previous page
        driver.back()

# Close the browser
driver.quit()
