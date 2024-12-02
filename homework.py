import requests
from datetime import datetime, timedelta
import webbrowser



# API URL for creating homework
url_create_homework = "https://api-adm.ambition.guru/api/v1/admin/exams"

# User input for homework title
user_title = input("Please enter the title for the Homework: ")


# Dynamic timestamps for the homework
current_datetime = datetime.now()
start_time = (current_datetime).strftime("%Y-%m-%d %H:%M:%S")
end_time = (current_datetime + timedelta(days=2)).strftime("%Y-%m-%d %H:%M:%S")

# Headers for API request
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:132.0) Gecko/20100101 Firefox/132.0",
    "Accept": "application/json, text/plain, */*",
    "Content-Type": "application/json",
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiYmUyYmRkMGQ2NDZlNmVmMzczYTBhOTU2NDIzMzk4ZWQ1M2Q3YmNlM2E3YTMyNDhiMTlkYWNkMDg1Y2ZjZWQzZTk5NWM2NzdiYjEyNjVlZTEiLCJpYXQiOjE3MzI5NDQwMjAuNDQxOTk0LCJuYmYiOjE3MzI5NDQwMjAuNDQxOTk3LCJleHAiOjE3MzM1NDg4MjAuNDM0OSwic3ViIjoiMzcyIiwic2NvcGVzIjpbImFkbWluIl19.MPIA2fBwHbByQydPL4kocTemdmR96Tmi8TXCR6h8dSRaDLU1ztksMN1vSft2xvxDCvvP6x4O7dfsqZe9VRzQZjHBMZ0nOVU6tIpd7bDVEx56ZXnyWpHk13Uq1I8cmIZ9UHnB382SA8kTQZmA5bMZ7nCh9tqxVa34utTYKqpz6b9rSVY9EHC_1xCGdxvNTzdmBrryO0LZ3mMHNFq9Iwi3UC7xcJNksMQ61CkwCpZ620eMZmqG9SusNOunBd3Wigxd3spl8vm6cVAieANOoqK2xL4GieoF4es9bkEZoJFcenVQoBCs6o9tDkYPZ6z4REZ18ovNOu4ki22gjdhotHl4JGHHps8yjhDmunHpTDIyTrD_3-HEm0YMCIhhJgo7Z9ZtZzQu-rVGWgfbUr2vXB-XrgcSwP91IAqEFpWKTu38Wl-FzXO4ZGyaOKGt86-8rtHUETk_gyRunRg_RQmhmXYEZ4qJEqtNlFO-Xwh-se5m1UA8pVHZxz6Krc22lSSWvXMC5fKtNh5IbRVCF8xwkmdkpSFHoB7el53Fj03Ij1cqAgEBzXe31ccYX49_F0entdVgEimyhtIhX6yAqEL7VXLh1tofudj90RNWnLtOyCLhJrii-t4NbfysAv-W_tONlDJuOh7HJ1dSwdKK8dR76bpoitMVWU_ifYvrfDdBgd8KtJc",
    "Connection": "keep-alive"
}

# Data for creating the homework
data_create_homework = {
    "guard_name": "admin-api",
    "join_in_middle": 1,
    "send_notification": 0,
    "is_featured": 0,
    "is_criteria": 0,
    "is_active": 1,
    "status": 0,
    "is_free": 1,
    "price": 0,
    "exam_setup_type": 1,
    "marks": 10,
   # "duration": 10,
    "negative_marking": 0,
    "start_time": start_time,
    "end_time": end_time,
     "questions": [
    {
        "body": "<p>अध्यापन अनुमति पत्रको अवधारणा प्रस्तुत गर्दै यसको आवश्यकता दर्साउनुहोस्। साथै नेपालमा अध्यापन अनुमति पत्रको सम्बन्धमा देखिएका समस्याहरू उल्लेख गर्नुहोस् । (२+४+४)</p>",
        "id": 115905,
        "order": 1,
        "marks": 1
    },
    {
        "body": "<p>शिक्षक भर्ना भनेको के हो ? नेपालमा शिक्षक भर्ना छनौट तथा नियुक्तिमा देखिएका समस्याहरू लेख्नुहोस् । (१+४)</p>",
        "id": 115904,
        "order": 2,
        "marks": 1
    },
    {
        "body": "<p>शिक्षक बढुवा भनेको के हो ? यसका उद्देश्यहरू उल्लेख गर्नुहोस् । (२+३)</p>",
        "id": 115903,
        "order": 3,
        "marks": 1
    },
    {
        "body": "<p>नेपालमा शिक्षकको पेसागत विकासको सम्बन्धमा भएका नीतिगत, संरचनागत एवम् कार्यक्रमगत प्रावधानहरूको चर्चा गर्नुहोस् ।</p>",
        "id": 115902,
        "order": 4,
        "marks": 1
    },
    {
        "body": "<p>शिक्षकको गुणस्तर एवम् प्रभावकारिताको बारेमा छोटकरीमा चर्चा गर्नुहोस् ।(२.५+२.५)</p>",
        "id": 115901,
        "order": 5,
        "marks": 1
    }
],
    "exam_reminders": [],
    "rewards": [{"position": 1, "prize": 5000}],
    "is_routine": False,
    "packages": [22],
    "showPackageform": False,
    "exam_threshold_id": 2,
    "title": user_title,
    "sub_title": user_title,
    "number_of_participant": "25",
    "points": "100",
    "number_of_questions": "15",
    "type": "HOMEWORK",
    "tags": [user_title],
    "pass_percentage": "10",
    "setup_through": 1,
    "exam_setup_id": None
}

# Send POST request to create homework
response_create_homework = requests.post(url_create_homework, headers=headers, json=data_create_homework)

if response_create_homework.status_code == 201:
    response_data = response_create_homework.json()
    homework_id = response_data.get("data", {}).get("id")
    print("Homework created successfully!")
    print(f"Homework ID: {homework_id}")
    print(f"Homework Title: {user_title}")
    
    # Construct the URL to open the homework
    homework_url = f"https://admin.ambition.guru/exams/mock-test-detail/{homework_id}?routeName=Exams"
    print(f"Opening homework in browser: {homework_url}")
    
    # Open the URL in the default browser
    webbrowser.open(homework_url)
else:
    print("Failed to create homework.")
    print("Status Code:", response_create_homework.status_code)
    print("Response:", response_create_homework.text)
