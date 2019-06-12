import tkinter 
import time
import RPi.GPIO as GPIO

def yes():

    #give high to motor
    print("In yes\n")

    control_pins = [7,11,13,15]

    for pin in control_pins:

        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, 0)
        halfstep_seq = [[1,0,0,0],[1,1,0,0],[0,1,0,0],[0,1,1,0],[0,0,1,0],[0,0,1,1],[0,0,0,1],[1,0,0,1]]


    for i in range(512):

        for halfstep in range(8):

            for pin in range(4):

                GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])

            time.sleep(0.001)

def start():

    #pin for IR sensor
    GPIO.setup(3,GPIO.IN)

    #time in which notification can be sent again
    time_to_sleep = 120

    #reading input from IR sensor
    i = GPIO.input(3)

    while(True): 
    
        i = GPIO.input(3)
        
        if(i == 1):
        
            break

    displaynew()

    #time.sleep(time_to_sleep)    	

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

#to prevent display of warnings
GPIO.setwarnings(False)

#to use configuration on board 
GPIO.setmode(GPIO.BOARD)

introdisplay()

GPIO.cleanup()
