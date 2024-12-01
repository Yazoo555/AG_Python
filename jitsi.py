import requests
from datetime import datetime
import webbrowser

# Prompt the user for the live class title
user_title = input("Please enter the title for the live class: ")

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
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiNzBiMjdkZDExYjYxMGU5NjQyNjAxYWU4N2M5YzUxNDM5NDA1OGYxZGExMWU5ZmY2MjU1OTk5ZTViZmY1OWQ3MDBlN2ExMWFkYTFiMzcwMDciLCJpYXQiOjE3MzI0Mzk5OTguODU4NzI4LCJuYmYiOjE3MzI0Mzk5OTguODU4NzMxLCJleHAiOjE3MzMwNDQ3OTguODUxOTU1LCJzdWIiOiIzNzIiLCJzY29wZXMiOlsiYWRtaW4iXX0.MIW1SXCmJHeg1bvc0jo2sk1rG_ifZ2ZedxNjk1yGj9XvvEmw9M0eXtPvyM6-xLy8SsgHs1JvwH-gpdYik2NShsU0hYbaPbXfdES-cOAtOsCwfYRTPy_U4BcOjidA0DltaHvQW-sH7gkKhWwpzJuYzpuJYFZIbfXEKPMy9u8PTXHc7Bcocde4Noy12LBmECJ8Dgyh02GhRTn4SfsV7jEViajJpFfafB3pqr3TMdD6WgFhb86-EzT6aicc_rx-hZ6Cu1uF_LLypesnOU60rSZruiJX8Gc5Z7B7L9tAZdCcOlAJJDt6vIhTRoBIi0hsO7uuCuLehuGR2ti08cSiOMtBEuCpm7SayukRstBy6cO1ByJapsgWXRMimhG1yGpZRcZUXmvp4uduCOF8K68SBPn11Mobw-i3Zdyo71vmTbK_LEkK2If2dIb2ch_LE659-wlS3L-F55S5p8Z75Ogh4neNQOHbeBWuIGZht5JxzY-jJcxZExKc7RQy2zBCUPaCMIGXIceOkERVN0HJ-6ytISZ45imt0fsYv07ybL7PnJY7k55c-rKv4ykhLH8iCu8RL0pd46m4C_LkMVqTZfDhebSBFH9WQlfrRnjlZPMn9ksSOQWTh7Dr-KDdsE7LKBTXdjp_9DdLiZ6x5UBfODOQYAukk382XpGSkcMtpwsbBJd3Zok",
    "Connection": "keep-alive",
    "Priority": "u=0"
}

# Get the current date and time
current_datetime = datetime.now()
start_date = current_datetime.strftime("%Y-%m-%d")  # Current date in "YYYY-MM-DD" format
start_time = current_datetime.strftime("%Y-%m-%d %H:%M")  # Current date and time in "YYYY-MM-DD HH:MM" format

# Map of available accounts
accounts = {
    11: {"name": "Guru Meet - 3 (DO)","email": "prashant@ambition.guru"},
    8: {"name": "Guru Meet - 2 (Jitsi)", "email": "suman@ambition.guru"},
    6: {"name": "Guru Meet - 1", "email": "niraj@ambition.guru"}
}

# Ask user to select an account or default to ID 6
print("Available Live Class Accounts:")
for account_id, account_info in accounts.items():
    print(f"{account_id}: {account_info['name']} ({account_info['email']})")

selected_account = input("Enter the ID of the live class account to use (default is 6): ")

# Validate and set account ID
try:
    live_class_account_id = int(selected_account)
    if live_class_account_id not in accounts:
        raise ValueError("Invalid ID")
except (ValueError, TypeError):
    print("Invalid or no input. Defaulting to account ID 6.")
    live_class_account_id = 6

data_create_meeting = {
    "type": 2,
    "password": "",
    "start_time": start_time,
    "duration": 60,
    "contact_email": "ambitionguru2022@gmail.com",
    "join_before_host": True,
    "formType": "add",
    "content_display_category_id": None,
    "channel": "jitsi_ag",
    "audios": [],
    "all_package": 0,
    "is_free": 1,
    "payable_type": 1,
    "live_class_account_ids": [live_class_account_id],
    "topic": user_title,            # Dynamic title for topic
    "app_title": user_title,        # Dynamic title for app title
    "app_sub_title": user_title,    # Dynamic title for app subtitle
    "tags": [user_title],
    "guru_org_id": 304,
    "meeting_type": 1,
    "remainder_template_id": [6],
    "description": user_title,      # Dynamic description
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
    print("Successfully created Live Class!")
    response_data = response_create_meeting.json()
    
    # Extract the meeting ID
    meeting_id = response_data.get('data', {}).get('id')
    print(f"Meeting ID: {meeting_id}")
    
    if meeting_id:
        # Step 2: Update the meeting status
        update_status_url = f"https://api-adm.ambition.guru/api/v1/admin/meeting/{meeting_id}/update-status"
        
        # Set the status dynamically (e.g., 1 for active, 0 for inactive)
        status = int(input("Enter the status for the live class (1 for active, 0 for inactive): "))
        data_update_status = {
            "status": status
        }
        
        response_update_status = requests.post(update_status_url, headers=headers, json=data_update_status)
        
        if response_update_status.status_code == 200:
            print(f"Successfully updated status for Live Class ID: {meeting_id} to {status}")
            
            # Construct the URL for the meeting details
            detail_url = f"https://admin.ambition.guru/meeting/{meeting_id}/students"
            print(f"Opening Live Class URL: {detail_url}")
            
            # Open the Live Class URL in Firefox or the default browser
            webbrowser.get("firefox").open(detail_url)
        else:
            print("Failed to update status.")
            print("Status Code:", response_update_status.status_code)
            print("Response Content:", response_update_status.text)
    else:
        print("Failed to extract meeting ID.")
else:
    print("Failed to create Live Class.")
    print("Status Code:", response_create_meeting.status_code)
    print("Response Content:", response_create_meeting.text)
