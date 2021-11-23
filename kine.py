from numpy import *
from math import *


class Kinematics:
    def __init__(self, l1, l2):
        self.l1 = l1
        self.l2 = l2

    def forward(self):  # forward kinematics using the rotation matrix and homogeneous transformation
        theta_1 = int(input("Enter lower joint angle [0 - 180 deg]: "))
        theta_2 = int(input("Enter upper joint angle [0 - 180 deg]: "))
        theta_1 = radians(theta_1)
        theta_2 = radians(theta_2)
        r0_1 = [[cos(theta_1), -sin(theta_1), 0],
                [sin(theta_1), cos(theta_1), 0],
                [0, 0, 1]]
        r1_2 = [[cos(theta_2), -sin(theta_2), 0],
                [sin(theta_2), cos(theta_2), 0],
                [0, 0, 1]]
        r0_2 = dot(r0_1, r1_2)
        print('\n')
        print(f'Rotation matrix R0,2 = \n{matrix(r0_2)}')
        print('\n')
        d0_1 = [[self.l1 * cos(theta_1)],
                [self.l1 * sin(theta_1)],
                [0]]
        d1_2 = [[self.l2 * cos(theta_2)],
                [self.l1 * sin(theta_2)],
                [0]]
        h0_1 = concatenate((r0_1, d0_1), 1)
        h0_1 = concatenate((h0_1, [[0, 0, 0, 1]]), 0)
        h1_2 = concatenate((r1_2, d1_2), 1)
        h1_2 = concatenate((h1_2, [[0, 0, 0, 1]]), 0)
        h0_2 = dot(h0_1, h1_2)
        print(f'Homogeneous transformation matrix = \n{matrix(h0_2)}')
        print('\n')
        x = h0_2[0, 3]
        y = h0_2[1, 3]
        print(f"End effector coordinates: x = {x}, y = {y} [mm]")
        theta_1 = int(degrees(theta_1))
        theta_2 = int(degrees(theta_2))
        angles = [theta_1, theta_2]
        return angles

    def inverse(self):  # inverse kinematics using plane trigonometric equations
        x = int(input("Enter x coordinate [mm]: "))
        y = int(input("Enter y coordinate [mm]: "))
        cos_theta_2 = (x ** 2 + y ** 2 - self.l1 ** 2 - self.l2 ** 2) / (2 * self.l1 * self.l2)
        sin_theta_2 = sqrt(1 - pow(cos_theta_2, 2))
        cos_theta_1 = (x * (self.l1 + self.l2 * cos_theta_2) +
                       y * self.l2 * sin_theta_2) / (x ** 2 + y ** 2)
        theta_1 = int(degrees(atan2(sqrt(1 - pow(cos_theta_1, 2)), cos_theta_1)))
        theta_2 = int(degrees(atan2(sqrt(1 - pow(cos_theta_2, 2)), cos_theta_2)))
        print('\n')
        print(f"Joint angles: theta 1 = {theta_1} [deg], theta 2 = {theta_2} [deg]")
        angles = [theta_1, theta_2]
        return angles
