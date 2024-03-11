# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) The Caterpillar Effect: A Caterpillar Recognition Model

> SG-DSI-41 Capstone Project by Sharifah Nurulhuda Taha A

---
**Problem Statement**
---

Singapore as a garden city has a large ecosystem of animals and plants living harmoniously in a biodiverse environment. Among hobbyists, parents and educators, there is a commonality in wanting to be able to identify a caterpillar that they might have found in their garden, or in the wild. Primary school educators specifically could find this a useful model to have, to engage the children and develop their curiosity, love and respect for nature.  Hobbyists rally together on social media groups to help each other achieve the goals of wanting to witness the magical metamorphosis from caterpillar to butterfly.

Caterpillars are found only on their host plants, where their parent butterfly lays their eggs. This ensures a fresh and ample supply of food for the development and survival of their young. Without this, they will often not survive.

This project explores using a Multi-class Convolutional Neural Network to distinguish between four species of caterpillars commonly found in Singapore:
1. Chocolate Pansy Caterpillar
2. Lime Butterfly Caterpillar
3. Painted Jezebel Caterpillar
4. Plain Tiger Caterpillar

In this project, we explore the following modelling techniques:
- Multi-class CNN with Adam Optimiser 
- Multi-class CNN with Adam Optimiser and Early Stopping
- Transfer Learning using VGG-16 with Adam Optimiser
- Transfer Learning using VGG-16 with Adam Optimiser and Early Stopping

Additionally, we also include:
- Using Streamlit as a demonstration platform to upload an image for image recognition
- An Age Input box for use with the OpenAI Assistants API
- Using the OpenAI Assistants API with Knowledge Retrieval function activated to answer user prompts based on age and the identified caterpillar type


These models will be evaluated using mainly Precision Scores (though other metrics are also discussed).


**A Brief Overview of the Frameworks**
---
We use both Multi-class CNNs and Transfer Learning using VGG-16 here.

In both models, we feed our training images through the neural network, which will learn to identify features and patterns throughout the images and attempt to classify them accurately.

**CNN Framework**
---
Here is a typical CNN framework:

<img src="https://editor.analyticsvidhya.com/uploads/25366Convolutional_Neural_Network_to_identify_the_image_of_a_bird.png" style="float: center; height: 250px">

However, there are drawbacks to creating CNNs from scratch. 

The following is taken from __[Disadvantages of CNN models.](https://sandeep-bhuiya01.medium.com/disadvantages-of-cnn-models-95395fe9ae40)__

* Heavy Computational Power needed (depending on the number of convolution and pooling layers)
* Poor Classification Performance when presented with a smaller dataset without data augmentation.

**Transfer Learning with VGG-16 Framework**
---
Here is a visual of using transfer learning with VGG-16.

<img src="https://storage.googleapis.com/lds-media/images/transfer-learning-fine-tuning-approach.width-1200.jpg" style="float: center; height: 250px">

The following are some research papers and articles that give insight to the use of VGG-16 models for transfer learning.

* __[Transfer Learning using VGG-16 with Deep Convolutional Neural Network for Classifying Images](https://www.researchgate.net/publication/337105858_Transfer_learning_using_VGG-16_with_Deep_Convolutional_Neural_Network_for_Classifying_Images)__

* __[Transfer Learning with VGG16 and Keras](https://towardsdatascience.com/transfer-learning-with-vgg16-and-keras-50ea161580b4)__

* __[Using pre-trained VGG Model](https://www.kaggle.com/code/saptarsi/using-pre-trained-vgg-model/notebook)__

We will also look at the effect of `Early Stopping` regularisation on the accuracy and other metrics of our model.


**Data Collection**
---

The data was collected by manually selecting suitable images from a cursory Google search.

For each species, 20 images were saved for further processing of data. This processing is automated using the notebook **01_Data_Augmentation.ipynb** which goes through the images in the folder and puts them through the data augmentation process. The result is a folder created within the data folder which contains the resulting augmented images.

The data goes through the process of Data Augmentation as follows:

1. Gamma Contrast
2. Sigmoid Contrast
3. Linear Contrast
4. Cropping
5. Elastic
6. Polar
7. Jigsaw
8. Shear
9. Adding Noise
10. Rotation
11. Horizontal Flip
12. Vertical Flip

The resulting images totalled up to 260 images per class.

The table below summarises the dataset used for modelling.

|Species|Destination Folder|Original Number of Images|Final Number of Augmented Images|
|-----|-----|-----|-----|
|Chocolate Pansy|`data/augmented/chocolate_pansy`|20|260|
|Lime|`data/augmented/lime_caterpillar`|20|260|
|Painted Jezebel|`data/augmented/painted_jezebel`|20|260|
|Plain Tiger|`data/augmented/plain_tiger`|20|260|


**Data Processing**
---


1) Checking for correct file format
    - Accepted formats: jpg, jpeg, png, bmp
    - Images in other formats will be deleted

2) Generating Labels
    - The labels for the 4 classes were generated image by image to be used for accuracy later

3) Resizing according to the needs of the models: 
    - 256 by 256 for CNN
    - 224 by 224 for VGG-16

4) Splitting the Data using train test split while ensuring balanced classes

5) Scaling the data 

