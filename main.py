from flask import Flask, render_template, redirect , url_for, request
from users import Users
from students import Students

app = Flask(__name__)

# Dummy data
students = [
    {'id': 1, 'last_name': "CALLEJO", 'first_name': "MARY CLAIRE", 'middle_name': "BACUNAWA", 'sex': "FEMALE", 'birthday': "09-16-1993", 'addres': "MUDIIT", 'course_id':"5"},
    {'id': 103, 'last_name': "ALAGAO", 'first_name': "DHARYLLE", 'middle_name': "AUSTRIA", 'sex': "MALE", 'birthday': "12-07-2003", 'address': "GADDANI", 'course_id': "3"},
    {'id': 2,'last_name': "CADA", 'first_name':  "ALIJUN", 'middle_name': "C", 'sex': "MALE", 'birthday': "10-19-2003", 'address': "LAGANGILANG", 'course_id': "2"},
    {'id': 5, 'last_name': "VILLASTIQUE", 'first_name': "MARIA CIELO",'middle_name': "BAATI", 	'sex': "FEMALE", 'birthday': "03-12-2002", 'address': "PRESENTAR", 'course_id': "7"},
    {'id': 6, 'last_name': "JACQUIAS", 'first_name': "ELOIZA", 'middle_name': "DUQUE",	'sex': "FEMALE", 'birthday': "04-01-2002",	'address': "SALLAPADAN", 'course_id': "9"}
]

@app.route('/')
def index():
    return render_template('login.html', students=students)

@app.route('/check-user', methods=['POST'])
def check_user():
    username = request.form["username"]
    password = request.form["password"]

    result = Users.check_user(username, password)

    if result:
        return redirect('student-list')
    else:
        return render_template('login.html')
  
  
@app.route('/student-list')
def student_list():

    students = Students.get_all()

    return render_template('student_list.html', students=students)

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

@app.route('/update_student/<int:student_id>', methods=['GET','POST'])
def update_students(student_id) :
    student = next((s for s in students if s['id'] == student_id), None)
    if student is None:
        return "Student not found", 404

    if request.method == 'POST': 
        # Update student logic here 
        student['last_name'] = request.form['last_name']
        student['first_name'] = request.form['first_name']
        student['middle_name'] = request.form['middle_name']
        student['sex'] = request.form['sex']
        student['birthday'] = request.form['birthday']
        student['address'] = request.form['address']
        student['course_id'] = int(request.form['course_id'])

        return redirect(url_for('index'))        

        return render_template('update_student.html', student=student)

@app.route('/delete_student/<int:student_id>', methods=['POST']) 
def delete_student(student_id):
    global students
    students = [s for s in students 
if s['id'] != student_id]
    return redirect(url_for('index'))
    
if __name__ == '__main__':
    app.run(debug=True)