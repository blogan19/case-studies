cases = {"case_id": "",
            "casestudy_type": "patient_review",
            "published": True,
            "tags":"",
            "user_group":"Pharmacists",
            "case_settings":
                {
                    "assessed": False, #assessed requires marking student attempts by author not assessed gives instant feedback
                    "prescribing": False, #prescribing allows the student to prescribe and ammend prescriptions
                    "orders": False #allows the user to send patient investigations etc
                },
            "case_instructions":"A patient has been admitted to your ward. Review their prescription chart and recent bloods before attempting the questions below",#set of instructions displayed at the top of the case study
            "patient_demographics":
                 {
                     "lastname":"",
                     "surname":"",
                     "age":"",
                     "gender":"",
                     "ethnicity":"",
                     "weight":"",
                     "height":""
                 },
             "allergies":{
                "Trimethoprim":"Rash"
             },
             "medications": [
                 {
                     "drug_id":"1",
                     "drug_name":"Bisoprolol",
                     "form":"Tablets",
                     "route":"Oral",
                     "dose":"2.5mg",
                     "frequency":"Once Daily",
                     "stat":"N",
                     "start_date":"05/07/22",
                     "end_date": ""
                 },
                 {
                     "drug_id":"2",
                     "drug_name":"Apixaban",
                     "form":"Tablets",
                     "route":"Oral",
                     "dose":"5mg",
                     "frequency":"Twice Daily",
                     "stat":"N",
                     "start_date":"05/07/22",
                     "end_date": ""
                 },
                 {
                     "drug_id":"3",
                     "drug_name":"Omeprazole",
                     "form":"capsules",
                     "route":"Oral",
                     "dose":"20mg",
                     "frequency":"Once Daily",
                     "stat":"N",
                     "start_date":"05/07/22",
                     "end_date": ""
                 },
                 {
                     "drug_id":"4",
                     "drug_name":"Amoxicillin",
                     "form":"Tablets",
                     "route":"Oral",
                     "dose":"500mg",
                     "frequency":"Three Times Daily",
                     "stat":"N",
                     "start_date":"05/07/22",
                     "end_date": "10/07/22",
                     "indication": "CAP",
                     "notes": "CURB65 score was 1"
                 }
             ],
             "biochemistry":[
                {
                    "result_type":"eGFR",
                    "results": [78,73,62,72],
                    "recorded_date": ["02/07/22","03/07/22","04/07/22","05/07/22"],
                    "unit":"ml/min",
                    "range": "<90 ml/min"
                },
                {
                    "result_type":"potassium",
                    "results": [3.3,3.8,4.0,3.9],
                    "recorded_date": ["02/07/22","03/07/22","04/07/22","05/07/22"],
                    "unit": "mmol/ml",
                    "range": "3.5-5.3mmol/ml"
                 }
             ],
             "microbiology":[
                {
                     "micro_id":"primary key of this instance",
                     "micro_test":"primary key of test type",
                     "template_id":"id of template used to generate result or null if custom",
                     "micro_result":"",
                     "micro_datetime": ""
                } 
             ],
             "observations":[
                 {
                     "observation_id":"",
                     "observation_result":"",
                     "observation_datetime": ""
                 }
             ],    
             "imaging":[
                 {
                     "image_url": "",
                     "image_description" : ""
                 }
             ],
             "conditions":['diabetes','COPD'],
             "presenting_complaint": ['community acquired pneumonia','fall'],
             "clinical_notes": [{
                "note_id":"1",
                "note_datetime":"05/07/2022 22:30:00",
                "note": "80yo pt found on floor by neighbour BIBA. Sats 92% on RA known COPD"
             },{
                "note_id":"2",
                "note_datetime":"06/07/2022 08:30:00",
                "note": "post take ward round. Consolidation on chest xray Curb score 1 start IV amox"
             }],
             "case_study_questions":[
                 {
                     "question_id":"mcq1",
                     "question_type":"mcq",
                     "question_title": "Antibiotic Choice",
                     "question":"Which of following would be the most appropriate antimicrobial is the patient has an allergy to penicillin?",
                     "options": ["Ciprofloxacin","Trimethoprim","Doxycycline","Clarithromycin","Nitrofurantoin"],
                     "answer":"Doxycycline"
                 }
             ]
        }