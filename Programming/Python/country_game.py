import random
capitals = {
    "Azerbaijan":"Baku"
    "United States": "Washington DC",
    "Canada": "Ottawa",
    "United Kingdom": "London",
    "Australia": "Canberra",
    "Germany": "Berlin",
    "France": "Paris",
    "Italy": "Rome",
    "Spain": "Madrid",
    "India": "New Delhi",
    "China": "Beijing",
    "Japan": "Tokyo",
    "Brazil": "Brasilia",
    "Mexico": "Mexico City",
    "Russia": "Moscow",
    "Argentina": "Buenos Aires",
    "Egypt": "Cairo",
    "Saudi Arabia": "Riyadh",
    "Turkey": "Ankara",
    "Indonesia": "Jakarta",
    "Nigeria": "Abuja",
    "Pakistan": "Islamabad",
    "Philippines": "Manila",
    "Vietnam": "Hanoi",
    "Thailand": "Bangkok",
    "Colombia": "Bogota",
    "Chile": "Santiago",
    "Malaysia": "Kuala Lumpur",
    "Singapore": "Singapore",
    "South Korea": "Seoul",
    "New Zealand": "Wellington",
    "Ukraine": "Kyiv",
    "Greece": "Athens",
    "Sweden": "Stockholm",
    "Norway": "Oslo",
    "Finland": "Helsinki",
    "Denmark": "Copenhagen",
    "Belgium": "Brussels",
    "Netherlands": "Amsterdam",
    "Portugal": "Lisbon",
    "Switzerland": "Bern",
    "Austria": "Vienna",
    "Czech Republic": "Prague",
    "Hungary": "Budapest",
    "Iceland": "Reykjavik",
    "Ireland": "Dublin",
    "Bangladesh": "Dhaka",
    "Kenya": "Nairobi",
    "Tanzania": "Dodoma",
    "Uganda": "Kampala",
    "Zimbabwe": "Harare",
    "Morocco": "Rabat",
    "Algeria": "Algiers",
    "Tunisia": "Tunis",
    "Iran": "Tehran",
    "Iraq": "Baghdad",
    "Afghanistan": "Kabul"
}
countries = [x for x in capitals.keys()]
points = 0
while len(countries) != 0:
    count = random.choice(countries)
    answ = input(f'What is the capital of {count}? ')
    if answ == capitals[count]:
        print('Yes!')
        points += 1
    else:
        print('Wrong. The answer is',capitals[count])
    countries.remove(count)

print('Your score:',points)
