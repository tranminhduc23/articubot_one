from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Node to run the map_server
        Node(
            package="nav2_map_server",
            executable="map_server",
            output="screen",
            parameters=[{"yaml_filename": "/home/duc/dev_ws/src/articubot_one/config/my_map.yaml"}]
        ),

        # Node to run RViz2
        Node(
            package="rviz2",
            executable="rviz2",
            name="rviz2",
            output="screen",
            arguments=["-d", "/home/duc/dev_ws/src/articubot_one/config/my_rviz_config.rviz"]
        ),
    ])
