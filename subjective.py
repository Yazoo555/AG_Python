import requests
from datetime import datetime, timedelta
import webbrowser
import time



# Endpoint URL
url_create_exam = "https://api-adm.ambition.guru/api/v1/admin/exams"
user_title = input("Please enter the title for the exam: ")


headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:133.0) Gecko/20100101 Firefox/133.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Content-Type': 'application/json',
    'Referer': 'https://admin.ambition.guru/',
    'X-Requested-With': 'XMLHttpRequest',
    'Origin': 'https://admin.ambition.guru',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiNmVkNmVhNDFkODFmY2JkM2UzYTQ0OWI3ZWY0YjQ0ZGQ3MjIzYzllZTRlNTkxNWZiZTJmYTVjZmVjNGFlYjA3MzVhYjQ4ZmNlYjY3ZjY0Y2QiLCJpYXQiOjE3MzUxMDc2OTguMjY1NjM4LCJuYmYiOjE3MzUxMDc2OTguMjY1NjQxLCJleHAiOjE3MzU3MTI0OTguMjU3NTA1LCJzdWIiOiI4MSIsInNjb3BlcyI6WyJhZG1pbiJdfQ.r4PnLM_v18EbmLG0SKmiF7DEhT4O2-DXMF089Ee7Ub-qP2Pr80-KJ_PCUEqG3jKE67JhxZ96vvt7g04bX6u2cyU1nts_vM5yWvM_A20e3mmeM7066xvh9FmkXfLxPxgpcMd0mrJn2YLp-0_rZ8KZQXQXcE1Nqzi0vX2Own2QpD_yHxk9ILW-757NLVYiXI32oi3enoYjjfDlKJxZfC2q-5W7p8qNtC-BHy-V6VvqUhIF0u3v0FEEH4npUD0P80ixg0dgnSFIUxcgI_wdhkHrrp4wMHHnwCKQ8DOOpVp13wo0_EREWTVYL6kkgqjFsjUkKmcfVpmiY7HyGxb1bTp5VxX676_vS0gs9BsJJ8v9f1AxxB44X1ZnPdeWNRESHM_qJ0OeH_EoryfZCvecHJ2Ul2BDjMdw9kVJ0dnjj5LeuXO9oSv5OrZywulL5VWsL4UeIAYZXxZoMenCY7PzgucZsFCEyS0cptJmROIddz0oUsiosLn23XE-eeTL3SXbaspF1pyhRdQYH3Kza6aKEG7b0MogAXNFYPTmn7mB4LibIm0zEtul1P3geXS1geF57cmOwuG4VDvNY6a0n0QWNNeSwCvWta7jA7zugy_QFkLcqGpmZPbGZoin7k_8Aiq4aS7HTlLLnrNptiVajV5TvrgFasiGiiw02RCI-h1GenPCb0Q",
    'Connection': 'keep-alive',
    'Priority': 'u=0',
}

# Current date and time for dynamic fields
current_datetime = datetime.now()

# Adjust times dynamically
start_time = (current_datetime + timedelta(minutes=5)).strftime("%Y-%m-%d %H:%M:%S")
registration_deadline = start_time
published_at = (current_datetime + timedelta(minutes=10)).strftime("%Y-%m-%d %H:%M:%S")

# Ask user if the test is free or paid
is_free_input = input("Is the test free? (yes/no): ").strip().lower()

if is_free_input == "yes":
    is_free = 1
    price = 0
else:
    is_free = 0
    price = float(input("Enter the price for the paid test: ").strip())

