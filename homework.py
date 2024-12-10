import requests
from datetime import datetime, timedelta
import webbrowser

# API URL for creating homework
url_create_homework = "https://api-adm.ambition.guru/api/v1/admin/exams"

# User input for homework title
user_title = input("Please enter the title for the Homework: ")

# Dynamic timestamps for the homework
current_datetime = datetime.now()
start_time = (current_datetime).strftime("%Y-%m-%d %H:%M:%S")
end_time = (current_datetime + timedelta(days=2)).strftime("%Y-%m-%d %H:%M:%S")
#published_at = current_datetime.strftime("%Y-%m-%d %H:%M:%S")  # Use the current time for published_at


# Headers for API request
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:132.0) Gecko/20100101 Firefox/132.0",
    "Accept": "application/json, text/plain, */*",
    "Content-Type": "application/json",
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiMjlhM2MzZDI1Y2ZlMDBlYTQ3ZWM3MWQwOWY1ZDE2NWJjMTJlMTJhZDAwMWEzNjUyMjU2NGYxNjE5NTNmZmEzODkzOWYwZmU2MjUxOTExYTkiLCJpYXQiOjE3MzM3NTQxMDYuMDY3OTkyLCJuYmYiOjE3MzM3NTQxMDYuMDY3OTk0LCJleHAiOjE3MzQzNTg5MDYuMDU4NzgxLCJzdWIiOiI4MSIsInNjb3BlcyI6WyJhZG1pbiJdfQ.Zf0ykC8frnrPKaktS6TTPD7Aqerf4RHrOk-pepB5lbpgBqJZogkT_TQKfsXisNfgTQ7ADx78b3rHF34p7CDR_wDfqQlmOwQNa0Q1YuDyGDUkUzGqysSodTQ4fMmdNM4exW3kY_vOaBwEvaA32UicD8qKtcE0EuOpCQyemWO09h_RqP6B6ZjSbFHQCUM_Gu5LqQls9aXQAmIHEpaMkdQuqjPQu02lCVermTFoYB4INLLPZq-_XJV1bHn8m8o9jKRfx4jvLBscoYinxdcjbr2mxHH0Ysj7Hx-Dh105WI-EWT-QMo7fB1xky3FE8pBi8Uz1XKZ5zCiVndZaBTkcBxtXX5ItC8PmiYA0rSEjmTjkTEkQJQyWE8D1YaaMbCLOJdMQzAEUzjAGI0nQUkrGbwQhtJAG5qsw21JglFeK-WlktwiqmmdkjzT4Ih358uvdCgirZ_qnLu5hmT1ehxeOU28HcHy-eLjEKDzSouqT_Qq-3dKCErBsbNOyMAS2-Kv9GLGQ-kPZK5-4vR6GLa74-Mn2-v1ezGV82_bTEXOOH-xmUbfb1kixzWrbhLJhSsEFzdhdA7Sud3oHBzPvH0P7ac0sBz1_veFHe_egZTs_vjFrbW5J3e3fHRRdzhk6-yURS1OSlKl5Hgz2fCag4pTJeBNFV-zVIQNffHkgkV3mHjajviE",
    "Connection": "keep-alive"
}

