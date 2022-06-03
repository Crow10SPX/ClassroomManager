import dbconnect as db
import sys 
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
    
    
class ClassroomManager(QWidget):
    styles = {
        "markButton":
            "QPushButton{background-color : rgb(0, 128, 255); color : white; font-family : Arial;"
            "border-style : outset; border-width : 2px; border-radius: 10px; padding: 6px; border-color : rgb(0, 128, 255);} QPushButton::hover { background-color : rgb(0, 221, 255);"
            "border-color : rgb(0, 221, 255); color : white;} QPushButton::pressed {color : rgb(0, 221, 255);}",
        "titleText":
            "color: black; font: 18px;",
        "noteButton":
            "QPushButton{background-color : rgb(0, 128, 255); color : white; font : bold 20px; font-family : Arial;"
            "border-style : outset; border-width : 2px; border-radius: 10px; min-width: 10em; padding: 6px; border-color : rgb(0, 128, 255);} QPushButton::hover { background-color : rgb(0, 221, 255);"
            "border-color : rgb(0, 221, 255); color : white;} QPushButton::pressed {color : rgb(0, 221, 255);}",
        "welcomeText":
            "color : black; font : 34px; font-family : Arial;",
        "classText":
            "color : black; font : 26px; font-family : Arial;",
        "genEntry":
            "background-color: white;",
        "genText":
            "color : black; font : 24px; font-family : Arial;",
        "genButton":
            "QPushButton{background-color : rgb(0, 128, 255); color : white; font : bold 20px; font-family : Arial;"
            "border-style : outset; border-width : 2px; border-radius: 10px; padding: 6px; border-color : rgb(0, 128, 255);} QPushButton::hover { background-color : rgb(0, 221, 255);"
            "border-color : rgb(0, 221, 255); color : white;} QPushButton::pressed {color : rgb(0, 221, 255);}",
        "navbar":
            "QTabBar{color : black; font : bold 60px; font-family : Arial;}"
            "QTabBar::tab:selected{background-color : rgba(0, 221, 255, 24); color : rgb(252, 50, 203);; font : bold 60px; font-family : Arial;}"
            "QTabBar::tab:!selected{background-color : rgb(255, 255, 255); color : rgb(252, 50, 203); font : bold 60px; font-family : Arial;}"
            "QTabBar::tab:hover{background-color: rgba(0, 221, 255, 24); font : bold 60px; font-family : Arial;}"
            "QTabWidget::pane { border: 0; }",
        "error":
            "color : rgb(255, 0, 0); font : 24px; font-family : Arial; background-color: rgba(255, 255, 255, 0)"
    }

    def __init__(self, parent=None):
        super(ClassroomManager, self).__init__(parent)
        self.buildScreen()
        self.loginPage()

    def buildScreen(self):
        # gives init widget "bgWidget" object name
        self.setObjectName("loginbgWidget")
        # creates background gradient referring only to bgWidget object of login
        self.setStyleSheet("QWidget#loginbgWidget {background-color: qlineargradient(spread:pad, x1:0.0640394, y1:0.082, x2:0.899836, y2:0.852, stop:0 rgba(94, 179, 222, 255), stop:1 rgba(255, 255, 255, 255))}")
        self.setWindowTitle("Classroom Manager")
        self.setWindowIcon(QtGui.QIcon("img/logo.png"))
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        
        
    def loginPage(self):
        # create main title logo
        self.classManagerLabel = QLabel(self)
        self.classManagerLabel.setFixedHeight(300)
        self.classManagerLabel.setFixedWidth(800)
        self.classManagerLabel.setScaledContents(True)
        self.classManagerLogo = QPixmap("img/logo.png")
        self.classManagerLabel.setPixmap(self.classManagerLogo)

        # create username login entry field and label
        self.usernameTitle = QLabel(self)
        self.usernameTitle.setText("Username:")
        self.usernameTitle.setStyleSheet(self.styles["genText"])
        self.usernameEntry = QLineEdit(self)
        self.usernameEntry.setFixedHeight(35) # makes username entry field box slightly taller
        self.usernameEntry.returnPressed.connect(self.login)  # pressing enter logs in
        self.usernameEntry.setStyleSheet(self.styles["genEntry"])
        
        # create password login entry field and label
        self.passwordTitle = QLabel(self)
        self.passwordTitle.setText("Password:")
        self.passwordTitle.setStyleSheet(self.styles["genText"])
        self.passwordEntry = QLineEdit(self)
        self.passwordEntry.setFixedHeight(35) # makes password entry field box slightly taller
        self.passwordEntry.setEchoMode(QLineEdit.Password) # hides password when entered in field
        self.passwordEntry.returnPressed.connect(self.login)  # pressing enter logs in
        self.passwordEntry.setStyleSheet(self.styles["genEntry"])
        
        # create login button for verification of username & password
        self.loginButton = QPushButton("Login")
        self.loginButton.clicked.connect(self.login)
        self.loginButton.setStyleSheet(self.styles["genButton"])
        
        # create spacer items for UI
        self.spacer1 = QSpacerItem(80, 80, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.spacer2 = QSpacerItem(150, 150, QSizePolicy.Expanding)
        self.spacer3 = QSpacerItem(150, 150, QSizePolicy.Expanding)
        
        # place all UI elements on the page 
        self.grid.addItem(self.spacer3, 0, 0, 1, 35, Qt.AlignCenter)
        self.grid.addWidget(self.classManagerLabel, 1, 0, 1, 35, Qt.AlignCenter)
        self.grid.addItem(self.spacer2, 2, 0, 1, 35, Qt.AlignCenter)
        self.grid.addItem(self.spacer1, 3, 0, Qt.AlignTop)
        self.grid.addWidget(self.usernameTitle, 4, 14, 1, 5, Qt.AlignLeft)
        self.grid.addWidget(self.usernameEntry, 5, 14, 1, 5, Qt.AlignTop)
        self.grid.addWidget(self.passwordTitle, 6, 14, 1, 5, Qt.AlignLeft)
        self.grid.addWidget(self.passwordEntry, 7, 14, 1, 5, Qt.AlignTop)
        self.grid.addWidget(self.loginButton, 8, 14, 1, 5, Qt.AlignTop)
        
    def deleteLoginPage(self):
        # delete UI elements from the page
        self.classManagerLabel.deleteLater()
        self.usernameTitle.deleteLater()
        self.usernameEntry.deleteLater()
        self.passwordTitle.deleteLater()
        self.passwordEntry.deleteLater()
        self.loginButton.deleteLater()
        # error message may or may not exist
        try:
            self.loginError.deleteLater()
        except:
            print("System: Login Page Deletion Exception.")
              
    def displayLoginError(self, error):
        # an error message may be displayed
        try:
            self.loginError.deleteLater()
            self.loginError = QLabel(self)
            self.loginError.setText(error)
            self.loginError.setStyleSheet(self.styles["error"])
            self.grid.addWidget(self.loginError, 9, 14, 1, 5, Qt.AlignTop)
        except:
            self.loginError = QLabel(self)
            self.loginError.setText(error)
            self.loginError.setStyleSheet(self.styles["error"])
            self.grid.addWidget(self.loginError, 9, 15, 1, 5, Qt.AlignTop)
            
    def login(self):
        print("Logging in...")
        # get the username & password entered by user
        self.loginU = self.usernameEntry.text()
        self.loginP = self.passwordEntry.text()
        # chcek that the username exists
        accountExists = db.checkUser(self.loginU)
        print("Account Exists: ", accountExists)
        # initially set verify to false
        accountVerified = False
        if accountExists:
            if db.requestPassword(self.loginU) == self.loginP:
                accountVerified = True
            # password doesn't match error message
            else:
                errorMsg = "Incorrect Password"
        # username doesn't exist meaning account doesn't exist
        else:
            errorMsg = "Account doesnt exist"
        
        # checked account exists, account verified has been returned as true 
        if accountVerified:
            # delete login UI and redirect to Timetable widget
            self.deleteLoginPage()
            welcomeMsg = QMessageBox()
            welcomeMsg.setWindowTitle("Welcome!")
            welcomeMsg.setText("Login Successful, Welcome to Classroom Manager!")
            welcomeMsg.exec_()
            self.timetablePage()
        else:
            # display error message to user
            self.displayLoginError(errorMsg)
        
        
    def timetablePage(self):
        self.setWindowTitle("Timetable Page")
        
        # put teacher profile picture of page
        profilePath = db.getProfilePicture(self.loginU)
        self.teacherProfileLabel = QLabel(self)
        self.teacherProfileLabel.setFixedHeight(400)
        self.teacherProfileLabel.setFixedWidth(400)
        self.teacherProfileLabel.setScaledContents(True)
        teacherPicture = QPixmap(profilePath)
        self.teacherProfileLabel.setPixmap(teacherPicture)

        # get teacher timetable picture
        timetablePath = db.getTimtetable(self.loginU)
        self.teacherTimetableLabel = QLabel(self)
        self.teacherTimetableLabel.setFixedHeight(500)
        self.teacherTimetableLabel.setFixedWidth(1000)
        self.teacherTimetableLabel.setScaledContents(True)
        teacherTimetable = QPixmap(timetablePath)
        self.teacherTimetableLabel.setPixmap(teacherTimetable)

        # class List title
        self.classLabel = QLabel(self)
        self.classLabel.setText("List of Classes:")
        self.classLabel.setStyleSheet(self.styles["classText"])

        # get teacher name 
        self.teacherLabel = QLabel(self)
        self.tName = db.getTeacherName(self.loginU)
        self.teacherLabel.setText(f"Current User: {self.tName}")
        self.teacherLabel.setStyleSheet(self.styles["classText"])

        # add welcome text
        self.welcomeTeacherLabel = QLabel(self)
        self.welcomeTeacherLabel.setText(f"Welcome to Classroom Manager, Mr. {self.tName}")
        self.welcomeTeacherLabel.setStyleSheet(self.styles["welcomeText"])

        # make logout button
        self.logoutButton = QPushButton("Logout")
        self.logoutButton.setFixedSize(250, 40)
        self.logoutButton.clicked.connect(self.logout)
        self.logoutButton.setStyleSheet(self.styles["genButton"])

        # generate class buttons
        self.makeClassButtons()
        
        # put UI elements on timetable page
        self.grid.addWidget(self.teacherProfileLabel, 0, 0, 1, 35)        
        self.grid.addWidget(self.teacherTimetableLabel, 0, 14, 0, 35, Qt.AlignCenter)
        self.grid.addWidget(self.classLabel, 1, 1, 4, 3)        
        self.grid.addWidget(self.teacherLabel, 2, 1, 1, 35)
        self.grid.addWidget(self.welcomeTeacherLabel, 0, 31)
        
        self.grid.addWidget(self.logoutButton, 18, 0, 20, 0, Qt.AlignLeft)
                
    def logout(self):
        self.deleteTimetablePage()
        self.loginPage()
               
    def makeClassButtons(self):
        # make the class buttons for the teacher's classes
        classes = db.getClasses(self.loginU)
        # create a vertical sublayout for the buttons
        self.listLayout = QVBoxLayout()
        # position new sublayout on the screen
        self.grid.addLayout(self.listLayout, 3, 1, 4, 6)
        self.setLayout(self.grid)
        classList = []
        # make the button equal to the maximum amount of buttons created relating to the amount of classes for that teacher
        self.classButton = [None]*len(classes)
        self.classDict = {'classList':classList}
        for i in classes:
            classList.append({"class":i[0]})   
        # index for the amount of buttons generated from the tuple of classes that the sql returns 
        u = 0
        for self.teacherClass in self.classDict["classList"]:
            self.classButton[u] = QPushButton(self.teacherClass["class"])
            self.classButton[u].setStyleSheet(self.styles["genButton"])
            self.classButton[u].setFixedSize(250, 40)
            self.classButton[u].clicked.connect(lambda:self.classPage(self.msgSender()))
            self.listLayout.addWidget(self.classButton[u])
            u+=1
        
          
    def deleteTimetablePage(self):
        self.teacherProfileLabel.deleteLater()
        self.classLabel.deleteLater()
        self.teacherLabel.deleteLater()
        self.teacherTimetableLabel.deleteLater()
        for button in self.classButton:
            button.deleteLater()
        self.welcomeTeacherLabel.deleteLater()
        self.logoutButton.deleteLater()

    def msgSender(self):
        self.className = self.sender().text()
        
    def classPage(self, sender):
        self.deleteTimetablePage()
        
        self.setWindowTitle(f"Class: {self.className}")
        
        self.students = db.getStudents(self.className)
        self.classSize = len(self.students)
        
        
        self.classSizeLabel = QLabel(self)
        self.classSizeLabel.setText(f"Number of Students: {self.classSize}")
        self.classSizeLabel.setStyleSheet(self.styles["classText"])
        
        self.thisClassLabel = QLabel(self)
        self.thisClassLabel.setText(f"Welcome to {self.className}")
        self.thisClassLabel.setStyleSheet(self.styles["classText"])
        
        self.studentsBox()
        
        self.backButton = QPushButton("Go Back")
        self.backButton.setFixedSize(250, 40)
        self.backButton.clicked.connect(lambda:self.goTimetable())
        self.backButton.setStyleSheet(self.styles["genButton"])
        self.grid.addWidget(self.backButton, 34, 0)
        
    def goTimetable(self):
        self.deleteClassPage()
        self.timetablePage()
        
    def deleteClassPage(self):
        self.backButton.deleteLater()
        self.thisClassLabel.deleteLater()
        self.classSizeLabel.deleteLater()
        self.classLayout.deleteLater()
        self.scrollArea.deleteLater()
        self.top_layout.deleteLater()
        self.top_widget.deleteLater()
        
        
    def studentsBox(self):
        self.classLayout= QVBoxLayout()
        # create a scroll area
        self.scrollArea = QScrollArea()
        
        # add scroll area to new layout
        self.classLayout.addWidget(self.scrollArea)
        
        self.top_widget = QWidget()
        self.top_layout = QVBoxLayout()

        # add labels in widget but above the group_box
        self.spacer4 = QSpacerItem(20,20, QSizePolicy.Expanding)
        self.top_layout.addWidget(self.classSizeLabel)
        self.top_layout.addItem(self.spacer4)
        self.top_layout.addWidget(self.thisClassLabel)
        self.top_layout.setAlignment(self.classSizeLabel, Qt.AlignHCenter)
        self.top_layout.setAlignment(self.thisClassLabel, Qt.AlignHCenter)
        
        self.viewNotes = [None]*self.classSize
        self.behaviourNote = [None]*self.classSize
        self.saveNote = [None]*self.classSize
        self.mark = [[None]*4]*self.classSize
        self.markLabel = [[None]*4]*self.classSize
        self.markvlayout = [[None]*4]*self.classSize
        

        
        for i in range(0, self.classSize):
            groupBox = QGroupBox()
            
            groupBox.setTitle(f"Student: {self.students[i]}")
        
            self.behaviourLayout = QHBoxLayout(groupBox)

            self.notePrompt = QLabel("Write a behaviour note:")
            self.notePrompt.setStyleSheet("color: black; font: 22px;")
            self.behaviourLayout.addWidget(self.notePrompt)
                        
            self.behaviourNote[i] = QTextEdit()
            self.behaviourNote[i].setFixedSize(780, 200)
            self.behaviourLayout.addWidget(self.behaviourNote[i])

            self.buttonLayout = QVBoxLayout()
            
            self.viewNotes[i] = QPushButton(groupBox)
            # get first name of students
            firstName = self.students[i].split()[0]
            self.viewNotes[i].setText(f"{firstName}'s Notes")
            self.viewNotes[i].setStyleSheet(self.styles["noteButton"])
            self.viewNotes[i].setFixedSize(200, 40)
            self.viewNotes[i].clicked.connect(self.msgBox)
            self.buttonLayout.addWidget(self.viewNotes[i])
            
            self.saveNote[i] = QPushButton(groupBox)
            self.saveNote[i].setText(f"Save Note")
            self.saveNote[i].setStyleSheet(self.styles["noteButton"])
            self.saveNote[i].setFixedSize(200, 40)
            self.saveNote[i].clicked.connect(self.saveBNote)
            self.buttonLayout.addWidget(self.saveNote[i])
            
            self.behaviourLayout.addLayout(self.buttonLayout)
                      
            self.top_layout.addWidget(groupBox)
        
        self.top_widget.setLayout(self.top_layout)
        self.scrollArea.setWidget(self.top_widget)
        self.grid.addLayout(self.classLayout, 1, 1, 30, 30, Qt.AlignCenter)
        
    
    def msgBox(self):
        sender = self.sender()
        for i in range(0, self.classSize):
            if self.viewNotes[i] == sender:
                buttonNum = i
        name = self.students[buttonNum]
        
        #get studentClassId
        self.getScId(name)
        studentNote = db.getNote(self.scId)
        stuNote = QDialog()
        stuNoteLabel = QLabel(f"{name}'s Notes:\n{studentNote}", stuNote)
        stuNoteLabel.move(20, 20)
        stuNote.resize(1000, 400)
        stuNote.setWindowTitle(f"{name}'s Notes")
        stuNote.setWindowModality(Qt.ApplicationModal)
        stuNote.exec_()
        
         
    def saveBNote(self):
        sender = self.sender()
        for i in range(0, self.classSize):
            if self.saveNote[i] == sender:
                noteNum = i
        if self.behaviourNote[noteNum].toPlainText() == "":
            self.studentNote = ""
            noNote = QMessageBox()
            noNote.setWindowTitle("Error")
            noNote.setIcon(QMessageBox.Warning)
            noNote.setText("Please write a behaviour note before saving")
            noNote.setStandardButtons(QMessageBox.Ok)
            noNote.exec_()  
        else:
            self.studentNote = (f"{self.behaviourNote[noteNum].toPlainText()}")
            self.behaviourNote[noteNum].clear()
            
        stuNames = db.getStudents(self.className)
        stuName = stuNames[noteNum]
        self.updateNote(stuName)

            
    def updateNote(self, name):
        self.getScId(name)
        #insert note into database
        db.insertNote(self.studentNote, self.scId)
        
    def getScId(self, name):
        cId = db.getClassId(self.className)
         
        #get student first and last name to get studentId  
        firstLast = name.split()
        first = firstLast[0]
        last = firstLast[1]
        
        sId = db.getStudentId(first, last)
    
        scId = db.getStudentClassId(sId, cId)
        self.scId = scId
                    


def main():
    appGui = QApplication(sys.argv)
    cm = ClassroomManager()
    screen = appGui.primaryScreen()
    print('Screen: %s' % screen.name())
    size = screen.size()
    print('Size: %d x %d' % (size.width(), size.height()))
    rect = screen.availableGeometry()
    print('Available: %d x %d' % (rect.width(), rect.height()))
    cm.setFixedSize(1920, 1040)
    cm.showMaximized()
    sys.exit(appGui.exec_()) 
    
    
if __name__ == '__main__':
    main()