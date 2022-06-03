import sqlite3

database = r"cmdb.db"

def checkUser(teacherUsername):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    # get passed in username and check it against db to check whether they are a valid user
    c.execute(f"SELECT username FROM Teacher WHERE Teacher.username= ?", [teacherUsername])
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
    c.execute(f"SELECT password FROM Teacher WHERE Teacher.username= ?", [teacherUsername])
    password = c.fetchall()[0][0]
    return password

def getClasses(teacherUsername):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    # get classes from db for the specified teacher
    c.execute(f"SELECT c.className FROM Class AS c, Teacher AS t WHERE t.username = ? AND c.teacherId = t.teacherId", [teacherUsername])
    className = c.fetchall()
    return className

def getTeacherName(teacherUsername):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    c.execute(f"SELECT t.firstName, t.lastName FROM Teacher as t WHERE t.username = ?", [teacherUsername])
    teacherName = c.fetchall()
    for i in teacherName:
        teacherName = i[0]+" "+i[1]
    return teacherName
    
def getProfilePicture(teacherUsername):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    c.execute(f"SELECT t.profilePicture FROM Teacher as t WHERE t.username = ?", [teacherUsername])
    teacherProfile = c.fetchall()
    for i in teacherProfile:
        teacherProfile = i[0]
    return teacherProfile

def getClasses(teacherUsername):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    # get classes from db for the specified teacher
    c.execute(f"SELECT c.className FROM Class AS c, Teacher AS t WHERE t.username = ? AND c.teacherId = t.teacherId", [teacherUsername])
    className = c.fetchall()
    return className 

def getTimtetable(teacherUsername):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    c.execute(f"SELECT t.timetablePicture FROM Teacher as t WHERE t.username = ?", [teacherUsername])
    teacherTimetable = c.fetchall()
    for i in teacherTimetable:
        teacherTimetable = i[0]
    return teacherTimetable

def getStudents(className):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    c.execute(f"SELECT DISTINCT s.firstName, s.lastName FROM Student as s, Class as c, studentClass as sc WHERE c.className = ? AND sc.classId = c.classId AND sc.studentId = s.studentId", [className])
    studentName = c.fetchall()
    students = []
    for i in studentName:
        studentName = i[0]+" "+i[1]
        students.append(studentName)
    return(students)

def getClassId(className):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    c.execute(f"SELECT c.classId FROM Class as c WHERE c.className = ?", [className])
    cId = c.fetchall()[0][0]
    return cId

def getStudentId(firstName, lastName):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    c.execute(f"SELECT s.studentId FROM Student as s WHERE s.firstName = ? AND s.lastName = ?", [firstName, lastName])
    sId = c.fetchone()[0]
    return sId

def getStudentClassId(studentId, classId):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    c.execute(f"SELECT sc.studentClassId FROM studentClass as sc WHERE sc.studentId = ? AND sc.classId = ?", [studentId, classId])
    scId = c.fetchall()[0][0]
    return scId

def insertNote(studentNote, studentClassId):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    c.execute("SELECT sc.behaviourNote FROM studentClass as sc WHERE sc.studentClassId = ?", [studentClassId])
    existingNote = c.fetchall()
    for i in existingNote:
        existingNote = i[0] 
    if existingNote == None:
        finalNote = f"{studentNote}"
    else:
        finalNote = f"{existingNote}\n{studentNote}"
    finalNote = finalNote.strip()
    c.execute("UPDATE studentClass SET behaviourNote = ? WHERE studentClass.studentClassId = ?", [finalNote, studentClassId])
    conn.commit()
    conn.close()

def getNote(studentClassId):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    c.execute(f"SELECT behaviourNote FROM studentClass WHERE studentClassId = ?", [studentClassId])
    noteTuple = c.fetchall()
    for i in noteTuple:
        note = i[0]
    return note

def getAssId(studentClassId):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    c.execute(f"SELECT assessmentId FROM Mark WHERE studentClassId = ?", [studentClassId])
    assId = c.fetchall()[0][0]
    return assId

def getAssNo(assId):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    c.execute(f"SELECT assessmentNum FROM Assessment WHERE assessmentId = ?", [assId])
    assNo = c.fetchall()[0][0]
    return assNo