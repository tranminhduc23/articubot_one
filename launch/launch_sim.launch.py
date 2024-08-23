import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    package_name = 'articubot_one'  # Tên gói chứa mô hình robot của bạn

    # Bao gồm file khởi động của robot_state_publisher
    rsp = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(
                get_package_share_directory(package_name), 'launch', 'rsp.launch.py'      # dung de lay duong dan toi thu muc share cua ros2, cu the la file launch cua gazebo va rsp.launch
            )
        ]),
        launch_arguments={'use_sim_time': 'true'}.items()
    )

    # Bao gồm file khởi động của Gazebo
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(
                get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py'    # file chuan cua gazebo_ros, khoi dong gazebo
            )
        ])
    )

    # Chạy node spawn_entity từ gói gazebo_ros
    spawn_entity = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=[
            '-topic', 'robot_description',        #-topic robot_description ma mo hinh URDF cua robot se duoc lay   
            '-entity', 'my-bot'                    # ten cua entity trong mo phong, mau chot la o - cua -entity
        ],
        output='screen'
    )

    return LaunchDescription([
        rsp,
        gazebo,
        spawn_entity,
    ])
