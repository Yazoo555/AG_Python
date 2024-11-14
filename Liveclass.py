import requests
from datetime import datetime

url = "https://api-adm.ambition.guru/api/v1/admin/meeting"

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:132.0) Gecko/20100101 Firefox/132.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Content-Type": "application/json",
    "Referer": "https://admin.ambition.guru/",
    "X-Requested-With": "XMLHttpRequest",
    "Origin": "https://admin.ambition.guru",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiYzEzNWZlYTZkY2ZlZjIyYWRkOTZhYjI3MWIyNjdiZWMwM2QyZTcwYjc5M2UxNTVjZmJiZWY1ODcxY2U3ODEwZWY0NmExZjU3OGVlN2EyNjYiLCJpYXQiOjE3MzEyMjA5OTEuMjkzODU3LCJuYmYiOjE3MzEyMjA5OTEuMjkzODYsImV4cCI6MTczMTgyNTc5MS4yODc2MzcsInN1YiI6IjM3MiIsInNjb3BlcyI6WyJhZG1pbiJdfQ.qTo4dHn_mDxwheH_oTqqnq4rpSZuuCmRqnHIQ28QmYTH01E43OWVhU9ojIucOU6eYscHtZtjoNj-yfivBZBE4PTy6z0LevxJu_Y-xFE9X_rTHxh20wTITXVEbX6RuN1NLxsL9U_LJv65Wonfe-OSHq0i3AL3cbnfw3QUl17TFUy95FCWu8uFuiEfpTdGGbA0rCnwg__9WheuVyepV0CmaaMyy1BBEs1FJ6WY9TzmB6nPjVyZSxgUK4ASGYJW9CcwsFpUmC2A14ErFiEH7qOdbZrggE2_22x0VNzeeaM7PVVX9YBi2Z2LDF0avM8jN_xqcSUijqtufI_5D_Hp02mRETEkRhXLZVMHybH4QWK0hVDkbK9XyjDSZc_JzqslCVZbsibZUcvc-pHyVHK-5D-i1uA5pMSuS72SAPKMYlVqmIQ0H0fkkBoLJPWy4rV1jJGokZPdfWzh-8DCFhHu6JqHAb-zJKnYhpR4ZmKO3ISekFMoihmfnC2yZazvVMhugkhJlKJYdvRVK03fbeudLPDQslyidRkUmiD8ibOxBry_rhxLWymgBewZAKn8zQnZnePoPdiw_wV3hm20Z-tAv3Mio6v1PFBrR9IVuhIuALw649LOdkKFmru6Pz16S3BKSXQZKvOQHwbqoY0IPAJm8DXcGjwWkOmqE9Sh-vo6FosEJBY",  # Replace with your actual token
    "Connection": "keep-alive",
    "Priority": "u=0"
}

# Get the current date and time
current_datetime = datetime.now()
start_date = current_datetime.strftime("%Y-%m-%d")  # Current date in "YYYY-MM-DD" format
start_time = current_datetime.strftime("%Y-%m-%d %H:%M")  # Current date and time in "YYYY-MM-DD HH:MM" format

# Get dynamic title from user
dynamic_title = input(f"Please enter the title for the exam ({start_date}): ")

data = {
    "type": 2,
    "password": "",
    "start_time": start_time,  # Use dynamic start time here
    "date": start_date,        # Add dynamic date here if required
    "duration": 60,
    "contact_email": "ambitionguru2022@gmail.com",
    "join_before_host": False,
    "formType": "add",
    "content_display_category_id": None,
    "channel": "zoom",
    "audios": [],
    "all_package": 0,
    "is_free": 0,
    "payable_type": 1,
    "topic": dynamic_title,            # Use dynamic title in topic
    "app_title": dynamic_title,         # Use dynamic title in app title
    "app_sub_title": dynamic_title,     # Use dynamic title in app subtitle
    "tags": [dynamic_title],
    "guru_org_id": 304,
    "meeting_type": 1,
    "remainder_template_id": [8],
    "live_class_account_ids": [10],
    "description": dynamic_title,
    "media_id": 1109946,
    "studio_id": 7,
    "chapter_meeting": [{
        "package_id": 22,
        "subject_id": 14396,
        "chapter_id": 15060,
        "subject_type": "Section",
        "syllabus_type": "CustomSyllabus",
        "chapter_ids": [15059, 15060]
    }]
}

# Send the POST request
response = requests.post(url, headers=headers, json=data)

# Print response status and content with error handling
print("Status Code:", response.status_code)
try:
    print("Response JSON:", response.json())
except requests.exceptions.JSONDecodeError:
    print("Failed to parse JSON. Response content:", response.text)

# Additional Success Message (based on status code check)
if response.status_code == 200:
    print("Successfully created Live Class!")
else:
    print("Failed to create Live Class.")
