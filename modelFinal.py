
# run one model in one window

from __future__ import print_function
from imutils.video import WebcamVideoStream
from imutils.video import FPS
import argparse
import imutils

import numpy as np
import os
import six.moves.urllib as urllib
import sys
import tarfile
import tensorflow as tf
import zipfile

from utils import label_map_util
from utils import visualization_utils as vis_util

from collections import defaultdict
from io import StringIO
from matplotlib import pyplot as plt
from PIL import Image
 
import cv2
cap0 = WebcamVideoStream(src=0).start()
#cap0 = WebcamVideoStream(src='rtsp://192.168.1.3:8080/h264_ulaw.sdp').start()
#cap1 = cv2.VideoCapture('rtsp://192.168.1.3:8080/h264_ulaw.sdp')
#cap0 = cv2.VideoCapture(0)
#cap1 = WebcamVideoStream(src='rtsp://192.168.1.3:8080/h264_ulaw.sdp').start()
 
sys.path.insert(0, '/Users/hassan/anaconda3/envs/myenv/lib/python3.6/site-packages/tensorflow/models/research/object_detection')
 
gun_label_map = label_map_util.load_labelmap('/Volumes/HASSAN/model/label_map.pbtxt')
gun_categories = label_map_util.convert_label_map_to_categories(
    gun_label_map, max_num_classes=1, use_display_name=True)
gun_category_index = label_map_util.create_category_index(gun_categories)

gun_detection_graph = tf.Graph()

with gun_detection_graph.as_default():
    gun_od_graph_def = tf.compat.v1.GraphDef()
    with tf.io.gfile.GFile('/Volumes/HASSAN/model/frozen_inference_graph2.pb', 'rb') as fid:
        gun_serialized_graph = fid.read()
        gun_od_graph_def.ParseFromString(gun_serialized_graph)
        tf.import_graph_def(gun_od_graph_def, name='')

    gun_session = tf.compat.v1.Session(graph=gun_detection_graph)

gun_image_tensor = gun_detection_graph.get_tensor_by_name('image_tensor:0')
gun_detection_boxes = gun_detection_graph.get_tensor_by_name(
    'detection_boxes:0')
gun_detection_scores = gun_detection_graph.get_tensor_by_name(
    'detection_scores:0')
gun_detection_classes = gun_detection_graph.get_tensor_by_name(
    'detection_classes:0')
gun_num_detections = gun_detection_graph.get_tensor_by_name(
    'num_detections:0')

batch_size = 1

while True:

    image_np_list = []
    for i in range(batch_size):
        image_np = cap0.read()

    # Expand dimensions since the model expects images to have shape: [1, None, None, 3]
    image_np = imutils.resize(image_np, width=400)
    image_np_expanded0 = np.expand_dims(image_np, axis=0)

    # Visualization of the results of a detection.
    (boxes, scores, classes, num) = gun_session.run(
    [gun_detection_boxes, gun_detection_scores,
    gun_detection_classes, gun_num_detections],
    feed_dict={gun_image_tensor: image_np_expanded0})
    vis_util.visualize_boxes_and_labels_on_image_array(
        image_np,
        np.squeeze(boxes),
        np.squeeze(classes).astype(np.int32),
        np.squeeze(scores),
        gun_category_index,
        use_normalized_coordinates=True,
        line_thickness=2)
      
    cv2.imshow('object detection', image_np)

    # Exit Option
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break