**CNN Model**
---
**Overview**
- Hidden Layers: 6
- Activation Functions: ReLU + Softmax (for final layer only)
- Optimiser: Adam, Learning Rate 0.001
- Loss Function: Sparse Categorical Cross Entropy
- Validation Split: 0.2

**Insights:**

Comparing the scores, while there seems to be a chance of overfitting in the testing metrics (close to 100%), comparing with the testing data is important.

Here are the differences in the various metrics for each class from training data to testing data:

|class|precision|recall|f1-score|
|---|---|---|---|
|chocolate_pansy|-0.15|-0.06|-0.10|
|lime_caterpillar|-0.04|-0.07|-0.05|
|painted_jezebel|0|-0.14|-0.07|
|plain_tiger|-0.10|-0.03|-0.06|

In this case, it is more important for us to have a high precision score as this might have dire consequences for the use case of this project. If a caterpillar is wrongly identified, it might not survive as the user might end up learning the wrong information and therefore, possibly providing the wrong feed, leading to starvation and death.

There is a significant difference in the metrics for precision in the `chocolate_pansy` and `plain_tiger` classes.

**CNN Model with Early Stopping**
---
**Overview**
- Final Number of Epochs: 8
- Activation Functions: ReLU + Softmax (for final layer only)
- Optimiser: Adam, Learning Rate 0.001
- Loss Function: Sparse Categorical Cross Entropy
- Validation Split: 0.2

**Insights:**

Comparing the scores, while there seems to be a chance of overfitting in the testing metrics (close to 100%), comparing with the testing data is important.

Here are the differences in the various metrics for each class from training data to testing data:

|class|precision|recall|f1-score|
|---|---|---|---|
|chocolate_pansy|-0.12|-0.07|-0.09|
|lime_caterpillar|-0.04|-0.07|-0.05|
|painted_jezebel|-0.01|-0.13|-0.07|
|plain_tiger|-0.09|0|-0.07|

The addition of early stopping does not seem to have made much difference in the scores. 

There is a need to explore other options to improve the metrics.


**Transfer Learning using VGG-16 Model**
---
**Overview**
- Hidden Layers: 19
- Activation Functions: ReLU + Softmax (for final layer only)
- Optimiser: Adam, Learning Rate 0.001
- Loss Function: Sparse Categorical Cross Entropy
- Validation Split: 0.2

**Insights:**

Comparing the scores, while there seems to be a chance of overfitting in the testing metrics (close to 100%), comparing with the testing data is important.

Here are the differences in the various metrics for each class from training data to testing data:

|class|precision|recall|f1-score|
|---|---|---|---|
|chocolate_pansy|-0.13|-0.01|-0.07|
|lime_caterpillar|0|-0.06|-0.03|
|painted_jezebel|-0.02|-0.06|-0.04|
|plain_tiger|-0.02|-0.07|-0.05|

There is a significant difference in the metrics for precision in the `chocolate_pansy` class, while the rest remain relatively acceptable.


**Transfer Learning using VGG-16 Model with Early Stopping**
---
**Overview**
- Final Number of Epochs: 7
- Activation Functions: ReLU + Softmax (for final layer only)
- Optimiser: Adam, Learning Rate 0.001
- Loss Function: Sparse Categorical Cross Entropy
- Validation Split: 0.2

**Insights:**

Comparing the scores, while there seems to be a chance of overfitting in the testing metrics (close to 100%), comparing with the testing data is important.

Here are the differences in the various metrics for each class from training data to testing data:

|class|precision|recall|f1-score|
|---|---|---|---|
|chocolate_pansy|-0.10|-0.01|-0.05|
|lime_caterpillar|0.02|-0.06|-0.02|
|painted_jezebel|-0.02|-0.06|0.04|
|plain_tiger|-0.04|-0.03|0.04|

The addition of early stopping made some difference in some classes, but negligible in others. 

Precision is still quite high for `chocolate_pansy`, while the f1-score for `painted_jezebel` and `plain_tiger` significantly improved.


**Application of Knowledge Retrieval in OpenAI's Assistant API**
---

In this project, this API was used as a Knowledge Retrieval system that accesses documents uploaded onto the server in OpenAI, to answer prompts provided by the user, taking into consideration the user's age (as inputted by them into the streamlit).

OpenAI's Assistant API (Beta) uses OpenAI's Chatbot function to integrate RAG with their existing ChatGPT models. 

__[Documentation for OpenAI's Assistant API (Beta)](https://platform.openai.com/docs/assistants/overview)__

As the system is still in testing stage, the documentation is a fluid document that undergoes changes every few months based on feedback from users and developers.

Here is a visual of how RAG works:

<img src="https://communitykeeper-media.s3.amazonaws.com/media/images/rag-overview.original.png" style="float: center; height: 250px">


Conclusion
---
- Based on metrics, the model with VGG-16 and Early Stopping is the best performing one. However, more work needs to be done to fine-tune the model for better unseen test performance

Future Work and Other Suitable Applications
---
- To be able to identify the species at any stage of its life cycle
- To expand to more species of butterflies and moths for classification
- Chatbot to include giving images as responses
- Chatbot to include recommended websites that the user can visit to find out more about their caterpillar
- Future applications of this model
    - Can expand to different types of animals like birds, snakes or other insects