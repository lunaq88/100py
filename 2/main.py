import pyautogui, easygui
f = easygui.enterbox()

for i in range (100):
	for word in f.split():
		pyautogui.typewrite(word)
		pyautogui.press("enter")
