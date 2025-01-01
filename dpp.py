import requests
from datetime import datetime, timedelta
import webbrowser

# Endpoint URL
url_create_exam = "https://api-adm.ambition.guru/api/v1/admin/exams"
user_title = input("Please enter the title for the exam: ")

# Headers
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:133.0) Gecko/20100101 Firefox/133.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Content-Type": "application/json",
    "Referer": "https://admin.ambition.guru/",
    "X-Requested-With": "XMLHttpRequest",
    "Origin": "https://admin.ambition.guru",
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiNmVkNmVhNDFkODFmY2JkM2UzYTQ0OWI3ZWY0YjQ0ZGQ3MjIzYzllZTRlNTkxNWZiZTJmYTVjZmVjNGFlYjA3MzVhYjQ4ZmNlYjY3ZjY0Y2QiLCJpYXQiOjE3MzUxMDc2OTguMjY1NjM4LCJuYmYiOjE3MzUxMDc2OTguMjY1NjQxLCJleHAiOjE3MzU3MTI0OTguMjU3NTA1LCJzdWIiOiI4MSIsInNjb3BlcyI6WyJhZG1pbiJdfQ.r4PnLM_v18EbmLG0SKmiF7DEhT4O2-DXMF089Ee7Ub-qP2Pr80-KJ_PCUEqG3jKE67JhxZ96vvt7g04bX6u2cyU1nts_vM5yWvM_A20e3mmeM7066xvh9FmkXfLxPxgpcMd0mrJn2YLp-0_rZ8KZQXQXcE1Nqzi0vX2Own2QpD_yHxk9ILW-757NLVYiXI32oi3enoYjjfDlKJxZfC2q-5W7p8qNtC-BHy-V6VvqUhIF0u3v0FEEH4npUD0P80ixg0dgnSFIUxcgI_wdhkHrrp4wMHHnwCKQ8DOOpVp13wo0_EREWTVYL6kkgqjFsjUkKmcfVpmiY7HyGxb1bTp5VxX676_vS0gs9BsJJ8v9f1AxxB44X1ZnPdeWNRESHM_qJ0OeH_EoryfZCvecHJ2Ul2BDjMdw9kVJ0dnjj5LeuXO9oSv5OrZywulL5VWsL4UeIAYZXxZoMenCY7PzgucZsFCEyS0cptJmROIddz0oUsiosLn23XE-eeTL3SXbaspF1pyhRdQYH3Kza6aKEG7b0MogAXNFYPTmn7mB4LibIm0zEtul1P3geXS1geF57cmOwuG4VDvNY6a0n0QWNNeSwCvWta7jA7zugy_QFkLcqGpmZPbGZoin7k_8Aiq4aS7HTlLLnrNptiVajV5TvrgFasiGiiw02RCI-h1GenPCb0Q",
}

# Current date and time for dynamic fields
current_datetime = datetime.now()

