from pynput.mouse import Button, Controller
from pynput import keyboard

mouse = Controller()

input('Aponte o mouse para a boleta e pressione Enter')
# Read pointer position
origem = mouse.position
print(f'The current pointer position is {origem}')

def relativeMove(x, y):
    mouse.position = origem
    # Move pointer relative to current position
    mouse.move(x, y)
    # Press and release
    mouse.press(Button.left)
    mouse.release(Button.left)
    mouse.position = origem

def zerar():
    print('Function 0 activated')
    relativeMove(50, 75)

def cancelaOrdemCompra():
    print('Function 1 activated')
    relativeMove(4, -611)

def maoGrande():
    print('Function 2 activated')
    relativeMove(155, 48)

def cancelaOrdemVenda():
    print('Function 3 activated')
    relativeMove(255, -611)

def compraMercado():
    print('Function 4 activated')
    relativeMove(65, 0)

def maoMedia():
    print('Function 5 activated')
    relativeMove(155, 24)

def vendaMercado():
    print('Function 6 activated')
    relativeMove(235, 0)

def compraBid():
    print('Function 7 activated')
    relativeMove(65, 48)

def maoPequena():
    print('Function 8 activated')
    relativeMove(155, 0)

def vendaAsk():
    print('Function 9 activated')
    relativeMove(235, 48)

if __name__ == '__main__':
    while True:
        def on_press(key):
            if hasattr(key, 'vk'):
                print('You entered a number from the numpad: ', key.char, key.vk)
                if key.vk == 96:
                    zerar()
                elif key.vk == 97:
                    cancelaOrdemCompra()
                elif key.vk == 98:
                    maoGrande()
                elif key.vk == 99:
                    cancelaOrdemVenda()
                elif key.vk == 100:
                    compraMercado()
                elif key.vk == 101:
                    maoMedia()
                elif key.vk == 102:
                    vendaMercado()
                elif key.vk == 103:
                    compraBid()
                elif key.vk == 104:
                    maoPequena()
                elif key.vk == 105:
                    vendaAsk()

        with keyboard.Listener(on_press = on_press) as listener:
            listener.join()
