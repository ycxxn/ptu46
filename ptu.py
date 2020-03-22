from pynput import keyboard
import time
class ptu_control:
    def __init__(self):
        self.pan_pos = 0

    def deg2ptu(self,cmd,deg):
        step = round((deg/90)*1750)
        n = cmd+str(step)+" *\n"
        print(n) 

    def reset(self):
        n = "r *\n"
        print(n)

    def right(self,deg):
        self.pan_pos += deg
        self.deg2ptu("pp",self.pan_pos)

    def left(self,deg):
        self.pan_pos -= deg
        self.deg2ptu("pp",self.pan_pos)

class ptu_keyboard_control(ptu_control):
    def __init__(self):
        super(ptu_control, self).__init__()
        self.pan_pos = 0
        self.main()

    def on_press(self,key):
        if key == keyboard.Key.right:
            self.right(1)
            print("right, pan_pos: {}".format(self.pan_pos))
        if key == keyboard.Key.left:
            self.left(1)
            print("left, pan_pos: {}".format(self.pan_pos))
        
    def on_release(self,key):
        # print("{0} released".format(key))
        if key == keyboard.Key.esc:
            return False

    def main(self):
        while True:
            with keyboard.Listener(on_press = self.on_press,on_release = self.on_release) as listener:
                listener.join()