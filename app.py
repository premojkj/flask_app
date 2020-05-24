from flask import Flask, render_template
import sys

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/page2')
def page2():
    return render_template('page2.html')

@app.route('/generalOverview')
def overview():
    return render_template('generalOverview_aboutGoldesp.html')


if __name__ == "__main__":
    # This section allows the user to use the '-d' argument  when starting
    # app.py to turn on debugging. If no CLA's are entered then dubugging will
    # be off. 
    if len(sys.argv) > 1 and sys.argv[1] == "-d":
        app.run(debug=True)
    else:
        app.run()
