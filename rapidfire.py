from datetime import datetime
import requests
import webbrowser

# Get user input for title
app_title = input("Enter the title for the meeting: ")

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiNmVkNmVhNDFkODFmY2JkM2UzYTQ0OWI3ZWY0YjQ0ZGQ3MjIzYzllZTRlNTkxNWZiZTJmYTVjZmVjNGFlYjA3MzVhYjQ4ZmNlYjY3ZjY0Y2QiLCJpYXQiOjE3MzUxMDc2OTguMjY1NjM4LCJuYmYiOjE3MzUxMDc2OTguMjY1NjQxLCJleHAiOjE3MzU3MTI0OTguMjU3NTA1LCJzdWIiOiI4MSIsInNjb3BlcyI6WyJhZG1pbiJdfQ.r4PnLM_v18EbmLG0SKmiF7DEhT4O2-DXMF089Ee7Ub-qP2Pr80-KJ_PCUEqG3jKE67JhxZ96vvt7g04bX6u2cyU1nts_vM5yWvM_A20e3mmeM7066xvh9FmkXfLxPxgpcMd0mrJn2YLp-0_rZ8KZQXQXcE1Nqzi0vX2Own2QpD_yHxk9ILW-757NLVYiXI32oi3enoYjjfDlKJxZfC2q-5W7p8qNtC-BHy-V6VvqUhIF0u3v0FEEH4npUD0P80ixg0dgnSFIUxcgI_wdhkHrrp4wMHHnwCKQ8DOOpVp13wo0_EREWTVYL6kkgqjFsjUkKmcfVpmiY7HyGxb1bTp5VxX676_vS0gs9BsJJ8v9f1AxxB44X1ZnPdeWNRESHM_qJ0OeH_EoryfZCvecHJ2Ul2BDjMdw9kVJ0dnjj5LeuXO9oSv5OrZywulL5VWsL4UeIAYZXxZoMenCY7PzgucZsFCEyS0cptJmROIddz0oUsiosLn23XE-eeTL3SXbaspF1pyhRdQYH3Kza6aKEG7b0MogAXNFYPTmn7mB4LibIm0zEtul1P3geXS1geF57cmOwuG4VDvNY6a0n0QWNNeSwCvWta7jA7zugy_QFkLcqGpmZPbGZoin7k_8Aiq4aS7HTlLLnrNptiVajV5TvrgFasiGiiw02RCI-h1GenPCb0Q",
    'Connection': 'keep-alive',
    'Origin': 'https://admin.ambition.guru',
    'Referer': 'https://admin.ambition.guru/',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:133.0) Gecko/20100101 Firefox/133.0',
    'X-Requested-With': 'XMLHttpRequest',
    'content-type': 'application/json',
}

# First API: Create meeting

# Get the current date and time
current_datetime = datetime.now()
start_date = current_datetime.strftime("%Y-%m-%d")  # Current date in "YYYY-MM-DD" format
start_time = current_datetime.strftime("%Y-%m-%d %H:%M")  # Current date and time in "YYYY-MM-DD HH:MM" format

accounts = {
    48: { "name": "Loksewa 3000 B", "participant_limit": 3000 },
    47: { "name": "Loksewa 3000 A", "participant_limit": 3000 },
    46: { "name": "ISV Zoom Account 10 - 1000", "participant_limit": 1000 },
    45: { "name": "ISV Zoom Account 9 - 1000", "participant_limit": 1000 },
    44: { "name": "Loksewa 1000 B", "participant_limit": 1000 },
    43: { "name": "Loksewa 1000 A", "participant_limit": 1000 },
    42: { "name": "ISV Zoom Account 6 - 500", "participant_limit": 500 },
    41: { "name": "ISV Zoom Account 5 - 500", "participant_limit": 500 },
    40: { "name": "Orientation 500", "participant_limit": 500 },
    39: { "name": "Loksewa 500 C", "participant_limit": 500 },
    38: { "name": "Loksewa 500 B", "participant_limit": 500 },
    37: { "name": "Loksewa 500 A", "participant_limit": 500 },
}

# Ask user to select an account or default to ID 10
print("Available Zoom Accounts:")
for account_id, account_info in accounts.items():
    print(f"{account_id}: {account_info['name']} (Participant Limit: {account_info['participant_limit']})")


selected_account = input("Enter the ID of the Zoom account to use (default is 10): ")

