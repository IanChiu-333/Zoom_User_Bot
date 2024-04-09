#Packages Required:
#pyautogui
#pillow
#opencv_python

#Features to add
#1. Indian and Chinese names - DONE
#2. Photo detection instead of manual wait and hard coded wait times - DONE
#3. Make into app/program
#4. Some with only first names - DONE

import pyautogui
import keyboard
import webbrowser
import time
import random
random_times = [0.5, 0.6, 0.7, 0.8, 0.9]

#Names Database
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

chinese_names = [
    "Zhang Wei", "Wang Wei", "Wang Fang", "Li Wei", "Wang Xiuying", "Li Xiuying", "Wang Di", "Wang Jing", "Wang Li", "Zhang Xiuying",
    "Li Qiang", "Zhang Jing", "Zhang Min", "Li Min", "Wang Min", "Wang Lei", "Wang Jun", "Zhang Li", "Wang Yong", "Li Jing",
    "Zhang Lei", "Zhang Yong", "Wang Ping", "Wang Gang", "Li Fang", "Li Jun", "Wang Jie", "Zhang Jie", "Li Na", "Li Jie",
    "Zhang Tao", "Wang Tao", "Wang Na", "Li Xia", "Zhang Na", "Wang Yang", "Wang Yu", "Zhang Peng", "Li Mei", "Zhang Min",
    "Wang Peng", "Li Qing", "Zhang Qiang", "Zhang Yan", "Wang Yan", "Wang Hao", "Zhang Jun", "Wang Dan", "Li Tao", "Wang Chao",
    "Li Gang", "Zhang Juan", "Li Li", "Li Yong", "Wang Yong", "Wang Guiying", "Zhang Yan", "Wang Ling", "Zhang Ling", "Wang Min",
    "Li Yan", "Zhang Min", "Wang Yu", "Zhang Yong", "Li Guiying", "Zhang Li", "Wang Qiang", "Zhang Qiang", "Wang Guiying", "Zhang Guiying",
    "Li Juan", "Wang Xia", "Zhang Xia", "Wang Gang", "Li Gang", "Wang Lili", "Zhang Dan", "Li Yu", "Wang Yuhua", "Wang Peng",
    "Li Gang", "Zhang Gang", "Wang Dandan", "Zhang Jie", "Li Yang", "Wang Yang", "Wang Tao", "Zhang Tao", "Li Ming", "Wang Ming",
    "Zhang Ming", "Wang Yu", "Li Guiying", "Zhang Qiang", "Wang Guiying", "Li Juan", "Zhang Xia", "Wang Xia", "Li Gang", "Wang Gang",
    "Wang Lili", "Zhang Dan", "Li Yu", "Wang Yuhua", "Wang Peng", "Li Gang", "Zhang Gang", "Wang Dandan", "Zhang Jie", "Li Yang",
]

indian_first_names = [
    "Aarav", "Aaradhya", "Aryan", "Anaya", "Advait", "Ishaan", "Vihaan", "Aahana", "Aisha", "Arjun",
    "Rohan", "Riya", "Aryan", "Arya", "Kabir", "Anika", "Rehan", "Aaliyah", "Ishan", "Vivaan",
    "Saanvi", "Zoya", "Shivansh", "Avni", "Krishna", "Aahil", "Ananya", "Shreyansh", "Ahaan", "Anvi",
    "Aryaan", "Myra", "Arnav", "Kiara", "Atharva", "Rudra", "Aadhya", "Kiaan", "Ritvik", "Anika",
    "Sia", "Ayush", "Saanvi", "Yuvan", "Amaira", "Riaan", "Rudransh", "Kavya", "Veer", "Avyukt",
    "Nitya", "Abeer", "Aadhira", "Ayaan", "Mahi", "Prisha", "Samaira", "Samarth", "Tanishka", "Aayan",
    "Anvi", "Parth", "Zain", "Anvi", "Pranav", "Aarnav", "Aaditya", "Arisha", "Aarush", "Sarah",
    "Arhaan", "Vedansh", "Veer", "Anaya", "Yashvi", "Ira", "Aayan", "Aanya", "Hridhaan", "Anvi",
    "Anvika", "Advika", "Advik", "Kian", "Aayansh", "Aditi", "Arhan", "Anvay", "Anaisha", "Ahana",
    "Saisha", "Shaurya", "Arnav", "Rishika", "Aryav", "Anya", "Sarthak", "Vedika", "Avani", "Anvisha",
    "Kavya", "Amaan"
]

indian_last_names = [
    "Patel", "Singh", "Kumar", "Jain", "Mehta", "Sharma", "Gupta", "Trivedi", "Desai",
    "Mehta", "Chopra", "Patil", "Reddy", "Soni", "Verma", "Mittal", "Shah", "Bhatt",
    "Malhotra", "Yadav", "Joshi"
]

#Change to run more times
for i in range(15):
    #Opens zoom in new tab
    webbrowser.open_new_tab("https://app.zoom.us/wc")

    #Finds Join Meeting button
    time.sleep(1) #Needed, for some reason the prediction isn't so good without waiting
    loc_Join_Meeting = pyautogui.locateOnScreen("Zoom_Join_Meeting.png", grayscale=True, confidence=.8)

    #Joins Zoom Room
    pyautogui.moveTo(loc_Join_Meeting, duration=random.choice(random_times))
    pyautogui.click()

    #Replace with meeting ID number
    pyautogui.write("766 719 8474")

    #Moves past ID screen
    loc_Join_Meeting_2 = pyautogui.locateOnScreen("Zoom_Join_Meeting2.png", grayscale=True, confidence=.8)
    pyautogui.moveTo(loc_Join_Meeting_2, duration=random.choice(random_times))
    pyautogui.click()

    #Load Buffer
    time.sleep(3)

    #Writes name and signs on
    loc_name_input = pyautogui.locateOnScreen("Name_Input.png", grayscale=True, confidence=.8)
    pyautogui.moveTo(loc_name_input, duration=random.choice(random_times))
    pyautogui.click()

    name_num = random.randint(1, 5)
    if name_num == 1:
        name = random.choice(first_names) + " " + random.choice(last_names)
    elif name_num == 2:
        name = random.choice(indian_first_names) + " " + random.choice(indian_last_names)
    elif name_num == 3:
        name = random.choice(chinese_names)
    else:
        name = random.choice(first_names)
    
    pyautogui.write(name)
    time.sleep(random.choice(random_times))
    pyautogui.press('enter')

    #Load Buffer
    time.sleep(5)

    #Joins Audio
    loc_join_audio = pyautogui.locateOnScreen("Join_Audio.png", grayscale=True, confidence=.8)
    pyautogui.moveTo(loc_join_audio, duration=random.choice(random_times))
    pyautogui.click()
    
