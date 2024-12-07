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
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiYmUyYmRkMGQ2NDZlNmVmMzczYTBhOTU2NDIzMzk4ZWQ1M2Q3YmNlM2E3YTMyNDhiMTlkYWNkMDg1Y2ZjZWQzZTk5NWM2NzdiYjEyNjVlZTEiLCJpYXQiOjE3MzI5NDQwMjAuNDQxOTk0LCJuYmYiOjE3MzI5NDQwMjAuNDQxOTk3LCJleHAiOjE3MzM1NDg4MjAuNDM0OSwic3ViIjoiMzcyIiwic2NvcGVzIjpbImFkbWluIl19.MPIA2fBwHbByQydPL4kocTemdmR96Tmi8TXCR6h8dSRaDLU1ztksMN1vSft2xvxDCvvP6x4O7dfsqZe9VRzQZjHBMZ0nOVU6tIpd7bDVEx56ZXnyWpHk13Uq1I8cmIZ9UHnB382SA8kTQZmA5bMZ7nCh9tqxVa34utTYKqpz6b9rSVY9EHC_1xCGdxvNTzdmBrryO0LZ3mMHNFq9Iwi3UC7xcJNksMQ61CkwCpZ620eMZmqG9SusNOunBd3Wigxd3spl8vm6cVAieANOoqK2xL4GieoF4es9bkEZoJFcenVQoBCs6o9tDkYPZ6z4REZ18ovNOu4ki22gjdhotHl4JGHHps8yjhDmunHpTDIyTrD_3-HEm0YMCIhhJgo7Z9ZtZzQu-rVGWgfbUr2vXB-XrgcSwP91IAqEFpWKTu38Wl-FzXO4ZGyaOKGt86-8rtHUETk_gyRunRg_RQmhmXYEZ4qJEqtNlFO-Xwh-se5m1UA8pVHZxz6Krc22lSSWvXMC5fKtNh5IbRVCF8xwkmdkpSFHoB7el53Fj03Ij1cqAgEBzXe31ccYX49_F0entdVgEimyhtIhX6yAqEL7VXLh1tofudj90RNWnLtOyCLhJrii-t4NbfysAv-W_tONlDJuOh7HJ1dSwdKK8dR76bpoitMVWU_ifYvrfDdBgd8KtJc",
    "Connection": "keep-alive",
    "Priority": "u=0"
}

# Get the current date and time
current_datetime = datetime.now()
start_date = current_datetime.strftime("%Y-%m-%d")  # Current date in "YYYY-MM-DD" format
start_time = current_datetime.strftime("%Y-%m-%d %H:%M")  # Current date and time in "YYYY-MM-DD HH:MM" format

# Map of available Zoom accounts

accounts = {
    20: {"name": "Zoom Account - (Science2 - niraj@yajtechnologies.com)", "participant_limit": 3000},
    10: {"name": "Zoom Account - 7 (Aqhter)", "participant_limit": 500},
    49: {"name": "ISV Zoom Account 13 - 3000", "participant_limit": 3000},
    7: {"name": "Zoom Account - 6 (Prashant)", "participant_limit": 500},
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
    48: {"name": "ISV Zoom Account 12 - 3000", "participant_limit": 3000}
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
    print("Invalid or no input. Defaulting to account ID 10.")
    live_class_account_id = 10

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
    "live_class_account_ids": [live_class_account_id],
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
