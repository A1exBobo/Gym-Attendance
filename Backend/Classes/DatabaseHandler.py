import sqlite3

class DatabaseHandler:
    def __init__(self):
        self.conn = sqlite3.connect("../Data/Database.sqlite")

    def CreateTable(self):
            cursor = self.conn.cursor();

            create_table = "CREATE TABLE GYMATTENDANCE(Data date CHECK(Data <= current_date) );"

            cursor.execute(create_table);

            self.conn.commit();
    

    def InsertDate(self):
            cursor = self.conn.cursor();

            insert_query = "INSERT INTO GYMATTENDANCE VALUES(CURRENT_DATE);"

            cursor.execute(insert_query);

            self.conn.commit();

    def DeleteRow(self):
            cursor = self.conn.cursor();

            delete_query = "DELETE FROM GYMATTENDANCE WHERE Data = CURRENT_DATE;"

            cursor.execute(delete_query);

            self.conn.commit();

    def CloseDb(self):
          self.conn.close()




#scurt test
db = DatabaseHandler()
db.InsertDate()
db.DeleteRow()
db.CloseDb()

## SOURCE: https://www.sqlitetutorial.net/sqlite-python/creating-database/