import os
import vertexai
from flask import Flask, request, jsonify
from vertexai.language_models import TextGenerationModel

app = Flask(__name__)
PROJECT_ID = os.environ.get('GCP_PROJECT')
LOCATION = os.environ.get('GCP_REGION')
vertexai.init(project=PROJECT_ID, location=LOCATION)

api_root = "/api/v1"

# Root Routes
@app.route("/")
def app_root():
    return f"Root Index - The app didn't die, at least. This project ({PROJECT_ID}) is running in GCP Region: {LOCATION}!"

@app.route("/api")
def index():
    return redirect("/api/v1")

@app.route(api_root)
def home():
    return "API Root - This will eventually redirect to a swagger UI maybe..."

# Simple Call
@app.route(api_root + '/simple-call', methods=['GET'])
def simple_call():
    # Get the query parameters from the request
    name = request.args.get('name')
    age = request.args.get('age')

    #now let's try the vertex api:
    generation_model = TextGenerationModel.from_pretrained("text-bison@001")
    prompt = "What is a large language model?"
    response = generation_model.predict(prompt=prompt)

    #Return the results
    return f"{name}, Age {age} asked, \"{prompt}\". PaLM Responded: " + response.text


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))