import requests
from datetime import datetime, timedelta
import webbrowser


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
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiNzBiMjdkZDExYjYxMGU5NjQyNjAxYWU4N2M5YzUxNDM5NDA1OGYxZGExMWU5ZmY2MjU1OTk5ZTViZmY1OWQ3MDBlN2ExMWFkYTFiMzcwMDciLCJpYXQiOjE3MzI0Mzk5OTguODU4NzI4LCJuYmYiOjE3MzI0Mzk5OTguODU4NzMxLCJleHAiOjE3MzMwNDQ3OTguODUxOTU1LCJzdWIiOiIzNzIiLCJzY29wZXMiOlsiYWRtaW4iXX0.MIW1SXCmJHeg1bvc0jo2sk1rG_ifZ2ZedxNjk1yGj9XvvEmw9M0eXtPvyM6-xLy8SsgHs1JvwH-gpdYik2NShsU0hYbaPbXfdES-cOAtOsCwfYRTPy_U4BcOjidA0DltaHvQW-sH7gkKhWwpzJuYzpuJYFZIbfXEKPMy9u8PTXHc7Bcocde4Noy12LBmECJ8Dgyh02GhRTn4SfsV7jEViajJpFfafB3pqr3TMdD6WgFhb86-EzT6aicc_rx-hZ6Cu1uF_LLypesnOU60rSZruiJX8Gc5Z7B7L9tAZdCcOlAJJDt6vIhTRoBIi0hsO7uuCuLehuGR2ti08cSiOMtBEuCpm7SayukRstBy6cO1ByJapsgWXRMimhG1yGpZRcZUXmvp4uduCOF8K68SBPn11Mobw-i3Zdyo71vmTbK_LEkK2If2dIb2ch_LE659-wlS3L-F55S5p8Z75Ogh4neNQOHbeBWuIGZht5JxzY-jJcxZExKc7RQy2zBCUPaCMIGXIceOkERVN0HJ-6ytISZ45imt0fsYv07ybL7PnJY7k55c-rKv4ykhLH8iCu8RL0pd46m4C_LkMVqTZfDhebSBFH9WQlfrRnjlZPMn9ksSOQWTh7Dr-KDdsE7LKBTXdjp_9DdLiZ6x5UBfODOQYAukk382XpGSkcMtpwsbBJd3Zok",
    "Connection": "keep-alive",
    "Priority": "u=0"
}

# Get the current date and time and calculate dynamic fields
current_datetime = datetime.now()
registration_deadline = (current_datetime + timedelta(minutes=2)).strftime("%Y-%m-%d %H:%M:%S")
start_time = (current_datetime + timedelta(minutes=2)).strftime("%Y-%m-%d %H:%M:%S")  # 5 + 3 minutes
published_at = (current_datetime + timedelta(minutes=10)).strftime("%Y-%m-%d %H:%M:%S")  # 8 + 10 minutes
#user_title = f"Mock Test {current_datetime.strftime('%Y-%m-%d')}"

print("Mock Test is:: ",user_title),

# Prompt user for allowing answer changes
try:
    allow_answer_change = int(input("Allow answer change? Enter 1 for Yes, 0 for No (default is 1): "))
    if allow_answer_change not in [0, 1]:
        raise ValueError("Invalid input")
except (ValueError, TypeError):
    print("Invalid or no input. Defaulting to allow answer change.")
    allow_answer_change = 1



