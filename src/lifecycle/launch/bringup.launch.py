from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    lifecycle_node = Node(
        package='lifecycle',
        executable='lifecycle_node',
        name='lifecyclenode'
    )

    lifecyclemanager = Node(
        package='lifecycle',
        executable='lifecycle_manager',
        name='lifecycle'
    )

    ld.add_action(lifecycle_node)
    ld.add_action(lifecyclemanager)

    return ld