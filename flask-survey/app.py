from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

surveys=survey

RESPONSES = "responses"

 
app = Flask(__name__)
app.config['SECRET_KEY'] = 'for'
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
debug = DebugToolbarExtension(app)


@app.route("/")
def show_survey():
    return render_template("home.html",survey=surveys)

@app.route("/begin", methods =["POST"])
def begin_button():
    session[RESPONSES] = []

    return redirect("/questions/0")


@app.route("/answer", methods= ["POST"])
def question_handler():
    try:
        choice = request.form['answer']
        response = session[RESPONSES]
        response.append(choice)
        session[RESPONSES]= response
        response_length = len(response)
        if response_length == 4:
            return redirect ("/complete")
    except:
        flash("Please choose an option!", "error")

    return redirect(f"/questions/{len(RESPONSES)}") 


@app.route("/questions/<int:question_id>")
def show_questions(question_id):
    response = session.get(RESPONSES)


    if (len(response) == len(survey.questions)):
        return redirect("/complete"), 
    
    if (len(response) != question_id):
        return redirect(f"/questions/{len(response)}")
    
    
    questions = survey.questions[question_id]

    return render_template("survey_questions.html", question_num=question_id, questions = questions)


@app.route("/complete")
def completed_survey():
    return render_template("complete.html")