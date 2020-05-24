from flask import Flask, render_template

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
    app.run(debug=True)
