from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import requests
import re
import time
import os


search_query = input("enter fatassery preferances: ")
print()
driver = webdriver.Chrome()

# def extract_address(soup):
#     address_keywords = ['address', 'location', 'office', 'headquarters']
    
#     address_tag = soup.find('address')
#     if address_tag:
#         return address_tag.get_text(strip=True)
    
#     for tag in soup.find_all(['p', 'div']):
#         if any(keyword in tag.get_text(strip=True).lower() for keyword in address_keywords):
#             address_text = tag.get_text(strip=True)
#             if len(address_text) > 10 and len(address_text) < 200:  
#                 return address_text
    
#     address_pattern = re.compile(r'\d{1,4}\s\w+\s(?:Street|St|Avenue|Ave|Boulevard|Blvd|Road|Rd|Lane|Ln|Way|Square|Sq|Court|Ct|Parkway|Pkwy|Drive|Dr|Place|Pl|Circle|Cir)\s[\w\s,]+')
#     address_match = address_pattern.search(soup.get_text())
#     if address_match:
#         #print(address_match)
#         return address_match.group()

#     return None

# def scrape_contact_info(url):
#     try:
        
#         response = requests.get(url)
        
#         soup = BeautifulSoup(response.content, 'html.parser')

        
#         text = soup.get_text()

#         email_regex = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
#         phone_regex = r'\(?\b[0-9]{3}[-.)\s]?[0-9]{3}[-.\s]?[0-9]{4}\b'

#         emails = re.findall(email_regex, text)
#         phones = re.findall(phone_regex, text)

#         phone = email = None
#         phone_pattern = re.compile(r'\(?\+?[0-9]*\)?[-.\s]?[0-9]+[-.\s]?[0-9]+[-.\s]?[0-9]+')
#         phone_match = phone_pattern.search(soup.get_text())
#         if phone_match:
#             phone = phone_match.group()
#             if len(phone) >= 12:
#                 phone = phone.strip()
#                 phone = phone.replace("\n", "")
#                 phones.append(phone)
        
#         email_pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')
#         email_match = email_pattern.search(soup.get_text())
#         if email_match:
#             # print(email_match)
#             email = email_match.group()
#             emails.append(email)
    
#         emails = list(set(emails))
#         phones = list(set(phones))
#         address = extract_address(soup)

#         # print(f"Found emails: {emails}")
#         # print(f"Found phone numbers: {phones}")
#         # print(f"Found address: {address}")

#         return emails, phones, address
    
#     except Exception as e:
#         emails = list()
#         phones = list()
#         address = None
#         # print(f"Found emails: {emails}")
#         # print(f"Found phone numbers: {phones}")
#         # print(f"Found address: {address}")
#         return emails, phones, address


def scroll_search_results(scrollable_div, pause_time=3):
    last_height = driver.execute_script("return arguments[0].scrollHeight", scrollable_div)
    
    while True:
        driver.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight);", scrollable_div)
        
        time.sleep(pause_time)
        
        new_height = driver.execute_script("return arguments[0].scrollHeight", scrollable_div)
        if new_height == last_height:
            break
        last_height = new_height

def search_google_maps(search_query):
    driver.get("https://maps.google.com")

    search_box = driver.find_element(By.ID, "searchboxinput")

    search_box.send_keys(search_query)

    search_box.send_keys(Keys.RETURN)

def extract_website_links():
    website_links = []
    try:
       
        scrollable_div = driver.find_element(By.CSS_SELECTOR, f'[role="feed"]')
        scroll_search_results(scrollable_div)
        css_selector = f'[class="hfpxzc"]'
        results = driver.find_elements(By.CSS_SELECTOR, css_selector)

        for result in results:
            try:
                website_links.append(result.get_attribute("href"))
                
            except Exception as e:
                print(f"Error extracting website link: {e}")
                continue

    except Exception as e:
        print(f"Error during extraction: {e}")

    return website_links

search_google_maps(search_query)
time.sleep(2)  
website_links = extract_website_links()
driver.quit()
driver = webdriver.Chrome()
more_web_link = []
for link in website_links:

    driver.get(link)
    css_selector = f'[data-item-id="menu"]'
    results = driver.find_elements(By.CSS_SELECTOR, css_selector)

    for result in results:
        try:
            more_web_link.append(result.get_attribute("href"))
            
        except Exception as e:
            print(f"Error extracting website link: {e}")
            continue
    # html = driver.page_source
    # soup = BeautifulSoup(html, 'html.parser')
    # company_name = None
    
    # company_name_tag = soup.find(['h1', 'title'])
    # if company_name_tag:
    #     company_name = company_name_tag.get_text(strip=True)
    # currLink = link
    # dummy = True
    # try:
       
    #     contact_link = WebDriverWait(driver, 1).until(
    #         EC.presence_of_element_located((By.LINK_TEXT, "Contact")) 
    #     )
    #     currLink = contact_link.get_attribute("href")

    # except Exception as e:
    #     dummy = False

    # try:
        
    #     contact_link = WebDriverWait(driver, 1).until(
    #         EC.presence_of_element_located((By.LINK_TEXT, "Contact Us"))  
    #     )
    #     currLink = contact_link.get_attribute("href")

    # except Exception as e:
    #     dummy = False

    # try:
        
    #     contact_link = WebDriverWait(driver, 1).until(
    #         EC.presence_of_element_located((By.LINK_TEXT, "CONTACT"))  
    #     )
    #     currLink = contact_link.get_attribute("href")

    # except Exception as e:
    #     dummy = False
    
    # try:
    #     contact_link = WebDriverWait(driver, 1).until(
    #         EC.presence_of_element_located((By.LINK_TEXT, "CONTACT US"))  
    #     )
    #     currLink = contact_link.get_attribute("href")

    # except Exception as e:
    #     dummy = False
    
    # emails, phones, address = scrape_contact_info(currLink)
    # email = ""
    # phone = ""
    # found = False
    # if len(emails) > 0:
    #     email = emails[0]
    #     found = True
    # if len(phones) > 0:
    #     phone = phones[0]
    #     if len(company_name) > 0:
    #         found = True
    # if found:
    #     print()
    #     # jsonRec = {
    #     #     "records" : [
    #     #         {
    #     #             "fields" : {
    #     #                 "Name": company_name,
    #     #                 "Email": email,
    #     #                 "Company/Org Name": company_name,
    #     #                 "Phone Number": phone,
    #     #                 "Address": address
    #     #             }
    #     #         }
    #     #     ]
    #     # }

    #     # response = requests.post(url, headers=headers, json=jsonRec)
more_web_link = set(more_web_link)
for link in more_web_link:
    print(link)
    


driver.quit()
