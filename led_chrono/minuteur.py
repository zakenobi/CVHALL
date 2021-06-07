import time

def countdown(t):
    hours, secs=divmod(t,3600)
    t=t-hours*3600
    #The loop runs until t=0
    while t:
        #Calculate the number of hours, minutes and seconds
        hours, secs=divmod(t,3600)
        mins, secs = divmod(t,60)
        #Print minutes and seconds using timeformat
        timer = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)
        print (timer, end ="\r")
        #The code waits 1 second
        time.sleep(1)
        #Decrementation of t
        t-=1
    
    print('Shuting down...')

t=input("Enter time in seconds : ")

countdown(int(t))
