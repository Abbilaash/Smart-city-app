#Importing the needed modules
import customtkinter
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import mysql.connector 
import tkinter
import func
import os
import pickle,threading,socket
import tkintermapview
import base64,io
from urllib.request import urlopen
import webbrowser


global USER_DET
USER_DET = {}


window = customtkinter.CTk()
window.geometry('1550x1000')
window.state('zoomed')
window.resizable(0, 0)
window.title(" Coimbatore Smart App - CLAY")
window.configure(fg_color="white")


def App():
    # Define the main app frame
    global app
    app = customtkinter.CTkFrame(master=window,fg_color="white")
    app.place(x=0,y=0,relheight=1,relwidth=1)

    def dashboard_func():
        dashFrame = customtkinter.CTkFrame(master=window,fg_color="white")
        dashFrame.place(x=0,y=0,relheight=1,relwidth=1)

        side_options_frame = Frame(dashFrame, bg="white",width=200,height=65)
        side_options_frame.place(x=0,y=0)
        side_options_frame.pack_propagate(False)
        top_line = Canvas(side_options_frame, height=1, bg="MediumPurple2", highlightthickness=0)
        top_line.place(x=0,y=59,relwidth=1)
        top_navbar = Frame(dashFrame, bg="white",height=60)
        top_navbar.place(x=200,y=0,relwidth=1)
        top_line1 = Canvas(top_navbar, height=1, bg="MediumPurple1", highlightthickness=0)
        top_line1.place(x=0,y=59,relwidth=1)

        UserLogo_logo = ImageTk.PhotoImage(Image.open("A:\\PROJECTS\\Coimbatore-smart-city-app\\Smart-city-app\\assets\\user-logo.png").resize((50,50)))
        UserLogo_set_lbl1 = customtkinter.CTkLabel(master=top_navbar,image=UserLogo_logo,text="")
        UserLogo_set_lbl1.place(x=1060,y=0)
        LoggedUserName_lbl = customtkinter.CTkLabel(master=top_navbar,text=USER_DET['NAME'],
                                                    font=("yu gothic ui", 19,"bold"),text_color="black")
        LoggedUserName_lbl.place(x=1100,y=5)


        # smart city app logo setting
        '''codegram_logo1 = ImageTk.PhotoImage(Image.open("codegram-logo1.png").resize((180,58)))
        logo_set_lbl1 = customtkinter.CTkLabel(master=side_options_frame,image=codegram_logo1,text="")
        logo_set_lbl1.place(x=0,y=0)'''
    
        SideOptions_frame = customtkinter.CTkFrame(master=dashFrame,width=200,border_width=1,
                                                   border_color="white",
                                                   fg_color="white")
        SideOptions_frame.place(x=5,y=50,relheight=0.9)

        top_line = Canvas(dashFrame, width=0, bg="MediumPurple1", highlightthickness=0)
        top_line.place(x=250,y=60,relheight=1)

        def home_func():
            home_frame = customtkinter.CTkFrame(master=dashFrame,fg_color="white")
            home_frame.place(x=210,y=50,relheight=1,relwidth=1)

            customtkinter.CTkLabel(master=home_frame,text="News",font=("yu gothic ui", 25,"bold"),fg_color="white",bg_color="white",text_color="gray20").place(x=35,y=30)

            mainNewsDisplayFrame = customtkinter.CTkScrollableFrame(master=home_frame,width=750,fg_color="gray80")
            mainNewsDisplayFrame.place(x=30,y=70,relheight=0.85)

            # Fetching the message
            GetNews = func.GetNews()
            def openINST(event,url):
                # Opening the website in browser
                webbrowser.open("https://www.deccanherald.com"+url)

            for news in GetNews:
                new_Frame = customtkinter.CTkFrame(master=mainNewsDisplayFrame,height=200,width=680,fg_color="gray60",corner_radius=20,border_width=9,border_color="gray80")
                new_Frame.pack(anchor="nw")
                customtkinter.CTkLabel(master=new_Frame,font=("yu gothic ui", 17,"bold"),text=news[0],text_color="black",fg_color="gray60",wraplength=300,anchor='w').place(x=280,y=20)
                #customtkinter.CTkLabel(master=new_Frame,font=("yu gothic ui", 16),text=news[1],text_color="black",fg_color="gray60").place(x=20,y=60)
                customtkinter.CTkLabel(master=new_Frame,font=("yu gothic ui", 14,'bold'),text=news[3],text_color="gray30",fg_color="gray60").place(x=280,y=150)
                raw_data = urlopen(news[2]).read()
                pic = ImageTk.PhotoImage(Image.open(io.BytesIO(raw_data)).resize((300,200)))
                customtkinter.CTkLabel(master=new_Frame,image=pic,text="").place(x=20,y=20)
                new_Frame.bind('<Double-1>',lambda event, url=news[1] : openINST(event,url))

            # Display the population
            # Display the weather report
            
            




        def explore_func():
            # making the explore main frame
            explore_frame = customtkinter.CTkFrame(master=dashFrame,fg_color="white")
            explore_frame.place(x=210,y=50,relheight=1,relwidth=1)

            MapDisplayFrame = customtkinter.CTkFrame(master=explore_frame,height=800,fg_color="gray80",width=120)
            MapDisplayFrame.place(x=30,y=30)

            map_widget = tkintermapview.TkinterMapView(MapDisplayFrame, width=800, height=800, corner_radius=10)
            map_widget.place(x=0,y=0)
            map_widget.set_position(48.860381, 2.338594)  # Paris, France
            map_widget.set_zoom(15)






        def service_corner_func():
            servicecorner_frame = customtkinter.CTkFrame(master=dashFrame,fg_color="white")
            servicecorner_frame.place(x=210,y=50,relheight=1,relwidth=1)

            # Civil issue frame
            civil_frame = customtkinter.CTkFrame(master=servicecorner_frame,width=500,border_color="black",border_width=1,fg_color="white",corner_radius=10)
            civil_frame.place(x=40,y=30,relheight=0.85)
            customtkinter.CTkLabel(master=servicecorner_frame,height=30,font=("yu gothic ui", 17),width=90,corner_radius=20,text="CIVIL",fg_color="MediumPurple2",text_color="black").place(x=100,y=20)

            # Crime issue frame
            criminal_frame = customtkinter.CTkFrame(master=servicecorner_frame,width=500,border_color="black",border_width=1,fg_color="white",corner_radius=10)
            criminal_frame.place(x=580,y=30,relheight=0.85)
            customtkinter.CTkLabel(master=servicecorner_frame,height=30,font=("yu gothic ui", 17),width=90,corner_radius=20,text="CRIME",fg_color="MediumPurple2",text_color="black").place(x=630,y=20)





        def DM_func():
            chat_frame = customtkinter.CTkFrame(master=dashFrame,fg_color="white")
            chat_frame.place(x=210,y=50,relheight=1,relwidth=1)

            # The frame where chat activity takes place
            MailDisplayMain_frame = customtkinter.CTkFrame(master=chat_frame,height=800,fg_color="gray80",width=900)
            MailDisplayMain_frame.place(x=30,y=30)

            # Creating the chat display
            chatDisplayBoard = customtkinter.CTkScrollableFrame(master=MailDisplayMain_frame,fg_color="gray80",height=700,width=850,border_color="black",border_width=1)
            chatDisplayBoard.place(x=10,y=10)
            
            chat_history = func.GetChat() #(sno,sender_name,message)
            for i in chat_history:
                username = i[1]
                content = i[2]
                msgFrame = customtkinter.CTkFrame(master=chatDisplayBoard,width=700,fg_color="gray60",corner_radius=20,border_width=9,border_color="gray80")
                msgFrame.pack(anchor="nw")
                customtkinter.CTkLabel(master=msgFrame,font=("yu gothic ui", 15,"bold"),text=username,text_color="black",fg_color="gray60").place(x=15,y=10)
                customtkinter.CTkLabel(master=msgFrame,font=("yu gothic ui", 14),text=content,text_color="black",fg_color="gray60",width=600,anchor='nw').place(x=15,y=40)

            # Creating the send message function
            PORT = 5000 #listening port
            SERVER = "192.168.29.25" #server ip
            ADDRESS = (SERVER, PORT)
            client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

            def listen_for_messages_From_server(client):
                while True:
                    try:
                        message = client.recv(2048).decode('utf-8')
                        if message != "":
                            username = message.split("~")[0]
                            content = message.split("~")[1]
                            msgFrame = customtkinter.CTkFrame(master=chatDisplayBoard,width=700,fg_color="gray60",corner_radius=20,border_width=9,border_color="gray80")
                            msgFrame.pack(anchor="nw")
                            customtkinter.CTkLabel(master=msgFrame,font=("yu gothic ui", 15,"bold"),text=username,text_color="black",fg_color="gray60").place(x=15,y=10)
                            customtkinter.CTkLabel(master=msgFrame,font=("yu gothic ui", 14),text=content,text_color="black",anchor='nw',fg_color="gray60",width=600).place(x=15,y=40)

                        else:
                            print("Message received is empty!")
                    except:
                        print("[-] Connection closed!")
                        break
            
            def send_message():
                message = message_box.get("0.0",END)
                message_box.delete('0.0',END)
                try:
                    client.sendall(message.encode())
                    func.SendMessage(USER_DET['USERNAME'],message)
                except Exception as e:
                    print(e)

            def communicate_to_server(client):
                username = USER_DET['USERNAME']
                client.sendall(username.encode())
                threading.Thread(target=listen_for_messages_From_server,args=(client, )).start()


            try:
                client.connect(ADDRESS)
                print("Connected to server")
            except:
                print("Unable to connect to server!")

            communicate_to_server(client)

            message_box = customtkinter.CTkTextbox(master=MailDisplayMain_frame,width=700,height=50,border_color='black',border_width=1,font=("yu gothic ui", 15),text_color="black",corner_radius=8,fg_color="gray80")
            message_box.place(x=10,y=740)
            
            customtkinter.CTkButton(master=MailDisplayMain_frame,width=100,fg_color='green',text='SEND',command=send_message,font=("yu gothic ui", 19,'bold'),height=50,corner_radius=8).place(x=725,y=740)

            








        global file_path
        file_path = os.path.dirname(os.path.realpath(__file__))

        dashboard_btn_img = customtkinter.CTkImage(Image.open(file_path + "/assets/dashboard_icon.png"),size=(20,20))
        dashboard_btn = customtkinter.CTkButton(master=SideOptions_frame,command=home_func,anchor="sw",hover_color="MediumPurple2",image=dashboard_btn_img,fg_color="white",compound="left",height=40,text_color="black",font=("yu gothic ui", 19,"bold"),text="  Home",corner_radius=8)
        dashboard_btn.place(x=5,y=70,relwidth=0.95)

        dm_btn_img = customtkinter.CTkImage(Image.open(file_path + "/assets/chat-icon.png"),size=(22,22))
        dm_btn = customtkinter.CTkButton(master=SideOptions_frame,command=DM_func,anchor="sw",hover_color="MediumPurple2",image=dm_btn_img,fg_color="white",text_color="black",compound="left",height=40,font=("yu gothic ui", 19,"bold"),text="  Chat",corner_radius=8)
        dm_btn.place(x=5,y=130,relwidth=0.95)

        explore_btn_img = customtkinter.CTkImage(Image.open(file_path + "/assets/explore-icon.png"),size=(22,22))
        explore_btn = customtkinter.CTkButton(master=SideOptions_frame,command=explore_func,anchor="sw",hover_color="MediumPurple2",image=explore_btn_img,fg_color="white",text_color="black",compound="left",height=40,font=("yu gothic ui", 19,"bold"),text="  Maps",corner_radius=8)
        explore_btn.place(x=5,y=190,relwidth=0.95)

        servicecorner_btn_img = customtkinter.CTkImage(Image.open(file_path + "/assets/public-service.png"),size=(22,22))
        servicecorner_btn = customtkinter.CTkButton(master=SideOptions_frame,command=service_corner_func,anchor="sw",hover_color="MediumPurple2",image=servicecorner_btn_img,fg_color="white",text_color="black",compound="left",height=40,font=("yu gothic ui", 19,"bold"),text="  Service Corner",corner_radius=8)
        servicecorner_btn.place(x=5,y=250,relwidth=0.95)

        home_func()

    #dashboard_func()
        
    # the user will create a new account
    def register_func():
        '''file = open('A:\\PROJECTS\\Coimbatore-smart-city-app\\auth.bin','wb')
        data = {
            'USERNAME':'abbi',
            'NAME':'abbi',
            'PASSWORD':'abbi',
            'AADHAAR':'123456789011',
            'PHONE':'8667093591'
        }
        with open("auth.bin", "wb") as file:
            pickle.dump(data, file)'''
        pass


    def LogIn_func():
        login_frame = customtkinter.CTkFrame(master=window,fg_color="white")
        login_frame.place(x=0,y=0,relheight=1,relwidth=1)
        img1=ImageTk.PhotoImage(Image.open("A:\\PROJECTS\\Coimbatore-smart-city-app\\Smart-city-app\\assets\\pattern.png"))
        l1=customtkinter.CTkLabel(master=login_frame,image=img1)
        l1.pack()
        frame=customtkinter.CTkFrame(master=l1, width=320, height=360, corner_radius=15,bg_color='black')
        frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        l2=customtkinter.CTkLabel(master=frame, text="Log into your Kovai smart \ncitizen app",font=('Century Gothic',20))
        l2.place(x=40, y=30)
        entry1=customtkinter.CTkEntry(master=frame, width=220,height=40, placeholder_text='Username')
        entry1.place(x=50, y=110)
        entry2=customtkinter.CTkEntry(master=frame, width=220,height=40, placeholder_text='Password', show="*")
        entry2.place(x=50, y=165)
        def login_btn():
            username = entry1.get()
            password = entry2.get()
            try:
                data = func.retreive_user_data(username,password)
                file = open('A:\\PROJECTS\\Coimbatore-smart-city-app\\auth.bin','wb')
                dat = {
                    'USERNAME':data[0],
                    'NAME':data[1],
                    'PASSWORD':data[2],
                    'AADHAAR':data[3],
                    'PHONENUMBER':data[4],
                    'GMAIL':data[5]
                }
                with open("auth.bin", "wb") as file:
                    pickle.dump(dat, file)
                USER_DET["USERNAME"] = data[0]
                USER_DET["NAME"] = data[1]
                USER_DET['AADHAAR'] = data[3]
                USER_DET['PHONENUMBER'] = data[4]
                USER_DET['GMAIL'] = data[5]
                login_frame.destroy()
                dashboard_func()
            except:
                data = ()
                l5=customtkinter.CTkLabel(master=frame, text="No credentials found!",font=('Century Gothic',14))
                l5.place(x=85, y=320)
            if len(data)>0:
                print(data)
        button1 = customtkinter.CTkButton(master=frame, width=220,height=50, text="LOGIN", command=login_btn, corner_radius=6)
        button1.place(x=50, y=260)
    
    # here the data will be stored at 'auth.bin' and the uder details will be fed at UDER_DET
    def LogIn():
        if os.path.exists('auth.bin'):
            if os.path.getsize("auth.bin")>0:
                auth_file = open('auth.bin','rb')
                data = pickle.load(auth_file)
                USER_DET["USERNAME"] = data['USERNAME']
                USER_DET["NAME"] = data['NAME']
                USER_DET['AADHAAR'] = data['AADHAAR']
                USER_DET['PHONENUMBER'] = data['PHONENUMBER']
                USER_DET['GMAIL'] = data['GMAIL']
                dashboard_func()
            else:
                LogIn_func()
        else:
            register_func()
    
    LogIn()

App()

window.mainloop()
