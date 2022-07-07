from django.shortcuts import redirect
from flask import Flask, request, render_template, flash, redirect
from example_case import cases
import json


#creates a class for our app
app= Flask(__name__)
app.secret_key = "widge"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def get_session_id():
    meeting_id = request.form['inputSessionID']
    print(meeting_id)
    if str(meeting_id) == '1234':
        return redirect('/live_session')    
    else:
        flash(f'{meeting_id} is not a valid session')
        return render_template("index.html")

@app.route('/live_session')
def load_session():
    case_instructions = cases['case_instructions']
    medications = cases['medications']
    biochemistry = cases['biochemistry']
    clinical_notes = cases['clinical_notes']
    questions = cases['case_study_questions']

    return render_template("case_study.html", medications=medications, biochemistry=biochemistry, case_instructions=case_instructions,clinical_notes=clinical_notes,questions=questions)


app.run(port=5000, debug=True)


