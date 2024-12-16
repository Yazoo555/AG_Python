import requests
from datetime import datetime, timedelta

# Endpoint URL
url_create_exam = "https://admin.ambition.guru/exams/subjective"

# Headers
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:133.0) Gecko/20100101 Firefox/133.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Referer": "https://admin.ambition.guru/",
    "Content-Type": "application/json",
    "X-Requested-With": "XMLHttpRequest",
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiMjlhM2MzZDI1Y2ZlMDBlYTQ3ZWM3MWQwOWY1ZDE2NWJjMTJlMTJhZDAwMWEzNjUyMjU2NGYxNjE5NTNmZmEzODkzOWYwZmU2MjUxOTExYTkiLCJpYXQiOjE3MzM3NTQxMDYuMDY3OTkyLCJuYmYiOjE3MzM3NTQxMDYuMDY3OTk0LCJleHAiOjE3MzQzNTg5MDYuMDU4NzgxLCJzdWIiOiI4MSIsInNjb3BlcyI6WyJhZG1pbiJdfQ.Zf0ykC8frnrPKaktS6TTPD7Aqerf4RHrOk-pepB5lbpgBqJZogkT_TQKfsXisNfgTQ7ADx78b3rHF34p7CDR_wDfqQlmOwQNa0Q1YuDyGDUkUzGqysSodTQ4fMmdNM4exW3kY_vOaBwEvaA32UicD8qKtcE0EuOpCQyemWO09h_RqP6B6ZjSbFHQCUM_Gu5LqQls9aXQAmIHEpaMkdQuqjPQu02lCVermTFoYB4INLLPZq-_XJV1bHn8m8o9jKRfx4jvLBscoYinxdcjbr2mxHH0Ysj7Hx-Dh105WI-EWT-QMo7fB1xky3FE8pBi8Uz1XKZ5zCiVndZaBTkcBxtXX5ItC8PmiYA0rSEjmTjkTEkQJQyWE8D1YaaMbCLOJdMQzAEUzjAGI0nQUkrGbwQhtJAG5qsw21JglFeK-WlktwiqmmdkjzT4Ih358uvdCgirZ_qnLu5hmT1ehxeOU28HcHy-eLjEKDzSouqT_Qq-3dKCErBsbNOyMAS2-Kv9GLGQ-kPZK5-4vR6GLa74-Mn2-v1ezGV82_bTEXOOH-xmUbfb1kixzWrbhLJhSsEFzdhdA7Sud3oHBzPvH0P7ac0sBz1_veFHe_egZTs_vjFrbW5J3e3fHRRdzhk6-yURS1OSlKl5Hgz2fCag4pTJeBNFV-zVIQNffHkgkV3mHjajviE",
}

# Current date and time for dynamic fields
current_datetime = datetime.now()

# Adjust times dynamically
start_time = (current_datetime + timedelta(minutes=5)).strftime("%Y-%m-%d %H:%M:%S")
registration_deadline = start_time
published_at = (current_datetime + timedelta(minutes=10)).strftime("%Y-%m-%d %H:%M:%S")

# Payload
data_create_exam = {
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
    "duration": "25",
    "negative_marking": "1",
    "start_time": start_time,
    "registration_deadline": registration_deadline,
    "questions": [
        {
            "body": "<p><strong>खण्ड - (क) कार्याल्य सञ्‍चालन र संगठनात्मक व्यवस्था</strong></p>",
            "id": 116745,
            "order": 1,
            "marks": 1,
            "extras": {
                "subject": {"id": 19893, "name": "Mental Agility Test (MAT)"},
                "unit": {"id": 20329, "name": "Feedback Session"}
            }
        },
        {
            "body": "<p><strong>निम्न प्रश्‍नको विवरण लेख्नुहोस्।</strong></p>",
            "id": 116419,
            "order": 2,
            "marks": 1,
            "extras": {
                "subject": {"id": 19893, "name": "Mental Agility Test (MAT)"},
                "unit": {"id": 20329, "name": "Feedback Session"}
            }
        },
        {
            "body": "<p><strong>स्रोतको हकको कारण:</strong></p>",
            "id": 116417,
            "order": 3,
            "marks": 1,
            "extras": {
                "subject": {"id": 19893, "name": "Mental Agility Test (MAT)"},
                "unit": {"id": 20329, "name": "Feedback Session"}
            }
        },
        # Add more questions as required
    ],
    "exam_reminders": [8],
    "rewards": [{"position": 1, "prize": 5000}],
    "is_routine": False,
    "criteria_fields": [],
    "auto_save_message": "<p>Mock test time is up. Your answer will be submitted automatically. All the best for your result.</p>",
    "self_submit_message": "<p>Thank you for submitting. Wishing you good results.</p>",
    "confirmation_message": "<p>Your mock test will be submitted. If needed, verify the answer. All the best for your results.</p>",
    "rules": (
        "<p>Student should attend the test solely.</p>"
        "<p>Students are suggested not to exit and resume the test.</p>"
        "<p>Students should attend the exam within the suggested time.</p>"
        "<p>Students should start and complete the exams from the same devices (i.e., user cannot change device).</p>"
        "<p>Students are suggested to have a stable internet connection.</p>"
    ),
    "terms_and_condition": (
        "<p>Students are not allowed to submit the answer through any source.</p>"
        "<p>If any unwanted activity is detected, then students can be disqualified for the exam...</p>"
        "<p>The AG team has to terminate the mock test if any suspicious activity is detected.</p>"
    ),
    "packages": [22],
    "showPackageform": False,
    "exam_threshold_id": 2,
    "title": "Subjective Mock Test",
    "sub_title": "Subjective Mock Test",
    "number_of_participant": "10",
    "points": "10",
    "number_of_questions": "10",
    "type": "Subjective",
    "description": "Subjective Mock Test",
    "participant_limit": "11",
    "published_at": published_at,
    "model_set_title": "Subjective Mock Test",
    "model_set_subtitle": "Subjective Mock Test",
    "pass_percentage": "10",
    "setup_through": 1,
    "exam_setup_id": None
}

# Make the API request to create the exam
response_create_exam = requests.post(url_create_exam, headers=headers, json=data_create_exam)

if response_create_exam.status_code == 201:
    exam_id = response_create_exam.json().get('data', {}).get('id')
    print("Subjective Mock Test Created Successfully. Exam ID:", exam_id)
    
    # Step 3: Open the exam URL in the browser
    exam_url = f"https://admin.ambition.guru/exams/mock-test-detail/{exam_id}?routeName=Subjective"
    print(f"Opening exam URL in browser: {exam_url}")
    webbrowser.open(exam_url)
    
    # Step 4: Lock the questions for the created exam
    url_lock_questions = f"https://admin.ambition.guru/api/v1/admin/exams/{exam_id}/lock-questions"
    response_lock_questions = requests.post(url_lock_questions, headers=headers)

    # Check if the locking was successful
    if response_lock_questions.status_code == 200:
        print(f"Questions locked successfully for Exam ID: {exam_id}")
    else:
        print(f"Failed to lock questions. Status Code: {response_lock_questions.status_code}")
        print("Response:", response_lock_questions.json())
else:
    print("Failed to create Subjective Mock Test. Status Code:", response_create_exam.status_code)
    print("Response:", response_create_exam.json())