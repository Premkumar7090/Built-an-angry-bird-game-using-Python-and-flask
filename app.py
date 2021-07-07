from flask import Flask
import main

app = Flask(__name__)

@app.route('/')
def run_script():
    
    return exec(main)


if __name__ == "__main__":
    app.run(debug=True)