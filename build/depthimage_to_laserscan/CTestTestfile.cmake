# CMake generated Testfile for 
# Source directory: /home/nvidia/ros2_catkin_ws/src/depthimage_to_laserscan
# Build directory: /home/nvidia/ros2_catkin_ws/build/depthimage_to_laserscan
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(depthimage_to_laserscan-test "/usr/bin/python3" "-u" "/opt/ros/foxy/share/ament_cmake_test/cmake/run_test.py" "/home/nvidia/ros2_catkin_ws/build/depthimage_to_laserscan/test_results/depthimage_to_laserscan/depthimage_to_laserscan-test.gtest.xml" "--package-name" "depthimage_to_laserscan" "--output-file" "/home/nvidia/ros2_catkin_ws/build/depthimage_to_laserscan/ament_cmake_gtest/depthimage_to_laserscan-test.txt" "--command" "/home/nvidia/ros2_catkin_ws/build/depthimage_to_laserscan/depthimage_to_laserscan-test" "--gtest_output=xml:/home/nvidia/ros2_catkin_ws/build/depthimage_to_laserscan/test_results/depthimage_to_laserscan/depthimage_to_laserscan-test.gtest.xml")
set_tests_properties(depthimage_to_laserscan-test PROPERTIES  LABELS "gtest" REQUIRED_FILES "/home/nvidia/ros2_catkin_ws/build/depthimage_to_laserscan/depthimage_to_laserscan-test" TIMEOUT "60" WORKING_DIRECTORY "/home/nvidia/ros2_catkin_ws/build/depthimage_to_laserscan" _BACKTRACE_TRIPLES "/opt/ros/foxy/share/ament_cmake_test/cmake/ament_add_test.cmake;118;add_test;/opt/ros/foxy/share/ament_cmake_gtest/cmake/ament_add_gtest_test.cmake;86;ament_add_test;/opt/ros/foxy/share/ament_cmake_gtest/cmake/ament_add_gtest.cmake;93;ament_add_gtest_test;/home/nvidia/ros2_catkin_ws/src/depthimage_to_laserscan/CMakeLists.txt;91;ament_add_gtest;/home/nvidia/ros2_catkin_ws/src/depthimage_to_laserscan/CMakeLists.txt;0;")
subdirs("gtest")
