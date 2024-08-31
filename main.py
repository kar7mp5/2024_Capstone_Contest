# main.py
from robot_control import Controller
from pynput import keyboard


ctr = Controller(17, 22, 24, 23)


def on_release(key):
    '''Main keyboard event
    
    Args:
        key (str): keyboard input.
    
    Returns:
        bool: False is to end up the program.
    '''
    print(key)

    if key == keyboard.Key.esc:
        print('End up the program.')
        return False

    if 'char' in dir(key):     #check if char method exists,
        match key.char:
            case 'a':
                print('left')
                ctr.left_turn(2)

            case 'd':
                print('right')
                ctr.right_turn(2)

            case 's':
                print('back')
                ctr.go_back(2)

            case 'w':
                print('front')
                ctr.forward(2)

            case 'e':
                print('stop')
                ctr.reset_pin()

            case _:
                print('Error occurred!')

        ctr.reset_pin()


def main():
    print("Program is started...")


    # Collect events until released
    with keyboard.Listener(on_release=on_release) as listener:
        listener.join()






if __name__=="__main__":
    main()
