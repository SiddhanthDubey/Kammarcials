from flask import Flask, session, abort, redirect, request, make_response, jsonify

from app import app
from model.survey import Survey

survey = Survey()


@app.route("/survey", methods=["GET"])
def survey_controller():
    try:
        result = survey.get_survey_model()

        return result
    except Exception as e:
        app.logger.error(f"Error in survey_controller: {str(e)}")
        return make_response({"message": "An error occurred while processing your request"}, 500)
