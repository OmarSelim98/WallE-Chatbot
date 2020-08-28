from flask import Flask, jsonify, request , render_template ,session,flash , redirect , url_for
import riveBot
from importlib import reload
from flask_cors import CORS, cross_origin
app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}})
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
app.config['CORS_HEADERS'] = 'Content-Type'
# Get All 
@app.route("/chat", methods=["POST"])
def chat():
    logged_in = True
    if request.method == "POST":
        request_data = request.get_json()
        message = request_data['message']
        response = {}
        if logged_in:
            if message:
                state, reply = riveBot.chat("localuser", message)
                if state == 0:
                    if reply == "finish":
                        reload(riveBot)
                        response["reply"] = str({'message': "We will start a new conversation", "type": "button",
                                                 "data": [{'text': "Ok", "value": "ok", "type": "button"}]})
                        response["status"] = 'Success'
                    else:
                        response["reply"] = reply
                        response["status"] = 'Success'

                    return jsonify(response)
                elif state == -1:
                    response["reply"] = "there is no response"
                    response['status'] = "Failed"

                    return jsonify(response)
            else:
                response["reply"] = "there is no message"
                response['status'] = "Failed"

                return jsonify(response)
        else:
            response["reply"] = "You must Login first"
            response['status'] = "Failed"

            return jsonify(response)

# Run Server
if __name__ == "__main__":
    app.run(host="0.0.0.0")