import pyrosim.pyrosim as pyrosim

# Start generating the SDF file
pyrosim.Start_SDF("boxes.sdf")

# Define the base size and number of blocks
base_size = 1  # Base size for the first block
num_blocks = 10  # Number of blocks in the tower

# Loop to create a tower of blocks
for i in range(num_blocks):
    size = base_size * (0.9 ** i)  # Reduce size by 10% for each level
    z_position = size / 2 + i * (base_size * 0.9)  # Adjust z position for the next block
    # Send the cube with the calculated position and size
    pyrosim.Send_Cube(name=f"Box{i}", pos=[0, 0, z_position], size=[size, size, size])

# End the SDF generation
pyrosim.End()
