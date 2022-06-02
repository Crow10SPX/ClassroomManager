import sqlite3

database = r"cmdb.db"

def checkUser(teacherUsername):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    # get passed in username and check it against db to check whether they are a valid user
    sql = f"SELECT username FROM Teacher WHERE Teacher.username= '{teacherUsername}'"
    c.execute(sql)
    name = c.fetchall()
    if len(name)>0:
        exists = True
    else:
        exists = False
    return exists

def requestPassword(teacherUsername):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    # get password from db that matches passed in username
    sql = f"SELECT password FROM Teacher WHERE Teacher.username= '{teacherUsername}'"
    c.execute(sql)
    password = c.fetchall()[0][0]
    return password

def getClasses(teacherUsername):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    # get classes from db for the specified teacher
    sql = f"SELECT c.className FROM Class AS c, Teacher AS t WHERE t.username = '{teacherUsername}' AND c.teacherId = t.teacherId" 
    c.execute(sql)
    className = c.fetchall()
    return className

def getTeacherName(teacherUsername):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    sql = f"SELECT t.firstName, t.lastName FROM Teacher as t WHERE t.username = '{teacherUsername}'"
    c.execute(sql)
    teacherName = c.fetchall()
    for i in teacherName:
        teacherName = i[0]+" "+i[1]
    return teacherName
    
def getProfilePicture(teacherUsername):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    sql = f"SELECT t.profilePicture FROM Teacher as t WHERE t.username = '{teacherUsername}'"
    c.execute(sql)
    teacherProfile = c.fetchall()
    for i in teacherProfile:
        teacherProfile = i[0]
    return teacherProfile

def getClasses(teacherUsername):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    # get classes from db for the specified teacher
    sql = f"SELECT c.className FROM Class AS c, Teacher AS t WHERE t.username = '{teacherUsername}' AND c.teacherId = t.teacherId" 
    c.execute(sql)
    className = c.fetchall()
    return className 

def getTimtetable(teacherUsername):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    sql = f"SELECT t.timetablePicture FROM Teacher as t WHERE t.username = '{teacherUsername}'"
    c.execute(sql)
    teacherTimetable = c.fetchall()
    for i in teacherTimetable:
        teacherTimetable = i[0]
    return teacherTimetable

def getStudents(className):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    sql = f"SELECT DISTINCT s.firstName, s.lastName FROM Student as s, Class as c, studentClass as sc WHERE c.className = '{className}' AND sc.classId = c.classId AND sc.studentId = s.studentId"
    c.execute(sql)
    studentName = c.fetchall()
    students = []
    for i in studentName:
        studentName = i[0]+" "+i[1]
        students.append(studentName)
    return(students)

def getClassId(className):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    sql = f"SELECT c.classId FROM Class as c WHERE c.className = '{className}'"
    c.execute(sql)
    cId = c.fetchall()
    return cId

def getStudentId(firstName, lastName):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    sql = f"SELECT s.studentId FROM Student as s WHERE s.firstName = '{firstName}' AND s.lastName = '{lastName}'"
    c.execute(sql)
    sId = c.fetchall()
    return sId

def getStudentClassId(studentId, classId):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    sql = f"SELECT sc.studentClassId FROM studentClass as sc WHERE sc.studentId = '{studentId}' AND sc.classId = '{classId}'"
    c.execute(sql)
    scId = c.fetchall()
    return scId

def insertNote(studentNote, studentClassId):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    sql1 = f"SELECT sc.behaviourNote FROM studentClass as sc WHERE sc.studentClassId ='{studentClassId}'"
    c.execute(sql1)
    row = c.fetchone()
    existingNote = row[0]
    if not existingNote:
        finalNote = f"'{studentNote}'"
    else:
        finalNote = f"'{existingNote}\n{studentNote}'"
    print(finalNote)
      
    sql2 = ("UPDATE studentClass SET behaviourNote ='{}' WHERE studentClass.studentClassId ='{}'".format(finalNote, studentClassId))
    c.execute(sql2)
    conn.commit()
    conn.close()

def getNote(studentClassId):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    sql = f"SELECT behaviourNote FROM studentClass WHERE studentClassId = '{studentClassId}'"
    c.execute(sql)
    noteTuple = c.fetchall()
    for i in noteTuple:
        note = i[0]
    note = str(note)
    note = note.replace("'","")
    return note

        
    
    
    
    
    
    

    