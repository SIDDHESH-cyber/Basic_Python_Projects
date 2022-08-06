import pyautogui
import multiprocessing
import time

def Screen_Shot(n):
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r'C:\Users\SIDDHESH PATEL\Desktop\screenshot.jpg')

def timer():
    for x in range(1,6):
        print(f"{x} Remaing Seconds Before Take Screen Shot")
        time.sleep(1)


def main():
    p = multiprocessing.Process(target=Screen_Shot,name="Screen",args=(5,))
    print("You have 5 Second From Now Before Taking Screen Shot....Hurry Up")
    timer()
    p.start()
    time.sleep(1)
    p.terminate()


if __name__ == "__main__":
    main()
