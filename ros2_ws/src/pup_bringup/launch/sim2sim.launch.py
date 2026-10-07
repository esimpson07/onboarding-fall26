"""Bring up the whole sim2sim stack: simulator + policy (+ optional teleop).

    ros2 launch pup_bringup sim2sim.launch.py headless:=false teleop:=true
    ros2 launch pup_bringup sim2sim.launch.py policy_path:=/ws/runs/colab/policy.npz

`pup_sim/launch/sim_only.launch.py` is the template this is built from.
"""

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from pup.envs.constants import CHECKPOINTS


def generate_launch_description() -> LaunchDescription:
    """Return the launch description for the full sim2sim stack."""
    # ===== TODO(student): Declare the launch arguments and the three nodes =====
    headless = LaunchConfiguration("headless")
    policy_path = LaunchConfiguration("policy_path")
    teleop = LaunchConfiguration("teleop")
    realtime_factor = LaunchConfiguration("realtime_factor")
    return LaunchDescription([
        DeclareLaunchArgument("headless", default_value="true",
                              description="run without the MuJoCo viewer window"),
        DeclareLaunchArgument("policy_path",
                              default_value=str(CHECKPOINTS / "pup_joystick_flat_reference.npz"),
                              description="exported .npz policy to run"),
        DeclareLaunchArgument("teleop", default_value="false",
                              description="open a keyboard teleop window"),
        DeclareLaunchArgument("realtime_factor", default_value="1.0",
                              description=">1 runs the physics faster than wall clock"),
        Node(
            package="pup_sim",
            executable="sim_node",
            name="pup_sim",
            output="screen",
            parameters=[{"headless": headless, "realtime_factor": realtime_factor}],
        ),
        Node(
            package="pup_bringup",
            executable="policy_node",
            name="pup_policy",
            output="screen",
            parameters=[{"policy_path": policy_path}],
        ),
        Node(
            package="pup_sim",
            executable="teleop_node",
            name="pup_teleop",
            output="screen",
            prefix="xterm -e",
            condition=IfCondition(teleop),
        ),
    ])
    # ===== end TODO =====
