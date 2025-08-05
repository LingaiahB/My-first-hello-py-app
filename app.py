from flask import Flask
import os
import sys

app = Flask(__name__)

@app.route("/")
def hello():
    return os.getenv("GREETING", "Hello, World!")

if __name__ == "__main__":
    port = 5000  # default port
    if len(sys.argv) > 1:
        # e.g., --port=5050
        for arg in sys.argv[1:]:
            if arg.startswith("--port="):
                port = int(arg.split("=")[1])
    app.run(host="0.0.0.0", port=port)
