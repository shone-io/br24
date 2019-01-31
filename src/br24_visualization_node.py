#!/usr/bin/python
import rospy
import Tkinter as tk
from shone_sensor_msgs.msg import Scanline
from pyOpenBR24.br24_ui import br24_image_window

if __name__ == '__main__':
    rospy.init_node('br24_viz')
    radar_topic = rospy.get_param('radar_topic', '/radars/x_band/scanline')
    print(radar_topic)

    root = tk.Tk()
    img_window = br24_image_window(root, refresh_period=t60)
    brsub = rospy.Subscriber(radar_topic,
                             Scanline,
                             img_window.draw_scanline_ros,
                             queue_size=100)
    root.mainloop()
