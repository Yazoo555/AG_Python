import requests
from datetime import datetime, timedelta
import webbrowser
import random
import logging

from auth import get_auth_token

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('homework_creator.log')
    ]
)

# API URL for creating homework
url_create_homework = "https://api-adm.ambition.guru/api/v1/admin/exams"

# User input for homework title
user_title = input("Please enter the title for the Homework: ")

# Dynamic timestamps for the homework
current_datetime = datetime.now()
start_time = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
end_time = (current_datetime + timedelta(days=2)).strftime("%Y-%m-%d %H:%M:%S")

# Headers for API request
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:132.0) Gecko/20100101 Firefox/132.0",
    "Accept": "application/json, text/plain, */*",
    "Content-Type": "application/json",
    "Authorization": f"Bearer {get_auth_token()}",
}

# All available questions
questions = [
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
        "body": "<p><strong><span style=\"font-size: 10pt\">2)</span><span style=\"font-size: 8pt\"> </span><span style=\"font-size: 9pt\">सत्यनारायण गुरुले</span><span style=\"font-size: 11pt\"> </span><span style=\"font-size: 10pt\">एउटा औद्योगिक जग्गा रु. १,६०,००,००० मा र एउटा प्रिन्टिङ मेसिन रु. ५,४०,००,००० मा किन्नुभएको छ। जग्गाको मूल्य प्रतिवर्ष २० % ले वृद्धि हुन्छ भने मेसिनको मूल्य प्रतिवर्ष २०% ले घट्छ, दुवै परिवर्तन वार्षिक चक्रिय रूपमा</span>&nbsp; हुन्छ। <span style=\"font-size: 10pt\">Satyanarayan Guru bought an industrial plot for Rs.16000000 </span>&nbsp;and a printing machine for Rs <span style=\"font-size: 10pt\">.54000000. The land's value increases by20% </span>&nbsp;per annum, while the machine's value decreases by &nbsp;20% per annum and both changes compounded annually.</p>",
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
                        "marks": 1
                    },
                    {
                        "id": 11520,
                        "name": "गणित",
                        "path": "11543.11520",
                        "rank": 6,
                        "type": "Subject",
                        "depth": -1,
                        "marks": 1
                    }
                ]
            },
            "chapter": {
                "id": 11544,
                "name": "चक्रीय ब्याज (Basic)",
                "type": "Chapter",
                "marks": 1,
                "parent_id": 11543
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
        "section_id": None
    },
    {
        "id": 141503,
        "body": "<p>एउटा माध्यमिक विद्यालयको कक्षा 10 मा अध्ययनरत 120 जना विद्यार्थीहरूको समूहमा सर्वेक्षण गर्दा 60 जनाले क्रिकेट खेल मन पराएका, 55 जनाले वास्केटबल खेल मन पराएको र 20 जनाले दुवै खेल मध्ये कुनै पनि मन नपराएको पाइयो</p>",
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
                        "marks": 1
                    },
                    {
                        "id": 11520,
                        "name": "गणित",
                        "path": "11522.11520",
                        "rank": 6,
                        "type": "Subject",
                        "depth": -1,
                        "marks": 1
                    }
                ]
            },
            "chapter": {
                "id": 11523,
                "name": "समुह (Basic)",
                "type": "Chapter",
                "marks": 1,
                "parent_id": 11522
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
        "section_id": None
    }
]

def get_random_questions():
    """
    Select and randomize questions from different types.
    Returns a list of randomly selected questions.
    """
    if len(questions) < 25:
        logging.warning(f"Only {len(questions)} questions available. This may affect distribution.")
    
    # Create copies for manipulation
    available_questions = questions.copy()
    random.shuffle(available_questions)
    
    # Create 5 types
    num_types = 5
    questions_per_type = [[] for _ in range(num_types)]
    
    # Distribute questions among types
    for i, question in enumerate(available_questions):
        type_index = i % num_types
        questions_per_type[type_index].append(question)
    
    # Select questions from each type
    selected_questions = []
    for type_questions in questions_per_type:
        if type_questions:  # Only select if we have questions of this type
            num_to_select = random.randint(5, 6)
            num_to_select = min(num_to_select, len(type_questions))
            selected = random.sample(type_questions, num_to_select)
            selected_questions.extend(selected)
    
    # Final shuffle and order update
    random.shuffle(selected_questions)
    for i, question in enumerate(selected_questions, 1):
        question['order'] = i
    
    logging.info(f"Selected {len(selected_questions)} questions")
    return selected_questions

def create_homework_data():
    """
    Create the homework data structure with randomly selected questions.
    """
    return {
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
        "questions": get_random_questions()
    }

def create_homework():
    """
    Create homework by sending POST request to the API.
    Returns the API response data.
    """
    try:
        homework_data = create_homework_data()
        response = requests.post(url_create_homework, headers=headers, json=homework_data)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"Failed to create homework: {str(e)}")
        return None

def lock_questions(homework_id):
    """
    Lock the questions for a given homework ID.
    Returns True if successful, False otherwise.
    """
    try:
        url_lock_questions = f"https://api-adm.ambition.guru/api/v1/admin/exams/{homework_id}/lock-questions"
        response = requests.post(url_lock_questions, headers=headers)
        response.raise_for_status()
        return True
    except requests.RequestException as e:
        logging.error(f"Failed to lock questions: {str(e)}")
        return False

def main():
    """
    Main function to orchestrate the homework creation process.
    """
    try:
        logging.info("Starting homework creation process")
        logging.info(f"Creating homework with title: {user_title}")
        
        # Create homework
        response_data = create_homework()
        if not response_data:
            logging.error("Failed to create homework")
            return
        
        # Get homework ID from response
        homework_id = response_data.get("data", {}).get("id")
        if not homework_id:
            logging.error("Failed to get homework ID from response")
            return
        
        logging.info(f"Homework created successfully! ID: {homework_id}")
        
        # Open homework in browser
        homework_url = f"https://admin.ambition.guru/exams/mock-test-detail/{homework_id}?routeName=Exams"
        logging.info(f"Opening homework in browser: {homework_url}")
        webbrowser.open(homework_url)
        
        # Lock questions
        if lock_questions(homework_id):
            logging.info(f"Questions locked successfully for Homework ID: {homework_id}")
        else:
            logging.error("Failed to lock questions")
        
        logging.info("Homework creation process completed")
        
    except Exception as e:
        logging.error(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()