#Imports
from my_package.model import ImageCaptioningModel
from my_package.data.dataset import Dataset
from my_package.data.download import Download
from my_package.data.transforms.flip import FlipImage
from my_package.data.transforms.rescale import RescaleImage
from my_package.data.transforms.blur import BlurImage
from my_package.data.transforms.crop import CropImage
from my_package.data.transforms.rotate import RotateImage
import numpy as np
from PIL import Image
import PIL


def experiment(annotation_file, captioner, transforms, outputs):
    '''
        Function to perform the desired experiments

        Arguments:
        annotation_file: Path to annotation file
        captioner: The image captioner
        transforms: List of transformation classes
        outputs: Path of the output folder to store the images
    '''

    #Create the instances of the dataset, download
    dset=Dataset(annotation_file,transforms)
    download=Download()

    #Print image names and their captions from annotation file using dataset object
    data=dset.__getann__(2)
    print("Image name =" , data["file_name"] , " \nImage caption = ",data["captions"])

    #Download images to ./data/imgs/ folder using download object
    path="./data/imgs/"+data["file_name"]
    download.__call__(path,data["url"])


    #Transform the required image (roll number mod 10) and save it seperately
    img=dset.__transformitem__(path)
    out_path="./data/output/"+data["file_name"]
    img=img.save(out_path)
    #Get the predictions from the captioner for the above saved transformed image  
    caption=captioner(out_path,2)
    print(caption)

def main():
    captioner = ImageCaptioningModel()
    experiment('./data/annotations.jsonl', captioner, [FlipImage(), BlurImage(1)], None) # Sample arguments to call experiment()


if __name__ == '__main__':
    main()