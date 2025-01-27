import requests
from datetime import datetime, timedelta
import webbrowser

from auth import get_auth_token

url_create_exam = "https://api-adm.ambition.guru/api/v1/admin/exams"
user_title = input("Please enter the title for the exam: ")

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:132.0) Gecko/20100101 Firefox/132.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Content-Type": "application/json",
    "Referer": "https://admin.ambition.guru/",
    "X-Requested-With": "XMLHttpRequest",
    "Origin": "https://admin.ambition.guru",
    "Authorization": f"Bearer {get_auth_token()}",
    "Connection": "keep-alive",
    "Priority": "u=0"
}

# Get the current date and time and calculate dynamic fields
current_datetime = datetime.now()

# Calculate registration deadline
registration_deadline = (current_datetime + timedelta(minutes=2)).strftime("%Y-%m-%d %H:%M:%S")


# Calculate start time
start_time = (current_datetime + timedelta(minutes=2)).strftime("%Y-%m-%d %H:%M:%S")  # 5 + 3 minutes

# Get duration input from user
try:
    duration = int(input("Enter the duration of the exam in minutes (default is 45): "))
except ValueError:
    print("Invalid or no input. Defaulting to 45 minutes.")
    duration = 45

# Calculate published_at time
published_at = (current_datetime + timedelta(minutes=2 + duration)).strftime("%Y-%m-%d %H:%M:%S")

# Prompt user for allowing answer changes
try:
    allow_answer_change = int(input("Allow answer change? Enter 1 for Yes, 0 for No (default is 1): "))
    if allow_answer_change not in [0, 1]:
        raise ValueError("Invalid input")
except (ValueError, TypeError):
    print("Invalid or no input. Defaulting to allow answer change.")
    allow_answer_change = 1

