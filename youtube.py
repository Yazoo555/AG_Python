import requests
from datetime import datetime, timedelta
from auth import get_auth_token
import webbrowser

def create_youtube_live_class():
    # Get user input for the topic
    topic = input("Please enter the topic for the YouTube Live Class: ")

    # Get current time and add 2 minutes for the start time
    current_time = datetime.now()
    start_time = (current_time + timedelta(minutes=2)).strftime("%Y-%m-%d %H:%M")

    # Cookies
    cookies = {
        'ambition_guru_session': 'eyJpdiI6IjN0VmdjQXBsMUxHblJJSTZuYTY2S1E9PSIsInZhbHVlIjoidzZsQUtPVXY0MzVvS2FqN0ZNb2ErNzgrVit0Q2txUHpabkFTWVdvbUJYZnBUdXcybTZpcFJ2WS9hSVJBS0JtUHVVeWpGMzAxZ1NjdU5ZUngyTDN5ZzVYWE9KaWJGd1c2ZEFNSFZoZmR1QVBRb0FHc2g5WDlWeEFyOVpLRjUrQy8iLCJtYWMiOiI2Y2ZiNmJjZGZiMGM0ZWNkY2YwMTEyYzE3ZmY2Y2NjNDNiM2ZiMzY3OTllZmQxOTdkYmFjM2NjZmJiODZlMGNkIiwidGFnIjoiIn0%3D',
    }

    # Headers with dynamic authorization
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:134.0) Gecko/20100101 Firefox/134.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'application/json',
        'Referer': 'https://admin.ambition.guru/',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'https://admin.ambition.guru',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'Authorization': f'Bearer {get_auth_token()}',
        'Connection': 'keep-alive',
        'Priority': 'u=0',
    }

    # JSON data with dynamic topic and start time
    json_data = {
        'type': 2,
        'password': '',
        'start_time': start_time,
        'duration': 60,
        'contact_email': 'ambitionguru2022@gmail.com',
        'join_before_host': True,
        'formType': 'add',
        'content_display_category_id': None,
        'channel': 'yt',
        'audios': [],
        'all_package': 0,
        'is_free': 1,
        'payable_type': 1,
        'live_class_account_ids': [13],
        'topic': topic,
        'app_title': topic,
        'app_sub_title': topic,
        'tags': [topic],
        'guru_org_id': 304,
        'meeting_type': 1,
        'remainder_template_id': [6],
        'description': topic,
        'media_id': 1190021,
        'status': 0,
        'studio_id': 5,
        'chapter_meeting': [
            {
                'package_id': 22,
                'subject_id': 15989,
                'chapter_id': 23668,
                'subject_type': 'Section',
                'syllabus_type': 'CustomSyllabus',
                'chapter_ids': [16208, 23668],
            },
        ],
        'playlist_category_ids': [47],
    }

    # Make the API request
    response = requests.post('https://api-adm.ambition.guru/api/v1/admin/meeting', 
                             cookies=cookies, headers=headers, json=json_data)

    # Process the response
    if response.status_code == 201:
        print("YouTube Live Class created successfully!")
        response_data = response.json()
        meeting_id = response_data.get('data', {}).get('id')
        if meeting_id:
            print(f"Meeting ID: {meeting_id}")
            
            # Construct the URL for the meeting details
            detail_url = f"https://admin.ambition.guru/meeting/{meeting_id}/students"
            print(f"Opening YouTube Live Class URL: {detail_url}")
            
            # Open the Live Class URL in Firefox or the default browser
            webbrowser.get("firefox").open(detail_url)
        else:
            print("Failed to extract meeting ID.")
    else:
        print(f"Failed to create YouTube Live Class. Status Code: {response.status_code}")
        print("Response:", response.text)

if __name__ == "__main__":
    create_youtube_live_class()

