from flask import Flask, render_template
import sys

app = Flask(__name__)

@app.route('/')
def index():
    try:
        return render_template('index.html')
    except Exception, e:
        return str(e)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/compass')
def compass():
    return render_template('compass.html')


if __name__ == "__main__":
    # This section allows the user to use the '-d' argument  when starting
    # app.py to turn on debugging. If no CLA's are entered then dubugging will
    # be off. 
    if len(sys.argv) > 1 and sys.argv[1] == "-d":
        app.run(debug=True)
    else:
        app.run(debug=False)
