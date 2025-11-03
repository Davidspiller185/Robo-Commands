from GuardRobot import GuardRobot
from DeliveryRobot import DeliveryRobot
gideon=GuardRobot("Gideon")
dora=DeliveryRobot("Dora")
lst_1=["SAY","MOVE","WHERE"]
for word in lst_1:
    if word == "SAY":
        gideon.say("hello")
        dora.speak("done")
    elif word == "MOVE":
        print(gideon.handle_command("MOVE"))
        dora.move_robot(3,2)
    else:
        print(gideon.handle_command("WHERE"))
        dora.were(DeliveryRobot.step_x,DeliveryRobot.step_y)




