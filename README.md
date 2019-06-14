# ros_diagnostics
ROS diagnostics package exercise

ROS 패키지 중 하드웨어의 상태를 모니터링을 하는 [diagnostic](http://wiki.ros.org/diagnostics) 패키지가 있다. 좀 더 정확히 설명하면, ROS와 하드웨어(센서, 엑츄에이터 등)를 연결해주는 **드라이버**가 잘 움직이고 있는지, 나쁜짓은 안하는지 등을 모니터링하기 쉽게 해주는 패키지이다.

하지만 [ROS Wiki](http://wiki.ros.org/diagnostics) 의 설명은 너무 어렵고, [nlamprian 블로그](http://nlamprian.me/blog/software/ros/2018/03/21/ros-diagnostics/)가 그나마 참고가 되긴 했지만 실제로 사용하기에는 어려움이... 시행착오가 많았다.

그럼에도 불구하고 이 패키지를 사용하려고 애쓴 이유는 ROS 기반으로 만들어진 하드웨어 드라이버가 기본적으로 diagnotics 패키지를 이용해서 하드웨어 드라이버의 상태를 모니터링할 수 있게 지원하고 이 기능을 사용하고 싶었기 때문이다. 이 기능을 내가 만들기는 너무너무 매우매우 귀찮기도 하고, 이 패키지를 이용하면 *센서가 많아질 경우* 이를 한번에 관리하고 로깅하고 다시 리플레이 해서 문제분석을 하기에 용이할 것 같다는 생각이 들었다. 

사설이 길었다, 최대한 쉽고 다른데 갔다 쓰기 편하게 예제 프로젝트를 만들어 본다. 그리고 이 패키지는 원래 하드웨어 드라이버의 모니터링을 위해서 만들어지기는 했지만, 어플리케이션(알고리즘)에도 monitoring 기능을 넣기 위한 방법을 같이 고민해 본다.

## Diagnostic 의 기본 구조
기본 구조 및 동작 원리

## Sensor 드라이버에 적용

## Application 에 적용

## Reference
* http://nlamprian.me/blog/software/ros/2018/03/21/ros-diagnostics/
* http://wiki.ros.org/diagnostics