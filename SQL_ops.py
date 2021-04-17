import mysql.connector
from mysql.connector import Error


class SQLObj:

    def __init__(self, host_name, user_name, user_password):
        """

        """
        self.host_name = host_name
        self.user_name = user_name
        self.user_password = user_password
        self.db_name = "education_quality"

        connection = self.create_connection(self.host_name, self.user_name, self.user_password)
        create_db_query = "CREATE DATABASE IF NOT EXISTS " + self.db_name 
        self.create_database(connection, create_db_query)

        connection = self.create_db_connection(self.host_name, self.user_name, self.user_password, self.db_name)
        create_tables_query = """
        CREATE TABLE IF NOT EXISTS students(
            id INT NOT NULL AUTO_INCREMENT,
            name_surname VARCHAR(50) NOT NULL,
            faculty INT NOT NULL,
            email VARCHAR(255) NOT NULL,
            year INT,
            PRIMARY KEY (id)
        );
        CREATE TABLE IF NOT EXISTS teachers(
            id INT NOT NULL AUTO_INCREMENT,
            name_surname VARCHAR(50) NOT NULL,
            pic_url VARCHAR(255),
            text_desc VARCHAR(1500),
            teaches VARCHAR(255),
            PRIMARY KEY (id)
        );
        CREATE TABLE IF NOT EXISTS comments(
            id INT NOT NULL AUTO_INCREMENT,
            date_time INT,
            is_negative BOOL,
            student_id INT NOT NULL,
            teacher_id INT NOT NULL,
            rate1 INT NOT NULL,
            rate2 INT NOT NULL,
            rate3 INT NOT NULL,
            rate4 INT NOT NULL,
            text VARCHAR(1500),
            PRIMARY KEY (id),
            FOREIGN KEY (student_id) REFERENCES students(id),
            FOREIGN KEY (teacher_id) REFERENCES teachers(id)
        );
        """
        self.create_table(connection, create_tables_query)

    @staticmethod
    def create_connection(host_name, user_name, user_password):
        connection = None
        try:
            connection = mysql.connector.connect(
                host=host_name,
                user=user_name,
                passwd=user_password,
            )
            print("Connection to MySQL successful")
        except Error as e:
            print(f"The error '{e}' occurred")

        return connection

    @staticmethod
    def create_database(connection, query):
        cursor = connection.cursor()
        try:
            cursor.execute(query)
            print("Database created successfully")
        except Error as e:
            print(f"The error '{e}' occurred")
        
    @staticmethod
    def create_table(connection, query):
        cursor = connection.cursor()
        try:
            cursor.execute(query)
            # connection.commit()
            print("Table/s created successfully")
        except Error as e:
            print(f"The error '{e}' occurred")

    @staticmethod
    def execute_query(connection, query):
        cursor = connection.cursor()
        try:
            cursor.execute(query)
            connection.commit()
            print("Query executed successfully")
        except Error as e:
            print(f"The error '{e}' occurred")

    @staticmethod
    def execute_read_query(connection, query):
        cursor = connection.cursor()
        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as e:
            print(f"The error '{e}' occurred")

    @staticmethod
    def create_db_connection(host_name, user_name, user_password, db_name):
        connection = None
        try:
            connection = mysql.connector.connect(
                host=host_name,
                user=user_name,
                passwd=user_password,
                database=db_name
            )
            print("create_db_connection")
        except Error as e:
            print(f"The error '{e}' occurred")

        return connection

    def insert_students(self, val_tupp, col_tupp = ("name_surname", "faculty", "email", "year")):
        col = '('
        for c in col_tupp:
            col += c + ', '
        col = col[:-2] + ')'
        connection = self.create_db_connection(self.host_name, self.user_name, self.user_password, self.db_name)
        student_query = "INSERT INTO students " + str(col) + " VALUES " + str(val_tupp) + ';'
        self.execute_query(connection, student_query)

    def insert_teachers(self, val_tupp, col_tupp = ("name_surname", "url_pic", "text_desc", "teaches")):
        col = '('
        for c in col_tupp:
            col += c + ', '
        col = col[:-2] + ')'

        connection = self.create_db_connection(self.host_name, self.user_name, self.user_password, self.db_name)
        teacher_query = "INSERT INTO teachers " + str(col) + " VALUES " + str(val_tupp) + ';'
        self.execute_query(connection, teacher_query)

    def insert_comments(self, val_tupp, col_tupp = ("name", "surname")):
        col = '('
        for c in col_tupp:
            col += c + ', '
        col = col[:-2] + ')'

        connection = self.create_db_connection(self.host_name, self.user_name, self.user_password, self.db_name)
        comment_query = "INSERT INTO comments " + str(col) + " VALUES " + str(val_tupp) + ';'
        self.execute_query(connection, comment_query)

    def get_teachers(self, col_names = ('*')):

        connection = self.create_db_connection(self.host_name, self.user_name, self.user_password, self.db_name)
        if isinstance(col_names, tuple):
            cols = ''
            for col_name in col_names:
                cols = cols + col_name + ', '
                cols = cols[:-2]
        else:
            cols = col_names

        get_teachers_query = "SELECT " + cols + " FROM teachers"
        return self.execute_read_query(connection, get_teachers_query)

    def get_students(self, col_names = ('*')):

        connection = self.create_db_connection(self.host_name, self.user_name, self.user_password, self.db_name)
        if isinstance(col_names, tuple):
            cols = ''
            for col_name in col_names:
                cols = cols + col_name + ', '
                cols = cols[:-2]
        else:
            cols = col_names

        get_students_query = "SELECT " + cols + " FROM students"
        return self.execute_read_query(connection, get_students_query)

    def get_comments(self, col_names = ('*')):

        connection = self.create_db_connection(self.host_name, self.user_name, self.user_password, self.db_name)
        if isinstance(col_names, tuple):
            cols = ''
            for col_name in col_names:
                cols = cols + col_name + ', '
                cols = cols[:-2]
        else:
            cols = col_names

        get_comments_query = "SELECT " + cols + " FROM comments"
        return self.execute_read_query(connection, get_comments_query)
