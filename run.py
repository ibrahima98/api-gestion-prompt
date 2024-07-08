from app import create_app
from flask import request, jsonify

app = create_app()

@app.before_request
def log_request():
    print(request.headers)
    print(request.data)
    print(request.json)
if __name__ == "__main__":
    app.run(debug=True)
