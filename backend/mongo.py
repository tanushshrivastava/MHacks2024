from pymongo import MongoClient
import os
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get MongoDB credentials from environment variables
mongoPass = os.getenv("mongoPass")
mongoUser = os.getenv("mongoUser")

# Replace with your actual MongoDB URI
uri = "mongodb+srv://" + mongoUser + ":" + mongoPass + "@greenback.y44sh.mongodb.net/?retryWrites=true&w=majority&appName=greenback"

client = MongoClient(uri)

# Define the database and collection
db = client['greenback']
collection = db['food']

# Path to the folder containing the JSON files
folder_path = 'restaurantsJsons'

# List to hold all the JSON data
all_data = []

# Iterate over each file in the folder
for file_name in os.listdir(folder_path):
    print(file_name)
    if file_name.endswith('.json'):  # Ensure it's a JSON file
        file_path = os.path.join(folder_path, file_name)
        try:
            # Open and load the JSON file
            with open(file_path, 'r') as json_file:
                data = json.load(json_file)
                all_data.append(data)  # Add the JSON data to the list
        except Exception as e:
            print(f"An error occurred while reading {file_name}: {e}")

# Insert all the data into the MongoDB collection
if all_data:
    with open('test.json', 'w', encoding='utf-8') as json_file:
        json.dump(all_data, json_file, indent=4, ensure_ascii=False)
    try:
        result = collection.insert_many(all_data[0])
        print(f"Inserted {len(result.inserted_ids)} documents.")
    except Exception as e:
        print("An error occurred while inserting data into MongoDB:", e)
else:
    print("No JSON data to insert.")

# Close the MongoDB connection
client.close()
