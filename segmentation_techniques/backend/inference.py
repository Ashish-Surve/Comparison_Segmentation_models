import config
import cv2
import segmentation_models as sm

# define network parameters
n_classes = 1 if len(CLASSES) == 1 else (len(CLASSES) + 1)  # case for binary and multiclass segmentation
activation = 'sigmoid' if n_classes == 1 else 'softmax'

BACKBONE = 'efficientnetb3'
CLASSES = ['car']

def inference(model, image):
    model_name = f"{config.MODEL_PATH}{model}.h5"
    model = sm.Unet(BACKBONE, classes=n_classes, activation=activation)
    model.load_weights(model_name) 
    image = np.expand_dims(image, axis=0)
    pr_mask = model.predict(image).round()
    image=denormalize(image.squeeze()
    pr_mask=pr_mask[..., 0].squeeze()
    return pr_mask

# helper function for data visualization
def visualize(**images):
    """PLot images in one row."""
    n = len(images)
    plt.figure(figsize=(16, 5))
    for i, (name, image) in enumerate(images.items()):
        plt.subplot(1, n, i + 1)
        plt.xticks([])
        plt.yticks([])
        plt.title(' '.join(name.split('_')).title())
        plt.imshow(image)
    plt.show()
    
# helper function for data visualization    
def denormalize(x):
    """Scale image to range 0..1 for correct plot"""
    x_max = np.percentile(x, 98)
    x_min = np.percentile(x, 2)    
    x = (x - x_min) / (x_max - x_min)
    x = x.clip(0, 1)
    return x    
    
