#!/usr/bin/env python
#1st line ensures script is executed as a Python script
#Every Python ROS Node will have this declaration at the top

# license removed for brevity

## Simple talker demo that published std_msgs/Strings messages
## to the 'chatter' topic

#Needed when writing an ROS Node.
import rospy
#so we can reuse the std_msgs/String message type 
#(a simple string container) for publishing. 
from std_msgs.msg import String

def talker():
    #Define the talker's interface to the rest of ROS
    #Declare node is publishing to the chatter topic
    #using the message type String
    #Queue # limits num messsages if not getting fast enough
    pub = rospy.Publisher('chatter', String, queue_size=10)
    #Tell rospy the name of your node
    #Anonymous eensures node has a unique name
    rospy.init_node('talker', anonymous=True)
    #Rate object rate-- Go through loop 10/s
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        # Write string to screen, Node's log file & rosout
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
