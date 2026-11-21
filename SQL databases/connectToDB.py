# Test the SQL connector package

import mysql.connector

con = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='save_file_scores')
c = con.cursor()

c.execute("""UPDATE `save_file_scores` SET `Score`='0' WHERE 1""")
con.commit()
c.execute("""SELECT * FROM save_file_scores""")

for row in c:
  print('Save_file : ', row[0])
  print('Score : ', row[1])   

c.close()