# Adjust times dynamically
start_time = (current_datetime + timedelta(minutes=2)).strftime("%Y-%m-%d %H:%M:%S")
registration_deadline = start_time
published_at = (current_datetime + timedelta(minutes=5)).strftime("%Y-%m-%d %H:%M:%S")

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
    "is_free": 0,
    "price": 0,
    "exam_setup_type": 1,
    "marks": 10,
    "duration": "15",
    "negative_marking": "1",
    "start_time": start_time,
    "registration_deadline": registration_deadline,
    "questions": [
        {
            "body": "<p>Who saw the cell under a microscope for the first time?</p>",
            "id": 49832,
            "order": 1,
            "marks": 1,
            "extras": {
                "subject": {"id": 1008, "name": "Botany (Advanced BC)"},
                "unit": {"id": 1842, "name": "Cell Biology"}
            }
        },
        {
            "body": "<p>Who coined the term 'cell'?</p>",
            "id": 49833,
            "order": 2,
            "marks": 1,
            "extras": {
                "subject": {"id": 1008, "name": "Botany (Advanced BC)"},
                "unit": {"id": 1842, "name": "Cell Biology"}
            }
        },
        {
            "body": "<p>Which is the smallest known cell?</p>",
            "id": 49834,
            "order": 3,
            "marks": 1,
            "extras": {
                "subject": {"id": 1008, "name": "Botany (Advanced BC)"},
                "unit": {"id": 1842, "name": "Cell Biology"}
            }
        },
        {
            "body": "<p>What is the term 'protoplasm' used for?</p>",
            "id": 49835,
            "order": 4,
            "marks": 1,
            "extras": {
                "subject": {"id": 1008, "name": "Botany (Advanced BC)"},
                "unit": {"id": 1842, "name": "Cell Biology"}
            }
        },
        {
            "body": "<p>Which structure controls all the activities of a living cell?</p>",
            "id": 49836,
            "order": 5,
            "marks": 1,
            "extras": {
                "subject": {"id": 1008, "name": "Botany (Advanced BC)"},
                "unit": {"id": 1842, "name": "Cell Biology"}
            }
        },
        {
            "body": "<p>Which organelle is responsible for ATP synthesis?</p>",
            "id": 49837,
            "order": 6,
            "marks": 1,
            "extras": {
                "subject": {"id": 1008, "name": "Botany (Advanced BC)"},
                "unit": {"id": 1842, "name": "Cell Biology"}
            }
        },
        {
            "body": "<p>What is the function of lysosomes?</p>",
            "id": 49838,
            "order": 7,
            "marks": 1,
            "extras": {
                "subject": {"id": 1008, "name": "Botany (Advanced BC)"},
                "unit": {"id": 1842, "name": "Cell Biology"}
            }
        },
        {
            "body": "<p>Which cell organelle is known as the 'powerhouse of the cell'?</p>",
            "id": 49839,
            "order": 8,
            "marks": 1,
            "extras": {
                "subject": {"id": 1008, "name": "Botany (Advanced BC)"},
                "unit": {"id": 1842, "name": "Cell Biology"}
            }
        },
        {
            "body": "<p>Which structure distinguishes plant cells from animal cells?</p>",
            "id": 49840,
            "order": 9,
            "marks": 1,
            "extras": {
                "subject": {"id": 1008, "name": "Botany (Advanced BC)"},
                "unit": {"id": 1842, "name": "Cell Biology"}
            }
        },
        {
            "body": "<p>What is the function of the Golgi apparatus?</p>",
            "id": 49841,
            "order": 10,
            "marks": 1,
            "extras": {
                "subject": {"id": 1008, "name": "Botany (Advanced BC)"},
                "unit": {"id": 1842, "name": "Cell Biology"}
            }
        }
    ],
    "exam_reminders": [8],
    "rewards": [{"position": 1, "prize": 5000}],
    "is_routine": False,
    "criteria_fields": [],
    "auto_save_message": "<p>Mock test time is up. Your answer will be submitted automatically. All the best for your result.</p>",
    "self_submit_message": "<p>Thank you for submitting. Wishing you good results.</p>",
    "confirmation_message": "<p>Your mock test will be submitted. If needed, verify the answer. All the best for your results.</p>",
    "rules": (
        "<p>Student should attend the test solely</p>"
        "<p>Students are suggested not to exit and resume the test.</p>"
    ),
    "terms_and_condition": (
        "<p>Students are not allowed to submit the answer through any source.</p>"
        "<p>If any unwanted activity is detected then students can be disqualified for the exam...</p>"
    ),
    "packages": [22],
    "showPackageform": False,
    "exam_threshold_id": 2,
    "title": user_title,
    "sub_title": user_title,
    "number_of_participant": "10",
    "points": "100",
    "number_of_questions": "10",
    "type": "DPP",
    "guru_org_id": 304,
    "description": "DPP Test",
    "published_at": published_at,
    "participant_limit": "10",
    "model_set_title": "DPP Test",
    "model_set_subtitle": "DPP Test",
    "pass_percentage": "10",
    "setup_through": 1,
    "exam_setup_id": None
}

# Debug payload
#print("Payload:", data_create_exam)

# Make the API request
response_create_exam = requests.post(url_create_exam, headers=headers, json=data_create_exam)

if response_create_exam.status_code == 201:
    exam_id = response_create_exam.json().get('data', {}).get('id')
    print("Exam Created Successfully. Exam ID:", exam_id)

    # Construct and open exam URL
    exam_url = f"https://admin.ambition.guru/exams/mock-test-detail/{exam_id}?routeName=Exams"
    print(f"Opening exam URL: {exam_url}")
    webbrowser.get("firefox").open(exam_url)

    # Step 2: Lock questions for the exam
    url_lock_questions = f"https://api-adm.ambition.guru/api/v1/admin/exams/{exam_id}/lock-questions"
    response_lock_questions = requests.post(url_lock_questions, headers=headers)

    if response_lock_questions.status_code == 200:
        print(f"Questions locked successfully for Exam ID: {exam_id}")
    else:
        print(f"Failed to lock questions. Status Code: {response_lock_questions.status_code}")
        print("Response:", response_lock_questions.json())
else:
    print("Failed to create exam. Status Code:", response_create_exam.status_code)
    print("Response:", response_create_exam.json())