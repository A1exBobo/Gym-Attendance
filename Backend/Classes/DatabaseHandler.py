import sqlite3

class DatabaseHandler:
    def __init__(self):
        self.conn = sqlite3.connect("../Data/Database.sqlite")

    def CreateTable(self):
            cursor = self.conn.cursor();

            create_table = "CREATE TABLE IF NOT EXISTS GYMATTENDANCE(Data date CHECK(Data <= current_date) );"

            cursor.execute(create_table);

            self.conn.commit();
    

    def InsertDate(self,date):
            cursor = self.conn.cursor();

            insert_query = f"INSERT INTO GYMATTENDANCE VALUES({date});"
            print(insert_query)
            cursor.execute(insert_query);

            self.conn.commit();

    def DeleteRow(self,date):
            cursor = self.conn.cursor();

            delete_query = f"DELETE FROM GYMATTENDANCE WHERE Data = ({date});"

            cursor.execute(delete_query);

            self.conn.commit();

    def CloseDb(self):
          self.conn.close()




#scurt test
db = DatabaseHandler()
db.CreateTable()
db.InsertDate(" '2006-11-22' ")         #YYYY-MM-DD format 
db.InsertDate(" '2026-09-23' ")
db.DeleteRow(" '2006-11-22' ")
db.CloseDb()

## SOURCE: https://www.sqlitetutorial.net/sqlite-python/creating-database/