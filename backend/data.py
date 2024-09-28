from pymongo import MongoClient

uri = "mongodb+srv://ayannair23:piZnOuJDco3Eurni@greenback.y44sh.mongodb.net/?retryWrites=true&w=majority&appName=greenback"

client = MongoClient(uri)

db = client['greenback']
collection = db['food']
dummy_data = [
    {
        "time": "B",  # Breakfast
        "place": "Bursley Dining Hall",
        "foods": [
            {
                "name": "Pancakes",
                "price": 2.99,
                "calories": 350.0,
                "protein": 10.0
            },
            {
                "name": "Omelette",
                "price": 3.50,
                "calories": 200.0,
                "protein": 12.0
            }
        ]
    },
    {
        "time": "L",  # Lunch
        "place": "Hopcat",
        "foods": [
            {
                "name": "Burger",
                "price": 5.99,
                "calories": 500.0,
                "protein": 20.0
            },
            {
                "name": "Salad",
                "price": 4.50,
                "calories": 150.0,
                "protein": 5.0
            }
        ]
    },
    {
        "time": "D",  # Dinner
        "place": "Mojo Dining Hall",
        "foods": [
            {
                "name": "Steak",
                "price": 10.99,
                "calories": 700.0,
                "protein": 50.0
            },
            {
                "name": "Pasta",
                "price": 6.99,
                "calories": 600.0,
                "protein": 15.0
            }
        ]
    }
]

try:
    result = collection.insert_many(dummy_data)
    print(f"Inserted {len(result.inserted_ids)} documents.")
except Exception as e:
    print("An error occurred:", e)

client.close()
