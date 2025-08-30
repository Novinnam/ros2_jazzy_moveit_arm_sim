import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/novinnam/Desktop/ros2_jazzy_moveit_arm_sim/ros2_ws/install/my_py_pkg'
