from ptu import ptu_control,ptu_keyboard_control
import time
from pynput import keyboard

ptu = ptu_keyboard_control()
# ptu = ptu_control()

# def on_press(key):
#     if key == keyboard.Key.right:
#         ptu.right(1)
#         print("right, pan_pos: {}".format(pan_pos))
#     if key == keyboard.Key.left:
#         ptu.left(1)
#         print("left, pan_pos: {}".format(pan_pos))
    

# def on_release(key):
#     print("{0} released".format(key))
#     if key == keyboard.Key.esc:
#         return False

# while True:
#     with keyboard.Listener(on_press = on_press,on_release = on_release) as listener:
#         # print(ptu.pan_pos)
#         listener.join()




# ptu = ptu_control()
# # ptu.left(1)
# ptu.reset()

# for i in range(30):
#     ptu.right(1)
#     print("right, pos = {}".format(ptu.pan_pos))
#     time.sleep(0.5)

# for i in range(30):
#     ptu.left(1)
#     print("left, pos = {}".format(ptu.pan_pos))
#     time.sleep(0.5)