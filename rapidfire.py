import requests
import webbrowser

# Get user input for title
app_title = input("Enter the title for the meeting: ")

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiMDZlZDc4NGM4YmE4ZDBhNGRiYzg3YjdmMmNkZjdkZTQwMDk5YzU3ZmE2MmNhN2QwNThmZTU5YWM3NDgyMTA2OGQ1OGU5NTRhNWI5ODZiNDYiLCJpYXQiOjE3MzQ0OTY4NjMuNDE2MTI5LCJuYmYiOjE3MzQ0OTY4NjMuNDE2MTM0LCJleHAiOjE3MzUxMDE2NjMuNDA4Mjk1LCJzdWIiOiI4MSIsInNjb3BlcyI6WyJhZG1pbiJdfQ.H0YqA22AfrACdZTJUZxB8IdQ-P6RrsC2kwStPBy7rd8sgndjXdfUSmh_sng0cvSvddxmXIKFNrHXMe8BJ8SFzQpFHNujvFL1hWFyJ6g_8mBocLzRzstoGnK65tQ8SSgCr70CAueMrZgd305VR-bclRQiF_idO9ygAe5qGpUps1DTP5BitJrusXc10c8wO9bWBMIgn0IzU09JCssIye4QptCAcAHRy_nrjwXECI7cjMzwGeHq18d9Dq33qSDG0jy_IrJVst56XepMqC9bDkU_MLtY_V13uA8g_XBuK-Hv1s1YaG0X24JO_TUKcqdYvJBkl1qNMP6pn6ng0gE-X-reoHIXradMarad1AWZOrqsHqm2w7H72GgqMGKV1W7LBnIj9BZHBkGDv_tlIS8MTMi2_oWBAamlTXdbHsjW7fox_NBcckSSXJzeYJr5QJgXE28lF1kI5_1JAS2El2-ZHaqBxmW4dTMhKfuYUs-G8lVnhgxnnVh462Qqt1grwORdybDKtAOF9zo9TvVQUxgw7rXHCL5pVut8I4-FHKX0uqsUNwTDlf5UoIUL8pN4dZuTZjtmU5sXqr5dytqFgctOT75O-Ny6kbQe4D_GgdwOuwV0BWOKkHgu9nXAztd_oOJfLLdoSPAhvuNvfhhZcmWVmGXLL7xrZcssF4T-vnGhd1tQAD8',
    'Connection': 'keep-alive',
    'Origin': 'https://admin.ambition.guru',
    'Referer': 'https://admin.ambition.guru/',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:133.0) Gecko/20100101 Firefox/133.0',
    'X-Requested-With': 'XMLHttpRequest',
    'content-type': 'application/json',
}

# First API: Create meeting

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
    'start_time': '2024-12-24 20:20',
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
