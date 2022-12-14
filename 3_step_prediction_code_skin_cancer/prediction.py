from keras.models import load_model
from keras.preprocessing.image import load_img,img_to_array
import numpy as np
import matplotlib.pyplot as plt


model1 = load_model('Skin_cancer_BC.h5',compile=False)  


from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(rescale = 1./255,
                                   shear_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip = True)

train_directory='train'
training_set = train_datagen.flow_from_directory(train_directory,
                                                 target_size = (224, 224),
                                                 batch_size = 32,
                                                 class_mode = 'categorical')

lab = training_set.class_indices
lab={k:v for v,k in lab.items()}

def output(location):
    img=load_img(location,target_size=(224,224,3))
    img=img_to_array(img)
    img=img/255
    img=np.expand_dims(img,[0])
    answer=model1.predict(img)
    y_class = answer.argmax(axis=-1)
    y = " ".join(str(x) for x in y_class)
    y = int(y)
    res = lab[y]
    print("Skin Cancer:  ",res)
    return res


img="E:\Project Folder\\11_Novmber\\Skin_Cancer_Detection\\3_step_prediction_code\\train\\malignant\\7.jpg"
pic=load_img(img,target_size=(224,224,3))
plt.imshow(pic)
result_final = output(img)

# plt.imshow(result_final) 