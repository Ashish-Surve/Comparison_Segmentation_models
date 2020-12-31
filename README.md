# Segmentation Comparision tool
This tools helps us to compare different segmentation models. 

Brief comparsion of segmentation models. Trained on collab for car/vehicle segmentation.

Tools used

    FastAPI: for the API
    streamlit : for the interface
    Docker: to containerize the app



Folder Structure:
```
Comparsion_Segmentation_models/ 
    docker-                       compose.yml - for creating the containers and network in one go.
    backend/                      backend service that uses FASTAPI.
        config.py                 stores paths and dictionary for easy access.
        Dockerfile                instructions on how to build backend container.
        inference.py              does the inferencing for our segment models.
        main.py                   FASTAPI based backend server.
        requirements.txt          
        Try_backend.ipynb         initial trial at training models(ignore)
        try_code.ipynb            trial 2 at training models(ignore)
        models/                   3 trained models for cars segmentation. 
            FPN-efficientnet.h5
            LinkedNet.h5
            U-net-efficientnet.h5
        storage/                  frontend saves files here(DEBUG purpose).
    frontend/                     frontend that serves UI using streamlit.
        Dockerfile                instructions on how to build frontend container.
        main.py                   Streamlit based backend server.
        requirements.txt
    storage/                      shared directory for storing uploaded image.
    storage2/                     shared directory for storing segmented image.
```
   ### TL;DR
   1. execute 
        ```docker-compose up -d```
        in root of repository
   2. open the http://localhost:8501/ or check the port of your frontend container using docker.


## Examples
#### Initially created a model with 5 epochs => 5 minutes of training on collab at max capacity.
#### Input / Output Unet efficientNet
<p float="left">
<img src="https://raw.githubusercontent.com/Ashish-Surve/Comparsion_Segmentation_models/main/images/input.png" width="48%" /> 
<img src="https://raw.githubusercontent.com/Ashish-Surve/Comparsion_Segmentation_models/main/images/output.jpeg" width="48%" />
</p>

## Training Information:
### Compartive Analysis:
| Model / Metric| Loss          | Mean-IoU  | Mean-f1   | 
| ------------- |:-------------:| ---------:| ---------:|
| U-net         | 0.6846        | 52.08 %   |  63.11 %  |
| FPN           | 0.3300        | 68.33 %   |  77.37 %  |
| LinkNet       | 0.9490        | 33.64 %   |  44.37 %  |


#### gt mask= generated Mask / pr mask = Predicted Mask

### Unet
![Unet-graph](https://raw.githubusercontent.com/Ashish-Surve/Comparsion_Segmentation_models/main/images/Unet.png)

![Unet-1](https://raw.githubusercontent.com/Ashish-Surve/Comparsion_Segmentation_models/main/images/Unet6.png)
![Unet-2](https://raw.githubusercontent.com/Ashish-Surve/Comparsion_Segmentation_models/main/images/unet3.png)
![Unet-3](https://raw.githubusercontent.com/Ashish-Surve/Comparsion_Segmentation_models/main/images/unet4.png)



### FPN
![FPN-graph](https://raw.githubusercontent.com/Ashish-Surve/Comparsion_Segmentation_models/main/images/fpn1.png)

![FPN-1](https://raw.githubusercontent.com/Ashish-Surve/Comparsion_Segmentation_models/main/images/fpn3.png)
![FPN-2](https://raw.githubusercontent.com/Ashish-Surve/Comparsion_Segmentation_models/main/images/fpn4.png)
![FPN-3](https://raw.githubusercontent.com/Ashish-Surve/Comparsion_Segmentation_models/main/images/FPN.png)




### LinkNet
![LinkNet-graph](https://raw.githubusercontent.com/Ashish-Surve/Comparsion_Segmentation_models/main/images/linkednet1.png)

![LinkNet-1](https://raw.githubusercontent.com/Ashish-Surve/Comparsion_Segmentation_models/main/images/linkednet3.png)
![LinkNet-2](https://raw.githubusercontent.com/Ashish-Surve/Comparsion_Segmentation_models/main/images/Linkednet4.png)
![LinkNet-3](https://raw.githubusercontent.com/Ashish-Surve/Comparsion_Segmentation_models/main/images/linkednet5.png)


## We will soon be adding the collab notebook if someone needs it.
   
