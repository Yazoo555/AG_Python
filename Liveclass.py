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
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiYmYyOGE1N2NjZDk2YmRjMWEwN2M3YWRmYTM4OWFlMTI4MWVhOTc1YjQxY2Q0Mjc4MmRiMDQ1ZDJlZGUwMzFlNTI2YmU0NWIwZGI1ZjQzZGUiLCJpYXQiOjE3MzE5MTc0NjAuNzcxMzMzLCJuYmYiOjE3MzE5MTc0NjAuNzcxMzM2LCJleHAiOjE3MzI1MjIyNjAuNzY0NzM4LCJzdWIiOiI4MSIsInNjb3BlcyI6WyJhZG1pbiJdfQ.e2dIHA3ZotS9m8YmJXBW0MpjLz6v5amC3rHxk6wIOUhlSJcby8SuGQj2WdpUFO7bZ42zkFK-VNAWGmp1_HhjoFVWtkFjXDDoxNb8yxCipntL6gZMx2WztkROaH6Jj1-ltnzs70F_hwMtY4pdi3iHOQsoO6xJJ0eJJ_QNdASsNOf352HAFkECmUIINvAE9kibOW6eHe159bpf2SmVsPHrKsgwieT849_vIwYlwtOTEg-yua3tyn5z5YnKM2qvCWzRKGeKLCRmUZKxEiIqSkEjfVPuGxc1FuZVVc73jja4jNhzvjfIA28ayb_SJjRQWiFjHmqmLGnK9Euxhn1i5hu0Aji_vuirFhx5WuVUpO3TbOk_B-djiLzqfm5MZDZH1TLd87IzcHldxrc5j8XyzgEqSX1eDFmUg84mf8qSCi1eNj8M3ZVRpNoc5Ku6hoiwEq85rRM-7elIvujkr3CcBV8PWknYn9kCi7pgam4XkR1ZzbOO_hi9XO3WwP8S1J_6CK8KKtRHsJBXhnGBd0TNPI_XCGLeZDtsPn6gml8gx0Ewvb3BYgmpE49LeBZcyWe7oTkW_AE6rLDBYHI0lPIcVTHj9n5da5xNZJ3eya7mOE5fnnQFfvoDf2OAI9fyRwRjwxEwFmZ2zmCRxzDkF9JN3OpRTKPyrQP3rR7Hbzt1w3CiSGI",
    "Connection": "keep-alive",
    "Priority": "u=0"
}

# Get the current date and time
current_datetime = datetime.now()
start_date = current_datetime.strftime("%Y-%m-%d")  # Current date in "YYYY-MM-DD" format
start_time = current_datetime.strftime("%Y-%m-%d %H:%M")  # Current date and time in "YYYY-MM-DD HH:MM" format

# Map of available Zoom accounts
accounts = {
    37: {"name": "ISV Zoom Account 1 - 500", "participant_limit": 500},
    20: {"name": "Zoom Account - (Science2 - niraj@yajtechnologies.com)", "participant_limit": 3000},
    10: {"name": "Zoom Account - 7 (Aqhter)", "participant_limit": 500},
    7: {"name": "Zoom Account - 6 (Prashant)", "participant_limit": 500}
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
