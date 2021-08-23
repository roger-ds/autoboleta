
from pynput.mouse import Controller

mouse = Controller()

while True:

    input('Aponte o mouse para a boleta e pressione Enter')

    # Read pointer position
    origem = mouse.position
    print(f'The current pointer position is {origem}')
