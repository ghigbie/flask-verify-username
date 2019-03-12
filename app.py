from flask import Flask, render_template, request
app = Flask(__name__)

title="Flask Username Verification"

@app.route('/')
def index():
    return render_template('home.html', title=title)

@app.route('/report')
def report():

    lower_letter = False
    upper_letter = False
    num_end = False

    user_name = request.args.get('user_name')

    lower_letter = any(char.islower() for char in user_name)
    upper_letter = any(char.isupper() for char in user_name)
    num_end = user_name[-1].isdigit()

    report = lower_letter and upper_letter and num_end

    verify_pass = 'Your username meets the requirements!!! Time to celebrate!'
    verify_fail = 'Your username does not meet all of the requirements.'

    return render_template('report.html', title=title, verify_pass=verify_pass, verify_fail=verify_fail, report=report, user_name=user_name, lower_letter=lower_letter, upper_letter=upper_letter, num_end=num_end)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('notfound.html', title=title, e=e)

if __name__ == '__main__':
    app.run(debug=True)
