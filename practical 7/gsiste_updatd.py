import gspread
import random
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import time
# Define the scope and authenticate with Google
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('ruchika.json', scope)
client = gspread.authorize(creds)

# Open the Google Spreadsheet by title or by key
spreadsheet = client.open("ruchika")  # or use .open_by_key("your_spreadsheet_key")

# Select the sheet to work with (e.g., the first sheet)
sheet = spreadsheet.sheet1

#Upload some data (example: adding rows to the sheet)

data = [
    ["Sensor", "Value", "Unit"],
    ["Air temp", "23.5", "C"],
    ["Smoke", "400","ppm"],
    ["humdity", "48", "%"],
    ["Burner Temp","387","C"],
    ["LPG Cylinder Pressure", "227","psi"]
]

# Update the sheet with the data
for row in data:
    sheet.append_row(row)

print("Data uploaded successfully!")



 
