#Give the user the ability to show anwser if they dont know
#Include hints and rewards for each question
#In the result, count how many capitals they got correct and how many countries, and show which ones they got correct and wrong
#Guess the country from the emoji flag 🇺🇸
#Include geographic questions like "Which country is known as the Land of a Thousand Lakes?"
#Advanced: Add a timer for each question to increase the difficulty and excitement.
#Advanced: Guess countries based on coordinates
#Plot successful guesses on an interactive map with Folium
#Use libraries like pygame for graphics and sound effects to make the game more engaging.

import random
from tkinter import *

class GeographyGame(Tk):
    def __init__(self):
        super().__init__()
        self.title("Geography Guessing Game")
        self.geometry('550x550')
        self.create_welcome_screen()
        
        #Variables required to play the game and show the result
        self.right = 0
        self.wrong = 0 

        self.countries_capitals = {
            "Afghanistan": "Kabul",
            "Albania": "Tirana",
            "Algeria": "Algiers",
            "Andorra": "Andorra la Vella",
            "Angola": "Luanda",
            "Antigua and Barbuda": "Saint John's",
            "Argentina": "Buenos Aires",
            "Armenia": "Yerevan",
            "Australia": "Canberra",
            "Austria": "Vienna",
            "Azerbaijan": "Baku",
            "Bahamas": "Nassau",
            "Bahrain": "Manama",
            "Bangladesh": "Dhaka",
            "Barbados": "Bridgetown",
            "Belarus": "Minsk",
            "Belgium": "Brussels",
            "Belize": "Belmopan",
            "Benin": "Porto-Novo",
            "Bhutan": "Thimphu",
            "Bolivia": "Sucre",
            "Bosnia and Herzegovina": "Sarajevo",
            "Botswana": "Gaborone",
            "Brazil": "Brasília",
            "Brunei": "Bandar Seri Begawan",
            "Bulgaria": "Sofia",
            "Burkina Faso": "Ouagadougou",
            "Burundi": "Gitega",
            "Cabo Verde": "Praia",
            "Cambodia": "Phnom Penh",
            "Cameroon": "Yaoundé",
            "Canada": "Ottawa",
            "Central African Republic": "Bangui",
            "Chad": "N'Djamena",
            "Chile": "Santiago",
            "China": "Beijing",
            "Colombia": "Bogotá",
            "Comoros": "Moroni",
            "Congo, Democratic Republic of the": "Kinshasa",
            "Congo, Republic of the": "Brazzaville",
            "Costa Rica": "San José",
            "Croatia": "Zagreb",
            "Cuba": "Havana",
            "Cyprus": "Nicosia",
            "Czech Republic": "Prague",
            "Denmark": "Copenhagen",
            "Djibouti": "Djibouti",
            "Dominica": "Roseau",
            "Dominican Republic": "Santo Domingo",
            "Ecuador": "Quito",
            "Egypt": "Cairo",
            "El Salvador": "San Salvador",
            "Equatorial Guinea": "Malabo",
            "Eritrea": "Asmara",
            "Estonia": "Tallinn",
            "Eswatini": "Mbabane",
            "Ethiopia": "Addis Ababa",
            "Fiji": "Suva",
            "Finland": "Helsinki",
            "France": "Paris",
            "Gabon": "Libreville",
            "Gambia": "Banjul",
            "Georgia": "Tbilisi",
            "Germany": "Berlin",
            "Ghana": "Accra",
            "Greece": "Athens",
            "Grenada": "Saint George's",
            "Guatemala": "Guatemala City",
            "Guinea": "Conakry",
            "Guinea-Bissau": "Bissau",
            "Guyana": "Georgetown",
            "Haiti": "Port-au-Prince",
            "Honduras": "Tegucigalpa",
            "Hungary": "Budapest",
            "Iceland": "Reykjavík",
            "India": "New Delhi",
            "Indonesia": "Jakarta",
            "Iran": "Tehran",
            "Iraq": "Baghdad",
            "Ireland": "Dublin",
            "Israel": "Jerusalem",
            "Italy": "Rome",
            "Jamaica": "Kingston",
            "Japan": "Tokyo",
            "Jordan": "Amman",
            "Kazakhstan": "Nur-Sultan",
            "Kenya": "Nairobi",
            "Kiribati": "Tarawa",
            "Korea, North": "Pyongyang",
            "Korea, South": "Seoul",
            "Kosovo": "Pristina",
            "Kuwait": "Kuwait City",
            "Kyrgyzstan": "Bishkek",
            "Laos": "Vientiane",
            "Latvia": "Riga",
            "Lebanon": "Beirut",
            "Lesotho": "Maseru",
            "Liberia": "Monrovia",
            "Libya": "Tripoli",
            "Liechtenstein": "Vaduz",
            "Lithuania": "Vilnius",
            "Luxembourg": "Luxembourg",
            "Madagascar": "Antananarivo",
            "Malawi": "Lilongwe",
            "Malaysia": "Kuala Lumpur",
            "Maldives": "Malé",
            "Mali": "Bamako",
            "Malta": "Valletta",
            "Marshall Islands": "Majuro",
            "Mauritania": "Nouakchott",
            "Mauritius": "Port Louis",
            "Mexico": "Mexico City",
            "Micronesia": "Palikir",
            "Moldova": "Chișinău",
            "Monaco": "Monaco",
            "Mongolia": "Ulaanbaatar",
            "Montenegro": "Podgorica",
            "Morocco": "Rabat",
            "Mozambique": "Maputo",
            "Myanmar": "Naypyidaw",
            "Namibia": "Windhoek",
            "Nauru": "Yaren District (de facto)",
            "Nepal": "Kathmandu",
            "Netherlands": "Amsterdam",
            "New Zealand": "Wellington",
            "Nicaragua": "Managua",
            "Niger": "Niamey",
            "Nigeria": "Abuja",
            "North Macedonia": "Skopje",
            "Norway": "Oslo",
            "Oman": "Muscat",
            "Pakistan": "Islamabad",
            "Palau": "Ngerulmud",
            "Panama": "Panama City",
            "Papua New Guinea": "Port Moresby",
            "Paraguay": "Asunción",
            "Peru": "Lima",
            "Philippines": "Manila",
            "Poland": "Warsaw",
            "Portugal": "Lisbon",
            "Qatar": "Doha",
            "Romania": "Bucharest",
            "Russia": "Moscow",
            "Rwanda": "Kigali",
            "Saint Kitts and Nevis": "Basseterre",
            "Saint Lucia": "Castries",
            "Saint Vincent and the Grenadines": "Kingstown",
            "Samoa": "Apia",
            "San Marino": "San Marino",
            "Sao Tome and Principe": "São Tomé",
            "Saudi Arabia": "Riyadh",
            "Senegal": "Dakar",
            "Serbia": "Belgrade",
            "Seychelles": "Victoria",
            "Sierra Leone": "Freetown",
            "Singapore": "Singapore",
            "Slovakia": "Bratislava",
            "Slovenia": "Ljubljana",
            "Solomon Islands": "Honiara",
            "Somalia": "Mogadishu",
            "South Africa": "Pretoria (administrative), Bloemfontein (judicial), Cape Town (legislative)",
            "South Sudan": "Juba",
            "Spain": "Madrid",
            "Sri Lanka": "Sri Jayawardenepura Kotte",
            "Sudan": "Khartoum",
            "Suriname": "Paramaribo",
            "Sweden": "Stockholm",
            "Switzerland": "Bern",
            "Syria": "Damascus",
            "Taiwan": "Taipei",
            "Tajikistan": "Dushanbe",
            "Tanzania": "Dodoma",
            "Thailand": "Bangkok",
            "Timor-Leste": "Dili",
            "Togo": "Lomé",
            "Tonga": "Nuku'alofa",
            "Trinidad and Tobago": "Port of Spain",
            "Tunisia": "Tunis",
            "Turkey": "Ankara",
            "Turkmenistan": "Ashgabat",
            "Tuvalu": "Funafuti",
            "Uganda": "Kampala",
            "Ukraine": "Kyiv",
            "United Arab Emirates": "Abu Dhabi",
            "United Kingdom": "London",
            "United States": "Washington, D.C.",
            "Uruguay": "Montevideo",
            "Uzbekistan": "Tashkent",
            "Vanuatu": "Port Vila",
            "Vatican City": "Vatican City",
            "Venezuela": "Caracas",
            "Vietnam": "Hanoi",
            "Yemen": "Sana'a",
            "Zambia": "Lusaka",
            "Zimbabwe": "Harare"
        }

        self.capitals_countries = {
            "Kabul": "Afghanistan",
            "Tirana": "Albania",
            "Algiers": "Algeria",
            "Andorra la Vella": "Andorra",
            "Luanda": "Angola",
            "Saint John's": "Antigua and Barbuda",
            "Buenos Aires": "Argentina",
            "Yerevan": "Armenia",
            "Canberra": "Australia",
            "Vienna": "Austria",
            "Baku": "Azerbaijan",
            "Nassau": "Bahamas",
            "Manama": "Bahrain",
            "Dhaka": "Bangladesh",
            "Bridgetown": "Barbados",
            "Minsk": "Belarus",
            "Brussels": "Belgium",
            "Belmopan": "Belize",
            "Porto-Novo": "Benin",
            "Thimphu": "Bhutan",
            "Sucre": "Bolivia",
            "Sarajevo": "Bosnia and Herzegovina",
            "Gaborone": "Botswana",
            "Brasília": "Brazil",
            "Bandar Seri Begawan": "Brunei",
            "Sofia": "Bulgaria",
            "Ouagadougou": "Burkina Faso",
            "Gitega": "Burundi",
            "Praia": "Cabo Verde",
            "Phnom Penh": "Cambodia",
            "Yaoundé": "Cameroon",
            "Ottawa": "Canada",
            "Bangui": "Central African Republic",
            "N'Djamena": "Chad",
            "Santiago": "Chile",
            "Beijing": "China",
            "Bogotá": "Colombia",
            "Moroni": "Comoros",
            "Kinshasa": "Congo, Democratic Republic of the",
            "Brazzaville": "Congo, Republic of the",
            "San José": "Costa Rica",
            "Zagreb": "Croatia",
            "Havana": "Cuba",
            "Nicosia": "Cyprus",
            "Prague": "Czech Republic",
            "Copenhagen": "Denmark",
            "Djibouti": "Djibouti",
            "Roseau": "Dominica",
            "Santo Domingo": "Dominican Republic",
            "Quito": "Ecuador",
            "Cairo": "Egypt",
            "San Salvador": "El Salvador",
            "Malabo": "Equatorial Guinea",
            "Asmara": "Eritrea",
            "Tallinn": "Estonia",
            "Mbabane": "Eswatini",
            "Addis Ababa": "Ethiopia",
            "Suva": "Fiji",
            "Helsinki": "Finland",
            "Paris": "France",
            "Libreville": "Gabon",
            "Banjul": "Gambia",
            "Tbilisi": "Georgia",
            "Berlin": "Germany",
            "Accra": "Ghana",
            "Athens": "Greece",
            "Saint George's": "Grenada",
            "Guatemala City": "Guatemala",
            "Conakry": "Guinea",
            "Bissau": "Guinea-Bissau",
            "Georgetown": "Guyana",
            "Port-au-Prince": "Haiti",
            "Tegucigalpa": "Honduras",
            "Budapest": "Hungary",
            "Reykjavík": "Iceland",
            "New Delhi": "India",
            "Jakarta": "Indonesia",
            "Tehran": "Iran",
            "Baghdad": "Iraq",
            "Dublin": "Ireland",
            "Jerusalem": "Israel",
            "Rome": "Italy",
            "Kingston": "Jamaica",
            "Tokyo": "Japan",
            "Amman": "Jordan",
            "Nur-Sultan": "Kazakhstan",
            "Nairobi": "Kenya",
            "Tarawa": "Kiribati",
            "Pyongyang": "Korea, North",
            "Seoul": "Korea, South",
            "Pristina": "Kosovo",
            "Kuwait City": "Kuwait",
            "Bishkek": "Kyrgyzstan",
            "Vientiane": "Laos",
            "Riga": "Latvia",
            "Beirut": "Lebanon",
            "Maseru": "Lesotho",
            "Monrovia": "Liberia",
            "Tripoli": "Libya",
            "Vaduz": "Liechtenstein",
            "Vilnius": "Lithuania",
            "Luxembourg": "Luxembourg",
            "Antananarivo": "Madagascar",
            "Lilongwe": "Malawi",
            "Kuala Lumpur": "Malaysia",
            "Malé": "Maldives",
            "Bamako": "Mali",
            "Valletta": "Malta",
            "Majuro": "Marshall Islands",
            "Nouakchott": "Mauritania",
            "Port Louis": "Mauritius",
            "Mexico City": "Mexico",
            "Palikir": "Micronesia",
            "Chișinău": "Moldova",
            "Monaco": "Monaco",
            "Ulaanbaatar": "Mongolia",
            "Podgorica": "Montenegro",
            "Rabat": "Morocco",
            "Maputo": "Mozambique",
            "Naypyidaw": "Myanmar",
            "Windhoek": "Namibia",
            "Yaren District (de facto)": "Nauru",
            "Kathmandu": "Nepal",
            "Amsterdam": "Netherlands",
            "Wellington": "New Zealand",
            "Managua": "Nicaragua",
            "Niamey": "Niger",
            "Abuja": "Nigeria",
            "Skopje": "North Macedonia",
            "Oslo": "Norway",
            "Muscat": "Oman",
            "Islamabad": "Pakistan",
            "Ngerulmud": "Palau",
            "Panama City": "Panama",
            "Port Moresby": "Papua New Guinea",
            "Asunción": "Paraguay",
            "Lima": "Peru",
            "Manila": "Philippines",
            "Warsaw": "Poland",
            "Lisbon": "Portugal",
            "Doha": "Qatar",
            "Bucharest": "Romania",
            "Moscow": "Russia",
            "Kigali": "Rwanda",
            "Basseterre": "Saint Kitts and Nevis",
            "Castries": "Saint Lucia",
            "Kingstown": "Saint Vincent and the Grenadines",
            "Apia": "Samoa",
            "San Marino": "San Marino",
            "São Tomé": "Sao Tome and Principe",
            "Riyadh": "Saudi Arabia",
            "Dakar": "Senegal",
            "Belgrade": "Serbia",
            "Victoria": "Seychelles",
            "Freetown": "Sierra Leone",
            "Singapore": "Singapore",
            "Bratislava": "Slovakia",
            "Ljubljana": "Slovenia",
            "Honiara": "Solomon Islands",
            "Mogadishu": "Somalia",
            "Pretoria (administrative), Bloemfontein (judicial), Cape Town (legislative)": "South Africa",
            "Juba": "South Sudan",
            "Madrid": "Spain",
            "Sri Jayawardenepura Kotte": "Sri Lanka",
            "Khartoum": "Sudan",
            "Paramaribo": "Suriname",
            "Stockholm": "Sweden",
            "Bern": "Switzerland",
            "Damascus": "Syria",
            "Taipei": "Taiwan",
            "Dushanbe": "Tajikistan",
            "Dodoma": "Tanzania",
            "Bangkok": "Thailand",
            "Dili": "Timor-Leste",
            "Lomé": "Togo",
            "Nuku'alofa": "Tonga",
            "Port of Spain": "Trinidad and Tobago",
            "Tunis": "Tunisia",
            "Ankara": "Turkey",
            "Ashgabat": "Turkmenistan",
            "Funafuti": "Tuvalu",
            "Kampala": "Uganda",
            "Kyiv": "Ukraine",
            "Abu Dhabi": "United Arab Emirates",
            "London": "United Kingdom",
            "Washington, D.C.": "United States",
            "Montevideo": "Uruguay",
            "Tashkent": "Uzbekistan",
            "Port Vila": "Vanuatu",
            "Vatican City": "Vatican City",
            "Caracas": "Venezuela",
            "Hanoi": "Vietnam",
            "Sana'a": "Yemen",
            "Lusaka": "Zambia",
            "Harare": "Zimbabwe"
        }
    
    def create_welcome_screen(self):
        self.clear_screen()

        welcome_label = Label(self, text=
        """
        Welcome to the Geography Game! 🌏 
        
        built with ❤️ by Anthony Reo
        """, 
        font=("Helvetica", 16))
        welcome_label.pack(pady=10)

        start_button = Button(self, text="Start Playing", command=self.mode_selection_screen, font=("Helvetica", 14))
        start_button.pack(pady=20)

    def mode_selection_screen(self):
        self.clear_screen()

        select_game_mode_label = Label(self, text="Select Game Mode", font=("Helvetica", 16))
        select_game_mode_label.pack(pady=20)

        country_mode_button = Button(self, text="Mode 1: Guess the Country", command=self.play_guess_capitals, font=("Helvetica", 14))
        country_mode_button.pack(pady=10)

        capital_mode_button = Button(self, text="Mode 2: Guess the Capital", command=self.play_guess_countries, font=("Helvetica", 14))
        capital_mode_button.pack(pady=10)

    def play_guess_capitals(self):
        self.clear_screen()

        self.random_country = random.choice(list(self.countries_capitals))
        guess = Label(self, text = f"Enter the Capital City of {self.random_country}")
        guess.pack()

        self.answer_entry = Entry(self, font=("Helvetica", 14))
        self.answer_entry.pack(pady=10)
            
        submit_button = Button(self, text="Submit", command=self.check_anwser_capitals, font=("Helvetica", 14))
        submit_button.pack(pady=10)

        skip_button = Button(self, text="Skip", command=self.play_guess_capitals, font=("Helvetica", 14))
        skip_button.pack(pady=10)

    def check_anwser_capitals(self):
        user_answer = self.answer_entry.get().lower()
        if user_answer == self.countries_capitals[self.random_country].lower():
            self.right += 1
            right_label = Label(self, text = "Nice! That's right. :D")
            right_label.pack()
            country, capital = self.countries_capitals.popitem()
            
            next_button = Button(self, text="Next", command=self.play_guess_capitals, font=("Helvetica", 14))
            next_button.pack(pady=10)

        else:
            self.wrong += 1
            wrong_label = Label(self, text = "Sorry that wasn't it. :/")
            wrong_label.pack()

            next_button = Button(self, text="Next", command=self.play_guess_capitals, font=("Helvetica", 14))
            next_button.pack(pady=10)

    def play_guess_countries(self):
        self.clear_screen()

        self.random_capital = random.choice(list(self.capitals_countries))
        guess = Label(self, text = f"Enter the Country of {self.random_capital}")
        guess.pack()

        self.answer_entry = Entry(self, font=("Helvetica", 14))
        self.answer_entry.pack(pady=10)
            
        submit_button = Button(self, text="Submit", command=self.check_anwser_countries, font=("Helvetica", 14))
        submit_button.pack(pady=10)

        skip_button = Button(self, text="Skip", command=self.play_guess_countries, font=("Helvetica", 14))
        skip_button.pack(pady=10)

    def check_anwser_countries(self):
        user_answer = self.answer_entry.get().lower()
        if user_answer == self.capitals_countries[self.random_capital].lower():
            self.right += 1
            right_label = Label(self, text = "Nice! That's right. :D")
            right_label.pack()
            capital, country = self.capitals_countries.popitem()
            
            next_button = Button(self, text="Next", command=self.play_guess_countries, font=("Helvetica", 14))
            next_button.pack(pady=10)

        else:
            self.wrong += 1
            wrong_label = Label(self, text = "Sorry that wasn't it. :/")
            wrong_label.pack()

            next_button = Button(self, text="Next", command=self.play_guess_countries, font=("Helvetica", 14))
            next_button.pack(pady=10)
    
    def clear_screen(self):
        for widget in self.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = GeographyGame()
    app.mainloop()