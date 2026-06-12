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
olcon build --packages-select (packagename)

# Source the workspace configuration to map active packages to your environment
source install/setup.bash

# To run any file 
ros2 run (folder name) (file name)
eg: ros2 run q1_pkg listener

