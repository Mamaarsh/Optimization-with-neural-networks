import pymysql
import random

class Data:
    def __init__(self):
        self.conn = pymysql.connect(
            host='localhost',
            user='root',
            password='M@m@rsh!a1384_',
            database='OSproj'
        )
        self.cursor = self.conn.cursor()

    def clear_table(self):
        self.cursor.execute("DELETE FROM dataset")
        self.conn.commit()

    def insert_data(self, arrival_time_1, arrival_time_2, arrival_time_3, arrival_time_4,
                    burst_time_1, burst_time_2, burst_time_3, burst_time_4):
        query = '''INSERT INTO dataset (
            arrival_time_1, arrival_time_2, arrival_time_3, arrival_time_4,
            burst_time_1, burst_time_2, burst_time_3, burst_time_4
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'''

        values = (
            arrival_time_1, arrival_time_2, arrival_time_3, arrival_time_4,
            burst_time_1, burst_time_2, burst_time_3, burst_time_4
        )

        self.cursor.execute(query, values)
        self.conn.commit()

    def get_data(self):
        query = "SELECT arrival_time_1, arrival_time_2, arrival_time_3, arrival_time_4, burst_time_1, burst_time_2, burst_time_3, burst_time_4 FROM dataset"
        self.cursor.execute(query)
        return self.cursor.fetchall()

def generate_random_data(data_obj, rows=1200):
    data_obj.clear_table()
    for _ in range(rows):
        data_obj.insert_data(
            random.randint(0, 20), random.randint(0, 20),
            random.randint(0, 20), random.randint(0, 20),
            random.randint(1, 20), random.randint(1, 20),
            random.randint(1, 20), random.randint(1, 20)
        )

if __name__ == "__main__":
    db = Data()
    generate_random_data(db, rows=1200)