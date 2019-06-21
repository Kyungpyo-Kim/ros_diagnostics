# ROS Diagnostics 패키지 이해하기

ROS 패키지 중 하드웨어의 상태를 모니터링을 하는 [diagnostic](http://wiki.ros.org/diagnostics) 패키지가 있다. 좀 더 정확히 설명하면, ROS와 하드웨어(센서, 엑츄에이터 등)를 연결해주는 **드라이버**가 잘 움직이고 있는지, 나쁜짓은 안하는지 등을 모니터링하기 쉽게 해주는 패키지이다.

하지만 [ROS Wiki](http://wiki.ros.org/diagnostics) 의 설명은 너무 어렵고, [nlamprian 블로그](http://nlamprian.me/blog/software/ros/2018/03/21/ros-diagnostics/)가 그나마 참고가 되긴 했지만 실제로 사용하기에는 어려움이... 시행착오가 많았다.

그럼에도 불구하고 이 패키지를 사용하려고 애쓴 이유는 ROS 기반으로 만들어진 하드웨어 드라이버가 기본적으로 diagnotics 패키지를 이용해서 하드웨어 드라이버의 상태를 모니터링할 수 있게 지원하고 이 기능을 사용하고 싶었기 때문이다. 이 기능을 내가 만들기는 너무너무 매우매우 귀찮기도 하고, 이 패키지를 이용하면 *센서가 많아질 경우* 이를 한번에 관리하고 로깅하고 다시 리플레이 해서 문제분석을 하기에 용이할 것 같다는 생각이 들었다. 

사설이 길었다, 최대한 쉽고 다른데 갔다 쓰기 편하게 예제 프로젝트를 만들어 본다. 그리고 이 패키지는 원래 하드웨어 드라이버의 모니터링을 위해서 만들어지기는 했지만, 어플리케이션(알고리즘)에도 monitoring 기능을 넣기 위한 방법을 같이 고민해 본다.

## Diagnostic 의 기본 구조
기본 구조 및 동작 원리

![기본 구조 다이어그램](https://github.com/Kyungpyo-Kim/ros_diagnostics/blob/master/doc/image/diagram.jpg?raw=true)

기본구조는 그림과 같이 크게 updater, aggregator, 그리고 rqt_monitor 이렇게 세개의 부분(모듈이라고 하겠다)으로 설명할 수 있을 것 같다.

#### Updator
Updator 는 말그대로 모니터링 하고자하는 **것들을** 업데이트 해주는 모듈이다. 이 것들에 해당하는 것은 **topic**, **node** 로 관리되는 task, 그리고 **service** 등이다.
미리 정의된 여러 모듈들을 이용해 publishing 되는 topic 의 frequency 나 task 의 life signal 등을 업데이트 해준다. ROS 의 diagnostics 패키지를 이용하기 위해서는 updator 를 통해 제공되는 모듈들을 이용해 업데이트를 하는 과정을 거쳐야 한다(코딩을 해줘야 한다!).

#### Aggregator
Aggregator 는 말그대로 updator 를 통해 update 된 결과들을 통합해주는 역할을 한다. 그냥 이정도로만 이해를 했다.

#### Rqt_monitor
업데이트 된 결과는 ROS의 몇가지 시각화 도구를 이용해서 모니터링이 가능해진다. 몇가지가 있지만 **rqt_monitor** 를 이용해 모니터링이 가능한데, 결과를 ***.ymal** 을 이용해서 카테고리를 구성하여 보기 쉽게 해준다.

#### 요약
요약하면, 여러가지 topic이나 task들을 **updator** 를 통해 업데이트 하고 **aggregator** 를 이용해 통합한 결과를 **rqt_monitor** 도구를 이용해 모니터링한다.

#### Getting Started
```bash
git clone https://github.com/Kyungpyo-Kim/ros_diagnostics.git
cd ros_diagnostics
catkin_make
source devel/setup.bash
roslaunch launch/all.launch
```


## Reference
* http://nlamprian.me/blog/software/ros/2018/03/21/ros-diagnostics/
* http://wiki.ros.org/diagnostics
* https://github.com/ros/diagnostics
