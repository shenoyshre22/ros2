# ROS 2 Communication Architecture Practice Manual

This repository contains five modular package implementations demonstrating generic publisher-subscriber messaging pipelines, multi-node daisy-chain filters, system clock data timestamping, and threshold data validation structures.

---

## 🏗️ 1. Universal Workspace Verification & Compilation

Prior to executing any nodes, the entire active workspace environment must be cleaned, compiled, and registered to ensure execution paths are current. Run the following sequence from the main workspace root directory:

```bash
# Navigate to the workspace root directory
cd ~/ros2_ws

# Force clean previous build artifacts to prevent stale path mapping
rm -rf build/ install/ log/

# Compile all local source subdirectory packages
colcon build

# Source the workspace configuration to map active packages to your environment
source install/setup.bash

