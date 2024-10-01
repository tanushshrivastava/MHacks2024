from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
import random
from itertools import combinations
import os
#from dotenv import load_dotenv

# Load environment variables
#load_dotenv()
#from dotenv import load_dotenv

#load_dotenv()
app = FastAPI()

# CORS settings to allow communication between frontend and backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load environment variables
#load_dotenv()

# Get MongoDB credentials from environment variables
mongoPass = os.getenv("mongoPass")
mongoUser = os.getenv("mongoUser")

# Replace with your actual MongoDB URI
uri = "mongodb+srv://username:password@greenback.y44sh.mongodb.net/?retryWrites=true&w=majority&appName=greenback"

# MongoDB connection
client = MongoClient(uri)  # Replace with your MongoDB connection string
db = client['greenback']
collection = db['food']


def find_best_combination(items, calorie_threshold, protein_threshold, price_threshold):
    """Finds the best combination of items closest to but under the specified thresholds."""
    best_combination = None
    min_difference = float('inf')

    # Iterate through all combinations of up to three items
    for r in range(1, 4):
        for combo in combinations(items, r):
            total_calories = sum(item.get('calories', 0) for item in combo)
            total_protein = sum(item.get('protein', 0) for item in combo)
            total_price = sum(item.get('price', 0) for item in combo)

            # Skip combinations that exceed any threshold
            if total_calories > calorie_threshold or total_protein > protein_threshold or total_price > price_threshold:
                continue

            # Calculate the difference from the thresholds
            difference = abs(calorie_threshold - total_calories) + \
                         abs(protein_threshold - total_protein) + \
                         abs(price_threshold - total_price)

            # Update best combination if this one is closer
            if difference < min_difference:
                min_difference = difference
                best_combination = {
                    "items": [item.get('name', 'Unknown Item') for item in combo],
                    "total_calories": total_calories,
                    "total_protein": total_protein,
                    "total_price": total_price,
                    "restaurant": combo[0].get('restaurant', 'Unknown Place')  # Get the restaurant name
                }

    # If no valid combination is found, pick a random item from the available list
    if not best_combination and items:
        print("No suitable combination found, selecting a random item.")
        random_item = random.choice(items)
        best_combination = {
            "items": [random_item.get('name', 'Unknown Item')],
            "total_calories": random_item.get('calories', 0),
            "total_protein": random_item.get('protein', 0),
            "total_price": random_item.get('price', 0),
            "restaurant": random_item.get('restaurant', 'Unknown Place')  # Get the restaurant name
        }

    return best_combination


@app.get("/api/search")
def search_meals(day: str, calorie_threshold: float, protein_threshold: float, price_threshold: float):
    """
    Searches for meals on a specific day and returns the best combination of items for breakfast, lunch, and dinner
    that meet the calorie, protein, and price thresholds. If no suitable combination is found, it picks a random item.
    """
    print(f"Searching for meals on: {day}")

    # Fetch all entries for the given day
    entries = list(collection.find({"day": day}))
    if not entries:
        print("No entries found for the specified day.")
        raise HTTPException(status_code=404, detail=f"No entries found for the day: {day}")

    # Filter for breakfast, lunch, and dinner entries
    breakfast_entries = [
        entry for entry in entries 
        if entry.get('meal_time', '').lower() == 'breakfast' or entry.get('meal_type', '').lower() == 'breakfast'
    ]

    lunch_entries = [
        entry for entry in entries 
        if entry.get('meal_time', '').lower() == 'lunch' or entry.get('meal_type', '').lower() == 'lunch'
    ]

    dinner_entries = [
        entry for entry in entries 
        if entry.get('meal_time', '').lower() == 'dinner' or entry.get('meal_type', '').lower() == 'dinner'
    ]

    # Function to get the best combination for a specific meal
    def get_best_combination(meal_entries, meal_calories, meal_protein, meal_price):
        all_items = []
        for meal in meal_entries:
            for place in meal.get('places', meal.get('restaurants', [])):  # Handle both 'places' and 'restaurants'
                for item in place.get('items', []):
                    all_items.append({
                        "name": item.get('name', 'Unknown Item'),
                        "calories": item.get('calories', 0),
                        "protein": item.get('protein', 0),
                        "price": item.get('price', 0),
                        "restaurant": place.get('restaurant', 'Unknown Place')  # Get the restaurant name
                    })

        # If no suitable combination is found, pick a random item
        if not all_items:
            return {"items": ["No suitable items available"], "total_calories": 0, "total_protein": 0, "total_price": 0, "restaurant": "Unknown Place"}
        
        return find_best_combination(all_items, meal_calories, meal_protein, meal_price)

    # Divide thresholds into 3 parts for each meal
    meal_calories = calorie_threshold / 3
    meal_protein = protein_threshold / 3
    meal_price = price_threshold / 3

    # Get the best combination for each meal
    best_breakfast = get_best_combination(breakfast_entries, meal_calories, meal_protein, meal_price)
    best_lunch = get_best_combination(lunch_entries, meal_calories, meal_protein, meal_price)
    best_dinner = get_best_combination(dinner_entries, meal_calories, meal_protein, meal_price)

    # Return the results for breakfast, lunch, and dinner
    return {
        "breakfast": best_breakfast,
        "lunch": best_lunch,
        "dinner": best_dinner
    }
