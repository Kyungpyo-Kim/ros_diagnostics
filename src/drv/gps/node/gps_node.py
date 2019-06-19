#!/usr/bin/env python
# -*- coding: utf-8 -*-

import roslib
roslib.load_manifest('diagnostic_updater')

import rospy

import diagnostic_updater
import diagnostic_msgs

from sensor_msgs.msg import NavSatFix
from sensor_msgs.msg import NavSatStatus 

class DummyTask(diagnostic_updater.DiagnosticTask):
    def __init__(self):
        diagnostic_updater.DiagnosticTask.__init__(self,
            "Updater Derived from DiagnosticTask")

    def run(self, stat):
        stat.summary(diagnostic_msgs.msg.DiagnosticStatus.WARN,
            "This is another silly updater.")
        stat.add("Stupidicity of this updater", 2000.)
        return stat

if __name__=='__main__':
    ## init
    rospy.init_node("gps_node")

    ## publish
    pub_nav_sat_fix = rospy.Publisher('gps/fix', NavSatFix, queue_size=1)
    pub_nav_sat_stat = rospy.Publisher('gps/stat', NavSatStatus, queue_size=1)

    updater = diagnostic_updater.Updater()

    updater.setHardwareID("gps")
    
    dt = DummyTask()
    updater.add(dt)


    freq_bounds = {'min':90, 'max':110} # If you update these values, the
    nav_sat_fix_freq = diagnostic_updater.TopicDiagnostic("/gps/nav_sat_fix", updater,
        diagnostic_updater.FrequencyStatusParam(freq_bounds, 0.1, 10),  
        diagnostic_updater.TimeStampStatusParam(min_acceptable = -1, max_acceptable = 5))

    while not rospy.is_shutdown():

        rospy.sleep(0.1)

        msg_nav_sat_fix = NavSatFix()
        msg_nav_sat_stat = NavSatStatus()

        pub_nav_sat_fix.publish(msg_nav_sat_fix)
        nav_sat_fix_freq.tick(msg_nav_sat_fix.header.stamp)

        pub_nav_sat_stat.publish(msg_nav_sat_stat)

        updater.update()