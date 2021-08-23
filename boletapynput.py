from pynput import keyboard
from pynput.mouse import Button, Controller

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

with keyboard.GlobalHotKeys({
        '<ctrl>+0': zerar,
        '<ctrl>+1': cancelaOrdemCompra,
        '<ctrl>+2': maoGrande,
        '<ctrl>+3': cancelaOrdemVenda,
        '<ctrl>+4': compraMercado,
        '<ctrl>+5': maoMedia,
        '<ctrl>+6': vendaMercado,
        '<ctrl>+7': compraBid,
        '<ctrl>+8': maoPequena,
        '<ctrl>+9': vendaAsk,
        '<ctrl>+<shift>+c': quit}) as h:
    h.join()
