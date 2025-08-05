from flask import Flask
import sys

app = Flask(__name__)

# Default greeting
greeting = "Hello, World!"

# Parse command-line arguments
for arg in sys.argv[1:]:
    if arg.startswith("--greeting="):
        greeting = arg.split("=")[1]

@app.route("/")
def hello():
    return greeting

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
