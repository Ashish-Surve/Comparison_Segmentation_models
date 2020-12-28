# Segmentation
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
   