# Payload
data_create_exam= {
    'guard_name': 'admin-api',
    'join_in_middle': 1,
    'allow_answer_change': 1,
    'send_notification': 0,
    'is_featured': 0,
    'is_criteria': 0,
    'is_active': 0,
    'status': 1,
    'is_free': is_free,
    'price': price,
    'exam_setup_type': 1,
    'marks': 10,
    'duration': '15',
    'negative_marking': '0.25',
    'start_time': start_time,
    'registration_deadline': registration_deadline,
    'questions': [
        {
            'body': '<p>शिक्षक भर्ना भनेको के हो ? नेपालमा शिक्षक भर्ना छनौट तथा नियुक्तिमा देखिएका समस्याहरू लेख्नुहोस् । (१+४)</p>',
            'id': 115904,
            'order': 14,
            'marks': 1,
            'extras': {
                'subject': {
                    'id': 19893,
                    'name': 'Mental Agility Test (MAT)',
                    'parent_id': None,
                    'type': 'Subject',
                    'course_id': 150,
                    'course': {
                        'id': 150,
                        'name': 'CEE NewCourse',
                        'category_id': 27,
                        'status': 1,
                        'type': 'ACADEMIC',
                        'created_at': '2024-05-02T08:32:21.000000Z',
                        'rank': 0,
                    },
                    'hasCustomSyllabus': False,
                    'hasChildren': True,
                },
                'unit': {
                    'id': 20329,
                    'name': 'Feedback Session',
                    'parent_id': 19893,
                    'type': 'Unit',
                    'marks': 1,
                    'children_count': 1,
                    'thumbnail': None,
                    'ancestors_and_self': [
                        {
                            'id': 20329,
                            'name': 'Feedback Session',
                            'parent_id': 19893,
                            'type': 'Unit',
                            'course_id': 150,
                            'admin_id': None,
                            'guru_org_id': 46,
                            'status': 1,
                            'extras': None,
                            'descriptions': None,
                            'rank': 0,
                            'created_at': '2024-05-07T10:14:03.000000Z',
                            'updated_at': '2024-05-07T10:14:03.000000Z',
                            'deleted_at': None,
                            'marks': 1,
                            'overview': '<p> </p>',
                            'causer_type': None,
                            'causer_id': None,
                            'depth': 0,
                            'path': '20329',
                        },
                        {
                            'id': 19893,
                            'name': 'Mental Agility Test (MAT)',
                            'parent_id': None,
                            'type': 'Subject',
                            'course_id': 150,
                            'admin_id': None,
                            'guru_org_id': 46,
                            'status': 1,
                            'extras': None,
                            'descriptions': None,
                            'rank': 0,
                            'created_at': '2024-05-02T08:51:03.000000Z',
                            'updated_at': '2024-06-21T10:38:01.000000Z',
                            'deleted_at': None,
                            'marks': 80,
                            'overview': '<p> </p>',
                            'causer_type': None,
                            'causer_id': None,
                            'depth': -1,
                            'path': '20329.19893',
                        },
                    ],
                },
                'chapter': {
                    'id': 20330,
                    'name': 'Feedback Session',
                    'marks': 1,
                    'parent_id': 20329,
                    'type': 'Chapter',
                    'ancestors_and_self': {},
                },
                'subject_type': 'Subject',
            },
            'section_id': None,
        },
        {
            'body': '<p>शिक्षक बढुवा भनेको के हो ? यसका उद्देश्यहरू उल्लेख गर्नुहोस् । (२+३)</p>',
            'id': 115903,
            'order': 13,
            'marks': 1,
            'extras': {
                'subject': {
                    'id': 19893,
                    'name': 'Mental Agility Test (MAT)',
                    'parent_id': None,
                    'type': 'Subject',
                    'course_id': 150,
                    'course': {
                        'id': 150,
                        'name': 'CEE NewCourse',
                        'category_id': 27,
                        'status': 1,
                        'type': 'ACADEMIC',
                        'created_at': '2024-05-02T08:32:21.000000Z',
                        'rank': 0,
                    },
                    'hasCustomSyllabus': False,
                    'hasChildren': True,
                },
                'unit': {
                    'id': 20329,
                    'name': 'Feedback Session',
                    'parent_id': 19893,
                    'type': 'Unit',
                    'marks': 1,
                    'children_count': 1,
                    'thumbnail': None,
                    'ancestors_and_self': [
                        {
                            'id': 20329,
                            'name': 'Feedback Session',
                            'parent_id': 19893,
                            'type': 'Unit',
                            'course_id': 150,
                            'admin_id': None,
                            'guru_org_id': 46,
                            'status': 1,
                            'extras': None,
                            'descriptions': None,
                            'rank': 0,
                            'created_at': '2024-05-07T10:14:03.000000Z',
                            'updated_at': '2024-05-07T10:14:03.000000Z',
                            'deleted_at': None,
                            'marks': 1,
                            'overview': '<p> </p>',
                            'causer_type': None,
                            'causer_id': None,
                            'depth': 0,
                            'path': '20329',
                        },
                        {
                            'id': 19893,
                            'name': 'Mental Agility Test (MAT)',
                            'parent_id': None,
                            'type': 'Subject',
                            'course_id': 150,
                            'admin_id': None,
                            'guru_org_id': 46,
                            'status': 1,
                            'extras': None,
                            'descriptions': None,
                            'rank': 0,
                            'created_at': '2024-05-02T08:51:03.000000Z',
                            'updated_at': '2024-06-21T10:38:01.000000Z',
                            'deleted_at': None,
                            'marks': 80,
                            'overview': '<p> </p>',
                            'causer_type': None,
                            'causer_id': None,
                            'depth': -1,
                            'path': '20329.19893',
                        },
                    ],
                },
                'chapter': {
                    'id': 20330,
                    'name': 'Feedback Session',
                    'marks': 1,
                    'parent_id': 20329,
                    'type': 'Chapter',
                    'ancestors_and_self': {},
                },
                'subject_type': 'Subject',
            },
            'section_id': None,
        },
        {
            'body': '<p>नेपालमा शिक्षकको पेसागत विकासको सम्बन्धमा भएका नीतिगत, संरचनागत एवम् कार्यक्रमगत प्रावधानहरूको चर्चा गर्नुहोस् ।</p>',
            'id': 115902,
            'order': 12,
            'marks': 1,
            'extras': {
                'subject': {
                    'id': 19893,
                    'name': 'Mental Agility Test (MAT)',
                    'parent_id': None,
                    'type': 'Subject',
                    'course_id': 150,
                    'course': {
                        'id': 150,
                        'name': 'CEE NewCourse',
                        'category_id': 27,
                        'status': 1,
                        'type': 'ACADEMIC',
                        'created_at': '2024-05-02T08:32:21.000000Z',
                        'rank': 0,
                    },
                    'hasCustomSyllabus': False,
                    'hasChildren': True,
                },
                'unit': {
                    'id': 20329,
                    'name': 'Feedback Session',
                    'parent_id': 19893,
                    'type': 'Unit',
                    'marks': 1,
                    'children_count': 1,
                    'thumbnail': None,
                    'ancestors_and_self': [
                        {
                            'id': 20329,
                            'name': 'Feedback Session',
                            'parent_id': 19893,
                            'type': 'Unit',
                            'course_id': 150,
                            'admin_id': None,
                            'guru_org_id': 46,
                            'status': 1,
                            'extras': None,
                            'descriptions': None,
                            'rank': 0,
                            'created_at': '2024-05-07T10:14:03.000000Z',
                            'updated_at': '2024-05-07T10:14:03.000000Z',
                            'deleted_at': None,
                            'marks': 1,
                            'overview': '<p> </p>',
                            'causer_type': None,
                            'causer_id': None,
                            'depth': 0,
                            'path': '20329',
                        },
                        {
                            'id': 19893,
                            'name': 'Mental Agility Test (MAT)',
                            'parent_id': None,
                            'type': 'Subject',
                            'course_id': 150,
                            'admin_id': None,
                            'guru_org_id': 46,
                            'status': 1,
                            'extras': None,
                            'descriptions': None,
                            'rank': 0,
                            'created_at': '2024-05-02T08:51:03.000000Z',
                            'updated_at': '2024-06-21T10:38:01.000000Z',
                            'deleted_at': None,
                            'marks': 80,
                            'overview': '<p> </p>',
                            'causer_type': None,
                            'causer_id': None,
                            'depth': -1,
                            'path': '20329.19893',
                        },
                    ],
                },
                'chapter': {
                    'id': 20330,
                    'name': 'Feedback Session',
                    'marks': 1,
                    'parent_id': 20329,
                    'type': 'Chapter',
                    'ancestors_and_self': {},
                },
                'subject_type': 'Subject',
            },
            'section_id': None,
        },
        {
            'body': '<p>शिक्षकको गुणस्तर एवम् प्रभावकारिताको बारेमा छोटकरीमा चर्चा गर्नुहोस् ।(२.५+२.५)</p>',
            'id': 115901,
            'order': 11,
            'marks': 1,
            'extras': {
                'subject': {
                    'id': 19893,
                    'name': 'Mental Agility Test (MAT)',
                    'parent_id': None,
                    'type': 'Subject',
                    'course_id': 150,
                    'course': {
                        'id': 150,
                        'name': 'CEE NewCourse',
                        'category_id': 27,
                        'status': 1,
                        'type': 'ACADEMIC',
                        'created_at': '2024-05-02T08:32:21.000000Z',
                        'rank': 0,
                    },
                    'hasCustomSyllabus': False,
                    'hasChildren': True,
                },
                'unit': {
                    'id': 20329,
                    'name': 'Feedback Session',
                    'parent_id': 19893,
                    'type': 'Unit',
                    'marks': 1,
                    'children_count': 1,
                    'thumbnail': None,
                    'ancestors_and_self': [
                        {
                            'id': 20329,
                            'name': 'Feedback Session',
                            'parent_id': 19893,
                            'type': 'Unit',
                            'course_id': 150,
                            'admin_id': None,
                            'guru_org_id': 46,
                            'status': 1,
                            'extras': None,
                            'descriptions': None,
                            'rank': 0,
                            'created_at': '2024-05-07T10:14:03.000000Z',
                            'updated_at': '2024-05-07T10:14:03.000000Z',
                            'deleted_at': None,
                            'marks': 1,
                            'overview': '<p> </p>',
                            'causer_type': None,
                            'causer_id': None,
                            'depth': 0,
                            'path': '20329',
                        },
                        {
                            'id': 19893,
                            'name': 'Mental Agility Test (MAT)',
                            'parent_id': None,
                            'type': 'Subject',
                            'course_id': 150,
                            'admin_id': None,
                            'guru_org_id': 46,
                            'status': 1,
                            'extras': None,
                            'descriptions': None,
                            'rank': 0,
                            'created_at': '2024-05-02T08:51:03.000000Z',
                            'updated_at': '2024-06-21T10:38:01.000000Z',
                            'deleted_at': None,
                            'marks': 80,
                            'overview': '<p> </p>',
                            'causer_type': None,
                            'causer_id': None,
                            'depth': -1,
                            'path': '20329.19893',
                        },
                    ],
                },
                'chapter': {
                    'id': 20330,
                    'name': 'Feedback Session',
                    'marks': 1,
                    'parent_id': 20329,
                    'type': 'Chapter',
                    'ancestors_and_self': {},
                },
                'subject_type': 'Subject',
            },
            'section_id': None,
        },
        {
            'body': '<p>अध्यापन अनुमति पत्रको अवधारणा प्रस्तुत गर्दै यसको आवश्यकता दर्साउनुहोस्। साथै नेपालमा अध्यापन अनुमति पत्रको सम्बन्धमा देखिएका समस्याहरू उल्लेख गर्नुहोस् । (२+४+४)</p>',
            'id': 115905,
            'order': 15,
            'marks': 1,
            'extras': {
                'subject': {
                    'id': 19893,
                    'name': 'Mental Agility Test (MAT)',
                    'parent_id': None,
                    'type': 'Subject',
                    'course_id': 150,
                    'course': {
                        'id': 150,
                        'name': 'CEE NewCourse',
                        'category_id': 27,
                        'status': 1,
                        'type': 'ACADEMIC',
                        'created_at': '2024-05-02T08:32:21.000000Z',
                        'rank': 0,
                    },
                    'hasCustomSyllabus': False,
                    'hasChildren': True,
                },
                'unit': {
                    'id': 20329,
                    'name': 'Feedback Session',
                    'parent_id': 19893,
                    'type': 'Unit',
                    'marks': 1,
                    'children_count': 1,
                    'thumbnail': None,
                    'ancestors_and_self': [
                        {
                            'id': 20329,
                            'name': 'Feedback Session',
                            'parent_id': 19893,
                            'type': 'Unit',
                            'course_id': 150,
                            'admin_id': None,
                            'guru_org_id': 46,
                            'status': 1,
                            'extras': None,
                            'descriptions': None,
                            'rank': 0,
                            'created_at': '2024-05-07T10:14:03.000000Z',
                            'updated_at': '2024-05-07T10:14:03.000000Z',
                            'deleted_at': None,
                            'marks': 1,
                            'overview': '<p> </p>',
                            'causer_type': None,
                            'causer_id': None,
                            'depth': 0,
                            'path': '20329',
                        },
                        {
                            'id': 19893,
                            'name': 'Mental Agility Test (MAT)',
                            'parent_id': None,
                            'type': 'Subject',
                            'course_id': 150,
                            'admin_id': None,
                            'guru_org_id': 46,
                            'status': 1,
                            'extras': None,
                            'descriptions': None,
                            'rank': 0,
                            'created_at': '2024-05-02T08:51:03.000000Z',
                            'updated_at': '2024-06-21T10:38:01.000000Z',
                            'deleted_at': None,
                            'marks': 80,
                            'overview': '<p> </p>',
                            'causer_type': None,
                            'causer_id': None,
                            'depth': -1,
                            'path': '20329.19893',
                        },
                    ],
                },
                'chapter': {
                    'id': 20330,
                    'name': 'Feedback Session',
                    'marks': 1,
                    'parent_id': 20329,
                    'type': 'Chapter',
                    'ancestors_and_self': {},
                },
                'subject_type': 'Subject',
            },
            'section_id': None,
        },
        {
            'body': '<p>शिक्षक सक्षमताको प्रारूप २०७२ अनुसारको शिक्षकको सक्षमताहरूको छोटकरीमा चर्चा गर्दै सो प्रारूप कार्यान्वयनमा देखिएका चुनौतीहरू औँल्याउनुहोस् । (६+४)</p>',
            'id': 115906,
            'order': 16,
            'marks': 1,
            'extras': {
                'subject': {
                    'id': 19893,
                    'name': 'Mental Agility Test (MAT)',
                    'parent_id': None,
                    'type': 'Subject',
                    'course_id': 150,
                    'course': {
                        'id': 150,
                        'name': 'CEE NewCourse',
                        'category_id': 27,
                        'status': 1,
                        'type': 'ACADEMIC',
                        'created_at': '2024-05-02T08:32:21.000000Z',
                        'rank': 0,
                    },
                    'hasCustomSyllabus': False,
                    'hasChildren': True,
                },
                'unit': {
                    'id': 20329,
                    'name': 'Feedback Session',
                    'parent_id': 19893,
                    'type': 'Unit',
                    'marks': 1,
                    'children_count': 1,
                    'thumbnail': None,
                    'ancestors_and_self': [
                        {
                            'id': 20329,
                            'name': 'Feedback Session',
                            'parent_id': 19893,
                            'type': 'Unit',
                            'course_id': 150,
                            'admin_id': None,
                            'guru_org_id': 46,
                            'status': 1,
                            'extras': None,
                            'descriptions': None,
                            'rank': 0,
                            'created_at': '2024-05-07T10:14:03.000000Z',
                            'updated_at': '2024-05-07T10:14:03.000000Z',
                            'deleted_at': None,
                            'marks': 1,
                            'overview': '<p> </p>',
                            'causer_type': None,
                            'causer_id': None,
                            'depth': 0,
                            'path': '20329',
                        },
                        {
                            'id': 19893,
                            'name': 'Mental Agility Test (MAT)',
                            'parent_id': None,
                            'type': 'Subject',
                            'course_id': 150,
                            'admin_id': None,
                            'guru_org_id': 46,
                            'status': 1,
                            'extras': None,
                            'descriptions': None,
                            'rank': 0,
                            'created_at': '2024-05-02T08:51:03.000000Z',
                            'updated_at': '2024-06-21T10:38:01.000000Z',
                            'deleted_at': None,
                            'marks': 80,
                            'overview': '<p> </p>',
                            'causer_type': None,
                            'causer_id': None,
                            'depth': -1,
                            'path': '20329.19893',
                        },
                    ],
                },
                'chapter': {
                    'id': 20330,
                    'name': 'Feedback Session',
                    'marks': 1,
                    'parent_id': 20329,
                    'type': 'Chapter',
                    'ancestors_and_self': {},
                },
                'subject_type': 'Subject',
            },
            'section_id': None,
        },
        {
            'body': '<p>शिक्षक व्यवस्थापनको अवधारणा प्रस्तुत गर्दै यसको महत्त्व उल्लेख गर्नुहोस् । साथै नेपालको सन्दर्भमा शिक्षक व्यवस्थापनमा देखिएका समस्याहरू औँल्याउनुहोस् । (२+३+५)</p>',
            'id': 115907,
            'order': 17,
            'marks': 1,
            'extras': {
                'subject': {
                    'id': 19893,
                    'name': 'Mental Agility Test (MAT)',
                    'parent_id': None,
                    'type': 'Subject',
                    'course_id': 150,
                    'course': {
                        'id': 150,
                        'name': 'CEE NewCourse',
                        'category_id': 27,
                        'status': 1,
                        'type': 'ACADEMIC',
                        'created_at': '2024-05-02T08:32:21.000000Z',
                        'rank': 0,
                    },
                    'hasCustomSyllabus': False,
                    'hasChildren': True,
                },
                'unit': {
                    'id': 20329,
                    'name': 'Feedback Session',
                    'parent_id': 19893,
                    'type': 'Unit',
                    'marks': 1,
                    'children_count': 1,
                    'thumbnail': None,
                    'ancestors_and_self': [
                        {
                            'id': 20329,
                            'name': 'Feedback Session',
                            'parent_id': 19893,
                            'type': 'Unit',
                            'course_id': 150,
                            'admin_id': None,
                            'guru_org_id': 46,
                            'status': 1,
                            'extras': None,
                            'descriptions': None,
                            'rank': 0,
                            'created_at': '2024-05-07T10:14:03.000000Z',
                            'updated_at': '2024-05-07T10:14:03.000000Z',
                            'deleted_at': None,
                            'marks': 1,
                            'overview': '<p> </p>',
                            'causer_type': None,
                            'causer_id': None,
                            'depth': 0,
                            'path': '20329',
                        },
                        {
                            'id': 19893,
                            'name': 'Mental Agility Test (MAT)',
                            'parent_id': None,
                            'type': 'Subject',
                            'course_id': 150,
                            'admin_id': None,
                            'guru_org_id': 46,
                            'status': 1,
                            'extras': None,
                            'descriptions': None,
                            'rank': 0,
                            'created_at': '2024-05-02T08:51:03.000000Z',
                            'updated_at': '2024-06-21T10:38:01.000000Z',
                            'deleted_at': None,
                            'marks': 80,
                            'overview': '<p> </p>',
                            'causer_type': None,
                            'causer_id': None,
                            'depth': -1,
                            'path': '20329.19893',
                        },
                    ],
                },
                'chapter': {
                    'id': 20330,
                    'name': 'Feedback Session',
                    'marks': 1,
                    'parent_id': 20329,
                    'type': 'Chapter',
                    'ancestors_and_self': {},
                },
                'subject_type': 'Subject',
            },
            'section_id': None,
        },
    ],
    'exam_reminders': [
        8,
    ],
    'rewards': [
        {
            'position': 1,
            'prize': 5000,
        },
    ],
    'is_routine': False,
    'criteria_fields': [],
    'auto_save_message': '<p>Mock test time is up. Your answer will be  submitted automatically. All the best for your result.</p>',
    'self_submit_message': '<p> Thank you for submitting. Wishing you good results.</p>',
    'confirmation_message': '<p> Your mock test will be submitted. If needed, verify the answer. All the best for your results. </p>',
    'rules': '  <p>Student should attend the test solely</p>\n<p>Students are suggested not to exit and resume the test.</p>\n<p>Students should attend the exam within the suggested time.</p>\n<p>Students should start and complete the exams from the same devices (i.e user cannot change device)</p>\n<p>Students are suggested to have a stable internet connection.</p>',
    'terms_and_condition': '<p>Students are not allowed to submit the answer through any source.</p><p>If any unwanted activity is detected then students can be disqualified for the exam, this solely depends upon the AG team.</p><p>The AG team has to terminate the mock test if any suspicious activity is detected.</p><p>When a user registers for a mock test the student agrees to accept the terms and condition and privacy policy of the application.</p><p> Students are not allowed to share their credentials to take the exam from multiple devices and the same account.</p><p>Students should attend the exam at the suggested time.</p><p>AG will not be responsible for any issue created due to internet or student devices.</p>',
    'packages': [
        22,
    ],
    'showPackageform': False,
    'exam_threshold_id': 2,
    'title': user_title,
    'sub_title': user_title,
    'number_of_participant': '10',
    'points': '100',
    'number_of_questions': '10',
    'type': 'Subjective',
    'description': 'Subjective Exam Check Package',
    'published_at': published_at,
    'pass_percentage': '10',
    'model_set_title': user_title,
    'model_set_subtitle': user_title,
    'setup_through': 1,
    'exam_setup_id': None,
    'participant_limit': '10',
}
 
