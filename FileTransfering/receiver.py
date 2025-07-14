import subprocess,os

port = input("Input the port number you want to use for the file transfer: ")

file_name=input("Enter the file name you want to store data to: ")

if os.path.exists(file_name):
	c=input("File already exist do you wanna overwrite (Y/N): ")
	if c=='N':
		sys.exit("Change File name and try again")
subprocess.run(f"nc -lvp {port} > {file_name}",shell=True)
print("File taken input succesfully")
