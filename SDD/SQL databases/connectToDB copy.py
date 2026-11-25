# Test the SQL connector package

import mysql.connector

conn = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='save_file_scores')
cursor = conn.cursor()

cursor.execute("""UPDATE `save_file_scores` SET `Score`='0' WHERE 1""")
conn.commit()
cursor.execute("""SELECT * FROM save_file_scores""")

for row in c:
  print('Save_file : ', row[0])
  print('Score : ', row[1])
  print('Score : ', row[0])
  print('Score : ', row[1])


class data():
  def __init__(self):
    self.__savefile_name = 'nameth'
    self.__savefile_score = 0

  def getName(self):
    return self.__savefile_name

  def setName(self, name):
    self.__savefile_name = name

  def getScore(self):
    return self.__savefile_score
  
  def setScore(self, score):
    self.__savefile_score = score

Savefiles = [data() for i in range(10)]

for i in range(len(Savefiles)):
  print(Savefiles[i].getName)
  print()

cursor.close()