from flask import Flask, request, render_template
from prime import find_Prime

app = Flask(__name__) # create Flask application instance

@app.route('/', methods=['GET', 'POST'])  # create routing of application for Get and Post Request
def calculate():
    result = None
    if request.method == 'POST':
        try:
            num1 = float(request.form['num1'])
            result = find_Prime(int(num1))
        except ValueError:
            result = 'Invalid input!'
    return render_template('index.html', result=result) # render the HTML template with the result

if __name__ == '__main__':   # run the application
    app.run(debug=True)
