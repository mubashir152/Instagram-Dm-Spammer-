import pyautogui
# print("Hello Mubashir")
# print(pyautogui.position())
# Coordinates where we want the mouse to click
pyautogui.moveTo(108, 677)
pyautogui.click()


pyautogui.PAUSE = 0.0001

# Data being fetched from text file
with open("Imitation_Game_The.txt", "r",encoding='utf-8') as script:
    for line in script.readlines():
        line = line.strip()
        # print(line)
        pyautogui.write(str(line))
        pyautogui.press("enter")


if __name__ == '__main__':
    print('PyCharm')






