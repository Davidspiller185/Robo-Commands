from SpeakableMixin import SpeakableMixin
class GuardRobot(SpeakableMixin):
    def say(self,text:str):
        print(f"the robot say:{text}")
    def handle_command(self,command:str):
        return f"unsupported command {command}"


