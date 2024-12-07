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
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiNWQxZjc5ZGRjZjBlNWViZDU2YTllNDA3ZjNmYmE1ZjM1NjJhYTY5ZThmMzUxMjJlYTJiNzYzOWQ0Y2IwYjdhNzY3MDdjMjVlM2IzOGEwZjkiLCJpYXQiOjE3MzM1NTIxMzcuNTczMzE0LCJuYmYiOjE3MzM1NTIxMzcuNTczMzE2LCJleHAiOjE3MzQxNTY5MzcuNTY1MzA2LCJzdWIiOiIzNzIiLCJzY29wZXMiOlsiYWRtaW4iXX0.lLA6MUyrNODe85u58gT6-yjajK8d7duxB3A69CcbKgh2RZaVvHCXX8bciYlKyVCyHFdMoQIonWaZpeRTfgI9o-KOg0xjOPnj7XkS1ulNsYXh29oRupElh2IU5_CEy6IYvLCjwXlSeVol6iUKtiy8fMos6O8YGH4fVh8Z9j386zXEXPcQnyfP73YfFP02gDp-5onloZkYIcNt420jT6O5DoE7RXzLHAwGx_7NVfY1assKSjb-1h1JXv3E13g5uVRbaor4HZgZk4CWt1SNgWMw1RsWMViSa1MNu_BBb457IPpYT-xpTJvF7pYLYYX911GlNi9b81ZAnEPSVpkm-v6Xcds55jENtF8nEf2VUxlJqg7HZ-rRBGwpdaVbjQrJ7cZckj42g0bkNidAPijj21lyIbLrq3z5NYYgQwjLkFoOzdODw1bUxE8UKVMzRiVEe9Z49h1c6_EhnpjQYPDRA4y7wDVuZNzPnoTZvCHTwVIiYrOdqnSvLWcq3_0Styxk11_iNhFxs_SpBc6I_V6GbXUqn4vfLlYD19fsA1tXnXLSqA2AHBajL5Oz3QpBNQHZuQIx32P0lCjLVVoqY5wUks86XHPsM1tm3kqv03UQLOLdkPFqqvu_DtLWVPJso__oZGTRV-FtCngCPgrmi-UlaNxttbNJ7V_lviILq-3Y2PcDAlc",
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
