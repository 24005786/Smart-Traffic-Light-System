import time
import random

class TrafficLightSystem:
    def __init__(self, direction):
        self.direction = direction 
        self.state = "Red" #beginning state

    def change_light(self, new_state, duration):
        self.state = new_state
        print(f"{self.direction} light is now {self.state}.")
        time.sleep (duration)

class TrafficController:
    def __init__(self):
        self.directions = [TrafficLightSystem("North"), TrafficLightSystem("East"),
                           TrafficLightSystem("South"), TrafficLightSystem("West")]
        self.green_duration = 25 #seconds
        self.yellow_duration = 5 #seconds
        self.red_duration = 25 #seconds
        self.pedestrian_duration = 10 #seconds
        
    def check_emergency_vehicle(self):
        #imitate detection of an emergency vehicle for random demonstration
        return random.choice([True, False]) #Randomly
    
    def handle_emergency(self):
        emergency_direction = random.choice(self.directions)
        print (f"Emergency vehicle approaching from {emergency_direction.direction}.")
        emergency_direction.change_light("Green", 15)
        self.set_other_directions("Red", emergency_direction)

    def cycle_traffic_lights(self):
        while True:
            if self.check_emergency_vehicle():
                self.handle_emergency()
            else:
                for light in self.directions:
                    light.change_light("Green", self.green_duration)
                    light.change_light("Yellow", self.yellow_duration)
                    light.change_light("Red", self.red_duration)
                    self.activate_pedestrian_crossing()

    def activate_pedestrian_crossing():
        print("Pedestrian crossing activated.")

if __name__ == "__main__":
    traffic_controller = TrafficController()
    traffic_controller.cycle_traffic_lights()


        

