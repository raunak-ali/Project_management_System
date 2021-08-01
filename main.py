import sys
from PyQt5 import QtCore, QtGui, QtWidgets,QtSql
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtSql import QSqlQueryModel,QSqlDatabase,QSqlQuery
from project import Ui_MainWindow
import sqlite3
class MainWindow:
	def __init__(self):
		self.main_win=QMainWindow()
		self.ui=Ui_MainWindow()
		self.ui.setupUi(self.main_win)
		self.ui.stackedWidget.setCurrentWidget(self.ui.home)
		regex=QtCore.QRegExp("[a-z-A-Z_]+")
		validator = QtGui.QRegExpValidator(regex)
		reegex=QtCore.QRegExp("[0-9_]+")
		vaalidator = QtGui.QRegExpValidator(reegex)
		

		self.ui.lineEdit_6.setValidator(validator)
		self.ui.name_3.setValidator(validator)
		self.ui.proj1_2.setValidator(validator)
		self.ui.proj2_2.setValidator(validator)
		self.ui.lineEdit.setValidator(vaalidator)
		self.ui.lineEdit_5.setValidator(vaalidator)
		self.ui.register_3.clicked.connect(self.showregister)
		self.ui.loggin.clicked.connect(self.showlogin)
		self.ui.conatct_2.clicked.connect(self.showcontact)
		self.ui.FAQ_2.clicked.connect(self.showfaq)
		self.ui.home_2.clicked.connect(self.show)
		self.ui.login_2.clicked.connect(self.showproject)
		self.ui.pro1.clicked.connect(self.showcalendera)
		self.ui.pro2.clicked.connect(self.showcalenderb)
		self.ui.save.clicked.connect(self.save)
		#self.ui.save.clicked.connect(self.saved)
		self.ui.editdis.clicked.connect(self.discrip)
		self.ui.editfile.clicked.connect(self.edi)
		self.ui.savefile.clicked.connect(self.fle)
		self.ui.bullets.clicked.connect(self.bulletList)
		self.ui.numbl.clicked.connect(self.numberList)
		self.ui.bold.clicked.connect(self.bold)
		self.ui.italic.clicked.connect(self.italic)
		self.ui.strike.clicked.connect(self.strike)
		self.ui.underline.clicked.connect(self.underline)
		self.ui.bullets_2.clicked.connect(self.bulletList2)
		self.ui.numbl_2.clicked.connect(self.numberList2)
		self.ui.bold_2.clicked.connect(self.bold2)
		self.ui.italic_2.clicked.connect(self.italic2)
		self.ui.strike_2.clicked.connect(self.strike2)
		self.ui.underline_2.clicked.connect(self.underline2)
		self.ui.pushButton_6.clicked.connect(self.showday)
		self.ui.pushButton_5.clicked.connect(self.showproject)
		self.ui.home_2.clicked.connect(self.show_home)
		
		self.ui.fontsize_2.valueChanged.connect(lambda size: self.ui.textEdit_2.setFontPointSize(size))

		self.ui.fontsize.valueChanged.connect(lambda size: self.ui.textEdit.setFontPointSize(size))
		
	def showdialog(self):
		self.msg = QMessageBox()
		self.msg.setIcon(QMessageBox.Information)
		self.msg.setText("YOU HAVE LEFT SOME ENTRY FIELDS EMPTY")
		self.msg.setInformativeText("MAKE SURE")
		self.msg.setWindowTitle("Cant proceed")
		self.msg.setDetailedText("check if you filled all the fields")
		self.msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
		x=self.msg.exec_()
	def showdialogb(self):
		self.msg = QMessageBox()
		self.msg.setIcon(QMessageBox.Information)
		self.msg.setText("user already registered")
		self.msg.setInformativeText("chooose a different password")
		self.msg.setWindowTitle("Cant proceed")
		self.msg.setDetailedText("the password you wrote is in already use thus cant be used for urself")
		self.msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
		x=self.msg.exec_()
	def showdialogc(self):
		self.msg = QMessageBox()
		self.msg.setIcon(QMessageBox.Information)
		self.msg.setText("password never registered")
		self.msg.setInformativeText("please enter a valid username and password")
		self.msg.setWindowTitle("Cant proceed")
		self.msg.setDetailedText("the password you wrote is not registered..please recheck or register with a new one")
		self.msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
		x=self.msg.exec_()
	def showdialogd(self):
		self.msg = QMessageBox()
		self.msg.setIcon(QMessageBox.Information)
		self.msg.setText("saved")
		self.msg.setInformativeText("your data is saved")
		self.msg.setWindowTitle("proceed")
		self.msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
		x=self.msg.exec_()
	def save(self):
		if (self.ui.lineEdit.text() and self.ui.name_3.text() and self.ui.proj1_2.text()  and self.ui.proj2_2.text()):
			self.conn=sqlite3.connect('pms1.db')
			self.c=self.conn.cursor()
			print("saveing")
			self.c.execute("SELECT password,* FROM pms1 WHERE password = " + self.ui.lineEdit.text())#imp 
			#self.c.execute("SELECT password,*FROM pms1 WHERE password = "+self.ui.lineEdit_5.text())
			self.res = self.c.fetchone()
			print("saviing")
			if self.res == None:
				print("saving")
				self.c.execute("""INSERT INTO pms1 VALUES(:password,:username,:project1,:project2)""",
				 	{'password':self.ui.lineEdit.text(),'username':self.ui.name_3.text(),'project1':self.ui.proj1_2.text(),'project2':self.ui.proj2_2.text()})
				self.conn.commit()
				self.saved()
				self.showdialogd()
			else:
				self.showdialogb()
		else:
			self.showdialog()
	def saved(self):
		if (self.ui.lineEdit.text() and self.ui.name_3.text() and self.ui.proj1_2.text() and self.ui.proj2_2.text()) :
			self.conn=sqlite3.connect('pms1.db')
			self.c=self.conn.cursor()
			self.c.execute("SELECT password,*FROM pms1 WHERE password = "+self.ui.lineEdit.text())#imp 
			#self.c.execute("SELECT password,*FROM pms1 WHERE password = "+self.ui.lineEdit_5.text())
			#c.execute("SELECT *FROM pms1")#imp 
			self.rows = self.c.fetchall()
			for self.row in self.rows:
				self.ne=self.row[3]
				self.re=self.row[4]
				self.conn=sqlite3.connect(self.row[3]+".db")
				self.c=self.conn.cursor()
				self.c.execute(""" CREATE TABLE """ +self.row[3]+"""(
					day INTEGER,
					discription TEXT,
					file BLOB
					)""")
				self.conn.commit()
				self.conn=sqlite3.connect(self.row[3]+".db")
				self.c=self.conn.cursor()
				self.n=1
				for self.n in range(1,31):
					def convertToBinaryData(filename):
					# Convert digital data to binary format
						with open(filename, 'rb') as file:
							blobData = file.read()
						return blobData
					self.f=open("C:/Users/Sharique/Desktop/raunak stuff/main/New folder/"+str(self.row[3])+""+str(self.n)+".txt","w+")
					self.resumeFile="C:/Users/Sharique/Desktop/raunak stuff/main/New folder/"+str(self.row[3])+""+str(self.n)+".txt"
					self.resume =convertToBinaryData(self.resumeFile)
					self.c.execute("""INSERT INTO """+self.row[3]+""" VALUES(:day,:discription,:file)""",
                                                    		{'day':str(self.n),'discription':"discription",'file':self.resume})
					self.conn.commit()
                   
			self.conn=sqlite3.connect(self.row[4]+".db")
			self.c=self.conn.cursor()
			self.c.execute(""" CREATE TABLE """ +self.row[4]+"""(
				day INTEGER,
				discription TEXT,
				file BLOB
			)""")
			self.conn.commit()
			self.conn=sqlite3.connect(self.row[4]+".db")
			self.c=self.conn.cursor()
			self.n=1
			for self.n in range(1,31):
				def convertToBinaryData(filename):
					# Convert digital data to binary format
						with open(filename, 'rb') as file:
							blobData = file.read()
						return blobData
				self.f=open("C:/Users/Sharique/Desktop/raunak stuff/main/New folder/"+str(self.row[4])+""+str(self.n)+".txt","w+")
				self.resumeFile="C:/Users/Sharique/Desktop/raunak stuff/main/New folder/"+str(self.row[4])+""+str(self.n)+".txt"	
				self.resume = convertToBinaryData(self.resumeFile)
				self.c.execute(""" INSERT INTO """+self.row[4]+""" VALUES(:day,:discription,:file)""",
                                	                {'day':str(self.n),'discription':"discription",'file':self.resume})
				self.conn.commit()
		else:
			print("nopes 2")      
		
		
	def showregister(self):
		self.ui.stackedWidget.setCurrentWidget(self.ui.register_2)
	def showlogin(self):
		self.ui.textEdit.clear()
		self.ui.stackedWidget.setCurrentWidget(self.ui.login)
	def showcontact(self):
		self.ui.stackedWidget.setCurrentWidget(self.ui.conatct)
	def showfaq(self):
		self.ui.stackedWidget.setCurrentWidget(self.ui.FAQ)
	def show(self):
		self.main_win.show()
	def show_home(self):
		self.ui.stackedWidget.setCurrentWidget(self.ui.home)
	def showproject(self):
		if self.ui.lineEdit_5.text(): 
			self.ui.textEdit.clear()
			self.ui.stackedWidget.setCurrentWidget(self.ui.project)
			self.conn=sqlite3.connect('pms1.db')
			self.c=self.conn.cursor()
			self.c.execute("SELECT password,*FROM pms1 WHERE password = "+self.ui.lineEdit_5.text())#imp
			self.res = self.c.fetchone()
			print("saviing")
			if self.res == None: 
			#c.execute("SELECT *FROM pms1")#imp 
				self.showdialogc()
			else:
				self.c.execute("SELECT password,*FROM pms1 WHERE password = "+self.ui.lineEdit_5.text())
				self.rows = self.c.fetchall()
				print(self.rows)
				for self.row in self.rows:
					self.ui.pro1.setText(self.row[3])
					self.ui.pro2.setText(self.row[4])
				self.conn.commit()
				self.conn.close()
			
				
		else:
			self.showdialog()
	def showcalenderb(self):
		self.ui.textEdit.clear()
		self.ui.stackedWidget.setCurrentWidget(self.ui.cal)
		self.ui.calendarWidget.clicked[QtCore.QDate].connect(self.showday)
		self.full=self.ui.calendarWidget.selectedDate()
		self.date=self.full.day()
		print(self.date)
		self.ui.projects.setText(self.ui.pro2.text())
	def showcalendera(self):
		self.ui.textEdit.clear()
		self.ui.stackedWidget.setCurrentWidget(self.ui.cal)
		self.ui.calendarWidget.clicked[QtCore.QDate].connect(self.showday)
		self.full=self.ui.calendarWidget.selectedDate()
		self.date=self.full.day()
		print(self.date)
		self.ui.projects.setText(self.ui.pro1.text())
	def showday(self):
		self.ui.textEdit_2.clear()
		self.ui.textEdit.clear()
		self.ui.stackedWidget.setCurrentWidget(self.ui.day)
		self.full=self.ui.calendarWidget.selectedDate()
		self.date=self.full.day()
		print(self.date)
		global disp
		self.conn=sqlite3.connect(self.ui.projects.text()+'.db')
		self.c=self.conn.cursor()
		self.c.execute("SELECT day,*FROM "+self.ui.projects.text()+" WHERE day = "+str(self.date))#imp 
		self.rats = self.c.fetchall()
		print("loading")
		print(self.rats)
		for self.rat in self.rats:
			print("b")
			self.i=self.rat[1]
			disp = self.rat[2]
			self.f=self.rat[3]
			print("c")
		print("d")
		self.ui.date.setText("Date :- "+str(self.date))
		self.ui.date_3.setText("Date :- "+str(self.date))
		self.conn.commit()
		self.conn.close()
		self.ui.textEdit.setText(disp)
		return disp
		
		
	def discrip(self):
		self.conn=sqlite3.connect(self.ui.projects.text()+'.db')
		self.c=self.conn.cursor()
		print("saving")
		self.c.execute("""UPDATE """+self.ui.projects.text()+""" SET day=:day,discription=:discription WHERE day = """+(str(self.date)),
			{'day':str(self.date),'discription':self.ui.textEdit.toHtml()})#imp 
		self.conn.commit()
		self.c.execute("SELECT*FROM "+self.ui.projects.text())
		self.rows=self.c.fetchall()
		print(self.rows)
		self.conn.commit()
		self.conn.close()
		self.showdialogd()
	def edi(self):
		self.ui.textEdit_2.clear()
		self.ui.stackedWidget.setCurrentWidget(self.ui.file)
		self.resumeFile="C:/Users/Sharique/Desktop/raunak stuff/main/New folder/"+str(self.ui.projects.text())+""+str(self.date)+".txt"
		self.v=open(self.resumeFile,'r')
		self.h=self.v.read()
		print("Stored blob data into: ")
		self.ui.textEdit_2.setText((self.h))
	def fle(self):
		self.resumeFile="C:/Users/Sharique/Desktop/raunak stuff/main/New folder/"+str(self.ui.projects.text())+""+str(self.date)+".txt"
		self.e=open(self.resumeFile,'w')
		self.e.write(self.ui.textEdit_2.toHtml())
		self.e.close()
		print("savedddd")
		self.showdialogd()
	def numberList(self):

        	self.cursor = self.ui.textEdit.textCursor()

        	# Insert list with numbers
        	self.cursor.insertList(QtGui.QTextListFormat.ListDecimal)
	def bulletList(self):

        	self.cursor = self.ui.textEdit.textCursor()

        # Insert bulleted list
        	self.cursor.insertList(QtGui.QTextListFormat.ListDisc)
	
	def bold(self):

        	if self.ui.textEdit.fontWeight() == QtGui.QFont.Bold:

            		self.ui.textEdit.setFontWeight(QtGui.QFont.Normal)

        	else:

            		self.ui.textEdit.setFontWeight(QtGui.QFont.Bold)

	def italic(self):

        	self.state = self.ui.textEdit.fontItalic()

        	self.ui.textEdit.setFontItalic(not self.state)

	def underline(self):
	
        	self.state = self.ui.textEdit.fontUnderline()

        	self.ui.textEdit.setFontUnderline(not self.state)
	def strike(self):

        # Grab the text's format
        	self.fmt = self.ui.textEdit.currentCharFormat()

        # Set the fontStrikeOut property to its opposite
        	self.fmt.setFontStrikeOut(not self.fmt.fontStrikeOut())

        # And set the next char format
        	self.ui.textEdit.setCurrentCharFormat(self.fmt)
