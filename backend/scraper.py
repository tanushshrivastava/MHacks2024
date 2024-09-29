import requests
from bs4 import BeautifulSoup
import json
import os
# Step 1: Specify the URL of the website from which to fetch the content
def scrape(url, hall, day, totalDay):
   response = requests.get(url)
   if response.status_code == 200:
        html_content = response.text
        # Step 3: Parse the content using BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Prepare to append or write new data
        results = []
        file_path = "diningHallJsons/" + day + totalDay +".json"
        if os.path.exists(file_path):
            # Read existing data first if file exists
            with open(file_path, 'r', encoding='utf-8') as file:
                try:
                    results = json.load(file)  # Load existing data
                except json.JSONDecodeError:
                    results = []  # If JSON is empty or invalid, start a new list

        # Step 4: Extract data including detailed nutrition information
        for h3 in soup.find_all('h3')[2:]:  # Starting from the third h3
            section = {
                'meal_time': h3.get_text(strip=True),
                'day': day,
                'type': "diningHall",
                'places': []
            }

            div_courses = h3.find_next('div', class_='courses')
            if div_courses:
                h4_tags = div_courses.find_all('h4')
                for h4 in h4_tags:
                    offering = {
                        'restaurant': hall + " - " + h4.get_text(strip=True),
                        'items': []
                    }

                    ul_items = h4.find_next('ul', class_='items')
                    if ul_items:
                        for li in ul_items.find_all('li'):
                            item_name_div = li.find('div', class_='item-name')
                            if item_name_div:
                                item_name = item_name_div.get_text(strip=True)
                                item = {
                                    'name': item_name  # Start the dictionary with just the name
                                }
                                nutrition_div = li.find('div', class_='nutrition')
                                if nutrition_div:
                                    table = nutrition_div.find('table', class_='nutrition-facts')
                                    if table:
                                        for row in table.find_all('tr'):
                                            cols = row.find_all('td')
                                            if len(cols) == 1 and 'Calories' in cols[0].get_text():
                                                calorie_text = cols[0].get_text()
                                                # Extract only the numeric part for calories
                                                calories = [int(s) for s in calorie_text.split() if s.isdigit()]
                                                if calories:
                                                    item['calories'] = calories[0]  # Add directly to item
                                            elif len(cols) == 2 and 'Protein' in cols[0].get_text():
                                                protein_text = int((cols[1].get_text().split(' ')[0])[:-1])
                                                item['protein'] = protein_text  # Add directly to item
                                            item['price'] = 0

                                if 'calories' in item or 'protein' in item:  # Check if any nutrition data was added
                                    offering['items'].append(item)

                    section['places'].append(offering)

            results.append(section)

        # Write the updated data to the JSON file
        with open(file_path, 'w', encoding='utf-8') as json_file:
            json.dump(results, json_file, indent=4, ensure_ascii=False)

   else:
        print(f"Failed to retrieve the page: Status code {response.status_code}")