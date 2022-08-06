import os
import sys
import random
import hang_img


def check_pos(m,cont):
 num = 0 
 a=input('Enter A Number : ').lower()
 for x in range(m):
   if a == names[x]:
       guess[x] = a
 os.system('cls')
 print(" ".join(guess))

 if a not in  names:
            cont +=1
            if cont == 1:
                  print(hang_img.hangman[cont])
                  check_pos(m,cont)
            elif cont == 2:
                  print(hang_img.hangman[cont])
                  check_pos(m,cont)
            elif cont == 3:
                  print(hang_img.hangman[cont])
                  check_pos(m,cont)
            elif cont == 4:
                  print(hang_img.hangman[cont])
                  check_pos(m,cont)
            elif cont == 5:
                  print(hang_img.hangman[cont])
                  check_pos(m,cont)
            else:
                print(hang_img.hangman[cont])
                print("\nThe Word Was : ",names)
                print("\nYou lost.\n\n")
                sys.exit()
 elif "_" in guess:
        print(hang_img.hangman[cont])
        check_pos(m,cont)
 else:
    print("\nYou Win.\n\n")
    sys.exit()

def main(): 
 global cont 
 cont =0
 global names
 rand_name=["siddhesh","vedant","harsh","aniket","malay","shubam"]
 names=random.choice(rand_name)
 print("This Is The Name : ",names)
 global m 
 m=len(names)
 global guess
 guess=[]
 for i in range(m):
    guess += "_"
 print(" ".join(guess))
 check_pos(m,cont)

if __name__ == "__main__":
      main()
