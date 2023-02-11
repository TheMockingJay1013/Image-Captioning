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
    
    img=img.save(outputs)
    #Get the predictions from the captioner for the above saved transformed image  
    caption=captioner(outputs,2)
    print(caption)

def main():
    captioner = ImageCaptioningModel()
    experiment('./data/annotations.jsonl', captioner, None, "./data/output/2_A.jpg") # Sample arguments to call experiment()
    print("First Experiment is Completed")
    experiment('./data/annotations.jsonl', captioner, [FlipImage('horizontal')], "./data/output/2_B.jpg")
    print("Second Experiment is Completed")
    experiment('./data/annotations.jsonl', captioner, [BlurImage(20)], "./data/output/2_C.jpg")
    print("Third Experiment is Completed")
    
    img=Image.open("./data/imgs/2.jpg")
    size=img.size
    nsize=(2*size[0],2*size[1])


    experiment('./data/annotations.jsonl', captioner, [RescaleImage(nsize)], "./data/output/2_D.jpg")
    print("Fourth Experiment is Completed")

    msize=(int(0.5*size[0]),int(0.5*size[1]))
    experiment('./data/annotations.jsonl', captioner, [RescaleImage(msize)], "./data/output/2_E.jpg")
    print("Fifth Experiment is Completed")
    experiment('./data/annotations.jsonl', captioner, [RotateImage(-90)], "./data/output/2_F.jpg")
    print("Sixth Experiment is Completed")
    experiment('./data/annotations.jsonl', captioner, [RotateImage(45)], "./data/output/2_G.jpg")
    print("Seventh Experiment is Completed")


if __name__ == '__main__':
    main()