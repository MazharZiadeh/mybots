import pyrosim.pyrosim as pyrosim

# Start generating the SDF file
pyrosim.Start_SDF("box.sdf")

# Create a box with a specific position and size
pyrosim.Send_Cube(name="Box", pos=[0, 0, 0.5], size=[1, 1, 1])

# End and save the SDF file
pyrosim.End()
