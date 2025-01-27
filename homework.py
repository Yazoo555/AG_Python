import requests
from datetime import datetime, timedelta
import webbrowser
import random
import sys

from auth import get_auth_token

homeworkType = sys.argv[0] # it's either start or end

if len(sys.argv) < 2 or sys.argv[1] not in ['start', 'end']:
    print("Error: The argument must be 'start' or 'end'.")
    sys.exit(1)  # Exit the program if invalid argument



# API URL for creating homework
url_create_homework = "https://api-adm.ambition.guru/api/v1/admin/exams"

# User input for homework title
user_title = input("Please enter the title for the Homework: ")

# Dynamic timestamps for the homework
if sys.argv[1] == 'start':
    current_datetime = datetime.now()
    start_time = (current_datetime).strftime("%Y-%m-%d %H:%M:%S")
    end_time = (current_datetime + timedelta(days=2)).strftime("%Y-%m-%d %H:%M:%S")
#published_at = current_datetime.strftime("%Y-%m-%d %H:%M:%S")  # Use the current time for published_at


elif  sys.argv[1] == 'end':
    current_datetime = datetime.now()  # Get the current date and time
    start_time = (current_datetime - timedelta(days=2)).strftime("%Y-%m-%d %H:%M:%S")  # 2 days before the current time
    end_time = current_datetime.strftime("%Y-%m-%d %H:%M:%S")  # Current time

