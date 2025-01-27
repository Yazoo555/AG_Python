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
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiYjU4NjYxNjRmYzZmYzg5MmFlNWU1YmI2NGRiY2Q4Y2Q3NmM2NGZmOTkwZTZmYmFmOThlMzk0YjY4OTA2MzA0MTllYjMyZWI4N2NkOWE4NTciLCJpYXQiOjE3Mzc0NDAzNTguODk4MjEzLCJuYmYiOjE3Mzc0NDAzNTguODk4MjE5LCJleHAiOjE3MzgwNDUxNTguODg1MjM1LCJzdWIiOiIzNzIiLCJzY29wZXMiOlsiYWRtaW4iXX0.NXp0UY9gLYkB9CNxI5WGyD6Qo_Hd-dNQZIonglARlka0g2nCaBR5ZTPsqGrsVXiSJmCF4TWbkwO9QQH6pb7ec4fc7Z4U2I6jj8bsjeVVMmGpDZMrQS38U-BgPk1lBOW9OdvvxdtBkT6Z6JN0OYhWaLgXbuqy64PFAYeyI-nDhuW3A8U1ovLm4OX537Xyv_QQouLAZbImapdcYyCnyhyoIAJPu2FWWznn9E5tBxkx5HPQQVPIc2BCWlhAfzXdN1YevGD4kWK_cCrKn4K_9-2j2Puf6kJ2Y11pHgis6W6Pu17khEWN5zOOeiMTmHV5FkIkBeD380dFnQf_cMlW9icI43RpR1wBsC-fCYLsbhv7Yca8jT-eTIeXgDMjoZFfjOYfjFuEzw_-ihDaFRMRCxbRk3IKUg-woaYvjZiUP3_JaLIeuVj1tr5Pv-GDcfxx87qbPZuimaaMM1xETRmCXlaqGZT-1xVp4XUVU9uygpLXCnY9b4I4d2i8uiyeVP6vjOe7L0_knecTxGCfqoEn61Et4Hp4QgJrGFLtPZJwTn6VbJnSg9hK4iDjEMBvw9oSx6BtMfPVAQDrmNaVmcFVESRpnX1H-7uuuHX_F4QK41S53zAcSNhFYmWCThfgq40Hzt2wDqHrAcRUh-gENpbzl2rhC_TkK_TLg97LuC1KYhWjWaY",
    "Connection": "keep-alive",
    "Priority": "u=0"
}

# Get the current date and time
current_datetime = datetime.now()
start_date = current_datetime.strftime("%Y-%m-%d")  # Current date in "YYYY-MM-DD" format
start_time = current_datetime.strftime("%Y-%m-%d %H:%M")  # Current date and time in "YYYY-MM-DD HH:MM" format

# Map of available Zoom accounts

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


selected_account = input("Enter the ID of the Zoom account to use (default is 37): ")

# Validate and set account ID
try:
    live_class_account_id = int(selected_account)
    if live_class_account_id not in accounts:
        raise ValueError("Invalid ID")
except (ValueError, TypeError):
    print("Invalid or no input. Defaulting to account ID 37.")
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
