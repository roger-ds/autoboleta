from pynput import keyboard

if __name__ == '__main__':
    while True:
        def on_press(key):
            if hasattr(key, 'vk'):
                print('You entered a number from the numpad: ', key.char, key.vk)

        with keyboard.Listener(on_press = on_press) as listener:
            listener.join()
