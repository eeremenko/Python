import time

class TrafficLight:

    __traffic_light_color = "Светофор"

    def running(self):
        while True:
            print("Red light")
            time.sleep(7)
            print("Yellow light")
            time.sleep(2)
            print("Green light")
            time.sleep(7)


a = TrafficLight()
a.running()