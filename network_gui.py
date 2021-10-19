from tkinter import *
import time, socket
import sys

root = Tk()
root.title("GUI to test the CPI BuC")
 
heading = Label(root, text="CPI buc test mute/unmute.",font=("arial",14,"bold"), wraplength=300)
heading.pack(pady=20)
       
ip = Label(root, text="IP address of the CPI BuC (ex:192.168.4.2)",font=("arial",10,"bold"))
ip.pack()

inputIP = StringVar()

ip1 = Entry(root, bd =5,textvariable=inputIP)
ip1.pack(pady=20)

timeV = Label(root, text="Interval b/w mute/unmute in mins (ex: 40 min)",font=("arial",10,"bold"))
timeV.pack()

timeValue = StringVar()

time1= Entry(root, bd =5,textvariable=timeValue)
time1.pack(pady=20)
 
#Actual buc code
def jump_function():
    text.insert(INSERT, "\nConnecting to buc on "+str(inputIP.get()))
    ipAddress = str(inputIP.get())
    time_value = int(str(timeValue.get()))*60
    i = 1;
    while i!=0:
        m1='\x02\x30\x00\x88\x00\xB8\x03'
        m2='\x02\x30\x00\x88\x01\xB9\x03'
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ipAddress,50000))
        text.insert(INSERT, "\nTesting round no: "+str(i))
        l=sock.proto 
        m=sock.type
        text.insert(INSERT, "\nsocket is connected-1")
        sock.send(m1)
        text.insert(INSERT, "\nkicker")
        reply = sock.recv(50000)
        text.insert(INSERT,"\n" +str(reply))
        sock.close()
        time.sleep(time_value)
		#Second socket connection
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ipAddress,50000))
        l=sock.proto 
        m=sock.type
        text.insert(INSERT, "\nsocket is connected-2")
        sock.send(m2)
        reply = sock.recv(50000)
        text.insert(INSERT, "\n" +str(reply))
        sock.close()
        time.sleep(time_value)
        i+=1
        text.delete(1.0, END)
        thrd = threading.Thread(target = jump_function)
        thrd.start()
       
tests_button = Button(root, text="Run Tests", command=jump_function)
tests_button.pack()

close_button = Button(root, text="Close", command=root.quit)
close_button.pack(pady=20)

text = Text(wrap="word")
text.pack(side="top", fill="both", expand=True)
text.tag_configure("stderr", foreground="black")
        
root.mainloop()