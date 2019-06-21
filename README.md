# ros_diagnostics
ROS diagnostics package exercise

## 관련 문서
* [ROS Diagnostics 패키지 이해하기](https://kyungpyo-kim/github.io)
* [ROS Diagnostics 패키지 센서 드라이버에 적용하기](https://kyungpyo-kim/github.io)
* [ROS Diagnostics 패키지 어플리케이션에 적용하기](https://kyungpyo-kim/github.io)

## Getting Started

```bash
git clone https://github.com/Kyungpyo-Kim/ros_diagnostics.git
cd ros_diagnostics
chmod +x src/drv/gps/node/gps_node.py
catkin_make
source devel/setup.bash
roslaunch launch/all.launch
```

#### Issue "/usr/bin/env: ‘python\r’: No such file or directory"
Window 에서 병렬로 code 를 작성하여 위와 같은 error 가 발생할 수 있다.
error 발생 시 다음 링크를 참고하여 "src/drv/gps/node/gps_node.py" 파일 속성을 변경하면 된다.
* [참고링크](https://118k.tistory.com/706)

## Reference
* http://nlamprian.me/blog/software/ros/2018/03/21/ros-diagnostics/
* http://wiki.ros.org/diagnostics
* https://github.com/ros/diagnostics
