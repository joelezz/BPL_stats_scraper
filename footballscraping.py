import tkinter as tk
from bs4 import BeautifulSoup
import requests
from pymongo import MongoClient

# Tkinter GUI setup
window = tk.Tk()
# Add your GUI components (labels, buttons, etc.) here

# MongoDB connection setup
client = MongoClient("mongodb+srv://joel:Tammikuu15@cluster0.nmrkwcu.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = client["FOOTBALL_REFEREE_STATS"]
collection = db["RED_CARDS_2022-23"]

# Function for web scraping and updating GUI
def scrape_data():
    url = "https://fbref.com/en/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Parsing logic for data involving goalscorers
    goalscorer_data = []
    table = soup.find("table", class_="stats_table")
    rows = table.find_all("tr")
    for row in rows:
        cells = row.find_all("td")
        if cells:
            player_cell = cells[0]
            player_name = player_cell.find("a").text.strip()
            team_element = player_cell.find("span", class_="fi-s")
            team = team_element.text.strip() if team_element else ""
            matches = int(cells[1].text.strip())
            goals = int(cells[2].text.strip())
            avg_goals_per_match = round(goals / matches, 2) if matches > 0 else 0.0
            goalscorer_data.append({"player": player_name, "team": team, "matches": matches, "goals": goals, "avg_goals_per_match": avg_goals_per_match})

    
    # Store the data in MongoDB
    collection.insert_many(goalscorer_data)
    
    # Update the GUI with the scraped data
    display_goalscorer_data(goalscorer_data)

# Function to display goalscorer data in the GUI
def display_goalscorer_data(data):
    # Clear previous data in the GUI
    for widget in window.winfo_children():
        widget.pack_forget()

    # Display the goalscorer data in a table or labels
    # Customize this based on your GUI design
    for i, entry in enumerate(data):
        player_label = tk.Label(window, text=entry['player'])
        player_label.grid(row=i, column=0)

        goal_label = tk.Label(window, text=entry['goals'])
        goal_label.grid(row=i, column=1)

        avg_goals_label = tk.Label(window, text=entry['avg_goals_per_match'])
        avg_goals_label.grid(row=i, column=2)



# Button event handler
def button_clicked():
    scrape_data()

# Bind the event handler to the button
button = tk.Button(window, text="Scrape Data", command=button_clicked)
# Add the button to the GUI
button.pack()

# Run the Tkinter event loop
window.mainloop()
