#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import random

import roslib
roslib.load_manifest('diagnostic_updater')
import rospy
import diagnostic_updater
import diagnostic_msgs
from sensor_msgs.msg import NavSatFix
from sensor_msgs.msg import NavSatStatus 


class GpsDiagnosticTask(diagnostic_updater.DiagnosticTask):
    def __init__(self):
        diagnostic_updater.DiagnosticTask.__init__(self,
            "Updater Derived from DiagnosticTask")

    def run(self, stat):
        stat.summary(diagnostic_msgs.msg.DiagnosticStatus.WARN,
            "This is another silly updater.")
        stat.add("Stupidicity of this updater", 2000.)
        return stat


class GpsNode():
    def __init__(self):

        rospy.init_node("gps_node")

        ## publish
        self.pub_nav_fix = rospy.Publisher('gps/fix', NavSatFix, queue_size=1)
        self.pub_nav_stat = rospy.Publisher('gps/stat', NavSatStatus, queue_size=1)

        ## diagnostics updater
        self.updater = diagnostic_updater.Updater()
        self.updater.setHardwareID("gps")
    
        gdt = GpsDiagnosticTask()
        self.updater.add(gdt)

        freq_bounds = {'min':18., 'max':22.} # If you update these values, the
        self.nav_fix_freq = diagnostic_updater.TopicDiagnostic("/gps/fix", self.updater,
            diagnostic_updater.FrequencyStatusParam(freq_bounds, 0.02, 10),  
            diagnostic_updater.TimeStampStatusParam(min_acceptable = -1, max_acceptable = 1))

        ## threading
        self.lock = threading.Lock()

        ## random
        random.seed()


    def diag_thread(self):
        self.lock.acquire()
        self.updater.update()
        self.lock.release()

        threading.Timer(1. / 50. , self.diag_thread).start()


    def pub(self):
        msg_nav_sat_fix = NavSatFix()
        msg_nav_sat_fix.header.stamp = rospy.Time.now() + rospy.Duration(random.gauss(0., 0.35))
        msg_nav_sat_stat = NavSatStatus()

        self.pub_nav_fix.publish(msg_nav_sat_fix)
        self.nav_fix_freq.tick(msg_nav_sat_fix.header.stamp)

        self.pub_nav_stat.publish(msg_nav_sat_stat)


    def run(self):

        self.diag_thread()

        while not rospy.is_shutdown():
            
            self.pub()

            freq = random.gauss(20, 5.0)
            rospy.sleep(1. / freq)


if __name__=='__main__':
    gn = GpsNode()
    gn.run()
    