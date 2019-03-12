from flask import Flask, render_template, request
app = Flask(__name__)

title="Flask Username Verification"

@app.route('/')
def index():
    return render_template('home.html', title=title)

@app.route('/report')
def report():
    verify_pass = 'Your username meets the requirements'
    verify_fail = 'Your useranme does not meet the requirements'
    user_name = request.args.get('username')
    return render_template('report.html', title=title, verify_pass=verify_pass, verify_fail=verify_fail, user_name=user_name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('notfound.html', title=title, e=e)

if __name__ == '__main__':
    app.run(debug=True)
