from flask import Flask,request,jsonify
import sqlite3
app = Flask (__name__)
def init_db():
    conn=sqlite3.connect('students.db')
    cursor=conn.cursor()
    cursor.execute('''
    Create  table if not exists students(
    id integer primary key AUTOINCREMENT,
    name text not null,
    email text not null,
    age integer 
    )
    ''')
    conn.commit()
    conn.close

@app.route('/students',methods=['POST'])
def insert_student():
    data=request.get_json()
    conn=sqlite3.connect('students.db')
    cursor=conn.cursor()
    cursor.execute('INSERT INTO students (name,email,age) values (?,?,?)',
    (data['name'],data['email'],data.get('age',0))
    )
    conn.commit()
    student_id=cursor.lastrowid
    conn.close()
    return jsonify({"message":"student created","id": student_id}),201
@app.route('/student',methods=['GET'])
def get_students():
    conn=sqlite3.connect('students.db')
    cursor=conn.cursor()
    cursor.execute('Select* from students')
    rows=cursor.fetchall()
    conn.close()
    students=[{"id":r[0],"name":r[1],"email":r[2],"age":r[3]}for r in rows]
    return jsonify(students)

if __name__=="__main__":
    init_db()
    app.run (debug=True)
