from flask import Flask, request, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

surveys=survey

 
app = Flask(__name__)
app.config['SECRET_KEY'] = 'for'
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
debug = DebugToolbarExtension(app)

RESPONSES = []

@app.route("/")
def show_survey():
    return render_template("home.html",survey=surveys)

@app.route("/begin", methods =["POST"])
def begin_button():
    return redirect("/questions/0"), list.clear(RESPONSES)


@app.route("/answer", methods= ["POST"])
def question_handler():
    try:
        choice = request.form['answer']
        RESPONSES.append(choice)
    except:
        flash("Please choose an option!", "error")
    
    
    return redirect(f"/questions/{len(RESPONSES)}")


@app.route("/questions/<int:qid>")
def show_questions(qid):
    if (len(RESPONSES) != qid):
        flash(f"Please do not press the back key, invalid question ID: {qid}.")
        return redirect(f"/questions/{len(RESPONSES)}")
    
    if (len(RESPONSES) == len(survey.questions)):
        return redirect("/complete"), list.clear(RESPONSES)
    
    questions = survey.questions[qid]
    return render_template("survey_questions.html", question_num=qid, questions = questions)




@app.route("/complete")
def completed_survey():
    return render_template("complete.html")