import time
t=int(input("how many seconds do you wanna count? "))
while t:

    mins=t//60
    secs=t%60

    timer=' {:02d}:{:02d}'.format(mins,secs)

    print(timer,end="\r")

    time.sleep(1)
    t=t-1
