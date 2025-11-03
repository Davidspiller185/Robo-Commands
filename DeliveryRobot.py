from  SpeakableMixin import SpeakableMixin
from  MovableMixin import MovableMixin
class DeliveryRobot(SpeakableMixin,MovableMixin):
    step_x=0
    step_y=0
    def speak(self,text:str):
        print(f"the robot say:{text}")

    def move_robot(self,x:int,y:int):
        DeliveryRobot.step_x=x
        DeliveryRobot.step_y=y
        print(f"move the robot by distance:{x},and by distance:{y} steps")