############################################################################
	def numberList2(self):

        	self.cursor = self.ui.textEdit_2.textCursor()

        	# Insert list with numbers
        	self.cursor.insertList(QtGui.QTextListFormat.ListDecimal)
	def bulletList2(self):

        	self.cursor = self.ui.textEdit_2.textCursor()

        # Insert bulleted list
        	self.cursor.insertList(QtGui.QTextListFormat.ListDisc)
	
	def bold2(self):

        	if self.ui.textEdit_2.fontWeight() == QtGui.QFont.Bold:

            		self.ui.textEdit_2.setFontWeight(QtGui.QFont.Normal)

        	else:

            		self.ui.textEdit_2.setFontWeight(QtGui.QFont.Bold)

	def italic2(self):

        	self.state = self.ui.textEdit_2.fontItalic()

        	self.ui.textEdit_2.setFontItalic(not self.state)

	def underline2(self):
	
        	self.state = self.ui.textEdit_2.fontUnderline()

        	self.ui.textEdit_2.setFontUnderline(not self.state)
	def strike2(self):

        # Grab the text's format
        	self.fmt = self.ui.textEdit_2.currentCharFormat()

        # Set the fontStrikeOut property to its opposite
        	self.fmt.setFontStrikeOut(not self.fmt.fontStrikeOut())

        # And set the next char format
        	self.ui.textEdit_2.setCurrentCharFormat(self.fmt)


	

if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	main_win=MainWindow()
	main_win.show()
	sys.exit(app.exec_())
