import tensorflow as tf

sess=tf.Session()

saver = tf.train.import_meta_graph('my_model-1000.meta')
saver.restore(sess,tf.train.latest_checkpoint('./'))

graph = tf.get_default_graph()
prediction = graph.get_tensor_by_name("op_prediction:0")

last = graph.get_tensor_by_name("last:0")
weight = graph.get_tensor_by_name("weight:0")
bias = graph.get_tensor_by_name("bias:0")
example = [[1][0][1][1][1][1][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0]]
session.run(prediction,example)

