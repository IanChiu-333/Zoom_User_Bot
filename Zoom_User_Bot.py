#Features to add
#1. Indian and Chinese names
#2. Photo detection instead of manual wait and hard coded wait times
#3. Make into app/program
#4. Some with only first names

import pyautogui
import keyboard
import webbrowser
import time
import random
random_times = [0.5, 0.6, 0.7, 0.8, 0.9]

for i in range(5):
    #Opens zoom in new tab
    webbrowser.open_new_tab("https://app.zoom.us/wc")

    #Joins Zoom Room
    pyautogui.moveTo(1300, 800, duration=random.choice(random_times))
    pyautogui.click()
    #Replace with meeting ID number
    pyautogui.write("766 719 8474")
    pyautogui.moveTo(1600, 800, duration=random.choice(random_times))
    pyautogui.click()

    #Load Buffer
    time.sleep(2)

    #Writes name and signs on
    pyautogui.moveTo(1800, 700, duration=random.choice(random_times))
    pyautogui.click()
    first_names = [
        "Emma", "Olivia", "Ava", "Isabella", "Sophia", "Charlotte", "Mia", "Amelia", "Harper", "Evelyn",
        "Abigail", "Emily", "Ella", "Elizabeth", "Camila", "Luna", "Sofia", "Avery", "Mila", "Aria",
        "Scarlett", "Penelope", "Layla", "Chloe", "Victoria", "Madison", "Eleanor", "Grace", "Nora", "Riley",
        "Zoey", "Hannah", "Hazel", "Lily", "Ellie", "Violet", "Lillian", "Zoe", "Stella", "Aurora",
        "Natalie", "Emilia", "Everly", "Leah", "Aubrey", "Willow", "Addison", "Lucy", "Audrey", "Bella",
        "Nova", "Brooklyn", "Paisley", "Savannah", "Claire", "Skylar", "Isla", "Genesis", "Naomi", "Elena",
        "Caroline", "Eliana", "Anna", "Maya", "Valentina", "Ruby", "Kennedy", "Ivy", "Ariana", "Aaliyah",
        "Cora", "Madelyn", "Alice", "Kinsley", "Hailey", "Gabriella", "Allison", "Gianna", "Serenity", "Samantha",
        "Sarah", "Autumn", "Quinn", "Eva", "Piper", "Sophie", "Sadie", "Delilah", "Josephine", "Nevaeh",
        "Adeline", "Arya", "Emery", "Lydia", "Clara", "Vivian", "Madeline", "Peyton", "Julia", "Rylee"
    ]
    last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor",
                "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin", "Thompson", "Garcia", "Martinez", "Robinson", 
                "Clark", "Rodriguez", "Lewis", "Lee", "Walker", "Hall", "Allen", "Young", "Hernandez", "King", "Wright", "Lopez", 
                "Hill", "Scott", "Green", "Adams", "Baker", "Gonzalez", "Nelson", "Carter", "Mitchell", "Perez", "Roberts", 
                "Turner", "Phillips", "Campbell", "Parker", "Evans", "Edwards", "Collins", "Stewart", "Sanchez", "Morris", "Rogers", 
                "Reed", "Cook", "Morgan", "Bell", "Murphy", "Bailey", "Rivera", "Cooper", "Richardson", "Cox", "Howard", "Ward", "Torres", 
                "Peterson", "Gray", "Ramirez", "James", "Watson", "Brooks", "Kelly", "Sanders", "Price", "Bennett", "Wood", "Barnes", "Ross", 
                "Henderson", "Coleman", "Jenkins", "Perry", "Powell", "Long", "Patterson", "Hughes", "Flores", "Washington", "Butler", "Simmons", 
                "Foster", "Gonzales", "Bryant", "Alexander", "Russell", "Griffin", "Diaz"
    ]
    name = random.choice(first_names) + " " + random.choice(last_names)
    pyautogui.write(name)
    time.sleep(random.choice(random_times))
    pyautogui.press('enter')

    #Load Buffer
    time.sleep(5)

    #Joins Audio
    pyautogui.moveTo(1350, 1000, duration=random.choice(random_times))
    pyautogui.click()
    
