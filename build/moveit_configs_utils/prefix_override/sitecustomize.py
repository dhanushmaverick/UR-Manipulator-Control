import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/pran/Robot_Arm_ur5/install/moveit_configs_utils'