# Validate and set account ID
try:
    live_class_account_id = int(selected_account)
    if live_class_account_id not in accounts:
        raise ValueError("Invalid ID")
except (ValueError, TypeError):
    print("Invalid or no input. Defaulting to account ID 37.")
    live_class_account_id = 37


json_data = {
    'type': 2,
    'password': '',
    "start_time": start_time,
    'duration': 60,
    'contact_email': 'ambitionguru2022@gmail.com',
    'join_before_host': True,
    'formType': 'add',
    'content_display_category_id': None,
    'channel': 'zoom',
    'audios': [6],
    'all_package': 0,
    'is_free': 1,
    'payable_type': 1,
    'topic': app_title,
    'app_title': app_title,
    'app_sub_title': app_title,
    'tags': [app_title],
    'guru_org_id': 304,
    'meeting_type': 2,
    'meeting_sub_type': '0',
    'remainder_template_id': [9],
    "live_class_account_ids": [live_class_account_id],
    'description': app_title,
    'media_id': 1190021,
    'status': 0,
    'studio_id': 8,
    'chapter_meeting': [
        {
            'package_id': 22,
            'subject_id': 25007,
            'unit_id': 25012,
            'chapter_id': 25020,
            'subject_type': 'Subject',
            'syllabus_type': 'Master',
        },
    ],
}

response = requests.post('https://api-adm.ambition.guru/api/v1/admin/meeting', headers=headers, json=json_data)

if response.status_code in [200, 201]:  # Check if the meeting creation was successful
    response_data = response.json()
    meeting_id = response_data.get('data', {}).get('id')  # Extract meeting ID

    if meeting_id:
        print(f"Meeting created successfully. Meeting ID: {meeting_id}")

        # Fourth API: Fetch chapter-wise questions
        chapter_questions_url = (
            'https://api-adm.ambition.guru/api/v1/admin/org-section/chapter-wise-question/11652'
            '?page=1&rowsPerPage=50&sortBy=id&columns=id,name&with=&descending=true&query=&filters='
            '{"no_contents":0,"tag_filter":null,"baseImage":false,"strongTag":false,'
            '"subject_id":11521,"unit_id":11652,"section_id":null}'
        )
        chapter_questions_response = requests.get(chapter_questions_url, headers=headers)

        if chapter_questions_response.status_code == 200:
            chapter_questions_data = chapter_questions_response.json()
            question_ids = [item['id'] for item in chapter_questions_data.get('data', [])]  # Collect question IDs

            print("Fetched chapter-wise questions successfully.")
            print(f"Question IDs: {question_ids}")

            # Fifth API: Save question to be asked
            for question_id in question_ids:
                save_question_url = f'https://api-adm.ambition.guru/api/v1/admin/meeting/{meeting_id}/questions/{question_id}/save-question-to-be-asked'
                save_question_response = requests.post(save_question_url, headers=headers)

                if save_question_response.status_code == 200:
                    print(f"Question {question_id} saved to be asked successfully.")
                else:
                    print(f"Failed to save question {question_id}. Status Code: {save_question_response.status_code}")
                    print(f"Response: {save_question_response.text}")

            # Sixth API: Fetch homework questions
            homework_questions_url = (
                f'https://api-adm.ambition.guru/api/v1/admin/meeting/{meeting_id}/get-home-work-questions'
                '?page=1&rowsPerPage=50&sortBy=id&columns=id,name&with=&descending=true&query=&filters={}'
            )
            homework_questions_response = requests.get(homework_questions_url, headers=headers)

            if homework_questions_response.status_code == 200:
                print("Fetched homework questions successfully.")
               # print("Response:", homework_questions_response.json())
            else:
                print(f"Failed to fetch homework questions. Status Code: {homework_questions_response.status_code}")
                print(f"Response: {homework_questions_response.text}")

            # Open the final URL in Firefox
            final_url = f'https://admin.ambition.guru/meeting/{meeting_id}/question'
            print(f"Opening the final URL: {final_url}")
            firefox = webbrowser.get('firefox')
            firefox.open(final_url)
        else:
            print(f"Failed to fetch chapter-wise questions. Status Code: {chapter_questions_response.status_code}")
            print(f"Response: {chapter_questions_response.text}")
    else:
        print("Meeting created, but meeting_id not found in the response.")
else:
    print(f"Failed to create meeting. Status Code: {response.status_code}")
    print(f"Response: {response.text}")
