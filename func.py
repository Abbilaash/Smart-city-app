import mysql.connector
from requests_html import HTMLSession
import requests 
import threading
from bs4 import BeautifulSoup 
from urllib.request import urlopen


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

def GetNews():
    url = "https://www.deccanherald.com/tags/coimbatore"
    news_list = []
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content,'html.parser')
        news_divs = soup.find_all('div', class_='-bdFE')
        for div in news_divs:
            news_text = div.find('h1').text.strip()
            news_url = div.find('a')['href']
            image = div.find('img')['data-src']
            date = div.find('div',class_='story-date IWO4Q').text
            news_list.append([news_text,news_url,image,date])
    return news_list