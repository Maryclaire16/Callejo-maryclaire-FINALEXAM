from connector import Connector

class Students:

    def get_all():
        query = "SELECT * FROM students"

        Connector.cursor.execute(query)
        result = Connector.cursor.fetchall()

        return result