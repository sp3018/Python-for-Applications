import socket
import random
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

host, port = '', 5000
queue = 5
s.bind((host, port))
s.listen(queue)
while True:
	client, address = s.accept()
	data = True
	while data:
		data = client.recv(4096)
		data_text = data.decode('utf-8')
		data_text = data_text.strip();
		data_text = data_text.lower()
		print(data_text)
		if(data_text == "bye" or data_text == "later" or data_text == "ttyl"):
			res="Goodbye!\n"
			client.send(bytes(res, 'utf-8'))
			client.close()
			break
		elif((data_text == "hi") or (data_text == "hello") or (data_text == "howdy") or (data_text == "hey") or (data_text == "hola")):
			res="Hi there!\n"
			client.send(bytes(res, 'utf-8'))
			continue
		else:
			res=random.choice(["Cool!\n", "Tell me more\n", "And how does that make you feel?\n"])
			client.send(bytes(res, 'utf-8'))
			continue
    #client.close()