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
* **"TopicDiagnostic"** 를 이용한 topic 관리 기능,
* **"DiagnosticTask"** 를 이용한 task 관리 기능이다.


파이썬 코드를 좀 더 들여다 보자.
(IMU 드라이버는 c++ 코드로 구현되어 있고, [nlamprian](http://nlamprian.me/blog/software/ros/2018/03/21/ros-diagnostics/)를 참고하였다. 해당 블로그에 코드도 잘 설명되어 있다!)

## **"TopicDiagnostic"** 를 이용한 Topic 관리 기능
```python
class GpsNode():
    def __init__(self):

        rospy.init_node("gps_node")

        ## publish
        self.pub_nav_fix = rospy.Publisher('gps/fix', NavSatFix, queue_size=1)
        
        """
        ...
        """

        freq_bounds = {'min':18., 'max':22.} # If you update these values, the
        self.nav_fix_freq = diagnostic_updater.TopicDiagnostic("/gps/fix", self.updater,
            diagnostic_updater.FrequencyStatusParam(freq_bounds, 0.02, 10),  
            diagnostic_updater.TimeStampStatusParam(min_acceptable = -1, max_acceptable = 1))
        """
        ...
        """
```
위의 코드에서 self.pub_nav_fix 와 self.nav_fix_freq 두개의 publisher 를 생성하였다. self.pub_nav_fix 는 실제 드라이버에서 publish 할 topic publisher 이고, self.nav_fix_freq 는 이와 함께 tick 을 만들어서 publisher 가 잘 동작하는지 확인할 수 있도록하는 diagnostic 기능을 제공하는 역할을 한다. c++ 에서는 이부분을 하나의 객체로 연결하여 사용할 수 있게 되어 있지만, python 에서는 따로 분리되어 있는 예제만 확인하였다. Topic 이름을 같이 사용하여 기능적으로는 동일하게 확인할 수 있도록 한 것 같다.

TopicDiagnostic 객체의 생성 파라미터는  frequency 와 timestamp 에 관한 파라미터가 있으며, 각각 최대/최소, 시간에 대해서는 얼만큼에 시간에 대해서 tolerance 를 갖게 하는지 설정할 수 있다.

```python
def pub(self):
    """
    ...
    """

    self.pub_nav_fix.publish(msg_nav_sat_fix)
    self.nav_fix_freq.tick(msg_nav_sat_fix.header.stamp)

    """
    ...
    """
```

동작은 위와같이 publish 와 tick 생성을 같이 수행하므로써, frequency 에는 이상이 없는지, timestamp 는 문제 없는지 모니터링 할 수 있게 해준다.


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

```python
class GpsNode():
    def __init__(self):

        """
        ...
        """
        ## diagnostics updater
        self.updater = diagnostic_updater.Updater()
        self.updater.setHardwareID("gps")
    
        gdt = GpsDiagnosticTask()
        self.updater.add(gdt)
```

그리고 Updater() 객체를 생성하고 여기에 **add** method를 이용하여 **GpsDiagnosticTask()** 클래스의 객체를 추가하면 updater 가 update 를 수행할 때 마다 run 함수를 호출할 수 있게 한다.

실제 사용을 위해서는 run 함수에서 알고리즘/센서처리로직을 수행하고, 그 결과에 대한 status와 설명을 추가하여 task 를 관리할 수 있게 된다.


## Summary
* **"TopicDiagnostic"** 를 이용해 publish 되는 topic 관리
  + frequency monitoring
  + timestamp monitoring
* **"DiagnosticTask"** 를 이용한 함수 오버로딩을 통한
  + 모니터링을 위한 status 및 message 생성

  ## Reference
* http://nlamprian.me/blog/software/ros/2018/03/21/ros-diagnostics/
* http://wiki.ros.org/diagnostics
* https://github.com/ros/diagnostics