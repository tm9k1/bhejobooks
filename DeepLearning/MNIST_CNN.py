''' MNIST dataset training 
Allows detection of Numbers '''
from __future__ import print_function
#Checking GPU running or not
# import tensorflow as tf
# device_name = tf.test.gpu_device_name()
# if device_name != '/device:GPU:0':
#   raise SystemError('GPU device not found')
# print('Found GPU at: {}'.format(device_name))
import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as k
# available -> Theano, CNTK, Tensorflow

batch_size = 120
num_classes = 10
epochs = 12

# image DIMENSIONSs
img_rows,img_cols=28,28

# segregate dataset into training and test
(x_train,y_train),(x_test,y_test)= mnist.load_data()

# Making sure that image format is not dependent on KERAS defaults anymore !
if k.image_data_format() == 'channels_first':
  x_train=x_train.reshape(x_train.shape[0],1,img_rows,img_cols)
  x_test=x_test.reshape(x_test.shape[0],img_rows,img_cols,1)
  input_shape=(1,img_rows,img_cols)
else:
  x_train=x_train.reshape(x_train.shape[0],img_rows,img_cols,1)
  x_test=x_test.reshape(x_test.shape[0],img_rows,img_cols,1)
  input_shape=(img_rows,img_cols,1)

x_train=x_train.astype('float32')
x_test=x_test.astype('float32')
x_train/=255
x_test/=255
print ('x_train shape : ', x_train.shape)
print(x_train.shape[0],' training samples')
print(x_test.shape[0],' test samples')

# convert the labels to binary class matrices [WHAT ???]

y_train=keras.utils.to_categorical(y_train,num_classes)
y_test=keras.utils.to_categorical(y_test,num_classes)

# TRAINING SESSION BEGINSSSSSSSSSSSSSSSSSSSSSSSSSSS

# Prepare A Convolutional Neural Network

model=Sequential()
model.add(Conv2D(32,kernel_size=(3,3),activation='relu',input_shape=input_shape)) # Convolutional Layer
model.add(Conv2D(64,(3,3),activation='relu')) # another convolutional Layer
model.add(MaxPooling2D(pool_size=(2,2)))  # reduce data to decrease training time by POOLING::MAX
model.add(Dropout(0.25))  # regularisation by omitting features by 25% chance by DROPOUT::0.25
model.add(Flatten())   # to squash multiple channels (feature map) to 1-D 
model.add(Dense(num_classes,activation='softmax')) # classifiaction to give probabilities to various num_classes by SOFTMAX

# Start Training 

model.compile(loss=keras.losses.categorical_crossentropy, optimizer=keras.optimizers.Adadelta(), metrics=['accuracy'])    # TRAIN
model.fit(x_train,y_train,batch_size=batch_size,epochs=epochs,validation_data=(x_test,y_test))                            # VALIDATION
score=model.evaluate(x_test,y_test,verbose=0)                                                                            # TEST
print('Test Loss : ',score[0])
print ('Test Accuracy : ',score[1])

 