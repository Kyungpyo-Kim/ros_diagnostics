# ROS Diagnostics 패키지 센서 드라이버에 적용하기

아래의 Getting started 를 참고하여 github에 업로드한 예제를 실행해 볼 수 있다.

#### Getting Started
```bash
git clone https://github.com/Kyungpyo-Kim/ros_diagnostics.git
cd ros_diagnostics
catkin_make
source devel/setup.bash
roslaunch launch/all.launch
```

센서 드라이버에 적용된 diagnostics 기능은
* **"DiagnosticTask"** 를 이용한 task 관리 기능,
* **"TopicDiagnostic"** 를 이용한 topic 관리 기능이다.

파이썬 코드를 좀 더 들여다 보자.
(IMU 드라이버는 c++ 코드로 구현되어 있고, [nlamprian](http://nlamprian.me/blog/software/ros/2018/03/21/ros-diagnostics/)를 참고하였다. 해당 블로그에 코드도 잘 설명되어 있다!)

## **"DiagnosticTask"** 를 이용한 task 관리 기능
```python
# gps_node.py
class GpsDiagnosticTask(diagnostic_updater.DiagnosticTask):
    def __init__(self):
        diagnostic_updater.DiagnosticTask.__init__(self,
            "Updater Derived from DiagnosticTask") ## task 이름

    def run(self, stat):
        stat.summary(diagnostic_msgs.msg.DiagnosticStatus.WARN,
            "This is another silly updater.") ## task 상태 업데이트
        stat.add("Stupidicity of this updater", 2000.)
        return stat
````

코드를 보면 초기화 및 run 함수를 통해서 task 의 이름, task 의 상태를 업데이트 할 수 있다.
stat.summary() 를 통해서 DiagnosticStatus 를 지정하고, task 의 상태에 대한 설명을 추가할 수 있다.

실제 사용을 위해서는 run 함수에서 알고리즘/센서처리로직을 수행하고, 그 결과에 대한 status와 설명을 추가하여 task 를 관리할 수 있게 된다.

```python
class GpsNode():
    def __init__(self):

        """
        ...
        """
    
        gdt = GpsDiagnosticTask()
        self.updater.add(gdt)
```