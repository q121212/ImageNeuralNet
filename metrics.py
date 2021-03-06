#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
This file defines methods for calculation main metrics for images.
Then this metrics need to recalculate in weights for different purposes and finally: metrics + thier weights need to use for neuron's calculations.
Metrics - is a fundamental characteristics of images from different perspectives.
'''

import sys, os
lib_path = os.path.abspath(os.path.join('.', 'ImageFileFormat/'))
sys.path.insert(0, lib_path)

lib_path = os.path.abspath(os.path.join('.', 'Models/'))
sys.path.insert(0, lib_path)

lib_path = os.path.abspath(os.path.join('.', 'Extract/'))
sys.path.insert(0, lib_path)

lib_path = os.path.abspath(os.path.join('.', 'Transform/'))
sys.path.insert(0, lib_path)

import iff
import models
import extract
import transform


############# First-order metrics #############

### Metrics for detecting the presence of different types of elements in image ###

###### Metrics for corners elements ######

def weight_calculation(image, list_of_primitives):
  '''This method calculates the weight. 
  If image contains some primitives from list_of_primitives, this method return weight of primitives in list_of_primitives.
  Any weight is made up of primitive types If some types of primitives are contained in the image, then the weight is equal to the summ of their.'''

  weight = 0
  for i in range(len(list_of_primitives)):
    if extract.extract_a_primitive(image, list_of_primitives[i]) != []:
      weight+=1
  
  return weight
  

def corner_primitives_weight(path_to_image):
  '''This method for calculates weight of corners primitives in image.'''

  # a corner's primitives include 4 corners and also + (i.e. cross)
  list_of_primitives = [[[1,1],[1,0]], [[1,1],[0,1]], [[0,1],[1,1]], [[1,0],[1,1]], [[0,1,0],[1,1,1],[0,1,0]]] 

  weight = weight_calculation(iff.extract_image_from_file(path_to_image), list_of_primitives)

  # The resulting weight can be intrepreted as follows:
  # 1 <= weight <= 4 - image contains weight amount types of corners
  # if weight == 5: image contains at least one cross
  print("Weight of corner primitives in image ({0}) is: {1}".format(path_to_image, weight))
  return weight

def amount_corners_weight(image):
  '''Method for calculating another weight of image: amount of corners.
  In facty it's a more advanced and detailed method than corner_primitives_weight method.'''

  # a corner's primitives include 4 corners and also + (i.e. cross)
  list_of_primitives = [[[1,1],[1,0]], [[1,1],[0,1]], [[0,1],[1,1]], [[1,0],[1,1]], [[0,1,0],[1,1,1],[0,1,0]]] 

  amount_of_corners = []
  for i in range(len(list_of_primitives)):
    amount_of_corners.append(len(extract.extract_a_primitive(image, list_of_primitives[i])))
  print('Amount of corners for every type of primitives are the next: {0}'.format(amount_of_corners))
  return amount_of_corners

###### Metrics for lines elements ######
def amount_lines(path_to_image):
  
  lines = extract.extract_a_one_pixel_width_line_segments(path_to_image)
  size_lines, length_of_lines = [], []
  for i in lines:
    size_lines.append(len(i))
    for j in i:
      length_of_lines.append(j[2])
  
  print(length_of_lines)
  print('Amount of horizontal and vertical lines in image are respectively, the next: {0}'.format(size_lines))
  return size_lines 

### Metrics for defining relative length of image elements ###

### Metrics to determine the mutual arrangement the elements ###


############# Second-order metrics  #############
### Metrics made from First-order metrics ###

if __name__ == '__main__':
  #  
  path_to_image = os.path.abspath(os.path.join('.', 'Extract/image_for_border_extraction.iff'))
  iff.draw_image_from_file(path_to_image)
  # corner_primitives_weight(path_to_image)
  image = iff.extract_image_from_file(path_to_image)
  amount_corners_weight(image)
  amount_lines(path_to_image)

  pass
