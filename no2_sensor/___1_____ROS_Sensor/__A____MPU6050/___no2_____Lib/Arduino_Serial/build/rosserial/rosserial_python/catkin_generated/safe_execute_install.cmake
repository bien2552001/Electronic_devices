execute_process(COMMAND "/home/bien/ros1/hardware/Arduino_Development/Arduino_Ros/Lib/Arduino_Serial/build/rosserial/rosserial_python/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/bien/ros1/hardware/Arduino_Development/Arduino_Ros/Lib/Arduino_Serial/build/rosserial/rosserial_python/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
