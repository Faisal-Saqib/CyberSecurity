import subprocess,sys,os,socket

def host_is_online(ip):
    try:
        result = subprocess.run(['ping', '-c', '1', ip], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return result.returncode == 0
    except:
        return False
def host_listening(ip,port):
	try:
		cur = socket.socket(socket.AF_INET,socket.SOCKET_STREAM)
		sock.settimeout(5)
		cur.connect((ip,int(port)))
		cur.close()
		return True
	except:
		return False

def ValidFileName(name):
	return name.find(' ')==-1

print("Required Item is Netcat, if not installed please install it manually")

# code to install nc but not finding correct way
# subprocess.run(["sudo","apt","update"])
# subprocess.run(["sudo","apt","install","nc"])

file_name_to_send=input("Enter the file name you want to send: ").strip()
if not ValidFileName(file_name_to_send):
	sys.exit("Error the filename contains spaces!, Rename it")
if not os.path.exists(file_name_to_send):
	sys.exit("File with the name '"+file_name_to_send+"' does not exists!!")

receiver_ip = input("Enter the ip address of the receiving device: ")
port = input("Enter the port used by the receiving device (leave empty for default): ")
if port=="":
	port="8080"


print(f"Preparing to send file {file_name_to_send} to {receiver_ip}:{port}")
if not host_is_online(receiver_ip):
	sys.exit(f"Mentioned ip({receiver_ip}) is not online")
else:
	print(f"Mentioned ip({receiver_ip}) is online")
# if not host_listening(receiver_ip,port):
# 	sys.exit(f"Mentioned ip({receiver_ip}) is not listening on port:{port}")
# else:
# 	print(f"Mentioned ip({receiver_ip}) is listening on port:{port}")
print("File transfer started")
subprocess.run(f"pv {file_name_to_send} | nc -q 1 {receiver_ip} {port}",shell=True)
print("File was sent Successfully")
