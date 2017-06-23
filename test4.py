# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 09:25:52 2017

@author: yiyuezhuo
"""

import tensorflow as tf
from tensorflow.python.framework import ops


X = tf.random_normal([])
Y = tf.Variable(X)
Z = ops.convert_to_tensor(Y)

sess = tf.Session()
sess.run(tf.initialize_all_variables())
sess.run(X)
sess.run(Y)
sess.run(Z)