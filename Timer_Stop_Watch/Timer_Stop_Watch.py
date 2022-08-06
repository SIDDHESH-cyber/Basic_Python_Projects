import os
import time

def Stop_Watch():
 second = 0    
 minute = 0    
 hours = 0    
 a=True
 while(a):    
  try:
     print("Simple_Stopwatch")    
     print('\n\n')    
     print('_____________')    
     print('  %d : %d : %d '%(hours,minute,second))    
     print('_____________')    
     time.sleep(1)    
     second+=1    
     if(second == 60):    
         second = 0    
         minute+=1    
     if(minute == 60):    
         minute = 0    
         hours+=1    
     os.system('cls')  
  except KeyboardInterrupt:
     a=False
     print("Timer Has Stopped")

def Timer():
  
  def countdown(t):
   while t:
    mins, secs = divmod(t, 60)
    timer = '{:02d}:{:02d}'.format(mins, secs)
    print(timer, end="\r")
    time.sleep(1)
    t -= 1    
   print('Time Up....................')
    
  t = input("Enter the time in seconds: ")  
  countdown(int(t))

def Choices():
    Choice=int(input("Enter Your Choice : "))
    print()
    os.system('cls')
    if Choice == 1:
        Stop_Watch()
        re_try=input("\n\nPress Y or y To Run Again This Task :")
        if re_try == 'y' or re_try == 'Y':
            os.system('cls')
            Stop_Watch()

    elif Choice == 2:
        Timer()
        re_try=input("\n\nPress Y or y To Run Again This Task :")
        if re_try == 'y' or re_try == 'Y':
            os.system('cls')
            Timer()

    else:
        print("Enter A Valid Option.")

def main():
    os.system('cls')
    print("Welcome To Timer And Stop_Watch :-\n")
    print("Please Select Any One Options :-\n")
    print("For Stop_Watch : 1\n")
    print("For Timer : 2\n")
    Choices()


if __name__ == "__main__":
    main()
