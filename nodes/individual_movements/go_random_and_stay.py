#!/usr/bin/env python
import rospy
from random import randrange
from swarm.msg import QuadHoverPos

if __name__ == '__main__':
    pub = rospy.Publisher('des_pos', QuadHoverPos, queue_size=1)
    rospy.init_node('go_up_and_stay', anonymous=True)
    rate = rospy.Rate(100)
    
    quad = QuadHoverPos();
    quad.header.frame_id = 'world'
    quad.position.x = 0
    quad.position.y = 0
    quad.position.z = 0
    quad.yaw = 0

    try:
        while not rospy.is_shutdown():
            quad.header.stamp = rospy.Time.now()
            if quad.header.stamp.secs >= 2:
                if quad.position.x == 0: quad.position.x = randrange(-10,11,1) / 10.0
                if quad.position.y == 0: quad.position.y = randrange(-10,11,1) / 10.0
                if quad.position.z == 0: quad.position.z = randrange(3,11,1) / 10.0
            pub.publish(quad)
            rospy.loginfo("[%f, %f, %f - %f]", quad.position.x, quad.position.y, quad.position.z, quad.yaw)
            rate.sleep()

    except rospy.ROSInterruptException:
        pass

    finally:
        quad.header.stamp = rospy.Time.now()
        quad.position.x = 0
        quad.position.y = 0
        quad.position.z = 0
        pub.publish(quad)
        rospy.loginfo("End of node")
