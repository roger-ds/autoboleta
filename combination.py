from pynput.mouse import Button, Controller, Listener
from pynput.keyboard import Key, KeyCode, Listener

mouse = Controller()

# Read pointer position
origem = mouse.position
print(f'The origin pointer position is {origem}')

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

# Create a mapping of keys to function (use frozenset as sets/lists are not hashable - so they can't be used as keys)
# Note the missing `()` after function_1 and function_2 as want to pass the function, not the return value of the function
combination_to_function = {
    frozenset([Key.ctrl_l, KeyCode(vk=96)]): zerar,  # left ctrl_l+ 0
    frozenset([Key.ctrl_l, KeyCode(vk=97)]): cancelaOrdemCompra,  # left ctrl_l+ 1
    frozenset([Key.ctrl_l, KeyCode(vk=98)]): maoGrande,  # left ctrl_l+ 2
    frozenset([Key.ctrl_l, KeyCode(vk=99)]): cancelaOrdemVenda,  # left ctrl_l+ 3
    frozenset([Key.ctrl_l, KeyCode(vk=100)]): compraMercado,  # left ctrl_l+ 4
    frozenset([Key.ctrl_l, KeyCode(vk=101)]): maoMedia,  # left ctrl_l+ 5
    frozenset([Key.ctrl_l, KeyCode(vk=102)]): vendaMercado,  # left ctrl_l+ 6
    frozenset([Key.ctrl_l, KeyCode(vk=103)]): compraBid,  # left ctrl_l+ 7
    frozenset([Key.ctrl_l, KeyCode(vk=104)]): maoPequena,  # left ctrl_l+ 8
    frozenset([Key.ctrl_l, KeyCode(vk=105)]): vendaAsk,  # left ctrl_l+ 9
    frozenset([Key.ctrl_l, KeyCode(vk=81)]): quit,  # left ctrl_l+ c
}

# The currently pressed keys (initially empty)
pressed_vks = set()

def get_vk(key):
    """
    Get the virtual key code from a key.
    These are used so case/shift modifications are ignored.
    """
    return key.vk if hasattr(key, 'vk') else key.value.vk


def is_combination_pressed(combination):
    """ Check if a combination is satisfied using the keys pressed in pressed_vks """
    return all([get_vk(key) in pressed_vks for key in combination])


def on_press(key):
    """ When a key is pressed """
    vk = get_vk(key)  # Get the key's vk
    pressed_vks.add(vk)  # Add it to the set of currently pressed keys

    for combination in combination_to_function:  # Loop through each combination
        if is_combination_pressed(combination):  # Check if all keys in the combination are pressed
            combination_to_function[combination]()  # If so, execute the function


def on_release(key):
    """ When a key is released """
    vk = get_vk(key)  # Get the key's vk
    pressed_vks.remove(vk)  # Remove it from the set of currently pressed keys


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