# Headers for API request
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:132.0) Gecko/20100101 Firefox/132.0",
    "Accept": "application/json, text/plain, */*",
    "Content-Type": "application/json",
    "Authorization": f"Bearer {get_auth_token()}",
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
   # "duration": 10,
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
    {
      "id": 143997,
      "body": "<p><strong><span style=\"font-size: 10pt\">2)</span><span style=\"font-size: 8pt\"> </span><span style=\"font-size: 9pt\">सत्यनारायण गुरुले</span><span style=\"font-size: 11pt\"> </span><span style=\"font-size: 10pt\">एउटा औद्योगिक जग्गा रु. १,६०,००,००० मा र एउटा प्रिन्टिङ मेसिन रु. ५,४०,००,००० मा किन्नुभएको छ। जग्गाको मूल्य प्रतिवर्ष २० % ले वृद्धि हुन्छ भने मेसिनको मूल्य प्रतिवर्ष २०% ले घट्छ, दुवै परिवर्तन वार्षिक चक्रिय रूपमा</span>&nbsp; हुन्छ। <span style=\"font-size: 10pt\">Satyanarayan Guru bought an industrial plot for Rs.16000000 </span>&nbsp;and a printing machine for Rs <span style=\"font-size: 10pt\">.54000000. The land's value increases by20% </span>&nbsp;per annum, while the machine's value decreases by &nbsp;20% per annum and both changes compounded annually.<br>&nbsp;a)सुरुको जनसङ्ख्या Po, वार्षिक जनसङ्ख्या वृद्धिदर R% र वार्षिक &nbsp;&nbsp;जनसङ्ख्या ह्रासदर&nbsp; D% भएमा सो सहरको T वर्षपछिको जनसङ्ख्या निकाल्ने सूत्र दुवै लेख्नुहोस् ।</strong><span style=\"font-size: 8pt\"> </span><strong><span style=\"font-size: 10pt\">If the initial population is </span>Po<span style=\"font-size: 10pt\"> the annual population growth rate is R% and the annual population decline rate is D%, write down the formulas to find the population of the city after T years.</span></strong></p><p><strong><span style=\"font-size: 10pt\">(b) दुई वर्षपछि जग्गाको मूल्य कति हुन्छ? Calculate the value of the land two years later.<br>(c) दुई वर्षपछि मेसिनको मूल्य कति हुन्छ? Determine the value of the machine two years later.<br>(d) कति वर्षपछि जग्गाको मूल्य र मेसिनको मूल्य बराबर हुन्छ? Estimate the number of years until the value of the land equals the value of the machine.</span></strong></p><p><strong><span style=\"font-size: 10pt\">&nbsp;</span></strong></p>",
      "pivot_id": 267203,
      "marks": 1,
      "order": 18,
      "extras": {
        "unit": {
          "id": 11543,
          "name": "चक्रीय ब्याज",
          "type": "Unit",
          "marks": 1,
          "parent_id": 11520,
          "thumbnail": None,
          "children_count": 2,
          "ancestors_and_self": [
            {
              "id": 11543,
              "name": "चक्रीय ब्याज",
              "path": "11543",
              "rank": 1,
              "type": "Unit",
              "depth": 0,
              "marks": 1,
              "extras": None,
              "status": 1,
              "admin_id": None,
              "overview": "<p></p><p></p>",
              "causer_id": None,
              "course_id": 80,
              "parent_id": 11520,
              "created_at": "2023-12-06T09:03:02.000000Z",
              "deleted_at": None,
              "updated_at": "2024-12-03T10:00:03.000000Z",
              "causer_type": None,
              "guru_org_id": 177,
              "descriptions": None
            },
            {
              "id": 11520,
              "name": "गणित",
              "path": "11543.11520",
              "rank": 6,
              "type": "Subject",
              "depth": -1,
              "marks": 1,
              "extras": None,
              "status": 1,
              "admin_id": None,
              "overview": None,
              "causer_id": None,
              "course_id": 80,
              "parent_id": None,
              "created_at": "2023-12-05T11:24:12.000000Z",
              "deleted_at": None,
              "updated_at": "2024-11-27T10:23:49.000000Z",
              "causer_type": None,
              "guru_org_id": 31,
              "descriptions": None
            }
          ]
        },
        "chapter": {
          "id": 11544,
          "name": "चक्रीय ब्याज (Basic)",
          "type": "Chapter",
          "marks": 1,
          "parent_id": 11543,
          "ancestors_and_self": []
        },
        "subject": {
          "id": 11520,
          "name": "गणित",
          "type": "Subject",
          "course": {
            "id": 80,
            "name": "SEE (Grade 10)",
            "rank": 0,
            "type": "ACADEMIC",
            "status": 1,
            "created_at": "2023-10-09T05:54:00.000000Z",
            "category_id": 45
          },
          "course_id": 80,
          "parent_id": None,
          "hasChildren": True,
          "hasCustomSyllabus": False
        },
        "subject_type": "Subject"
      },
      "answers": [],
      "correct_answer": None,
      "section_id": None
    },

    {
      "id": 141503,
      "body": "<p>एउटा माध्यमिक विद्यालयको कक्षा 10 मा अध्ययनरत 120 जना विद्यार्थीहरूको समूहमा सर्वेक्षण गर्दा 60 जनाले क्रिकेट खेल मन पराएका, 55 जनाले वास्केटबल खेल मन पराएको र 20 जनाले दुवै खेल मध्ये कुनै पनि मन नपराएको पाइयो <br>In survey conducted among 120 students studying in class 10 of a secondary school, it was found that 60 students liked cricket game, 55 students liked basketball game and 20 students did not like any of two games.</p><p>(क) यदि 𝐂 र 𝐁 ले क्रमश: क्रिकेट र बास्केटबल खेल मन पराउने विद्यार्थीहरूको समूहहरूलाई जनाउँछ भने 𝒏((𝑩∪𝑪) ̅) को गणनात्मकता लेख्नुहोस् ।</p><p> If 𝐂 and 𝐁 denote the sets of students who liked cricket and basketball game respectively, write the cardinality of 𝒏((𝑩∪𝑪) ̅).</p><p>(ख) माथिको जानकारीलाई भेन चित्रमा प्रस्तुत गर्नुहोस् ।</p><p>Present the above information in a Venn-diagram.</p><p>(ग) क्रिकेटमात्र मन पराउने विद्यार्थीहरूको सड्ख्या पत्ता लगाउनुहोस् ।</p><p>Find the number of students who liked cricket only.</p><p>(घ) क्रिकेट र वास्केट बल दुवै खेल मन पराउने र यी दुई बाहेक अन्य खेल मन पराउने विद्यार्थीहरूको सड्ख्या बिच तुलना गर्नुहोस् । Compare the number of students who liked both cricket and basket ball and who liked except these two games.</p>",
      "pivot_id": 267190,
      "marks": 1,
      "order": 16,
      "extras": {
        "unit": {
          "id": 11522,
          "name": "समुह",
          "type": "Unit",
          "marks": 1,
          "parent_id": 11520,
          "thumbnail": None,
          "children_count": 2,
          "ancestors_and_self": [
            {
              "id": 11522,
              "name": "समुह",
              "path": "11522",
              "rank": 0,
              "type": "Unit",
              "depth": 0,
              "marks": 1,
              "extras": None,
              "status": 1,
              "admin_id": None,
              "overview": None,
              "causer_id": None,
              "course_id": 80,
              "parent_id": 11520,
              "created_at": "2023-12-06T05:45:34.000000Z",
              "deleted_at": None,
              "updated_at": "2024-12-03T09:59:28.000000Z",
              "causer_type": None,
              "guru_org_id": 46,
              "descriptions": None
            },
            {
              "id": 11520,
              "name": "गणित",
              "path": "11522.11520",
              "rank": 6,
              "type": "Subject",
              "depth": -1,
              "marks": 1,
              "extras": None,
              "status": 1,
              "admin_id": None,
              "overview": None,
              "causer_id": None,
              "course_id": 80,
              "parent_id": None,
              "created_at": "2023-12-05T11:24:12.000000Z",
              "deleted_at": None,
              "updated_at": "2024-11-27T10:23:49.000000Z",
              "causer_type": None,
              "guru_org_id": 31,
              "descriptions": None
            }
          ]
        },
        "chapter": {
          "id": 11523,
          "name": "समुह (Basic)",
          "type": "Chapter",
          "marks": 1,
          "parent_id": 11522,
          "ancestors_and_self": []
        },
        "subject": {
          "id": 11520,
          "name": "गणित",
          "type": "Subject",
          "course": {
            "id": 80,
            "name": "SEE (Grade 10)",
            "rank": 0,
            "type": "ACADEMIC",
            "status": 1,
            "created_at": "2023-10-09T05:54:00.000000Z",
            "category_id": 45
          },
          "course_id": 80,
          "parent_id": None,
          "hasChildren": True,
          "hasCustomSyllabus": False
        },
        "subject_type": "Subject"
      },
      "answers": [],
      "correct_answer": None,
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
    webbrowser.open(homework_url)

    # Lock the questions for the created homework
    url_lock_questions = f"https://api-adm.ambition.guru/api/v1/admin/exams/{homework_id}/lock-questions"
    response_lock_questions = requests.post(url_lock_questions, headers=headers)

    # Check if the locking was successful
    if response_lock_questions.status_code == 200:
        print(f"Questions locked successfully for Homework ID: {homework_id}")
    else:
        print("Failed to lock questions.")
        print("Status Code:", response_lock_questions.status_code)
        print("Response:", response_lock_questions.text)

else:
    print("Failed to create homework.")
    print("Status Code:", response_create_homework.status_code)
    print("Response:", response_create_homework.text)


      # Print some information about the selected questions
print(f"\nTotal questions selected: {len(data_create_homework['questions'])}")
print("Sample of selected questions:")
for i, q in enumerate(data_create_homework['questions'][:3]):
    print(f"Question {i + 1}: {q['body'][:100]}...")