print("Exam configuration:")
print(f"Is Free: {'Yes' if is_free else 'No'}")
if not is_free:
    print(f"Price: {price}")
    
# Make the API request to create the exam
response_create_exam = requests.post(url_create_exam, headers=headers, json=data_create_exam)

if response_create_exam.status_code == 201:
    exam_id = response_create_exam.json().get('data', {}).get('id')
    print("Subjective Mock Test Created Successfully. Exam ID:", exam_id)
    
    # Step 3: Open the exam URL in the browser
    exam_url = f"https://admin.ambition.guru/exams/mock-test-detail/{exam_id}?routeName=Subjective"
    print(f"Opening exam URL in browser: {exam_url}")
    webbrowser.open(exam_url)

    #time.sleep(2)

    
    # Step 4: Lock the questions for the created exam
    url_lock_questions = f"https://api-adm.ambition.guru/api/v1/admin/exams/{exam_id}/lock-questions"
    response_lock_questions = requests.post(url_lock_questions, headers=headers)

 
# Check if the locking was successful
if response_lock_questions.status_code == 200:
    print(f"Questions locked successfully for Exam ID: {exam_id}")
else:
    print(f"Failed to lock questions. Status Code: {response_lock_questions.status_code}")
    print("Response Headers:", response_lock_questions.headers)
    print("Response Text:", response_lock_questions.text)  # Log raw response

    # Handle empty or invalid JSON response gracefully
    try:
        print("Response JSON:", response_lock_questions.json())
    except requests.exceptions.JSONDecodeError:
        print("No JSON content in response.")
 
 