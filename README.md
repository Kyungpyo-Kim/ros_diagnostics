# ros_diagnostics
ROS diagnostics package exercise

ROS 패키지 중 하드웨어의 상태를 모니터링을 하는 [diagnostic](http://wiki.ros.org/diagnostics) 패키지가 있다. 좀 더 정확히 설명하면, ROS와 하드웨어(센서, 엑츄에이터 등)를 연결해주는 **드라이버**가 잘 움직이고 있는지, 나쁜짓은 안하는지 등을 모니터링하기 쉽게 해주는 패키지이다.

하지만 [ROS Wiki](http://wiki.ros.org/diagnostics) 의 설명은 너무 어렵고, [nlamprian 블로그](http://nlamprian.me/blog/software/ros/2018/03/21/ros-diagnostics/)가 그나마 참고가 되긴 했지만 실제로 사용하기에는 어려움이... 시행착오가 많았다.

그럼에도 불구하고 이 패키지를 사용하려고 애쓴 이유는 ROS 기반으로 만들어진 하드웨어 드라이버가 기본적으로 diagnotics 패키지를 이용해서 하드웨어 드라이버의 상태를 모니터링할 수 있게 지원하고 이 기능을 사용하고 싶었기 때문이다. 이 기능을 내가 만들기는 너무너무 매우매우 귀찮기도 하고, 이 패키지를 이용하면 *센서가 많아질 경우* 이를 한번에 관리하고 로깅하고 다시 리플레이 해서 문제분석을 하기에 용이할 것 같다는 생각이 들었다. 

사설이 길었다, 최대한 쉽고 다른데 갔다 쓰기 편하게 예제 프로젝트를 만들어 본다. 그리고 이 패키지는 원래 하드웨어 드라이버의 모니터링을 위해서 만들어지기는 했지만, 어플리케이션(알고리즘)에도 monitoring 기능을 넣기 위한 방법을 같이 고민해 본다.

## Diagnostic 의 기본 구조
기본 구조 및 동작 원리

![기본 구조 다이어그램](/doc/iamge/diagram.png)
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

## Sensor 드라이버에 적용
센서 드라이버에 적용하는 방법을 먼저 살펴본다.

센서 ROS에서 제공되는 센서 드라이버들은 대부분 diagnostics 패키지를 이용하여 센서의 상태들을 업데이트하여 모니터링 할 수 있도록 해준다. 대표적인 것들이 드라이버를 통해 확인한 센서의 연결 상태나 publish 되는 센서 데이터의 주기 등이다. 써보니깐 *잘 만든 드라이버*는 자세한 진단결과를 뱉어 준다.

센서 드라이버를 직접 만드는 경우는 거의 없기를... 없어야 하는데... 생각보다 많다. 그래서 publish 되는 topic 의 주기를 모니터링 하고 센서의 연결상태를 update 하는 방법에 대해서 정리해 보았다.

이부분은 다음의 블로그를 많이 참고 하였다. [[요기]](http://nlamprian.me/blog/software/ros/2018/03/21/ros-diagnostics/)

#### 센서 드라이버 작성하기
Diagnostics 패키지를 이용하여 센서 드라이버를 작성하는 방법을 먼저 정리해 본다. 앞에서 잠깐 언급한 *잘 만든 드라이버*는 다음의 결과들을 진단하여 모니터링할 수 있게 해준다.
* Publishing 되는 센서의 결과 topic 의 주기
* 센서의 연결 상태

#### Aggregator 실행

#### Rqt_monitor 로 모니터링 하기


## Application 에 적용

## Reference
* http://nlamprian.me/blog/software/ros/2018/03/21/ros-diagnostics/
* http://wiki.ros.org/diagnostics
* https://github.com/ros/diagnostics