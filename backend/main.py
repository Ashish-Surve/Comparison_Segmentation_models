import asyncio
import time
import uuid
from concurrent.futures import ProcessPoolExecutor
from functools import partial

import os
import cv2
import uvicorn
from fastapi import File
from fastapi import FastAPI
from fastapi import UploadFile
import numpy as np
from PIL import Image

import config
import inference
import glob

# Set this to 0 when building docker image.
# Set 1 when debugging on own machine.
#DEBUG variable
DEBUG=0

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome from the API"}



@app.post("/{style}")
async def get_image(style: str, file: UploadFile = File(...)):
    image = np.array(Image.open(file.file))
    print(image.shape)
    image = cv2.resize(image, (480, 360),  interpolation = cv2.INTER_NEAREST) 
    # PIL - BGR cv2 - RGB
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    print(os.path.join(os.path.sep,f"{config.IMAGE_PATH}","something.jpg"))
    if DEBUG==1:
        cv2.imwrite(os.path.join(f"{config.IMAGE_PATH}","something.jpg"), image)
    else:    
        # first sep for root since storage etc in root
        cv2.imwrite(os.path.join(os.path.sep,f"{config.IMAGE_PATH}","something.jpg"), image)
    # model = config.STYLES[style]
    start = time.time()
    if DEBUG==1:
        output, _ = inference.inference(style, os.path.join(f"{config.IMAGE_PATH}",""))
    else:
        output, _ = inference.inference(style, os.path.join(os.path.sep,f"{config.IMAGE_PATH}",""))
    if DEBUG==1:
        name = os.path.join(f"storage2",f"{str(uuid.uuid4())}.png")   
    else:
        name = os.path.join(os.path.sep, f"storage2",f"{str(uuid.uuid4())}.png")
    print(f"name: {name}")
    # name = file.file.filename
    output= output*255
    output = output.astype('uint8')
    #output = cv2.cvtColor(output, cv2.COLOR_GRAY2BGR)
    cv2.imwrite(name, output)
    # TODO: Remove below folder empty code
    # We need to create a folder for every image bcoz we need a placeholder
    # for using the below Dataset Class.
    if DEBUG==1:
        files = glob.glob(os.path.join(f"{config.IMAGE_PATH}","*"))   
    else: 
        files = glob.glob(os.path.join(os.path.sep,f"{config.IMAGE_PATH}","*"))
    for f in files:
        os.remove(f)
    return {"name": name, "time": time.time() - start}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080)
