from setuptools import find_packages, setup

package_name = 'mypkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='charan',
    maintainer_email='charan@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "test_node = mypkg.first:main",
            "drawcircle = mypkg.drawcircle:main",
            "pose_sub = mypkg.pose_sub:main",
            "turtlecontroller = mypkg.turtle_controller:main",
            "teleopclient = mypkg.teleop_client:main"
        ],
    },
)
