"""
The purpose of this project is to demonstrate forward and inverse kinematics of a 2dof planar manipulator using python
and a 3D printed prototype using 2 servomotors and a Arduino Uno board.
The program takes input from the user and calculates forward and inverse kinematics, actuating the servos based on the
output values.
"""

from kine import *
from main import Servo, connect_port


user_choice = """
Enter action: 
- press "f" to calculate forward kinematics
- press "i" to calculate inverse kinematics
- press "q" to terminate

Enter: """


# if arduino board is not detected, you can still run only the calculations
def option_1():
    choice = input("""Arduino is not connected. Continue with only calculations?(y/n) \nEnter: """)
    while choice != 'n':
        if choice == 'y':
            user_input = input(user_choice)
            if user_input == 'f':
                l1 = int(input("Enter l1: "))
                l2 = int(input("Enter l2: "))
                calculation = Kinematics(l1, l2)
                calculation.forward()
            elif user_input == 'i':
                l1 = int(input("Enter l1 [mm]: "))
                l2 = int(input("Enter l2 [mm]: "))
                calculation = Kinematics(l1, l2)
                calculation.inverse()
            elif user_input == 'q':
                break
            else:
                raise TypeError("Your selection is not one listed above. Please try again.")


# actuates the servos based on the output values of the kinematic calculations
def option_2():
    user_input = input(user_choice)
    while user_input != 'q':
        if user_input == 'f':
            calculation = Kinematics(75, 75)
            result = calculation.forward()
            Servo(angle=result[0], pin=10).rotate_servo()
            Servo(angle=result[1], pin=11).rotate_servo()
            key_1 = input(" - press 'h' to get in home position and continue: ")
            while key_1 == 'h':
                Servo(angle=result[0], pin=10).home()
                Servo(angle=result[1], pin=11).home()
                break
        elif user_input == 'i':
            calculation = Kinematics(75, 75)
            result = calculation.inverse()
            Servo(angle=result[0], pin=10).rotate_servo()
            Servo(angle=result[1], pin=11).rotate_servo()
            key_2 = input(" - press 'h' to get in home position and continue: ")
            while key_2 == 'h':
                Servo(angle=result[0], pin=10).home()
                Servo(angle=result[1], pin=11).home()
                break
        else:
            raise TypeError("Your selection is not one listed above. Please try again.")
        user_input = input(user_choice)


def menu():
    if connect_port == 'None':
        option_1()
    else:
        option_2()


menu()
