import tkinter 
import time

def yes():
	#give high to motor
	print("In YES\n")

def start():

	i = 0

	while(True):        

		time.sleep(5)

		#get input        
		if(i == 0):

			break    

	displaynew()

def introdisplay():

	m = tkinter.Tk(className = "|| FEED YOUR PET ||")
	m.title("Pet Feeding Service")

	welcmsg = tkinter.Label( m , text = "!! Welcome to pet feeding system !!" , bg = "lightgreen") 
	welcmsg.pack()
	
	startb = tkinter.Button(m , text = 'START', width = 25, command = start)
	startb.pack()    

	killb = tkinter.Button(m , text = 'Exit', width=25, command = m.destroy)	
	killb.pack()

	m.mainloop()

def displaynew():

	m = tkinter.Tk(className = "|| FEED YOUR PET ||")

	m.title("Pet Feeding Service")

	choicemsg = tkinter.Label(m, text = "Press button to make a choice" , bg = "lightgreen") 
	choicemsg.pack()

	yesb = tkinter.Button(m , text = 'YES', width = 25, command = yes)
	nob = tkinter.Button(m , text = 'NO', width = 25, command = m.destroy)
	killb = tkinter.Button(m , text = 'Exit', width=25, command = m.destroy)	

	yesb.pack()
	nob.pack()
	killb.pack()

	m.mainloop()

introdisplay()
