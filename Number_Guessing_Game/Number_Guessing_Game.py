import random
import sys

def game(n, u):
 num = 1
 while u != n:
  if(n > u):
    u = int(input("Write A Higher Number Please : "))
  elif(n < u):
    u = int(input("Write A Lower Number Please : "))
  else:
     print("You Got Right Answer.")
  num = num + 1
 return num


def main():
    n = random.randint(1, 100)
    # print(n)
    u = int(input("Enter A Number And Guess The Correct Answer : "))
    s = game(n, u)
    print(f"You Got The Answer Correct In : {s}")

    re = input("Do You Want To Play This Game Again (Press Y or y) : ")
    if re == "y" or re == "Y":
     main()
    else:
     sys.exit(0)


if __name__ == "__main__":
 main()
