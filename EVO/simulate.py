import pybullet as p
import time

# Connect to PyBullet GUI
physicsClient = p.connect(p.GUI)

# Simulate the world for 1000 steps
for i in range(1000000):
    p.stepSimulation()
    print(i)
    time.sleep(1/60)  # Sleep for 1/60th of a second

# Disconnect from PyBullet
p.disconnect()
