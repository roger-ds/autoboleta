from pynput.mouse import Button, Controller
from pynput import keyboard

mouse = Controller()

input('Aponte o mouse para a 1a boleta e pressione Enter')
# Read pointer position
origem1 = mouse.position
print(f'The current pointer position is {origem1}')

input('Aponte o mouse para a 2a boleta e pressione Enter')
# Read pointer position
origem2 = mouse.position
print(f'The current pointer position is {origem2}')

origem = origem1

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
    relativeMove(-103, 123)

def cancelaOrdemCompra():
    print('Function 1 activated')
    relativeMove(0, 123)

def maoGrande():
    print('Function 2 activated')
    relativeMove(0, 99)

def cancelaOrdemVenda():
    print('Function 3 activated')
    relativeMove(0, 123)

def compraMercado():
    print('Function 4 activated')
    relativeMove(-100, 51)

def maoMedia():
    print('Function 5 activated')
    relativeMove(0, 75)

def vendaMercado():
    print('Function 6 activated')
    relativeMove(100, 51)

def compraBid():
    print('Function 7 activated')
    relativeMove(-100, 99)

def maoPequena():
    print('Function 8 activated')
    relativeMove(0, 51)

def vendaAsk():
    print('Function 9 activated')
    relativeMove(100, 99)

if __name__ == '__main__':
    while True:
        def on_press(key):
            global origem
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
                elif key.vk == 106:
                    origem = origem2
                    relativeMove(0,0)
                elif key.vk == 111:
                    origem = origem1
                    relativeMove(0,0)


        with keyboard.Listener(on_press = on_press) as listener:
            listener.join()
