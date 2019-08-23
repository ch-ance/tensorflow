import tensorflow as tf

a = tf.Variable(3, name="z")
b = tf.Variable(14, name="y")
f = a * b

init = tf.global_variables_initializer()
with tf.Session() as s:
    init.run()
    print(f.eval())
