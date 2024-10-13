import pybullet as p
import pybullet_data
import time

# Connect to the PyBullet GUI
p.connect(p.GUI)

# Set the additional search path for PyBullet data
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# Add gravity
p.setGravity(0, 0, -9.8)

# Load the plane (floor)
planeId = p.loadURDF("plane.urdf")

# Load the world from the SDF file
p.loadSDF("boxes.sdf")

# Simulate the world for a specified number of steps
for i in range(1000000000000):
    p.stepSimulation()
    print(i)  # Print the current step count
    time.sleep(1 / 60)  # Sleep to create a frame rate of 60 FPS

# Disconnect from the simulation
p.disconnect()
