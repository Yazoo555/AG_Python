import requests
from datetime import datetime, timedelta
import webbrowser

# Endpoint URL
url_create_exam = "https://api-adm.ambition.guru/api/v1/admin/exams"
user_title = input("Please enter the title for the exam: ")



# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"encryptedUserId":"eyJpdiI6IjZBQ0NhL2poSDd1YkxQVnRHTzFoUkE9PSIsInZhbHVlIjoia2lXdVpyRFlNaXljL0FERkw0UXE4QT09IiwibWFjIjoiOTkwODM5ZjZjOWE0ZTk5MjRlYmI4ODhmMmVlZGRjZTM2ZmE0ZGEzZjM5YTgxMTY3ZDg4MGZiY2FlOTRlYzRmMiIsInRhZyI6IiJ9","key":"7659ebe0-9fb7-4539-8f67-f55a11851231"}'
#response = requests.post('https://api-adm.ambition.guru/api/v1/admin/login-with-qr-auth', headers=headers, data=data, verify=False)

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
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiMDZlZDc4NGM4YmE4ZDBhNGRiYzg3YjdmMmNkZjdkZTQwMDk5YzU3ZmE2MmNhN2QwNThmZTU5YWM3NDgyMTA2OGQ1OGU5NTRhNWI5ODZiNDYiLCJpYXQiOjE3MzQ0OTY4NjMuNDE2MTI5LCJuYmYiOjE3MzQ0OTY4NjMuNDE2MTM0LCJleHAiOjE3MzUxMDE2NjMuNDA4Mjk1LCJzdWIiOiI4MSIsInNjb3BlcyI6WyJhZG1pbiJdfQ.H0YqA22AfrACdZTJUZxB8IdQ-P6RrsC2kwStPBy7rd8sgndjXdfUSmh_sng0cvSvddxmXIKFNrHXMe8BJ8SFzQpFHNujvFL1hWFyJ6g_8mBocLzRzstoGnK65tQ8SSgCr70CAueMrZgd305VR-bclRQiF_idO9ygAe5qGpUps1DTP5BitJrusXc10c8wO9bWBMIgn0IzU09JCssIye4QptCAcAHRy_nrjwXECI7cjMzwGeHq18d9Dq33qSDG0jy_IrJVst56XepMqC9bDkU_MLtY_V13uA8g_XBuK-Hv1s1YaG0X24JO_TUKcqdYvJBkl1qNMP6pn6ng0gE-X-reoHIXradMarad1AWZOrqsHqm2w7H72GgqMGKV1W7LBnIj9BZHBkGDv_tlIS8MTMi2_oWBAamlTXdbHsjW7fox_NBcckSSXJzeYJr5QJgXE28lF1kI5_1JAS2El2-ZHaqBxmW4dTMhKfuYUs-G8lVnhgxnnVh462Qqt1grwORdybDKtAOF9zo9TvVQUxgw7rXHCL5pVut8I4-FHKX0uqsUNwTDlf5UoIUL8pN4dZuTZjtmU5sXqr5dytqFgctOT75O-Ny6kbQe4D_GgdwOuwV0BWOKkHgu9nXAztd_oOJfLLdoSPAhvuNvfhhZcmWVmGXLL7xrZcssF4T-vnGhd1tQAD8",
},

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