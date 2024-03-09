from flask import request, make_response
from app import app
from model.survey import Survey

survey = Survey()


@app.route("/get_survey", methods=["GET"])
def get_survey_controller():
    try:
        result = survey.get_survey_model()

        return result
    except Exception as e:
        app.logger.error(f"Error in survey_controller: {str(e)}")
        return make_response({"message": "An error occurred while processing your request"}, 500)


@app.route("/get_survey_question", methods=["GET"])
def get_survey_question_controller():
    try:
        # data = json.loads(request.data.decode("utf-8"))
        data = request.form
        result = survey.get_survey_question_model(data)
        return result
    except Exception as e:
        app.logger.error(f"Error in survey_controller: {str(e)}")
        return make_response({"message": "An error occurred while processing your request"}, 500)


@app.route("/submit_survey", methods=["POST"])
def survey_submission_controller():
    try:
        # data = json.loads(request.data.decode("utf-8"))
        data = request.form
        return survey.survey_submission_model(data)
    except Exception as e:
        app.logger.error(f"Error in submit_survey_controller: {str(e)}")
        return make_response({"message": "An error occurred while processing your request"}, 500)
