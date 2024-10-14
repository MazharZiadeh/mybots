import pyrosim.pyrosim as pyrosim
import pybullet_data

def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Ground", pos=[0,0,0], size=[10,10,0.1])
    pyrosim.End()

def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    
    # Create the torso (root link)
    pyrosim.Send_Cube(name="Torso", pos=[0,0,1], size=[1,1,1])
    
    # Create the back leg
    pyrosim.Send_Cube(name="BackLeg", pos=[-0.5,0,0], size=[1,1,1])
    
    # Create the front leg
    pyrosim.Send_Cube(name="FrontLeg", pos=[0.5,0,0], size=[1,1,1])
    
    # Add joints to connect BackLeg and FrontLeg to the Torso
    pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[-0.5,0,1])
    pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[0.5,0,1])
    
    pyrosim.End()

# Call the functions to create the world and robot
Create_World()
Create_Robot()
