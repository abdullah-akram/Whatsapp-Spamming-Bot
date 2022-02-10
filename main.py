
import pyautogui
import webbrowser as wb
import time
import pywhatkit as kit


def whatsapp_bot(hr,min):
    kit.sendwhatmsg('+xxxxxxxxxxx', 'Testing spamming bot\n', hr, min)

    wb.open("web.whatsapp.com")
    time.sleep(20)
    file1 = open('file.txt', 'r')
    count = 0
    while True:
        count += 1
        line = file1.readline()
        if not line:
            break
        print(line)
        chars = list(line)
        i = 0
        for ch in chars:
            pyautogui.press(chars[i])
            i += 1
        pyautogui.press("enter")
    file1.close()





whatsapp_bot(4,28)