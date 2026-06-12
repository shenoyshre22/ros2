# ROS 2 Communication Architecture Practice Manual

This repository contains five modular package implementations demonstrating generic publisher-subscriber messaging pipelines, multi-node daisy-chain filters, system clock data timestamping, and threshold data validation structures.

---

##  1. Universal Workspace Verification & Compilation

Prior to executing any nodes, the entire active workspace environment must be cleaned, compiled, and registered to ensure execution paths are current. Run the following sequence from the main workspace root directory:

```bash
# Navigate to the workspace root directory ALWAYS if you want to run the codes , (source is to edit codes or make package)
cd ~/ros2_ws

# Force clean previous build artifacts to prevent stale path mapping
rm -rf build/ install/ log/

# Compile all local source subdirectory packages
colcon build
# but if you want to compile just one file then:
colcon build --packages-select (packagename)

# Source the workspace configuration to map active packages to your environment
source install/setup.bash

# To run any file 
ros2 run (folder name)(file name)
eg: ros2 run q1_pkg listener

```
##  2. How to Navigate to the folders for code:

```bash
go to any question say for now assignment1_pkg --> assignment1_pkg --> (navigate to any given file) listener.py / publisher_one.py etc
```

## 3. VS Code edits:

add the codes in vs code or using the nano command in terminal. then edit setup.py 
navigate to folder name -> foldername with the same name -> setup.py -> last parah under entry_points
to register Python scripts as executable nodes, you must add the mapping 
and inside the `console_scripts` array of each package's `setup.py` file.
the format is :
```bash
"test_node = my_robot_controller.my_first_node:main"
in the format: executable_name = package_name.file_name:main'
```
This is done because ROS 2 requires an explicit entry point to bind your source code to the terminal environment, allowing the underlying discovery system to recognize and call your custom execution loops during a `ros2 run` command.

