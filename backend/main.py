from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
import random
from itertools import combinations

app = FastAPI()

# CORS settings to allow communication between frontend and backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# MongoDB connection
client = MongoClient("mongodb+srv://ayannair23:piZnOuJDco3Eurni@greenback.y44sh.mongodb.net/?retryWrites=true&w=majority&appName=greenback")  # Replace with your MongoDB connection string
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
                    "total_price": total_price
                }

    return best_combination

@app.get("/api/search")
def search_meals(day: str, calorie_threshold: float, protein_threshold: float, price_threshold: float):
    """
    Searches for meals on a specific day and returns the best combination of items from breakfast, lunch, and dinner
    that meet the calorie, protein, and price thresholds.
    """
    print(f"Searching for meals on: {day}")

    # Fetch all entries for the given day
    entries = list(collection.find({"day": day}))
    if not entries:
        print("No entries found for the specified day.")
        raise HTTPException(status_code=404, detail=f"No entries found for the day: {day}")

    # Randomly select one entry for each meal type if available
    breakfast_entries = [entry for entry in entries if entry.get('meal_time', '').lower() == 'breakfast']
    lunch_entries = [entry for entry in entries if entry.get('meal_time', '').lower() == 'lunch']
    dinner_entries = [entry for entry in entries if entry.get('meal_time', '').lower() == 'dinner']

    # Check if any of the lists are empty and handle accordingly
    breakfast = random.choice(breakfast_entries) if breakfast_entries else None
    lunch = random.choice(lunch_entries) if lunch_entries else None
    dinner = random.choice(dinner_entries) if dinner_entries else None

    # Combine the selected entries and gather items if they exist
    all_items = []
    for meal in [breakfast, lunch, dinner]:
        if meal:
            for place in meal.get('places', []):
                for item in place.get('items', []):
                    all_items.append({
                        "name": item.get('name', 'Unknown Item'),
                        "calories": item.get('calories', 0),
                        "protein": item.get('protein', 0),
                        "price": item.get('price', 0)
                    })

    # Find the best combination of items that match the thresholds
    best_combination = find_best_combination(all_items, calorie_threshold, protein_threshold, price_threshold)

    # Return the best combination found
    if not best_combination:
        raise HTTPException(status_code=404, detail="No suitable combination found.")

    return {"best_combination": best_combination}