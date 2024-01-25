import socket,threading

HOST = '192.168.29.25'
PORT = 5000
active_clients = []

def listen_for_messages(client,username):
	while 1:
		try:
			message = client.recv(2048).decode('utf-8')
			if message != "":
				final_msg = username+'~'+message
				send_messages_to_all(final_msg)
			else:
				pass
		except:
			print(f"[!] {client} is missing!")
			break

def send_messages_to_client(client,message):
	try:
		client.sendall(message.encode())
	except:
		print("[!] Client not found!")

def send_messages_to_all(message):
	for user in active_clients:
		send_messages_to_client(user[1],message)


def client_handler(client):
	while 1:
		username = client.recv(2048).decode('utf-8')
		if username != "":
			active_clients.append((username,client))
			break
		else:
			print("Client username is empty!")
	threading.Thread(target=listen_for_messages,args=(client,username, )).start()

def main():
	server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	try:
		server.bind((HOST,PORT))
		print(f"Server {HOST} listening in {PORT}")
	except:
		print("Unable to bind to host!")
		
	server.listen(50000)
	
	while True:
		client,address = server.accept()
		print(f"Successfully connected to {address[0]} {address[1]}")

		threading.Thread(target=client_handler,args=(client, )).start()

if __name__=='__main__':
	main()