from Robot import Robot
class SpeakableMixin(Robot):
    def __init__(self,name,talk=True):
        super().__init__(name)
        self.talk=talk
