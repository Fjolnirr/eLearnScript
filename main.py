import pyautogui
import keyboard

def clicker():
    on_off = 1

    pyautogui.FAILSAFE = False

    while True:

        if keyboard.is_pressed('z'):
            on_off = 1
        if keyboard.is_pressed('x'):
            on_off = 0
            print("Çalışma durdu.")
            continue

        if on_off == 1:
            # Mouse'u belirli bir koordinata hareket ettir
            pyautogui.moveTo(x=1320, y=985, duration=5)

            # Mouse ile tıklama işlemi gerçekleştir
            pyautogui.click()

            # pyautogui.moveTo(x=976, y=582, duration=0.1)
            # pyautogui.click()

            # pyautogui.moveTo(x=976, y=482, duration=0.1)
            # pyautogui.click()

            pyautogui.moveTo(x=965, y=633, duration=0.1)
            pyautogui.click()

            print("aldim kabul ettim chmod 777...")
        else:
            print("Durdum..")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    clicker()
