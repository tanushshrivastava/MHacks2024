from pymongo import MongoClient

from dotenv import load_dotenv
import os

load_dotenv()

mongoPass = os.getenv("mongoPass")
mongoUser = os.getenv("mongoUser")

uri = "mongodb+srv://" + mongoUser + ":" + mongoPass + "@greenback.y44sh.mongodb.net/?retryWrites=true&w=majority&appName=greenback"

client = MongoClient(uri)

db = client['greenback']
collection = db['food']
dummy_data = [
    {
        "meal_time": "Breakfast",
        "places": [
            {
                "restaurant": "bursley - Hot Cereal",
                "items": [
                    {
                        "name": "Oatmeal",
                        "price": 0,
                        "calories": 183,
                        "protein": 8
                    },
                    {
                        "name": "Brown Sugar",
                        "price": 0,
                        "calories": 15,
                        "protein": 0
                    }
                ]
            },
            {
                "restaurant": "bursley - Toast",
                "items": [
                    {
                        "name": "Roasted Cauliflower",
                        "price": 0,
                        "calories": 16,
                        "protein": 1
                    },
                    {
                        "name": "Scrambled Tofu",
                        "price": 0,
                        "calories": 74,
                        "protein": 9
                    },
                    {
                        "name": "Scrambled Eggs",
                        "price": 0,
                        "calories": 163,
                        "protein": 15
                    },
                    {
                        "name": "Blueberry Buttermilk Pancakes",
                        "price": 0,
                        "calories": 105,
                        "protein": 4
                    },
                    {
                        "name": "Corned Beef Hash",
                        "price": 0,
                        "calories": 128,
                        "protein": 11
                    },
                    {
                        "name": "Pork Sausage Links",
                        "price": 0,
                        "calories": 181,
                        "protein": 12
                    },
                    {
                        "name": "Patatas Bravas",
                        "price": 0,
                        "calories": 159,
                        "protein": 2
                    }
                ]
            },
            {
                "restaurant": "bursley - MBakery",
                "items": [
                    {
                        "name": "Blueberry Muffins",
                        "price": 0,
                        "calories": 164,
                        "protein": 2
                    },
                    {
                        "name": "Lemon Poppyseed Muffins",
                        "price": 0,
                        "calories": 181,
                        "protein": 2
                    },
                    {
                        "name": "Chocolate Croissant",
                        "price": 0,
                        "calories": 150,
                        "protein": 4
                    }
                ]
            }
        ]
    },
    {
        "meal_time": "Lunch",
        "places": [
            {
                "restaurant": "bursley - Soup",
                "items": [
                    {
                        "name": "Spinach, Shiitake & Tofu Soup",
                        "price": 0,
                        "calories": 65,
                        "protein": 7
                    },
                    {
                        "name": "Black Bean & Sausage Soup",
                        "price": 0,
                        "calories": 293,
                        "protein": 15
                    }
                ]
            },
            {
                "restaurant": "bursley - Signature Maize",
                "items": [
                    {
                        "name": "Marinated Chicken Thigh Halal",
                        "price": 0,
                        "calories": 159,
                        "protein": 20
                    },
                    {
                        "name": "Seasoned Quinoa",
                        "price": 0,
                        "calories": 232,
                        "protein": 12
                    },
                    {
                        "name": "Mediterranean Salad",
                        "price": 0,
                        "calories": 65,
                        "protein": 1
                    }
                ]
            },
            {
                "restaurant": "bursley - Signature Blue",
                "items": [
                    {
                        "name": "Lemon Baked Tofu",
                        "price": 0,
                        "calories": 115,
                        "protein": 14
                    },
                    {
                        "name": "Mediterranean Salad",
                        "price": 0,
                        "calories": 65,
                        "protein": 1
                    },
                    {
                        "name": "Seasoned Quinoa",
                        "price": 0,
                        "calories": 232,
                        "protein": 12
                    }
                ]
            },
            {
                "restaurant": "bursley - 24 Carrots",
                "items": [
                    {
                        "name": "Dal",
                        "price": 0,
                        "calories": 122,
                        "protein": 10
                    },
                    {
                        "name": "Cilantro Chutney",
                        "price": 0,
                        "calories": 10,
                        "protein": 1
                    },
                    {
                        "name": "Roasted Garbanzo's w/ Cilantro",
                        "price": 0,
                        "calories": 25,
                        "protein": 2
                    },
                    {
                        "name": "Basmati Rice",
                        "price": 0,
                        "calories": 156,
                        "protein": 4
                    }
                ]
            },
            {
                "restaurant": "bursley - Halal",
                "items": [
                    {
                        "name": "Beef Roast Sandwich",
                        "price": 0,
                        "calories": 487,
                        "protein": 24
                    },
                    {
                        "name": "Ruffles Potato Chips",
                        "price": 0,
                        "calories": 160,
                        "protein": 3
                    },
                    {
                        "name": "Pepperoncini",
                        "price": 0,
                        "calories": 5,
                        "protein": 0
                    }
                ]
            },
            {
                "restaurant": "bursley - Pizziti",
                "items": [
                    {
                        "name": "BLT Pizza",
                        "price": 0,
                        "calories": 416,
                        "protein": 19
                    },
                    {
                        "name": "Cheese Pizza",
                        "price": 0,
                        "calories": 269,
                        "protein": 14
                    },
                    {
                        "name": "Pepperoni Pizza",
                        "price": 0,
                        "calories": 298,
                        "protein": 16
                    },
                    {
                        "name": "Garlic Cheese Bread",
                        "price": 0,
                        "calories": 222,
                        "protein": 12
                    }
                ]
            },
            {
                "restaurant": "bursley - Wild Fire Maize",
                "items": [
                    {
                        "name": "Dearborn Bratwurst on White Bun",
                        "price": 0,
                        "calories": 354,
                        "protein": 23
                    },
                    {
                        "name": "Caramelized Onions",
                        "price": 0,
                        "calories": 32,
                        "protein": 1
                    },
                    {
                        "name": "Criss Cross Fries",
                        "price": 0,
                        "calories": 283,
                        "protein": 2
                    }
                ]
            },
            {
                "restaurant": "bursley - Two Oceans",
                "items": [
                    {
                        "name": "Vietnamese Chicken Thighs w/ Peanuts",
                        "price": 0,
                        "calories": 134,
                        "protein": 15
                    },
                    {
                        "name": "Lemon Glazed Grilled Tofu",
                        "price": 0,
                        "calories": 271,
                        "protein": 26
                    },
                    {
                        "name": "Fresh Steamed Broccoli Florets",
                        "price": 0,
                        "calories": 39,
                        "protein": 4
                    },
                    {
                        "name": "Medium Grain Rice",
                        "price": 0,
                        "calories": 157,
                        "protein": 4
                    }
                ]
            },
            {
                "restaurant": "bursley - Deli",
                "items": []
            },
            {
                "restaurant": "bursley - MBakery",
                "items": [
                    {
                        "name": "Sugar Cookies",
                        "price": 0,
                        "calories": 162,
                        "protein": 3
                    },
                    {
                        "name": "Chocolate Chunk Cookies",
                        "price": 0,
                        "calories": 152,
                        "protein": 3
                    },
                    {
                        "name": "Blueberry Banana Cake w/Coconut",
                        "price": 0,
                        "calories": 407,
                        "protein": 4
                    },
                    {
                        "name": "Birthday Cake Bars",
                        "price": 0,
                        "calories": 472,
                        "protein": 6
                    }
                ]
            }
        ]
    },
    {
        "meal_time": "Dinner",
        "places": [
            {
                "restaurant": "bursley - Soup",
                "items": [
                    {
                        "name": "Spinach, Shiitake & Tofu Soup",
                        "price": 0,
                        "calories": 65,
                        "protein": 7
                    },
                    {
                        "name": "Black Bean & Sausage Soup",
                        "price": 0,
                        "calories": 293,
                        "protein": 15
                    }
                ]
            },
            {
                "restaurant": "bursley - Signature Maize",
                "items": [
                    {
                        "name": "Bou's Lao Wings",
                        "price": 0,
                        "calories": 167,
                        "protein": 17
                    },
                    {
                        "name": "Sesame Ginger Slaw",
                        "price": 0,
                        "calories": 41,
                        "protein": 1
                    },
                    {
                        "name": "Chopped Green Onions",
                        "price": 0,
                        "calories": 5,
                        "protein": 0
                    },
                    {
                        "name": "Medium Grain Rice",
                        "price": 0,
                        "calories": 157,
                        "protein": 4
                    }
                ]
            },
            {
                "restaurant": "bursley - Signature Blue",
                "items": [
                    {
                        "name": "Fried Breaded Cauliflower",
                        "price": 0,
                        "calories": 229,
                        "protein": 5
                    },
                    {
                        "name": "Lao Sauce",
                        "price": 0,
                        "calories": 143,
                        "protein": 3
                    },
                    {
                        "name": "Chopped Green Onions",
                        "price": 0,
                        "calories": 5,
                        "protein": 0
                    },
                    {
                        "name": "Sesame Ginger Slaw",
                        "price": 0,
                        "calories": 41,
                        "protein": 1
                    },
                    {
                        "name": "Medium Grain Rice",
                        "price": 0,
                        "calories": 157,
                        "protein": 4
                    }
                ]
            },
            {
                "restaurant": "bursley - 24 Carrots",
                "items": [
                    {
                        "name": "Vegan Shepherd's Pie",
                        "price": 0,
                        "calories": 79,
                        "protein": 4
                    },
                    {
                        "name": "Parsley",
                        "price": 0,
                        "calories": 5,
                        "protein": 1
                    }
                ]
            },
            {
                "restaurant": "bursley - Halal",
                "items": [
                    {
                        "name": "Lamb Korma",
                        "price": 0,
                        "calories": 207,
                        "protein": 15
                    },
                    {
                        "name": "Basmati Rice",
                        "price": 0,
                        "calories": 156,
                        "protein": 4
                    },
                    {
                        "name": "Roasted Green Beans",
                        "price": 0,
                        "calories": 37,
                        "protein": 2
                    },
                    {
                        "name": "Cilantro",
                        "price": 0,
                        "calories": 3,
                        "protein": 0
                    }
                ]
            },
            {
                "restaurant": "bursley - Pizziti",
                "items": [
                    {
                        "name": "BLT Pizza",
                        "price": 0,
                        "calories": 416,
                        "protein": 19
                    },
                    {
                        "name": "Garlic Cheese Bread",
                        "price": 0,
                        "calories": 222,
                        "protein": 12
                    },
                    {
                        "name": "Pepperoni Pizza",
                        "price": 0,
                        "calories": 298,
                        "protein": 16
                    },
                    {
                        "name": "Cheese Pizza",
                        "price": 0,
                        "calories": 269,
                        "protein": 14
                    }
                ]
            },
            {
                "restaurant": "bursley - Wild Fire Maize",
                "items": [
                    {
                        "name": "Dearborn Bratwurst on White Bun",
                        "price": 0,
                        "calories": 354,
                        "protein": 23
                    },
                    {
                        "name": "Caramelized Onions",
                        "price": 0,
                        "calories": 32,
                        "protein": 1
                    },
                    {
                        "name": "Criss Cross Fries",
                        "price": 0,
                        "calories": 283,
                        "protein": 2
                    }
                ]
            },
            {
                "restaurant": "bursley - Two Oceans",
                "items": [
                    {
                        "name": "Vietnamese Chicken Thighs w/ Peanuts",
                        "price": 0,
                        "calories": 134,
                        "protein": 15
                    },
                    {
                        "name": "Lemon Glazed Grilled Tofu",
                        "price": 0,
                        "calories": 271,
                        "protein": 26
                    },
                    {
                        "name": "Fresh Steamed Broccoli Florets",
                        "price": 0,
                        "calories": 39,
                        "protein": 4
                    },
                    {
                        "name": "Medium Grain Rice",
                        "price": 0,
                        "calories": 157,
                        "protein": 4
                    }
                ]
            },
            {
                "restaurant": "bursley - Deli",
                "items": []
            },
            {
                "restaurant": "bursley - MBakery",
                "items": [
                    {
                        "name": "Vernor's Bundt Cake",
                        "price": 0,
                        "calories": 445,
                        "protein": 7
                    },
                    {
                        "name": "Blueberry Banana Cake w/Coconut",
                        "price": 0,
                        "calories": 407,
                        "protein": 4
                    }
                ]
            }
        ]
    },
    {
        "meal_time": "Breakfast",
        "places": [
            {
                "restaurant": "east-quad - Hot Cereal",
                "items": [
                    {
                        "name": "Oatmeal",
                        "price": 0,
                        "calories": 183,
                        "protein": 8
                    },
                    {
                        "name": "Grits",
                        "price": 0,
                        "calories": 1081,
                        "protein": 0
                    }
                ]
            },
            {
                "restaurant": "east-quad - Toast",
                "items": [
                    {
                        "name": "Scrambled Eggs",
                        "price": 0,
                        "calories": 163,
                        "protein": 15
                    },
                    {
                        "name": "Sauteed Mixed Peppers & Onions",
                        "price": 0,
                        "calories": 12,
                        "protein": 0
                    },
                    {
                        "name": "Korean Style Breakfast Power Bowl",
                        "price": 0,
                        "calories": 262,
                        "protein": 19
                    },
                    {
                        "name": "Patatas Bravas",
                        "price": 0,
                        "calories": 159,
                        "protein": 2
                    },
                    {
                        "name": "Halal Turkey Bacon",
                        "price": 0,
                        "calories": 120,
                        "protein": 11
                    },
                    {
                        "name": "Cinnamon Swirl French Toast",
                        "price": 0,
                        "calories": 279,
                        "protein": 12
                    },
                    {
                        "name": "Scrambled Tofu",
                        "price": 0,
                        "calories": 157,
                        "protein": 18
                    }
                ]
            },
            {
                "restaurant": "east-quad - MBakery",
                "items": [
                    {
                        "name": "Blueberry Muffins",
                        "price": 0,
                        "calories": 164,
                        "protein": 2
                    },
                    {
                        "name": "Apple Cinnamon Muffins",
                        "price": 0,
                        "calories": 181,
                        "protein": 2
                    },
                    {
                        "name": "Cinnamon Sugar Donuts",
                        "price": 0,
                        "calories": 314,
                        "protein": 5
                    }
                ]
            }
        ]
    },
    {
        "meal_time": "Lunch",
        "places": [
            {
                "restaurant": "east-quad - Soup",
                "items": [
                    {
                        "name": "Loaded Baked Potato Soup",
                        "price": 0,
                        "calories": 442,
                        "protein": 13
                    },
                    {
                        "name": "Mushroom Barley Soup",
                        "price": 0,
                        "calories": 168,
                        "protein": 8
                    }
                ]
            },
            {
                "restaurant": "east-quad - Signature Maize",
                "items": [
                    {
                        "name": "Buffalo Chicken Wings",
                        "price": 0,
                        "calories": 265,
                        "protein": 26
                    },
                    {
                        "name": "Honey BBQ Chicken Wings",
                        "price": 0,
                        "calories": 358,
                        "protein": 17
                    },
                    {
                        "name": "Macaroni Salad",
                        "price": 0,
                        "calories": 212,
                        "protein": 7
                    },
                    {
                        "name": "Celery Sticks",
                        "price": 0,
                        "calories": 3,
                        "protein": 0
                    },
                    {
                        "name": "Carrot Sticks",
                        "price": 0,
                        "calories": 15,
                        "protein": 0
                    },
                    {
                        "name": "Blue Cheese Dressing",
                        "price": 0,
                        "calories": 122,
                        "protein": 2
                    }
                ]
            },
            {
                "restaurant": "east-quad - 24 Carrots",
                "items": [
                    {
                        "name": "Portabella & Poblano Fajitas",
                        "price": 0,
                        "calories": 182,
                        "protein": 4
                    },
                    {
                        "name": "Black Beans and Brown Rice",
                        "price": 0,
                        "calories": 147,
                        "protein": 5
                    },
                    {
                        "name": "Corn Salsa",
                        "price": 0,
                        "calories": 39,
                        "protein": 1
                    },
                    {
                        "name": "Avocado Wedge",
                        "price": 0,
                        "calories": 45,
                        "protein": 1
                    },
                    {
                        "name": "Cheese Lasagna Rollups",
                        "price": 0,
                        "calories": 308,
                        "protein": 18
                    },
                    {
                        "name": "Roasted Broccoli",
                        "price": 0,
                        "calories": 42,
                        "protein": 3
                    },
                    {
                        "name": "Broccoli Alfredo Flatbread Pizza",
                        "price": 0,
                        "calories": 155,
                        "protein": 10
                    }
                ]
            },
            {
                "restaurant": "east-quad - Halal",
                "items": [
                    {
                        "name": "Tandoori Salmon",
                        "price": 0,
                        "calories": 199,
                        "protein": 29
                    },
                    {
                        "name": "Tomato Cucumber Raita",
                        "price": 0,
                        "calories": 20,
                        "protein": 3
                    },
                    {
                        "name": "Lemon Wedges",
                        "price": 0,
                        "calories": 3,
                        "protein": 0
                    },
                    {
                        "name": "Basmati Rice",
                        "price": 0,
                        "calories": 156,
                        "protein": 4
                    }
                ]
            },
            {
                "restaurant": "east-quad - Pizziti",
                "items": [
                    {
                        "name": "Cheese Pizza",
                        "price": 0,
                        "calories": 269,
                        "protein": 14
                    },
                    {
                        "name": "Pepperoni Pizza",
                        "price": 0,
                        "calories": 298,
                        "protein": 16
                    },
                    {
                        "name": "Cheese Bread",
                        "price": 0,
                        "calories": 207,
                        "protein": 12
                    }
                ]
            },
            {
                "restaurant": "east-quad - Wild Fire Maize",
                "items": [
                    {
                        "name": "Turkey Burger on White Bun",
                        "price": 0,
                        "calories": 261,
                        "protein": 35
                    },
                    {
                        "name": "Criss Cross Fries",
                        "price": 0,
                        "calories": 283,
                        "protein": 2
                    }
                ]
            },
            {
                "restaurant": "east-quad - MBakery",
                "items": [
                    {
                        "name": "Chocolate Chunk Cookies",
                        "price": 0,
                        "calories": 152,
                        "protein": 3
                    },
                    {
                        "name": "Blueberry Banana Cake w/Coconut",
                        "price": 0,
                        "calories": 407,
                        "protein": 4
                    },
                    {
                        "name": "Birthday Cake Bars",
                        "price": 0,
                        "calories": 472,
                        "protein": 6
                    }
                ]
            }
        ]
    },
    {
        "meal_time": "Dinner",
        "places": [
            {
                "restaurant": "east-quad - Soup",
                "items": [
                    {
                        "name": "Mushroom Barley Soup",
                        "price": 0,
                        "calories": 168,
                        "protein": 8
                    },
                    {
                        "name": "Loaded Baked Potato Soup",
                        "price": 0,
                        "calories": 442,
                        "protein": 13
                    }
                ]
            },
            {
                "restaurant": "east-quad - Signature Maize",
                "items": [
                    {
                        "name": "French Dip Au Jus",
                        "price": 0,
                        "calories": 327,
                        "protein": 33
                    },
                    {
                        "name": "Macaroni & Cheese",
                        "price": 0,
                        "calories": 225,
                        "protein": 12
                    }
                ]
            },
            {
                "restaurant": "east-quad - 24 Carrots",
                "items": [
                    {
                        "name": "Piri Piri Tofu",
                        "price": 0,
                        "calories": 132,
                        "protein": 15
                    },
                    {
                        "name": "Basmati Rice",
                        "price": 0,
                        "calories": 156,
                        "protein": 4
                    },
                    {
                        "name": "Cheese Lasagna Rollups",
                        "price": 0,
                        "calories": 308,
                        "protein": 18
                    },
                    {
                        "name": "Fresh Steamed Broccoli Florets",
                        "price": 0,
                        "calories": 39,
                        "protein": 4
                    },
                    {
                        "name": "Broccoli Alfredo Flatbread Pizza",
                        "price": 0,
                        "calories": 155,
                        "protein": 10
                    }
                ]
            },
            {
                "restaurant": "east-quad - Halal",
                "items": [
                    {
                        "name": "Lamb Gyro Meat",
                        "price": 0,
                        "calories": 139,
                        "protein": 12
                    },
                    {
                        "name": "Garlic Sauce",
                        "price": 0,
                        "calories": 189,
                        "protein": 0
                    },
                    {
                        "name": "Lemon Parsley Rice",
                        "price": 0,
                        "calories": 152,
                        "protein": 5
                    },
                    {
                        "name": "Grilled Vegetables",
                        "price": 0,
                        "calories": 53,
                        "protein": 2
                    },
                    {
                        "name": "Cucumber Relish",
                        "price": 0,
                        "calories": 23,
                        "protein": 0
                    }
                ]
            },
            {
                "restaurant": "east-quad - Pizziti",
                "items": [
                    {
                        "name": "Cheese Pizza",
                        "price": 0,
                        "calories": 269,
                        "protein": 14
                    },
                    {
                        "name": "Cheese Bread",
                        "price": 0,
                        "calories": 207,
                        "protein": 12
                    },
                    {
                        "name": "Pepperoni Pizza",
                        "price": 0,
                        "calories": 298,
                        "protein": 16
                    }
                ]
            },
            {
                "restaurant": "east-quad - Wild Fire Maize",
                "items": [
                    {
                        "name": "Turkey Burger on White Bun",
                        "price": 0,
                        "calories": 261,
                        "protein": 35
                    },
                    {
                        "name": "Criss Cross Fries",
                        "price": 0,
                        "calories": 283,
                        "protein": 2
                    }
                ]
            },
            {
                "restaurant": "east-quad - MBakery",
                "items": [
                    {
                        "name": "Vernor's Bundt Cake",
                        "price": 0,
                        "calories": 445,
                        "protein": 7
                    },
                    {
                        "name": "Blueberry Banana Cake w/Coconut",
                        "price": 0,
                        "calories": 407,
                        "protein": 4
                    }
                ]
            }
        ]
    },
    {
        "meal_time": "Breakfast",
        "places": [
            {
                "restaurant": "markley - Hot Cereal",
                "items": [
                    {
                        "name": "Oatmeal",
                        "price": 0,
                        "calories": 183,
                        "protein": 8
                    }
                ]
            },
            {
                "restaurant": "markley - Toast",
                "items": [
                    {
                        "name": "Scrambled Tofu",
                        "price": 0,
                        "calories": 157,
                        "protein": 18
                    },
                    {
                        "name": "Cinnamon Swirl French Toast",
                        "price": 0,
                        "calories": 279,
                        "protein": 12
                    },
                    {
                        "name": "Grilled Ham",
                        "price": 0,
                        "calories": 76,
                        "protein": 13
                    },
                    {
                        "name": "Patatas Bravas",
                        "price": 0,
                        "calories": 159,
                        "protein": 2
                    },
                    {
                        "name": "Roasted Baby Carrots",
                        "price": 0,
                        "calories": 184,
                        "protein": 0
                    },
                    {
                        "name": "Scrambled Eggs",
                        "price": 0,
                        "calories": 163,
                        "protein": 15
                    }
                ]
            },
            {
                "restaurant": "markley - MBakery",
                "items": [
                    {
                        "name": "Apple Cinnamon Muffins",
                        "price": 0,
                        "calories": 181,
                        "protein": 2
                    },
                    {
                        "name": "Vanilla Honey Glazed Donut",
                        "price": 0,
                        "calories": 304,
                        "protein": 4
                    }
                ]
            }
        ]
    },
    {
        "meal_time": "Lunch",
        "places": [
            {
                "restaurant": "markley - Soup",
                "items": [
                    {
                        "name": "Loaded Baked Potato Soup",
                        "price": 0,
                        "calories": 442,
                        "protein": 13
                    }
                ]
            },
            {
                "restaurant": "markley - Signature Maize",
                "items": [
                    {
                        "name": "Kung Pao Chicken",
                        "price": 0,
                        "calories": 242,
                        "protein": 20
                    },
                    {
                        "name": "Sesame Sugar Snap Peas",
                        "price": 0,
                        "calories": 71,
                        "protein": 4
                    },
                    {
                        "name": "Medium Grain Rice",
                        "price": 0,
                        "calories": 157,
                        "protein": 4
                    },
                    {
                        "name": "Singapore Noodles w/ Edamame",
                        "price": 0,
                        "calories": 89,
                        "protein": 5
                    },
                    {
                        "name": "Spring Rolls",
                        "price": 0,
                        "calories": 49,
                        "protein": 1
                    }
                ]
            },
            {
                "restaurant": "markley - Signature Blue",
                "items": [
                    {
                        "name": "Singapore Noodles w/ Edamame",
                        "price": 0,
                        "calories": 89,
                        "protein": 5
                    },
                    {
                        "name": "Sesame Sugar Snap Peas",
                        "price": 0,
                        "calories": 71,
                        "protein": 4
                    },
                    {
                        "name": "Spring Rolls",
                        "price": 0,
                        "calories": 49,
                        "protein": 1
                    }
                ]
            },
            {
                "restaurant": "markley - Halal",
                "items": [
                    {
                        "name": "Balsamic Glazed Chicken",
                        "price": 0,
                        "calories": 129,
                        "protein": 29
                    },
                    {
                        "name": "Oven Roasted Garlic Potatoes",
                        "price": 0,
                        "calories": 86,
                        "protein": 2
                    },
                    {
                        "name": "Broccolini Saute",
                        "price": 0,
                        "calories": 54,
                        "protein": 3
                    }
                ]
            },
            {
                "restaurant": "markley - MBakery",
                "items": [
                    {
                        "name": "Chocolate Chunk Cookies",
                        "price": 0,
                        "calories": 152,
                        "protein": 3
                    },
                    {
                        "name": "Whipped Topping",
                        "price": 0,
                        "calories": 20,
                        "protein": 0
                    },
                    {
                        "name": "Birthday Cake Bars",
                        "price": 0,
                        "calories": 472,
                        "protein": 6
                    },
                    {
                        "name": "Blueberry Banana Cake w/Coconut",
                        "price": 0,
                        "calories": 407,
                        "protein": 4
                    }
                ]
            }
        ]
    },
    {
        "meal_time": "Dinner",
        "places": [
            {
                "restaurant": "markley - Soup",
                "items": [
                    {
                        "name": "Loaded Baked Potato Soup",
                        "price": 0,
                        "calories": 442,
                        "protein": 13
                    }
                ]
            },
            {
                "restaurant": "markley - Signature Maize",
                "items": [
                    {
                        "name": "Buffalo Chicken Wings",
                        "price": 0,
                        "calories": 265,
                        "protein": 26
                    }
                ]
            },
            {
                "restaurant": "markley - 24 Carrots",
                "items": [
                    {
                        "name": "Balsamic Marinated Tempeh",
                        "price": 0,
                        "calories": 313,
                        "protein": 20
                    },
                    {
                        "name": "Grilled Vegetables",
                        "price": 0,
                        "calories": 53,
                        "protein": 2
                    },
                    {
                        "name": "Lemon Parsley Rice",
                        "price": 0,
                        "calories": 152,
                        "protein": 5
                    },
                    {
                        "name": "Grecian Pita Fold",
                        "price": 0,
                        "calories": 230,
                        "protein": 11
                    }
                ]
            },
            {
                "restaurant": "markley - Halal",
                "items": [
                    {
                        "name": "Lemon Parsley Rice",
                        "price": 0,
                        "calories": 152,
                        "protein": 5
                    },
                    {
                        "name": "Grilled Vegetables",
                        "price": 0,
                        "calories": 53,
                        "protein": 2
                    },
                    {
                        "name": "Hot Halal Sliced Roast Beef",
                        "price": 0,
                        "calories": 221,
                        "protein": 29
                    }
                ]
            },
            {
                "restaurant": "markley - MBakery",
                "items": [
                    {
                        "name": "Chocolate Chunk Cookies",
                        "price": 0,
                        "calories": 152,
                        "protein": 3
                    },
                    {
                        "name": "Vernor's Bundt Cake",
                        "price": 0,
                        "calories": 445,
                        "protein": 7
                    },
                    {
                        "name": "Blueberry Banana Cake w/Coconut",
                        "price": 0,
                        "calories": 407,
                        "protein": 4
                    }
                ]
            }
        ]
    },
    {
        "meal_time": "Breakfast",
        "places": [
            {
                "restaurant": "mosher-jordan - Hot Cereal",
                "items": [
                    {
                        "name": "Oatmeal",
                        "price": 0,
                        "calories": 164,
                        "protein": 8
                    }
                ]
            },
            {
                "restaurant": "mosher-jordan - Toast",
                "items": [
                    {
                        "name": "Roasted Broccoli",
                        "price": 0,
                        "calories": 42,
                        "protein": 3
                    },
                    {
                        "name": "Potato Tots",
                        "price": 0,
                        "calories": 262,
                        "protein": 1
                    },
                    {
                        "name": "Scrambled Eggs",
                        "price": 0,
                        "calories": 163,
                        "protein": 15
                    },
                    {
                        "name": "Bruschetta Tofu Scramble",
                        "price": 0,
                        "calories": 134,
                        "protein": 14
                    },
                    {
                        "name": "Cajun Andouille Sausage",
                        "price": 0,
                        "calories": 182,
                        "protein": 14
                    },
                    {
                        "name": "Baked Buttermilk Waffles",
                        "price": 0,
                        "calories": 179,
                        "protein": 5
                    },
                    {
                        "name": "Blueberry Sauce",
                        "price": 0,
                        "calories": 23,
                        "protein": 0
                    }
                ]
            },
            {
                "restaurant": "mosher-jordan - MBakery",
                "items": [
                    {
                        "name": "Chocolate Chocolate Chip Muffins",
                        "price": 0,
                        "calories": 176,
                        "protein": 3
                    },
                    {
                        "name": "Cappuccino Chocolate Chip Muffins",
                        "price": 0,
                        "calories": 202,
                        "protein": 3
                    },
                    {
                        "name": "Cinnamon Rolls",
                        "price": 0,
                        "calories": 112,
                        "protein": 4
                    }
                ]
            }
        ]
    },
    {
        "meal_time": "Lunch",
        "places": [
            {
                "restaurant": "mosher-jordan - Soup",
                "items": [
                    {
                        "name": "Chicken Noodle Soup",
                        "price": 0,
                        "calories": 103,
                        "protein": 8
                    }
                ]
            },
            {
                "restaurant": "mosher-jordan - Signature Maize",
                "items": [
                    {
                        "name": "BBQ Pork Chops",
                        "price": 0,
                        "calories": 212,
                        "protein": 21
                    },
                    {
                        "name": "Yukon Gold Potatoes",
                        "price": 0,
                        "calories": 148,
                        "protein": 4
                    },
                    {
                        "name": "Baked Butternut Squash",
                        "price": 0,
                        "calories": 55,
                        "protein": 2
                    }
                ]
            },
            {
                "restaurant": "mosher-jordan - Signature Blue",
                "items": [
                    {
                        "name": "BBQ Tempeh",
                        "price": 0,
                        "calories": 162,
                        "protein": 22
                    },
                    {
                        "name": "Yukon Gold Potatoes",
                        "price": 0,
                        "calories": 148,
                        "protein": 4
                    },
                    {
                        "name": "Baked Butternut Squash",
                        "price": 0,
                        "calories": 55,
                        "protein": 2
                    }
                ]
            },
            {
                "restaurant": "mosher-jordan - World Palate Maize",
                "items": [
                    {
                        "name": "Bou's Lao Wings",
                        "price": 0,
                        "calories": 167,
                        "protein": 17
                    },
                    {
                        "name": "Medium Grain Rice",
                        "price": 0,
                        "calories": 157,
                        "protein": 4
                    },
                    {
                        "name": "Spicy Ginger Slaw",
                        "price": 0,
                        "calories": 62,
                        "protein": 2
                    }
                ]
            },
            {
                "restaurant": "mosher-jordan - 24 Carrots",
                "items": [
                    {
                        "name": "Potato Dal Curry",
                        "price": 0,
                        "calories": 82,
                        "protein": 4
                    },
                    {
                        "name": "Basmati Rice",
                        "price": 0,
                        "calories": 156,
                        "protein": 4
                    },
                    {
                        "name": "Naan Bread",
                        "price": 0,
                        "calories": 170,
                        "protein": 7
                    },
                    {
                        "name": "Pickled Red Onion",
                        "price": 0,
                        "calories": 62,
                        "protein": 0
                    }
                ]
            },
            {
                "restaurant": "mosher-jordan - Halal",
                "items": [
                    {
                        "name": "Halal Grilled Chicken Thigh",
                        "price": 0,
                        "calories": 152,
                        "protein": 24
                    },
                    {
                        "name": "Savory Spinach Side Salad",
                        "price": 0,
                        "calories": 12,
                        "protein": 2
                    },
                    {
                        "name": "Raspberry Vinaigrette Dressing",
                        "price": 0,
                        "calories": 160,
                        "protein": 0
                    }
                ]
            },
            {
                "restaurant": "mosher-jordan - Pizziti",
                "items": [
                    {
                        "name": "Pepperoni Pizza",
                        "price": 0,
                        "calories": 298,
                        "protein": 16
                    },
                    {
                        "name": "Cheese Pizza",
                        "price": 0,
                        "calories": 269,
                        "protein": 14
                    },
                    {
                        "name": "Blue Cheese Bacon & Green Onion Pizza",
                        "price": 0,
                        "calories": 362,
                        "protein": 22
                    }
                ]
            },
            {
                "restaurant": "mosher-jordan - Wild Fire Maize",
                "items": [
                    {
                        "name": "Beef and Mushroom Blended Burger",
                        "price": 0,
                        "calories": 277,
                        "protein": 32
                    },
                    {
                        "name": "Beef & Mushroom Blended Burger w/ Cheese",
                        "price": 0,
                        "calories": 404,
                        "protein": 40
                    },
                    {
                        "name": "Battered Cod Sandwich",
                        "price": 0,
                        "calories": 264,
                        "protein": 16
                    },
                    {
                        "name": "Seasoned Fries",
                        "price": 0,
                        "calories": 176,
                        "protein": 2
                    }
                ]
            },
            {
                "restaurant": "mosher-jordan - Wild Fire Blue",
                "items": [
                    {
                        "name": "Crispy Veggie Patty on White Bun",
                        "price": 0,
                        "calories": 340,
                        "protein": 16
                    },
                    {
                        "name": "Seasoned Fries",
                        "price": 0,
                        "calories": 176,
                        "protein": 2
                    }
                ]
            },
            {
                "restaurant": "mosher-jordan - Deli",
                "items": []
            },
            {
                "restaurant": "mosher-jordan - MBakery",
                "items": [
                    {
                        "name": "Monster Candy Cookies",
                        "price": 0,
                        "calories": 152,
                        "protein": 3
                    },
                    {
                        "name": "Birthday Cake Bars",
                        "price": 0,
                        "calories": 472,
                        "protein": 6
                    },
                    {
                        "name": "Blueberry Banana Cake w/Coconut",
                        "price": 0,
                        "calories": 407,
                        "protein": 4
                    }
                ]
            }
        ]
    },
    {
        "meal_time": "Dinner",
        "places": [
            {
                "restaurant": "mosher-jordan - Soup",
                "items": [
                    {
                        "name": "Chicken Noodle Soup",
                        "price": 0,
                        "calories": 103,
                        "protein": 8
                    }
                ]
            },
            {
                "restaurant": "mosher-jordan - Signature Maize",
                "items": [
                    {
                        "name": "Meat Sauce",
                        "price": 0,
                        "calories": 120,
                        "protein": 8
                    },
                    {
                        "name": "Gemelli Pasta",
                        "price": 0,
                        "calories": 71,
                        "protein": 3
                    }
                ]
            },
            {
                "restaurant": "mosher-jordan - Signature Blue",
                "items": [
                    {
                        "name": "Marinara Sauce",
                        "price": 0,
                        "calories": 64,
                        "protein": 2
                    },
                    {
                        "name": "Gemelli Pasta",
                        "price": 0,
                        "calories": 71,
                        "protein": 3
                    }
                ]
            },
            {
                "restaurant": "mosher-jordan - World Palate Maize",
                "items": [
                    {
                        "name": "MSC Blackened Cod",
                        "price": 0,
                        "calories": 71,
                        "protein": 18
                    },
                    {
                        "name": "Baked Sweet Potatoes",
                        "price": 0,
                        "calories": 53,
                        "protein": 1
                    },
                    {
                        "name": "Garlic Roasted Broccoli",
                        "price": 0,
                        "calories": 34,
                        "protein": 3
                    }
                ]
            },
            {
                "restaurant": "mosher-jordan - World Palate Blue",
                "items": [
                    {
                        "name": "Blackened Tofu",
                        "price": 0,
                        "calories": 193,
                        "protein": 21
                    },
                    {
                        "name": "Baked Sweet Potatoes",
                        "price": 0,
                        "calories": 53,
                        "protein": 1
                    },
                    {
                        "name": "Garlic Roasted Broccoli",
                        "price": 0,
                        "calories": 34,
                        "protein": 3
                    }
                ]
            },
            {
                "restaurant": "mosher-jordan - 24 Carrots",
                "items": [
                    {
                        "name": "Vegan Chili Cornbread Pie",
                        "price": 0,
                        "calories": 282,
                        "protein": 13
                    },
                    {
                        "name": "Fresh Pico De Gallo",
                        "price": 0,
                        "calories": 5,
                        "protein": 0
                    }
                ]
            },
            {
                "restaurant": "mosher-jordan - Halal",
                "items": [
                    {
                        "name": "Lime Tarragon Chicken",
                        "price": 0,
                        "calories": 296,
                        "protein": 22
                    },
                    {
                        "name": "Medium Grain Rice",
                        "price": 0,
                        "calories": 157,
                        "protein": 4
                    },
                    {
                        "name": "Chopped Green Onions",
                        "price": 0,
                        "calories": 5,
                        "protein": 0
                    }
                ]
            },
            {
                "restaurant": "mosher-jordan - Pizziti",
                "items": [
                    {
                        "name": "Pepperoni Pizza",
                        "price": 0,
                        "calories": 298,
                        "protein": 16
                    },
                    {
                        "name": "Cheese Pizza",
                        "price": 0,
                        "calories": 269,
                        "protein": 14
                    },
                    {
                        "name": "Blue Cheese Bacon & Green Onion Pizza",
                        "price": 0,
                        "calories": 362,
                        "protein": 22
                    }
                ]
            },
            {
                "restaurant": "mosher-jordan - Wild Fire Maize",
                "items": [
                    {
                        "name": "Beef and Mushroom Blended Burger",
                        "price": 0,
                        "calories": 277,
                        "protein": 32
                    },
                    {
                        "name": "Beef & Mushroom Blended Burger w/ Cheese",
                        "price": 0,
                        "calories": 404,
                        "protein": 40
                    },
                    {
                        "name": "Battered Cod Sandwich",
                        "price": 0,
                        "calories": 264,
                        "protein": 16
                    },
                    {
                        "name": "Seasoned Fries",
                        "price": 0,
                        "calories": 176,
                        "protein": 2
                    }
                ]
            },
            {
                "restaurant": "mosher-jordan - Wild Fire Blue",
                "items": [
                    {
                        "name": "Crispy Veggie Patty on White Bun",
                        "price": 0,
                        "calories": 340,
                        "protein": 16
                    },
                    {
                        "name": "Seasoned Fries",
                        "price": 0,
                        "calories": 176,
                        "protein": 2
                    }
                ]
            },
            {
                "restaurant": "mosher-jordan - Deli",
                "items": []
            },
            {
                "restaurant": "mosher-jordan - MBakery",
                "items": [
                    {
                        "name": "Monster Candy Cookies",
                        "price": 0,
                        "calories": 152,
                        "protein": 3
                    },
                    {
                        "name": "Vernor's Bundt Cake",
                        "price": 0,
                        "calories": 445,
                        "protein": 7
                    }
                ]
            }
        ]
    },
    {
        "meal_time": "Breakfast",
        "places": [
            {
                "restaurant": "north-quad - Hot Cereal",
                "items": [
                    {
                        "name": "Oatmeal",
                        "price": 0,
                        "calories": 183,
                        "protein": 8
                    }
                ]
            },
            {
                "restaurant": "north-quad - Toast",
                "items": [
                    {
                        "name": "Sauteed Vegetables",
                        "price": 0,
                        "calories": 54,
                        "protein": 2
                    },
                    {
                        "name": "Scrambled Tofu",
                        "price": 0,
                        "calories": 157,
                        "protein": 18
                    },
                    {
                        "name": "Scrambled Eggs",
                        "price": 0,
                        "calories": 163,
                        "protein": 15
                    },
                    {
                        "name": "Cinnamon Swirl French Toast",
                        "price": 0,
                        "calories": 139,
                        "protein": 6
                    },
                    {
                        "name": "Halal Turkey Bacon",
                        "price": 0,
                        "calories": 60,
                        "protein": 5
                    },
                    {
                        "name": "Patatas Bravas",
                        "price": 0,
                        "calories": 159,
                        "protein": 2
                    }
                ]
            },
            {
                "restaurant": "north-quad - MBakery",
                "items": [
                    {
                        "name": "Blueberry Muffins",
                        "price": 0,
                        "calories": 164,
                        "protein": 2
                    },
                    {
                        "name": "Cinnamon Sugar Donuts",
                        "price": 0,
                        "calories": 314,
                        "protein": 5
                    },
                    {
                        "name": "Apple Cinnamon Muffins",
                        "price": 0,
                        "calories": 181,
                        "protein": 2
                    }
                ]
            }
        ]
    },
    {
        "meal_time": "Lunch",
        "places": [
            {
                "restaurant": "north-quad - Soup",
                "items": [
                    {
                        "name": "Stir Fry Vegetable Soup",
                        "price": 0,
                        "calories": 33,
                        "protein": 2
                    }
                ]
            },
            {
                "restaurant": "north-quad - Signature Maize",
                "items": [
                    {
                        "name": "Vegan Brazilian Black Bean Stew",
                        "price": 0,
                        "calories": 146,
                        "protein": 5
                    },
                    {
                        "name": "Medium Grain Rice",
                        "price": 0,
                        "calories": 157,
                        "protein": 4
                    },
                    {
                        "name": "Brazilian Kale",
                        "price": 0,
                        "calories": 94,
                        "protein": 4
                    }
                ]
            },
            {
                "restaurant": "north-quad - Signature Blue",
                "items": [
                    {
                        "name": "Pita Wedges",
                        "price": 0,
                        "calories": 153,
                        "protein": 7
                    },
                    {
                        "name": "Fried Pita Chips",
                        "price": 0,
                        "calories": 269,
                        "protein": 7
                    },
                    {
                        "name": "Hummus",
                        "price": 0,
                        "calories": 55,
                        "protein": 2
                    },
                    {
                        "name": "Quinoa Lentil Salad",
                        "price": 0,
                        "calories": 64,
                        "protein": 3
                    },
                    {
                        "name": "Ruby Wild Grain Blend",
                        "price": 0,
                        "calories": 150,
                        "protein": 5
                    }
                ]
            },
            {
                "restaurant": "north-quad - Pizziti",
                "items": [
                    {
                        "name": "Italian Sausage Flatbread Pizza",
                        "price": 0,
                        "calories": 148,
                        "protein": 11
                    },
                    {
                        "name": "Cheese Flatbread Pizza",
                        "price": 0,
                        "calories": 88,
                        "protein": 6
                    }
                ]
            },
            {
                "restaurant": "north-quad - Wild Fire Maize",
                "items": [
                    {
                        "name": "Stir Fried Chicken",
                        "price": 0,
                        "calories": 130,
                        "protein": 17
                    },
                    {
                        "name": "Jalapeno Lime Sauce",
                        "price": 0,
                        "calories": 19,
                        "protein": 0
                    },
                    {
                        "name": "Vegetable Stir Fry Blend",
                        "price": 0,
                        "calories": 26,
                        "protein": 3
                    },
                    {
                        "name": "Medium Grain Rice",
                        "price": 0,
                        "calories": 157,
                        "protein": 4
                    }
                ]
            },
            {
                "restaurant": "north-quad - Wild Fire Blue",
                "items": [
                    {
                        "name": "Pork Carnitas",
                        "price": 0,
                        "calories": 150,
                        "protein": 12
                    },
                    {
                        "name": "Tortilla Chips",
                        "price": 0,
                        "calories": 142,
                        "protein": 3
                    },
                    {
                        "name": "Spicy Black Beans",
                        "price": 0,
                        "calories": 16,
                        "protein": 1
                    },
                    {
                        "name": "Cebollas Encurtidas",
                        "price": 0,
                        "calories": 23,
                        "protein": 0
                    }
                ]
            },
            {
                "restaurant": "north-quad - MBakery",
                "items": [
                    {
                        "name": "Oatmeal Raisin Cookies",
                        "price": 0,
                        "calories": 142,
                        "protein": 3
                    },
                    {
                        "name": "Chocolate Chunk Cookies",
                        "price": 0,
                        "calories": 152,
                        "protein": 3
                    }
                ]
            }
        ]
    },
    {
        "meal_time": "Dinner",
        "places": [
            {
                "restaurant": "north-quad - Soup",
                "items": [
                    {
                        "name": "Stir Fry Vegetable Soup",
                        "price": 0,
                        "calories": 33,
                        "protein": 2
                    }
                ]
            },
            {
                "restaurant": "north-quad - Signature Maize",
                "items": [
                    {
                        "name": "Piri Piri Tofu",
                        "price": 0,
                        "calories": 132,
                        "protein": 15
                    },
                    {
                        "name": "Cucumber Salad",
                        "price": 0,
                        "calories": 18,
                        "protein": 0
                    },
                    {
                        "name": "Coconut Jasmine Rice",
                        "price": 0,
                        "calories": 165,
                        "protein": 5
                    },
                    {
                        "name": "Fresh Steamed Broccoli Florets",
                        "price": 0,
                        "calories": 39,
                        "protein": 4
                    }
                ]
            },
            {
                "restaurant": "north-quad - Signature Blue",
                "items": [
                    {
                        "name": "Pita Wedges",
                        "price": 0,
                        "calories": 153,
                        "protein": 7
                    },
                    {
                        "name": "Fried Pita Chips",
                        "price": 0,
                        "calories": 269,
                        "protein": 7
                    },
                    {
                        "name": "Hummus",
                        "price": 0,
                        "calories": 55,
                        "protein": 2
                    },
                    {
                        "name": "Quinoa Lentil Salad",
                        "price": 0,
                        "calories": 64,
                        "protein": 3
                    },
                    {
                        "name": "Ruby Wild Grain Blend",
                        "price": 0,
                        "calories": 150,
                        "protein": 5
                    }
                ]
            },
            {
                "restaurant": "north-quad - Pizziti",
                "items": [
                    {
                        "name": "Italian Sausage Flatbread Pizza",
                        "price": 0,
                        "calories": 148,
                        "protein": 11
                    },
                    {
                        "name": "Cheese Flatbread Pizza",
                        "price": 0,
                        "calories": 88,
                        "protein": 6
                    }
                ]
            },
            {
                "restaurant": "north-quad - Wild Fire Maize",
                "items": [
                    {
                        "name": "Garlic Parmesan Chicken Drumsticks",
                        "price": 0,
                        "calories": 348,
                        "protein": 44
                    },
                    {
                        "name": "Italian Beans & Rice",
                        "price": 0,
                        "calories": 45,
                        "protein": 3
                    },
                    {
                        "name": "Pesto Sauce",
                        "price": 0,
                        "calories": 347,
                        "protein": 1
                    },
                    {
                        "name": "Tomato and Fresh Basil Garnish",
                        "price": 0,
                        "calories": 17,
                        "protein": 0
                    }
                ]
            },
            {
                "restaurant": "north-quad - Wild Fire Blue",
                "items": [
                    {
                        "name": "Stir Fried Chicken",
                        "price": 0,
                        "calories": 130,
                        "protein": 17
                    },
                    {
                        "name": "Jalapeno Lime Sauce",
                        "price": 0,
                        "calories": 19,
                        "protein": 0
                    },
                    {
                        "name": "Vegetable Stir Fry Blend",
                        "price": 0,
                        "calories": 53,
                        "protein": 5
                    },
                    {
                        "name": "Medium Grain Rice",
                        "price": 0,
                        "calories": 157,
                        "protein": 4
                    }
                ]
            },
            {
                "restaurant": "north-quad - MBakery",
                "items": [
                    {
                        "name": "Vernor's Bundt Cake",
                        "price": 0,
                        "calories": 445,
                        "protein": 7
                    }
                ]
            }
        ]
    },
    {
        "meal_time": "Breakfast",
        "places": [
            {
                "restaurant": "south-quad - Hot Cereal",
                "items": [
                    {
                        "name": "Oatmeal",
                        "price": 0,
                        "calories": 183,
                        "protein": 8
                    }
                ]
            },
            {
                "restaurant": "south-quad - Toast",
                "items": [
                    {
                        "name": "Bok Choy",
                        "price": 0,
                        "calories": 16,
                        "protein": 3
                    },
                    {
                        "name": "Southwest Tofu Scramble",
                        "price": 0,
                        "calories": 122,
                        "protein": 15
                    },
                    {
                        "name": "O'Brien Potatoes",
                        "price": 0,
                        "calories": 85,
                        "protein": 2
                    },
                    {
                        "name": "Scrambled Eggs",
                        "price": 0,
                        "calories": 163,
                        "protein": 15
                    },
                    {
                        "name": "Pork Sausage Links",
                        "price": 0,
                        "calories": 181,
                        "protein": 12
                    },
                    {
                        "name": "Texas French Toast",
                        "price": 0,
                        "calories": 148,
                        "protein": 9
                    }
                ]
            },
            {
                "restaurant": "south-quad - MBakery",
                "items": [
                    {
                        "name": "Blueberry Muffins",
                        "price": 0,
                        "calories": 164,
                        "protein": 2
                    },
                    {
                        "name": "Apple Cinnamon Muffins",
                        "price": 0,
                        "calories": 181,
                        "protein": 2
                    },
                    {
                        "name": "Cinnamon Rolls",
                        "price": 0,
                        "calories": 112,
                        "protein": 4
                    }
                ]
            }
        ]
    },
    {
        "meal_time": "Lunch",
        "places": [
            {
                "restaurant": "south-quad - Soup",
                "items": [
                    {
                        "name": "Authentic Minestrone",
                        "price": 0,
                        "calories": 122,
                        "protein": 7
                    },
                    {
                        "name": "Beef Chili",
                        "price": 0,
                        "calories": 150,
                        "protein": 11
                    }
                ]
            },
            {
                "restaurant": "south-quad - Signature Maize",
                "items": [
                    {
                        "name": "French Dip Sandwich",
                        "price": 0,
                        "calories": 222,
                        "protein": 23
                    },
                    {
                        "name": "Au Jus",
                        "price": 0,
                        "calories": 2,
                        "protein": 0
                    },
                    {
                        "name": "Kettle Potato Chips",
                        "price": 0,
                        "calories": 162,
                        "protein": 3
                    }
                ]
            },
            {
                "restaurant": "south-quad - 24 Carrots",
                "items": [
                    {
                        "name": "Vegan Chili Cornbread Pie",
                        "price": 0,
                        "calories": 282,
                        "protein": 13
                    },
                    {
                        "name": "Pickled Jalapeno Peppers",
                        "price": 0,
                        "calories": 3,
                        "protein": 0
                    },
                    {
                        "name": "Sliced Tomatoes",
                        "price": 0,
                        "calories": 8,
                        "protein": 1
                    },
                    {
                        "name": "Crispy Veggie Patty on White Bun",
                        "price": 0,
                        "calories": 241,
                        "protein": 16
                    },
                    {
                        "name": "Sauteed Swiss Chard",
                        "price": 0,
                        "calories": 42,
                        "protein": 2
                    },
                    {
                        "name": "Quinoa Lentil Salad",
                        "price": 0,
                        "calories": 64,
                        "protein": 3
                    }
                ]
            },
            {
                "restaurant": "south-quad - Halal",
                "items": [
                    {
                        "name": "Herb Baked Chicken",
                        "price": 0,
                        "calories": 155,
                        "protein": 21
                    },
                    {
                        "name": "Roasted Fingerling Potatoes",
                        "price": 0,
                        "calories": 180,
                        "protein": 3
                    },
                    {
                        "name": "Roasted Michigan Vegetables",
                        "price": 0,
                        "calories": 69,
                        "protein": 2
                    }
                ]
            },
            {
                "restaurant": "south-quad - Vita",
                "items": [
                    {
                        "name": "Bowtie Pasta",
                        "price": 0,
                        "calories": 92,
                        "protein": 5
                    },
                    {
                        "name": "Garlic Cream Sauce",
                        "price": 0,
                        "calories": 226,
                        "protein": 1
                    },
                    {
                        "name": "Marinara Sauce",
                        "price": 0,
                        "calories": 32,
                        "protein": 1
                    }
                ]
            },
            {
                "restaurant": "south-quad - Sabroso",
                "items": [
                    {
                        "name": "Taco Chicken",
                        "price": 0,
                        "calories": 79,
                        "protein": 11
                    },
                    {
                        "name": "Mojito Tofu",
                        "price": 0,
                        "calories": 112,
                        "protein": 16
                    },
                    {
                        "name": "Yellow Rice",
                        "price": 0,
                        "calories": 191,
                        "protein": 5
                    },
                    {
                        "name": "Sauteed Mixed Peppers & Onions",
                        "price": 0,
                        "calories": 12,
                        "protein": 0
                    }
                ]
            },
            {
                "restaurant": "south-quad - Pizziti",
                "items": [
                    {
                        "name": "Chicken Ranch Pizza with Bacon",
                        "price": 0,
                        "calories": 319,
                        "protein": 21
                    },
                    {
                        "name": "Pepperoni Pizza",
                        "price": 0,
                        "calories": 219,
                        "protein": 12
                    },
                    {
                        "name": "Cheese Pizza",
                        "price": 0,
                        "calories": 198,
                        "protein": 11
                    }
                ]
            },
            {
                "restaurant": "south-quad - Wild Fire Maize",
                "items": [
                    {
                        "name": "Beef and Mushroom Blended Burger",
                        "price": 0,
                        "calories": 277,
                        "protein": 32
                    },
                    {
                        "name": "Halal Paprika Chicken Breast White Bun",
                        "price": 0,
                        "calories": 194,
                        "protein": 29
                    },
                    {
                        "name": "French Fries",
                        "price": 0,
                        "calories": 190,
                        "protein": 2
                    }
                ]
            },
            {
                "restaurant": "south-quad - Two Oceans",
                "items": [
                    {
                        "name": "Marinated Beef",
                        "price": 0,
                        "calories": 118,
                        "protein": 21
                    },
                    {
                        "name": "Japanese Curry",
                        "price": 0,
                        "calories": 44,
                        "protein": 1
                    },
                    {
                        "name": "Medium Grain Rice",
                        "price": 0,
                        "calories": 157,
                        "protein": 4
                    },
                    {
                        "name": "Oven Roasted Vegetables",
                        "price": 0,
                        "calories": 54,
                        "protein": 2
                    }
                ]
            },
            {
                "restaurant": "south-quad - Smoke",
                "items": [
                    {
                        "name": "BBQ Chicken on White Bun",
                        "price": 0,
                        "calories": 274,
                        "protein": 27
                    },
                    {
                        "name": "Creamy Coleslaw Salad",
                        "price": 0,
                        "calories": 165,
                        "protein": 1
                    }
                ]
            },
            {
                "restaurant": "south-quad - Kosher",
                "items": [
                    {
                        "name": "Vegetable Rice Soup",
                        "price": 0,
                        "calories": 83,
                        "protein": 3
                    },
                    {
                        "name": "Beef Mostaccioli",
                        "price": 0,
                        "calories": 164,
                        "protein": 15
                    },
                    {
                        "name": "Vegan Mostaccioli",
                        "price": 0,
                        "calories": 71,
                        "protein": 4
                    },
                    {
                        "name": "Green Peas",
                        "price": 0,
                        "calories": 76,
                        "protein": 7
                    },
                    {
                        "name": "Romaine Salad",
                        "price": 0,
                        "calories": 11,
                        "protein": 1
                    },
                    {
                        "name": "Fresh Fruit Cup",
                        "price": 0,
                        "calories": 46,
                        "protein": 1
                    }
                ]
            },
            {
                "restaurant": "south-quad - Breads and Rolls",
                "items": [
                    {
                        "name": "White Sandwich Loaf",
                        "price": 0,
                        "calories": 88,
                        "protein": 4
                    },
                    {
                        "name": "Whipped Butter",
                        "price": 0,
                        "calories": 102,
                        "protein": 0
                    },
                    {
                        "name": "Whipped Margarine",
                        "price": 0,
                        "calories": 67,
                        "protein": 0
                    }
                ]
            },
            {
                "restaurant": "south-quad - Deli",
                "items": []
            },
            {
                "restaurant": "south-quad - MBakery",
                "items": [
                    {
                        "name": "Birthday Cake Bars",
                        "price": 0,
                        "calories": 472,
                        "protein": 6
                    },
                    {
                        "name": "Blueberry Banana Cake w/Coconut",
                        "price": 0,
                        "calories": 407,
                        "protein": 4
                    },
                    {
                        "name": "Sugar Cookies",
                        "price": 0,
                        "calories": 162,
                        "protein": 3
                    },
                    {
                        "name": "Chocolate Chunk Cookies",
                        "price": 0,
                        "calories": 152,
                        "protein": 3
                    }
                ]
            }
        ]
    },
    {
        "meal_time": "Dinner",
        "places": [
            {
                "restaurant": "south-quad - Soup",
                "items": [
                    {
                        "name": "Authentic Minestrone",
                        "price": 0,
                        "calories": 122,
                        "protein": 7
                    },
                    {
                        "name": "Beef Chili",
                        "price": 0,
                        "calories": 150,
                        "protein": 11
                    }
                ]
            },
            {
                "restaurant": "south-quad - Signature Maize",
                "items": [
                    {
                        "name": "Halal Roast Beef",
                        "price": 0,
                        "calories": 232,
                        "protein": 31
                    },
                    {
                        "name": "Garlicky Mashed Potatoes",
                        "price": 0,
                        "calories": 131,
                        "protein": 3
                    },
                    {
                        "name": "Roasted Brussels Sprouts",
                        "price": 0,
                        "calories": 49,
                        "protein": 5
                    },
                    {
                        "name": "Blue Cheese Cream Sauce",
                        "price": 0,
                        "calories": 95,
                        "protein": 4
                    }
                ]
            },
            {
                "restaurant": "south-quad - 24 Carrots",
                "items": [
                    {
                        "name": "Cajun Tofu",
                        "price": 0,
                        "calories": 136,
                        "protein": 15
                    },
                    {
                        "name": "Fresh Pineapple Salsa",
                        "price": 0,
                        "calories": 34,
                        "protein": 0
                    },
                    {
                        "name": "Red Beans & Rice",
                        "price": 0,
                        "calories": 154,
                        "protein": 9
                    },
                    {
                        "name": "Cauliflower",
                        "price": 0,
                        "calories": 28,
                        "protein": 3
                    },
                    {
                        "name": "Crispy Veggie Patty on White Bun",
                        "price": 0,
                        "calories": 241,
                        "protein": 16
                    },
                    {
                        "name": "Sauteed Swiss Chard",
                        "price": 0,
                        "calories": 42,
                        "protein": 2
                    },
                    {
                        "name": "Quinoa Lentil Salad",
                        "price": 0,
                        "calories": 64,
                        "protein": 3
                    }
                ]
            },
            {
                "restaurant": "south-quad - Halal",
                "items": [
                    {
                        "name": "Blackened Chicken Thigh",
                        "price": 0,
                        "calories": 141,
                        "protein": 21
                    },
                    {
                        "name": "Crispy Salt & Vinegar Potatoes",
                        "price": 0,
                        "calories": 132,
                        "protein": 3
                    },
                    {
                        "name": "Spinach Saute",
                        "price": 0,
                        "calories": 23,
                        "protein": 2
                    },
                    {
                        "name": "Skillet Corn Sauce",
                        "price": 0,
                        "calories": 36,
                        "protein": 1
                    }
                ]
            },
            {
                "restaurant": "south-quad - Vita",
                "items": [
                    {
                        "name": "Gemelli Pasta",
                        "price": 0,
                        "calories": 92,
                        "protein": 5
                    },
                    {
                        "name": "Garlic Cream Sauce",
                        "price": 0,
                        "calories": 226,
                        "protein": 1
                    },
                    {
                        "name": "Marinara Sauce",
                        "price": 0,
                        "calories": 32,
                        "protein": 1
                    }
                ]
            },
            {
                "restaurant": "south-quad - Sabroso",
                "items": []
            },
            {
                "restaurant": "south-quad - Pizziti",
                "items": [
                    {
                        "name": "Chicken Ranch Pizza with Bacon",
                        "price": 0,
                        "calories": 319,
                        "protein": 21
                    },
                    {
                        "name": "Pepperoni Pizza",
                        "price": 0,
                        "calories": 219,
                        "protein": 12
                    },
                    {
                        "name": "Cheese Pizza",
                        "price": 0,
                        "calories": 198,
                        "protein": 11
                    }
                ]
            },
            {
                "restaurant": "south-quad - Wild Fire Maize",
                "items": [
                    {
                        "name": "Beef and Mushroom Blended Burger",
                        "price": 0,
                        "calories": 277,
                        "protein": 32
                    },
                    {
                        "name": "Halal Paprika Chicken Breast White Bun",
                        "price": 0,
                        "calories": 194,
                        "protein": 29
                    },
                    {
                        "name": "French Fries",
                        "price": 0,
                        "calories": 190,
                        "protein": 2
                    }
                ]
            },
            {
                "restaurant": "south-quad - Two Oceans",
                "items": [
                    {
                        "name": "Stir Fried Chicken",
                        "price": 0,
                        "calories": 59,
                        "protein": 13
                    },
                    {
                        "name": "Tofu",
                        "price": 0,
                        "calories": 80,
                        "protein": 12
                    },
                    {
                        "name": "Stir Fry Hunan Sauce",
                        "price": 0,
                        "calories": 90,
                        "protein": 0
                    },
                    {
                        "name": "Teriyaki Sauce",
                        "price": 0,
                        "calories": 46,
                        "protein": 2
                    }
                ]
            },
            {
                "restaurant": "south-quad - Kosher",
                "items": []
            },
            {
                "restaurant": "south-quad - Deli",
                "items": []
            },
            {
                "restaurant": "south-quad - MBakery",
                "items": [
                    {
                        "name": "Vernor's Bundt Cake",
                        "price": 0,
                        "calories": 445,
                        "protein": 7
                    },
                    {
                        "name": "Blueberry Banana Cake w/Coconut",
                        "price": 0,
                        "calories": 407,
                        "protein": 4
                    },
                    {
                        "name": "Sugar Cookies",
                        "price": 0,
                        "calories": 162,
                        "protein": 3
                    },
                    {
                        "name": "Chocolate Chunk Cookies",
                        "price": 0,
                        "calories": 152,
                        "protein": 3
                    }
                ]
            }
        ]
    },
    {
        "meal_time": "Breakfast",
        "places": [
            {
                "restaurant": "twigs-at-oxford - Hot Cereal",
                "items": [
                    {
                        "name": "Oatmeal",
                        "price": 0,
                        "calories": 183,
                        "protein": 8
                    }
                ]
            },
            {
                "restaurant": "twigs-at-oxford - Toast",
                "items": [
                    {
                        "name": "Korean Style Breakfast Power Bowl",
                        "price": 0,
                        "calories": 262,
                        "protein": 19
                    },
                    {
                        "name": "Veggie Breakfast Sausage Patties",
                        "price": 0,
                        "calories": 70,
                        "protein": 12
                    },
                    {
                        "name": "Scrambled Eggs",
                        "price": 0,
                        "calories": 163,
                        "protein": 15
                    },
                    {
                        "name": "Cinnamon Swirl French Toast",
                        "price": 0,
                        "calories": 139,
                        "protein": 6
                    },
                    {
                        "name": "Patatas Bravas",
                        "price": 0,
                        "calories": 159,
                        "protein": 2
                    },
                    {
                        "name": "Sauteed Mixed Peppers & Onions",
                        "price": 0,
                        "calories": 12,
                        "protein": 0
                    },
                    {
                        "name": "Scrambled Tofu",
                        "price": 0,
                        "calories": 157,
                        "protein": 18
                    }
                ]
            },
            {
                "restaurant": "twigs-at-oxford - MBakery",
                "items": [
                    {
                        "name": "Blueberry Muffins",
                        "price": 0,
                        "calories": 164,
                        "protein": 2
                    },
                    {
                        "name": "Cinnamon Sugar Donuts",
                        "price": 0,
                        "calories": 314,
                        "protein": 5
                    },
                    {
                        "name": "Apple Cinnamon Muffins",
                        "price": 0,
                        "calories": 181,
                        "protein": 2
                    }
                ]
            }
        ]
    },
    {
        "meal_time": "Lunch",
        "places": [
            {
                "restaurant": "twigs-at-oxford - Soup",
                "items": [
                    {
                        "name": "Loaded Baked Potato Soup",
                        "price": 0,
                        "calories": 442,
                        "protein": 13
                    }
                ]
            },
            {
                "restaurant": "twigs-at-oxford - Signature Maize",
                "items": [
                    {
                        "name": "BBQ Chicken Sandwich w/ White Bun",
                        "price": 0,
                        "calories": 305,
                        "protein": 25
                    },
                    {
                        "name": "Chipotle Lime Cauliflower Florets",
                        "price": 0,
                        "calories": 79,
                        "protein": 3
                    },
                    {
                        "name": "Wild Rice Blend",
                        "price": 0,
                        "calories": 122,
                        "protein": 3
                    },
                    {
                        "name": "Orange Tofu Stir Fry",
                        "price": 0,
                        "calories": 136,
                        "protein": 8
                    }
                ]
            },
            {
                "restaurant": "twigs-at-oxford - Halal",
                "items": [
                    {
                        "name": "Taco Beef",
                        "price": 0,
                        "calories": 131,
                        "protein": 11
                    },
                    {
                        "name": "Yellow Rice",
                        "price": 0,
                        "calories": 381,
                        "protein": 10
                    }
                ]
            },
            {
                "restaurant": "twigs-at-oxford - Wild Fire Maize",
                "items": [
                    {
                        "name": "French Fries",
                        "price": 0,
                        "calories": 190,
                        "protein": 2
                    },
                    {
                        "name": "Black Bean Vegetarian Patty",
                        "price": 0,
                        "calories": 150,
                        "protein": 19
                    },
                    {
                        "name": "Beef & Mushroom Blended Burger w/ Cheese",
                        "price": 0,
                        "calories": 364,
                        "protein": 39
                    },
                    {
                        "name": "Turkey Burger on White Bun",
                        "price": 0,
                        "calories": 261,
                        "protein": 35
                    }
                ]
            },
            {
                "restaurant": "twigs-at-oxford - MBakery",
                "items": [
                    {
                        "name": "Birthday Cake Bars",
                        "price": 0,
                        "calories": 472,
                        "protein": 6
                    },
                    {
                        "name": "Blueberry Banana Cake w/Coconut",
                        "price": 0,
                        "calories": 407,
                        "protein": 4
                    },
                    {
                        "name": "Monster Candy Cookies",
                        "price": 0,
                        "calories": 152,
                        "protein": 3
                    },
                    {
                        "name": "Chocolate Chunk Cookies",
                        "price": 0,
                        "calories": 152,
                        "protein": 3
                    }
                ]
            }
        ]
    },
    {
        "meal_time": "Dinner",
        "places": [
            {
                "restaurant": "twigs-at-oxford - Soup",
                "items": [
                    {
                        "name": "Loaded Baked Potato Soup",
                        "price": 0,
                        "calories": 442,
                        "protein": 13
                    }
                ]
            },
            {
                "restaurant": "twigs-at-oxford - Signature Maize",
                "items": [
                    {
                        "name": "Homemade Sweet Chili Chicken Wings",
                        "price": 0,
                        "calories": 276,
                        "protein": 27
                    },
                    {
                        "name": "Chicken Wings",
                        "price": 0,
                        "calories": 273,
                        "protein": 28
                    },
                    {
                        "name": "Fried Cauliflower Buffalo Bites",
                        "price": 0,
                        "calories": 256,
                        "protein": 5
                    },
                    {
                        "name": "Fried Breaded Cauliflower",
                        "price": 0,
                        "calories": 229,
                        "protein": 5
                    },
                    {
                        "name": "Filipino Vegetable Pancit",
                        "price": 0,
                        "calories": 174,
                        "protein": 5
                    },
                    {
                        "name": "Spring Rolls",
                        "price": 0,
                        "calories": 49,
                        "protein": 1
                    }
                ]
            },
            {
                "restaurant": "twigs-at-oxford - Halal",
                "items": [
                    {
                        "name": "Lamb Gyro Meat",
                        "price": 0,
                        "calories": 139,
                        "protein": 12
                    },
                    {
                        "name": "Lemon Parsley Rice",
                        "price": 0,
                        "calories": 152,
                        "protein": 5
                    },
                    {
                        "name": "Garlic Sauce",
                        "price": 0,
                        "calories": 189,
                        "protein": 0
                    },
                    {
                        "name": "Grilled Vegetables",
                        "price": 0,
                        "calories": 53,
                        "protein": 2
                    }
                ]
            },
            {
                "restaurant": "twigs-at-oxford - MBakery",
                "items": [
                    {
                        "name": "Blueberry Banana Cake w/Coconut",
                        "price": 0,
                        "calories": 407,
                        "protein": 4
                    },
                    {
                        "name": "Vernor's Bundt Cake",
                        "price": 0,
                        "calories": 445,
                        "protein": 7
                    }
                ]
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

