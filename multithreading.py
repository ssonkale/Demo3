#Multithreading
import threading
import time

#1.Display square of elements of list
#2. Display cube of elements of the list
#How to create thread?=> 2 methods

def square(L): #=>t1
    print("Square of elements")
    for i in L:
        print('Thread-1'," ",i,"=",i*i)
        time.sleep(2)#=>blocked


def cube(L): #=>t2
    print("Cube of elements")
    for i in L:
        print('Thread-2'," ",i,"=",i**3)
        time.sleep(2)

L=[1,2,3,4,5]
#creation of thread
t1=threading.Thread(target=square,args=(L,)) #=> in new state
t2=threading.Thread(target=cube,args=(L,))

t1.start() #=>in Runnable state
t1.join()

t2.start() #=>in Runnable state
t2.join()

print("\n This is main process ")
print("\n This is multithreading program")
print("\n Done")









