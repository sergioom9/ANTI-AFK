import random
import pyautogui
import time


def tiempo_espera():
    print("Cada cuántos segundos realizar movimiento (Sin determinar = 5 segundos)")
    entrada = input().strip()
    if entrada.isdigit():
        print(f"Establecido auto-movimiento cada {entrada} segundos ")
        return int(entrada)
    else:
        print("Establecido auto-movimiento cada 5 segundos ")
        return 5



def movimiento(x,y):
    randx = random.randint(0,x)
    randy = random.randint(0,y)
    print("Realizando ANTI-AFK...")
    pyautogui.moveTo(randx, randy)


def main():
        seconds_to_repeat = tiempo_espera()
        x, y = pyautogui.size()

        while 1:
            movimiento(x,y)
            time.sleep(seconds_to_repeat)


if __name__ == "__main__":
    main()