import pybullet as p
import time

# Connect to PyBullet GUI
physicsClient = p.connect(p.GUI)

# Load the world described in box.sdf
p.loadSDF("box.sdf")

# Simulate the world for 1000 steps
for i in range(10000000000):
    p.stepSimulation()
    print(i)
    time.sleep(1/60)

# Disconnect from PyBullet
p.disconnect()
