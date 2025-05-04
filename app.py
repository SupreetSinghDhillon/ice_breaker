from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template

load_dotenv()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    name = request.form.get("name")
    
    # Call the ice_break_with function from ice_breaker.py
    from ice_breaker import ice_break_with
    result = ice_break_with(name)
    
    # Convert the result to a dictionary
    result_dict = {
        "summary": result.summary,
        "facts": result.facts
    }
    
    return jsonify(result_dict)

if __name__ == "__main__":
    app.run(debug=True, port=5001)



