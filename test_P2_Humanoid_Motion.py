from HUMANOID.HUMANOID_MOVEMENTS import *
# Iniciar la comunicacion
robot = HUMANOID_MOVEMENT("B32")

startCom()

robot.start()
robot.Tpose()
stopCom()