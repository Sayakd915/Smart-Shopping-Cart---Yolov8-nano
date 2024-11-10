import sqlite3
from ultralytics import YOLO
from datetime import datetime

conn = sqlite3.connect('detected_items.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        item_name TEXT,
        confidence REAL,
        detection_time TEXT
    )
''')
conn.commit()

model = YOLO('C:/Users/SAYAK DAS/OneDrive/Desktop/Metrics/best.pt')

results = model('C:/Users/SAYAK DAS/OneDrive/Desktop/Metrics/test_image.jpg')

for result in results[0].boxes.data.tolist():
    item_name = results[0].names[int(result[5])]  
    confidence = result[4]  
    detection_time = datetime.now().isoformat() 

    cursor.execute('''
        INSERT INTO items (item_name, confidence, detection_time)
        VALUES (?, ?, ?)
    ''', (item_name, confidence, detection_time))

conn.commit()

conn = sqlite3.connect('detected_items.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM items")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
