# Copyright 2023 Matthew Lock
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Driver for the Jetbot robot."""

import rclpy
# from controller import Camera

class JetbotDriver:
    def init(self, webots_node, properties):

        self.__robot = webots_node.robot
        self.__timestep = int(self.__robot.getBasicTimeStep())

        self.webots_node = webots_node

        # self.left_motor = webots_node.robot.getDevice(properties['left_motor'])
        # self.left_motor.setPosition(float('inf'))
        # self.left_motor.setVelocity(0.0)

        # self.right_motor = webots_node.robot.getDevice(properties['right_motor'])
        # self.right_motor.setPosition(float('inf'))
        # self.right_motor.setVelocity(0.0)

        # Sensors
        self.__camera = self.__robot.getDevice('camera')
        self.__camera.enable(self.__timestep)

        # Enable camera
        # self.__camera_sampling_period = 
        # self.__camera.enable(self.__timestep)

        # ROS2 interface
        rclpy.init(args=None)
        self.__node = rclpy.create_node('jetbot_driver')

    def step(self):
        rclpy.spin_once(self.__node, timeout_sec=0.0)

