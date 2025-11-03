
from Robot import Robot
class MovableMixin(Robot):
    count_step_x=0
    count_step_y=0
    def __init__(self,name,move=True):
        super().__init__(name)
        self.move=move
    def were(self,x:int,y:int):
        MovableMixin.count_step_x+=x
        MovableMixin.count_step_y+=y
        print(MovableMixin.count_step_x)
        print(MovableMixin.count_step_y)

