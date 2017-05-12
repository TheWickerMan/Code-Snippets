import time
import os

#Set to any subdirectory
DirectoryName="ChangeThisDirectoryName"

#Grabs dates
MonthYear = str(time.strftime("%m%Y"))
DayMonthYear = str(time.strftime("%d%m%Y"))

class Main():

	def Check(self):
		#Uncomment for a monthly directory
		'''
		if os.path.isdir(DirectoryName+MonthYear)==False:
			self.MakeMonth()
		'''

		#Uncomment for a monthly file
		'''
		if os.path.isfile(DirectoryName+MonthYear)==False:
			self.MakeMonthPart()
		'''

		#Uncomment for a daily directory
		'''
		if os.path.isdir(DirectoryName+DayMonthYear)==False:
			self.MakeDay()
		'''

		#Uncomment for a daily file
		'''
		if os.path.isfile(DirectoryName+DayMonthYear)==False:
			self.MakeDayPart()
		'''

	def MakeMonthFull(self):
		os.makedirs(DirectoryName+MonthYear)
		self.MakeMonthPart()

	def MakeDayFull(self):
		os.makedirs(DirectoryName+DayMonthYear)
		self.MakeDayPart()

	def MakeMonthPart(self):
		open(DirectoryName+MonthYear,"w").close()

	def MakeDayPart(self):
		open(DirectoryName+DayMonthYear,"w").close()
