import os
import vertexai
from flask import Flask, request, jsonify
from vertexai.language_models import TextGenerationModel

app = Flask(__name__)
PROJECT_ID = os.environ.get('GCP_PROJECT')
LOCATION = os.environ.get('GCP_REGION')
vertexai.init(project=PROJECT_ID, location=LOCATION)

# Root Simple Fallback
@app.route("/")
def hello_world():
    """Example Hello World route."""
    name = os.environ.get("NAME", "World")
    return f"Hello Revised {name}!"

# Define the route for the API endpoint
@app.route('/api', methods=['GET'])
def api():
    # Get the query parameters from the request
    name = request.args.get('name')
    age = request.args.get('age')

    # Create a dictionary with the query parameters
    data = {'name': name, 'age': age}

    #now let's try the vertex api:
    generation_model = TextGenerationModel.from_pretrained("text-bison@001")
    prompt = "What is a large language model?"
    response = generation_model.predict(prompt=prompt)

    # Return the dictionary as a JSON response
    #return jsonify(data)
    return response.text


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))