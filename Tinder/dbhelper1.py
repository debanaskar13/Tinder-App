import mysql.connector


class DBhelper:

    def __init__(self):
        # to connect to the database
        try :
            self.conn = mysql.connector.connect(host = 'localhost',user = 'root',password = '',database ='finder')
            self.mycursor = self.conn.cursor()
            print("connected to DB")
        except Exception as e :
            print(e)

    def check_login(self,email,password):
        self.mycursor.execute(f"SELECT * FROM users WHERE email LIKE '{email}' AND password LIKE '{password}'")
        data = self.mycursor.fetchall()

        return data

    def insert_user(self,name,email,password,filename=None):

        try :
            if filename!=None:
                self.mycursor.execute(f"INSERT INTO users (user_id,name,email,password,dp) VALUES (NULL,'{name}','{email}','{password}','{filename}')")
                self.conn.commit()
                return 1
            else:
                self.mycursor.execute(f"INSERT INTO users (user_id,name,email,password) VALUES (NULL,'{name}','{email}','{password}')")
                self.conn.commit()
                return 1
        except Exception as e :
            return e

    def update_profile(self,user_id,info):
        try:
            self.mycursor.execute(f'UPDATE users SET bio="{info[0]}" ,age={info[1]} ,gender="{info[2]}",city="{info[3]}" WHERE user_id={user_id}')
            self.conn.commit()
            return 1
        except :
            return 0
    
    def update_dp(self,user_id,filename):
        try:
            self.mycursor.execute(f"UPDATE users SET dp='{filename}' WHERE user_id={user_id}")
            self.conn.commit()
            return 1
        except Exception as e :
            print(e)

    def change_password(self,user_id,password):
        try :
            self.mycursor.execute(f'UPDATE users SET password="{password}" WHERE user_id={user_id}')
            self.conn.commit()
            return 1
        except :
            return 0

    def fetch_others(self,user_id):
        self.mycursor.execute(f"SELECT * FROM users WHERE user_id NOT LIKE {user_id}")
        data=self.mycursor.fetchall()
        return data
        
    def propose(self,romeo_id,juliet_id):
        self.mycursor.execute(f"SELECT * FROM proposals WHERE romeo_id ={romeo_id} AND juliet_id ={juliet_id}")
        data=self.mycursor.fetchall()
        if len(data)!=0:
            return -1
        else:
            try:
                self.mycursor.execute(f"INSERT INTO proposals (proposal_id,romeo_id,juliet_id) values (NULL,{romeo_id},{juliet_id})")
                self.conn.commit()
                return 1
            except:
                return 0

    def view_proposals(self,romeo_id):
        self.mycursor.execute(f"SELECT * FROM proposals JOIN users ON users.user_id=proposals.juliet_id WHERE romeo_id={romeo_id}")
        data=self.mycursor.fetchall()
        return data

    def view_requests(self,juliet_id):
        self.mycursor.execute(f"SELECT * FROM proposals JOIN users ON users.user_id=proposals.romeo_id WHERE juliet_id={juliet_id}")
        data=self.mycursor.fetchall()
        return data