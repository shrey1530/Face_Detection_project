import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("./serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://face-detection-153015-default-rtdb.asia-southeast1.firebasedatabase.app/"
})



ref = db.reference('Face')

data = {
    "153015":
        {
            "name": "Shreya Chatterjee",
            "Age": 21,
            "Gender": "Female",
            "Identification_Mark": "Mole under Left eye",
            "last_attendance_time": "2023-11-11 00:54:34"
        },
    "153215":
        {
            "name": "Suman Kumari",
            "Age": 22,
            "Gender": "Female",
            "Identification_Mark": "Nothing",
            "last_attendance_time": "2023-12-12 00:54:34"
        },
    "153615":
        {
            "name": "Gunjan Chaudhury",
            "Age": 21,
            "Gender": "Female",
            "Identification_Mark":"Curly Hair",
            "last_attendance_time": "2024-01-11 00:54:34"
        },
        "153715":
        {
            "name": "Farheen Ahmed",
            "Age": 21,
            "Gender": "Female",
            "Identification_Mark":"Nothing",
            "last_attendance_time": "2024-01-11 00:54:34"
        }

}

for key, value in data.items():
    ref.child(key).set(value)