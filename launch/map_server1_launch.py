from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='nav2_util',
            executable='lifecycle_bringup',
            output='screen',
            arguments=['map_server'],
            parameters=[{'yaml_filename': '/home/duc/dev_ws/src/articubot_one/config/my_map.yaml'}]
        ),
    ])
