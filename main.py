from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')
  
@app.route('/student-list')
def student_list():
    return render_template('student_list.html')

@app.route('/courses')
def courses():
    return render_template('course.html')

@app.route('/grades')
def grades():
    return render_template('grades.html')

@app.route('/login')
def login():
    return 'This is a sample login'

if __name__ == '__main__':
    app.run()