data_create_exam =  {
  "guard_name": "admin-api",
  "join_in_middle": 1,
  "allow_answer_change": 1,
  "send_notification": 0,
  "is_featured": 0,
  "is_criteria": 0,
  "is_active": 1,
  "status": 1,
  "is_free": 1,
  "price": 0,
  "exam_setup_type": 1,
  "marks": 10,
  "duration": "5",
  "negative_marking": "0.25",
  "start_time": start_time,  # Use the calculated start_time
  "registration_deadline": registration_deadline,
  "questions": [
    {
      "body": "<p>Two wire loops of different radii are placed in a plane such that they are concentric. The current in outer loop is clockwise and increasing with time. The current in the inner loop is</p>",
      "id": 1820,
      "order": 1,
      "marks": 1,
      "extras": {
        "subject": { "id": 2392, "name": "Physics" },
        "unit": { "id": 2434, "name": "Magnetism" }
      }
    },
    {
      "body": "<p>Whenever there is a change in magnetic flux linked with a circuit, an emf is induced which is proportional to the rate of change of magnetic flux linked with the circuit. This law is called :</p>",
      "id": 4541,
      "order": 2,
      "marks": 1,
      "extras": {
        "subject": { "id": 2392, "name": "Physics" },
        "unit": { "id": 2434, "name": "Magnetism" }
      }
    },
    {
      "body": "<p>Faraday's law of electromagnetic induction states that induced emf in a circuit is :</p>",
      "id": 4548,
      "order": 3,
      "marks": 1,
      "extras": {
        "subject": { "id": 2392, "name": "Physics" },
        "unit": { "id": 2434, "name": "Magnetism" }
      }
    },
    {
      "body": "<p>The direction of the induced current in a circuit is always such that it opposes the cause due to which it is produced. This law is named as :</p>",
      "id": 4551,
      "order": 4,
      "marks": 1,
      "extras": {
        "subject": { "id": 2392, "name": "Physics" },
        "unit": { "id": 2434, "name": "Magnetism" }
      }
    },
    {
      "body": "<p>Lenz's law gives </p>",
      "id": 4553,
      "order": 5,
      "marks": 1,
      "extras": {
        "subject": { "id": 2392, "name": "Physics" },
        "unit": { "id": 2434, "name": "Magnetism" }
      }
    },
    {
      "body": "<p>Lenz's law is a consequence of the law of conservation of</p>",
      "id": 4556,
      "order": 6,
      "marks": 1,
      "extras": {
        "subject": { "id": 2392, "name": "Physics" },
        "unit": { "id": 2434, "name": "Magnetism" }
      }
    },
    {
      "body": "<p>When a magnet is removed with its N-pole towards a closed coil, the nearer end of the coil acts as :</p>",
      "id": 4559,
      "order": 7,
      "marks": 1,
      "extras": {
        "subject": { "id": 2392, "name": "Physics" },
        "unit": { "id": 2434, "name": "Magnetism" }
      }
    },
    {
      "body": "<p>A magnet is moved towards a coil (A) quickly (B) slowly. Then the induced emf is :</p>",
      "id": 4564,
      "order": 8,
      "marks": 1,
      "extras": {
        "subject": { "id": 2392, "name": "Physics" },
        "unit": { "id": 2434, "name": "Magnetism" }
      }
    },
    {
      "body": "<p>Whenever a magnet is moved either towards or away from a conducting coil, an emf is induced; the magnitude of which is independent of :</p>",
      "id": 4568,
      "order": 9,
      "marks": 1,
      "extras": {
        "subject": { "id": 2392, "name": "Physics" },
        "unit": { "id": 2434, "name": "Magnetism" }
      }
    },
    {
      "body": "<p>The self inductance of a coil is measure of :</p>",
      "id": 4571,
      "order": 10,
      "marks": 1,
      "extras": {
        "subject": { "id": 2392, "name": "Physics" },
        "unit": { "id": 2434, "name": "Magnetism" }
      }
    }
  ],
  "exam_reminders": [3],
  "rewards": [
    { "position": 1, "prize": 5000 }
  ],
  "is_routine": False,
  "criteria_fields": [],
  "auto_save_message": "<p>Mock test time is up. Your answer will be submitted automatically. All the best for your result.</p>",
  "self_submit_message": "<p>Thank you for submitting. Wishing you good results.</p>",
  "confirmation_message": "<p>Your mock test will be submitted. If needed, verify the answer. All the best for your results.</p>",
  "rules": "<p>Student should attend the test solely</p><p>Students are suggested not to exit and resume the test.</p>",
  "terms_and_condition": "<p>Students are not allowed to submit the answer through any source.</p><p>If any unwanted activity is detected, students can be disqualified for the exam...</p>",
  "packages": [22],
  "showPackageform": False,
  "exam_threshold_id": 2,
    "title": user_title,
    "sub_title": user_title,
  "number_of_participant": "12",
  "points": "12",
  "number_of_questions": "10",
  "description": "Mocktest 23456",
  "published_at": published_at,
  "pass_percentage": "12",
    "model_set_title": user_title,
    "model_set_subtitle": user_title,
        "setup_through": 1,
  "exam_setup_id": None,
  "participant_limit": "10"
}


# Debug payload
print("Payload:", data_create_exam)
response_create_exam = requests.post(url_create_exam, headers=headers, json=data_create_exam)

if response_create_exam.status_code == 201:
    exam_id = response_create_exam.json().get('data', {}).get('id')
    print("Exam Created Successfully. Exam ID:", exam_id)

    # Construct the URL to open
    exam_url = f"https://admin.ambition.guru/exams/mock-test-detail/{exam_id}?routeName=Exams"

    # Open the URL in Firefox
    print(f"Opening exam URL: {exam_url}")
    webbrowser.get("firefox").open(exam_url)

    # Lock the questions for the created exam
    url_lock_questions = f"https://api-adm.ambition.guru/api/v1/admin/exams/{exam_id}/lock-questions"
    response_lock_questions = requests.post(url_lock_questions, headers=headers)

    # Check if the locking was successful
    if response_lock_questions.status_code == 200:
        print(f"Questions locked successfully for Exam ID: {exam_id}")
    else:
        print("Failed to lock questions. Status Code:", response_lock_questions.status_code)
else:
    print("Failed to create exam. Status Code:", response_create_exam.status_code)
    print("Response:", response_create_exam.json())