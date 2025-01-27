from datetime import datetime
import requests
import webbrowser

# Get user input for title
app_title = input("Enter the title for the meeting: ")

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiYjU4NjYxNjRmYzZmYzg5MmFlNWU1YmI2NGRiY2Q4Y2Q3NmM2NGZmOTkwZTZmYmFmOThlMzk0YjY4OTA2MzA0MTllYjMyZWI4N2NkOWE4NTciLCJpYXQiOjE3Mzc0NDAzNTguODk4MjEzLCJuYmYiOjE3Mzc0NDAzNTguODk4MjE5LCJleHAiOjE3MzgwNDUxNTguODg1MjM1LCJzdWIiOiIzNzIiLCJzY29wZXMiOlsiYWRtaW4iXX0.NXp0UY9gLYkB9CNxI5WGyD6Qo_Hd-dNQZIonglARlka0g2nCaBR5ZTPsqGrsVXiSJmCF4TWbkwO9QQH6pb7ec4fc7Z4U2I6jj8bsjeVVMmGpDZMrQS38U-BgPk1lBOW9OdvvxdtBkT6Z6JN0OYhWaLgXbuqy64PFAYeyI-nDhuW3A8U1ovLm4OX537Xyv_QQouLAZbImapdcYyCnyhyoIAJPu2FWWznn9E5tBxkx5HPQQVPIc2BCWlhAfzXdN1YevGD4kWK_cCrKn4K_9-2j2Puf6kJ2Y11pHgis6W6Pu17khEWN5zOOeiMTmHV5FkIkBeD380dFnQf_cMlW9icI43RpR1wBsC-fCYLsbhv7Yca8jT-eTIeXgDMjoZFfjOYfjFuEzw_-ihDaFRMRCxbRk3IKUg-woaYvjZiUP3_JaLIeuVj1tr5Pv-GDcfxx87qbPZuimaaMM1xETRmCXlaqGZT-1xVp4XUVU9uygpLXCnY9b4I4d2i8uiyeVP6vjOe7L0_knecTxGCfqoEn61Et4Hp4QgJrGFLtPZJwTn6VbJnSg9hK4iDjEMBvw9oSx6BtMfPVAQDrmNaVmcFVESRpnX1H-7uuuHX_F4QK41S53zAcSNhFYmWCThfgq40Hzt2wDqHrAcRUh-gENpbzl2rhC_TkK_TLg97LuC1KYhWjWaY",
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
