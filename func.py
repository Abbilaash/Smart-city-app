import mysql.connector



host="localhost"
user="abbi"
password="root"
database="smart-city-app"


def retreive_user_data(username,password):
    conn = mysql.connector.connect(
        host=host,user=user,password=password,database=database
    )
    cursor = conn.cursor()
    cursor.execute("SELECT `username`, `name`, `password`, `aadhaar`,`phonenumber`,`gmail` FROM `users` WHERE username=%s and password=%s",(username,password,))
    data = cursor.fetchall()
    cursor.close()
    conn.commit()
    conn.close()
    
    return data[0] #-> (username,name,password,aadhaar,phonenumber,gmail)


def add_user(username,name,passs,aadhaar,phonenumber,gmail):
    conn = mysql.connector.connect(host=host,user=user,password=password,database=database)
    cursor = conn.cursor()
    query = 'INSERT INTO users(username,name,password,aadhaar,phonenumber,gmail) VALUES (%s,%s,%s,%s,%s,%s)'
    cursor.execute(query,(username,name,passs,aadhaar,phonenumber,gmail,))
    conn.commit()
    cursor.close()
    conn.close()


#add_user('abbi','abbi','abbi',123456789011,8667093591,'abilaashat@gmail.com')
#retreive_user_data('abbi','abbi')

    
def GetChat():
    conn = mysql.connector.connect(host=host,user=user,password=password,database=database)
    cursor = conn.cursor(buffered=True)
    query = 'SELECT sno,sender_name,message FROM chat'
    cursor.execute(query)
    data = cursor.fetchmany(100)
    conn.commit()
    cursor.close()
    conn.close()
    return data

def SendMessage(sender_name,message):
    conn = mysql.connector.connect(host=host,user=user,password=password,database=database)
    cursor = conn.cursor()
    query = 'INSERT INTO chat(sender_name,message) VALUES (%s,%s)'
    cursor.execute(query,(sender_name,message,))
    conn.commit()
    cursor.close()
    conn.close()