# Data for creating the homework
data_create_homework = {
    "id": 5241,
    "title": user_title,
    "exam_threshold_id": 2,
    "description": None,
    "year": None,
    "status": 0,
    "exam_setup_id": None,
    "negative_marking": "0",
    "start_time": start_time,
    "end_time": end_time,
    "duration": 10,
    "marks": 10,
    "number_of_questions": 5,
    "extras": [
        {
            "id": 19893,
            "name": "Mental Agility Test (MAT)",
            "marks": 5,
            "parent_id": None,
            "number_of_question": 5,
            "subject": {
                "id": 19893,
                "name": "Mental Agility Test (MAT)"
            }
        }
    ],
    "is_active": 1,
    "allow_answer_change": 1,
    "is_default": 0,
    "participant_limit": 0,
    "terms_and_condition": "<p>Students are not allowed to submit the answer through any source.</p>"
                           "<p>If any unwanted activity is detected then students can be disqualified for the exam, this solely depends upon the AG team.</p>",
    "rules": "<p>Student should attend the test solely</p>"
             "<p>Students are suggested not to exit and resume the test.</p>",
    "is_free": 1,
    "rewards": [{"prize": 5000, "position": 1}],
    "registration_deadline": start_time,
    "tags": [user_title],
    "banner_title": None,
    "banner_description": None,
    "is_criteria": 0,
    "criteria_fields": [],
    "is_featured": 0,
    "is_published": 0,
   # "published_at": published_at,
    "price": 0,
    "pass_percentage": "10",
    "auto_save_message": "<p>Mock test time is up. Your answer will be submitted automatically. All the best for your result.</p>",
    "self_submit_message": "<p> Thank you for submitting. Wishing you good results.</p>",
    "exam_reminders": [],
    "media": [],
    "packages": [22],
    "join_in_middle": 1,
    "confirmation_message": "<p> Your mock test will be submitted. If needed, verify the answer. All the best for your results. </p>",
    "number_of_participant": 100,
    "type": "HOMEWORK",
    "locked": False,
    "setup_through": 1,

    "questions": [
        {
            "body": "<p>शिक्षकको गुणस्तर एवम् प्रभावकारिताको बारेमा छोटकरीमा चर्चा गर्नुहोस् ।(२.५+२.५)</p>",
            "id": 115901,
            "order": 11,
            "marks": 1,
            "extras": {
                "unit": {
                    "id": 20329,
                    "name": "Feedback Session",
                    "type": "Unit",
                    "marks": 1,
                    "parent_id": 19893,
                    "thumbnail": None,
                    "children_count": 1,
                    "ancestors_and_self": [
                        {
                            "id": 20329,
                            "name": "Feedback Session",
                            "path": "20329",
                            "rank": 0,
                            "type": "Unit",
                            "depth": 0,
                            "marks": 1
                        },
                        {
                            "id": 19893,
                            "name": "Mental Agility Test (MAT)",
                            "path": "20329.19893",
                            "rank": 0,
                            "type": "Subject",
                            "depth": -1,
                            "marks": 80
                        }
                    ]
                },
                "chapter": {
                    "id": 20330,
                    "name": "Feedback Session",
                    "type": "Chapter",
                    "marks": 1,
                    "parent_id": 20329
                },
                "subject": {
                    "id": 19893,
                    "name": "Mental Agility Test (MAT)",
                    "type": "Subject",
                    "course": {
                        "id": 150,
                        "name": "CEE NewCourse",
                        "rank": 0,
                        "type": "ACADEMIC",
                        "status": 1,
                        "created_at": "2024-05-02T08:32:21.000000Z",
                        "category_id": 27
                    },
                    "course_id": 150,
                    "parent_id": None,
                    "hasChildren": True,
                    "hasCustomSyllabus": False
                },
                "subject_type": "Subject"
            },
            "section_id": None
        },
        {
            "body": "<p>नेपालमा शिक्षकको पेसागत विकासको सम्बन्धमा भएका नीतिगत, संरचनागत एवम् कार्यक्रमगत प्रावधानहरूको चर्चा गर्नुहोस् ।</p>",
            "id": 115902,
            "order": 12,
            "marks": 1,
            "extras": {
                "unit": {
                    "id": 20329,
                    "name": "Feedback Session",
                    "type": "Unit",
                    "marks": 1,
                    "parent_id": 19893,
                    "thumbnail": None,
                    "children_count": 1,
                    "ancestors_and_self": [
                        {
                            "id": 20329,
                            "name": "Feedback Session",
                            "path": "20329",
                            "rank": 0,
                            "type": "Unit",
                            "depth": 0,
                            "marks": 1
                        },
                        {
                            "id": 19893,
                            "name": "Mental Agility Test (MAT)",
                            "path": "20329.19893",
                            "rank": 0,
                            "type": "Subject",
                            "depth": -1,
                            "marks": 80
                        }
                    ]
                },
                "chapter": {
                    "id": 20330,
                    "name": "Feedback Session",
                    "type": "Chapter",
                    "marks": 1,
                    "parent_id": 20329
                },
                "subject": {
                    "id": 19893,
                    "name": "Mental Agility Test (MAT)",
                    "type": "Subject",
                    "course": {
                        "id": 150,
                        "name": "CEE NewCourse",
                        "rank": 0,
                        "type": "ACADEMIC",
                        "status": 1,
                        "created_at": "2024-05-02T08:32:21.000000Z",
                        "category_id": 27
                    },
                    "course_id": 150,
                    "parent_id": None,
                    "hasChildren": True,
                    "hasCustomSyllabus": False
                },
                "subject_type": "Subject"
            },
            "section_id": None
        },
        {
        "body": "<p>अध्यापन अनुमति पत्रको अवधारणा प्रस्तुत गर्दै यसको आवश्यकता दर्साउनुहोस्। साथै नेपालमा अध्यापन अनुमति पत्रको सम्बन्धमा देखिएका समस्याहरू उल्लेख गर्नुहोस् । (२+४+४)</p>",
        "id": 115905,
        "order": 15,
        "marks": 1,
        "extras": {
            "unit": {
                "id": 20329,
                "name": "Feedback Session",
                "type": "Unit",
                "marks": 1,
                "parent_id": 19893,
                "thumbnail": None,
                "children_count": 1,
                "ancestors_and_self": [
                    {
                        "id": 20329,
                        "name": "Feedback Session",
                        "path": "20329",
                        "rank": 0,
                        "type": "Unit",
                        "depth": 0,
                        "marks": 1
                    },
                    {
                        "id": 19893,
                        "name": "Mental Agility Test (MAT)",
                        "path": "20329.19893",
                        "rank": 0,
                        "type": "Subject",
                        "depth": -1,
                        "marks": 80
                    }
                ]
            },
            "chapter": {
                "id": 20330,
                "name": "Feedback Session",
                "type": "Chapter",
                "marks": 1,
                "parent_id": 20329
            },
            "subject": {
                "id": 19893,
                "name": "Mental Agility Test (MAT)",
                "type": "Subject",
                "course": {
                    "id": 150,
                    "name": "CEE NewCourse",
                    "rank": 0,
                    "type": "ACADEMIC",
                    "status": 1,
                    "created_at": "2024-05-02T08:32:21.000000Z",
                    "category_id": 27
                },
                "course_id": 150,
                "parent_id": None,
                "hasChildren": True,
                "hasCustomSyllabus": None
            },
            "subject_type": "Subject"
        },
        "section_id": None
    },

    {
        "body": "<p>शिक्षक बढुवा भनेको के हो ? यसका उद्देश्यहरू उल्लेख गर्नुहोस् । (२+३)</p>",
        "id": 115903,
        "order": 13,
        "marks": 1,
        "extras": {
            "unit": {
                "id": 20329,
                "name": "Feedback Session",
                "type": "Unit",
                "marks": 1,
                "parent_id": 19893,
                "thumbnail": None,
                "children_count": 1,
                "ancestors_and_self": [
                    {
                        "id": 20329,
                        "name": "Feedback Session",
                        "path": "20329",
                        "rank": 0,
                        "type": "Unit",
                        "depth": 0,
                        "marks": 1
                    },
                    {
                        "id": 19893,
                        "name": "Mental Agility Test (MAT)",
                        "path": "20329.19893",
                        "rank": 0,
                        "type": "Subject",
                        "depth": -1,
                        "marks": 80
                    }
                ]
            },
            "chapter": {
                "id": 20330,
                "name": "Feedback Session",
                "type": "Chapter",
                "marks": 1,
                "parent_id": 20329
            },
            "subject": {
                "id": 19893,
                "name": "Mental Agility Test (MAT)",
                "type": "Subject",
                "course": {
                    "id": 150,
                    "name": "CEE NewCourse",
                    "rank": 0,
                    "type": "ACADEMIC",
                    "status": 1,
                    "created_at": "2024-05-02T08:32:21.000000Z",
                    "category_id": 27
                },
                "course_id": 150,
                "parent_id": None,
                "hasChildren": True,
                "hasCustomSyllabus": False
            },
            "subject_type": "Subject"
        },
        "section_id": None
    },
    ]

}


# Send POST request to create homework
response_create_homework = requests.post(url_create_homework, headers=headers, json=data_create_homework)



if response_create_homework.status_code == 201:
    response_data = response_create_homework.json()
    homework_id = response_data.get("data", {}).get("id")
    print("Homework created successfully!")
    print(f"Homework ID: {homework_id}")
    print(f"Homework Title: {user_title}")
    
    # Construct the URL to open the homework
    homework_url = f"https://admin.ambition.guru/exams/mock-test-detail/{homework_id}?routeName=Exams"
    print(f"Opening homework in browser: {homework_url}")
    
    # Open the URL in the default browser
    webbrowser.open(homework_url)
else:
    print("Failed to create homework.")
    print("Status Code:", response_create_homework.status_code)
    print("Response:", response_create_homework.text)


      