import time
import sys
import threading

from neopixel import NeoPixel
from .tools import cmath

from .animations import *

class AnimatorController():
    def __init__(self,
                pixels: NeoPixel,
                animation: str = "sunrise",
                update_rate: int = 60):
        
        super(AnimatorController, self)
        self._stop = threading.Event()

        self._pixels = pixels

        self.FPS = update_rate

        self._update_time = (1.0/update_rate)
        self._running = False
        self._animation = self.__get_animation(animation)
        self._interlace = False

        self._thread = threading.Thread(target=self.__update)
        self._thread.daemon = True

        self._thread.setName("Update pixels Cycle")

    def run(self):
        """ Start the animator controller routine"""        
        try:
            self._running = True
            self._thread.start()
        except (KeyboardInterrupt, SystemExit):
            print ('\n! Received keyboard interrupt, quitting threads.\n')

    def stop(self):
        """ Stop the animator controller routine"""
        self._running = False
        self._thread.join()

    def __update(self):
        """ Update the state of animation and draw it into pixels"""

        self._animation.start()
        while self._running:
            if not self._animation.loop and self._animation.done:
                self.stop()
                break

            # Starting the execution cycle
            start_cycle_time = time.process_time()

            delta_time = 1.0 / self.FPS
            self._animation.update(delta_time)
            self._pixels.show()

            # Ending the execution cycle
            end_cycle_time = time.process_time()
            

            cycle_time = (end_cycle_time - start_cycle_time)            
            self.__calc_FPS(cycle_time + self.__wait_next_update(cycle_time))
            self.__print_FPS()


    def __wait_next_update(self, cycle_time):
        """
        Wait for next update cycle if the executation cycle was executed quicker
        than refresh rate
        """
        waitTime = cmath.clamp(self._update_time - cycle_time)    
        
        if(waitTime > 0):
            time.sleep(waitTime)

        return waitTime

    def __calc_FPS(self, cycle_time):
        """ Calculate the 'Frames' per second """
        self.FPS = int(1.0/cycle_time)


    def __print_FPS(self):
        """ Print the FPS in console """
        sys.stdout.write(f"\rFPS: {self.FPS}")
        sys.stdout.flush()


    def __get_animation(self, animation: str):
        animations_list = {
            "fire"          : FireAnimation(self._pixels),
            "fade"          : FadeAnimation(self._pixels),
            "pingpong"      : PingPongAnimation(self._pixels),
            "test"          : TestColorsAnimation(self._pixels),
            "rainbow"       : RainbowPerlinAnimation(self._pixels),
            "rainbowwheel"  : RainbowWheelAnimation(self._pixels),
            "sunrise"       : SunriseAnimation(self._pixels)
        }

        return animations_list[str.lower(animation)]

    