data_create_exam = {
    "guard_name": "admin-api",
    "join_in_middle": 1,
    "allow_answer_change": allow_answer_change,  # Dynamic allow answer change
    "send_notification": 0,
    "is_featured": 0,
    "is_criteria": 0,
    "is_active": 1,
    "status": 1,
    "is_free": 1,
    "price": 0,
    "exam_setup_type": 1,
    "marks": "50",
    "duration": "45",
    "negative_marking": "1",
    "start_time": start_time,
    "registration_deadline": registration_deadline,

    "questions": [
        {
            "body": "<p>Two wire loops of different radii are placed in a plane such that they are concentric. The current in outer loop is clockwise and increasing with time. The current in the inner loop is</p>",
            "id": 1820,
            "order": 1,
            "marks": 1
        },
        {
            "body": "<p>Whenever there is a change in magnetic flux linked with a circuit, an emf is induced which is proportional to the rate of change of magnetic flux linked with the circuit. This law is called :</p>",
            "id": 4541,
            "order": 2,
            "marks": 1
        },
        {
            "body": "<p>Faraday's law of electromagnetic induction states that induced emf in a circuit is :</p>",
            "id": 4548,
            "order": 3,
            "marks": 1
        },
        {
            "body": "<p>The direction of the induced current in a circuit is always such that it opposes the cause due to which it is produced. This law is named as :</p>",
            "id": 4551,
            "order": 4,
            "marks": 1
        },
        {
            "body": "<p>Lenz's law gives </p>",
            "id": 4553,
            "order": 5,
            "marks": 1
        },
        {
            "body": "<p>Lenz's law is a consequence of the law of conservation of</p>",
            "id": 4556,
            "order": 6,
            "marks": 1
        },
        {
            "body": "<p>When a magnet is removed with its N-pole towards a closed coil, the nearer end of the coil acts as :</p>",
            "id": 4559,
            "order": 7,
            "marks": 1
        },
        {
            "body": "<p>A magnet is moved towards a coil (A) quickly (B) slowly. Then the induced emf is :</p>",
            "id": 4564,
            "order": 8,
            "marks": 1
        },
        {
            "body": "<p>Whenever a magnet is moved either towards or away from a conducting coil, an emf is induced; the magnitude of which is independent of :</p>",
            "id": 4568,
            "order": 9,
            "marks": 1
        },
        {
            "body": "<p>The self inductance of a coil is a measure of :</p>",
            "id": 4571,
            "order": 10,
            "marks": 1
        },
        {
            "body": "<p>The unit of inductance is </p>",
            "id": 4572,
            "order": 11,
            "marks": 1
        },
        {
            "body": "<p>Two pure inductors each of self-inductance L are connected in series, the net inductance is :</p>",
            "id": 4575,
            "order": 12,
            "marks": 1
        },
        {
            "body": "<p>An inductor coil of inductance L is divided into two equal parts and both parts are connected in parallel. The net inductance is</p>",
            "id": 4584,
            "order": 13,
            "marks": 1
        },
        {
            "body": "<p>When a wire loop is rotated in a magnetic field, the direction of induced emf changes once in every :</p>",
            "id": 4588,
            "order": 14,
            "marks": 1
        },
        {
            "body": "<p>Self-inductance of a coil varies as :</p>",
            "id": 4592,
            "order": 15,
            "marks": 1
        },
        {
            "body": "<p>The self-inductance of a straight wire is :</p>",
            "id": 4599,
            "order": 16,
            "marks": 1
        },
        {
            "body": "<p>In a resistance box, the resistance coil is doubled on itself to avoid :</p>",
            "id": 4601,
            "order": 17,
            "marks": 1
        },
        {
            "body": "<p>Eddy currents are:</p>",
            "id": 4607,
            "order": 18,
            "marks": 1
        },
        {
            "body": "<p>Why the current does not rise immediately in a circuit containing inductance :</p>",
            "id": 4610,
            "order": 19,
            "marks": 1
        },
        {
            "body": "<p>To induce emf in a coil, the magnetic flux linking :</p>",
            "id": 4612,
            "order": 20,
            "marks": 1
        }
    ],


    "exam_reminders": [11],
    "rewards": [{"position": 1, "prize": 5000}],
    "is_routine": False,
    "criteria_fields": [],
    "auto_save_message": "<p>Mock test time is up. Your answer will be submitted automatically...</p>",
    "self_submit_message": "<p>Thank you for submitting. Wishing you good results.</p>",
    "confirmation_message": "<p>Your mock test will be submitted...</p>",
    "rules": "<p>Student should attend the test solely</p>...",
    "terms_and_condition": "<p>Students are not allowed to submit...</p>",
    "packages": [22],
    "showPackageform": False,
    "exam_threshold_id": 2,
#"title": "Mock Test ",
  #  "sub_title": "Mock Test Testing",
    "number_of_participant": "50",
    "points": "100",
    "number_of_questions": "25",
    "description": "Mock Test Testing",
    "published_at": published_at,
    "participant_limit": "20",
    "pass_percentage": "25",
   # "model_set_title": "Mock Test Testing",S
#    "model_set_subtitle": "Mock Test Testing",
    "setup_through": 1,
    "exam_setup_id": None,
      
    # Set user-provided title dynamically in multiple fields
    "title": user_title,
    "sub_title": user_title,
    "model_set_title": user_title,
    "model_set_subtitle": user_title,
}

# Send the request to create the exam
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
