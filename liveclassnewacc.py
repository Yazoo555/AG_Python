import requests
from datetime import datetime
import webbrowser

from auth import get_auth_token

# URL and headers setup
url_create_meeting = "https://api-adm.ambition.guru/api/v1/admin/meeting"
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

# Get current date and time
current_datetime = datetime.now()
start_time = current_datetime.strftime("%Y-%m-%d %H:%M")

# Map of available Zoom accounts
accounts = {
    37: {"name": "ISV Zoom Account 1 - 500", "participant_limit": 500},
    38: {"name": "ISV Zoom Account 2 - 500", "participant_limit": 500},
    39: {"name": "ISV Zoom Account 3 - 500", "participant_limit": 500},
    40: {"name": "ISV Zoom Account 4 - 500", "participant_limit": 500},
    41: {"name": "ISV Zoom Account 5 - 500", "participant_limit": 500},
    42: {"name": "ISV Zoom Account 6 - 500", "participant_limit": 500},
    43: {"name": "ISV Zoom Account 7 - 1000", "participant_limit": 1000},
    44: {"name": "ISV Zoom Account 8 - 1000", "participant_limit": 1000},
    45: {"name": "ISV Zoom Account 9 - 1000", "participant_limit": 1000},
    46: {"name": "ISV Zoom Account 10 - 1000", "participant_limit": 1000},
    47: {"name": "ISV Zoom Account 11 - 3000", "participant_limit": 3000},
    48: {"name": "ISV Zoom Account 12 - 3000", "participant_limit": 3000},
    49: {"name": "ISV Zoom Account 13 - 3000", "participant_limit": 3000}
}

# Loop through each account and create a meeting
for account_id, account_info in accounts.items():
    # Create live class data using the Zoom account name
    user_title = account_info["name"]
    data_create_meeting = {
        "type": 2,
        "password": "",
        "start_time": start_time,
        "duration": 60,
        "contact_email": "ambitionguru2022@gmail.com",
        "join_before_host": True,
        "formType": "add",
        "content_display_category_id": None,
        "channel": "zoom",
        "audios": [],
        "all_package": 0,
        "is_free": 1,
        "payable_type": 1,
        "live_class_account_ids": [account_id],
        "topic": user_title,
        "app_title": user_title,
        "app_sub_title": user_title,
        "tags": [user_title],
        "guru_org_id": 304,
        "meeting_type": 1,
        "remainder_template_id": [6],
        "description": user_title,
        "media_id": 1125982,
        "studio_id": 3,
        "chapter_meeting": [{
            "package_id": 22,
            "subject_id": 14399,
            "chapter_id": 16154,
            "subject_type": "Section",
            "syllabus_type": "CustomSyllabus",
            "chapter_ids": [16150, 16154]
        }]
    }

    # Step 1: Create the live class
    response_create_meeting = requests.post(url_create_meeting, headers=headers, json=data_create_meeting)

    if response_create_meeting.status_code == 201:
        print(f"Successfully created Live Class: {user_title}")
        response_data = response_create_meeting.json()
        
        # Extract the meeting ID
        meeting_id = response_data.get('data', {}).get('id')
        print(f"Meeting ID: {meeting_id}")
        
        if meeting_id:
            # Step 2: Update the meeting status to active (1)
            update_status_url = f"https://api-adm.ambition.guru/api/v1/admin/meeting/{meeting_id}/update-status"
            data_update_status = {
                "status": 0  # Active status
            }
            
            response_update_status = requests.post(update_status_url, headers=headers, json=data_update_status)
            
            if response_update_status.status_code == 200:
                print(f"Successfully updated status for Live Class ID: {meeting_id} to active (1)")
                
                # Construct the URL for the meeting details
                detail_url = f"https://admin.ambition.guru/meeting/{meeting_id}/students"
                print(f"Opening Live Class URL: {detail_url}")
                
                # Open the Live Class URL in the default browser (Firefox)
                webbrowser.get("firefox").open(detail_url)
            else:
                print("Failed to update status.")
                print("Status Code:", response_update_status.status_code)
                print("Response Content:", response_update_status.text)
        else:
            print("Failed to extract meeting ID.")
    else:
        print(f"Failed to create Live Class: {user_title}")
        print("Status Code:", response_create_meeting.status_code)
        print("Response Content:", response_create_meeting.text)
