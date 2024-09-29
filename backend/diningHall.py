from scraper import scrape

rootDiningHallLink = "https://dining.umich.edu/menus-locations/dining-halls/"
dateFormat = "/?menuDate=2024-"
diningHallsExtension = ["bursley", "east-quad", "markley", "mosher-jordan", "north-quad", "south-quad", "twigs-at-oxford"]

dayInput = "04"
monthInput = "10"

month = monthInput
day = dayInput

foods = []
links = []

for hall in diningHallsExtension:
    finalLink = rootDiningHallLink+hall+dateFormat+month+"-"+day
    links.append(finalLink)

for count, link in enumerate(links):
    scrape(link, diningHallsExtension[count])
    
    