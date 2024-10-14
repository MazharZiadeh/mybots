import pybullet as p
import pybullet_data
import time

# Connect to the physics server (GUI)
p.connect(p.GUI)

# Set additional search path to find URDF files
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# Load the plane (floor)
planeId = p.loadURDF("plane.urdf")

# Load the robot URDF file
robotId = p.loadURDF("body.urdf")

# Set gravity
p.setGravity(0, 0, -9.8)

# Simulate the world
for i in range(10000):
    p.stepSimulation()
    time.sleep(1/240)  # Slow down the simulation to make it visible

# Disconnect from the physics server
p.disconnect()
