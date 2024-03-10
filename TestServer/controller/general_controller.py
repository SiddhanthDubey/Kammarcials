from flask import request, make_response
from app import app
from model.query import Query

query = Query()


@app.route("/user_query", methods=["POST"])
def user_query_controller():
    try:
        # data = json.loads(request.data.decode("utf-8"))
        data = request.form
        result = query.user_query_model(data)
        app.logger.info("User query received successfully")

        return result
    except Exception as e:
        app.logger.error(f"Error in general_controller: {str(e)}")
        return make_response({"message": "An error occurred while processing your request"}, 500)