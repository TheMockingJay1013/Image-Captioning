#Imports
import numpy as np
from PIL import Image
import random

class CropImage(object):
    '''
        Performs either random cropping or center cropping.
    '''

    def __init__(self, shape, crop_type='center'):
        '''
            Arguments:
            shape: output shape of the crop (h, w)
            crop_type: center crop or random crop. Default: center
        '''
        self.height,self.width=shape
        self.type=crop_type

    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)
        '''
        #handling numpy array
        # if not isinstance(image,PIL.Image.Image): # if given as numpy array, then convert into PIL Image
        #     image = Image.fromarray(image)

        #end of handling numpy array

        img_width,img_height=image.size
        
        if self.type=='center' :
            left=img_width/2 -self.width/2
            right=left+self.width
            upper=img_height/2 -self.height/2
            lower=upper+self.height
        else : 
            left=np.random.randint(0,img_width-self.width)
            right=left+self.width
            upper=np.random.randint(0,img_height-self.height)
            lower=upper+self.height
        
        return image.crop((left,upper,right,lower))


#testing

if __name__=="__main__" :
    img=Image.open("/home/hp/Downloads/download.png")
    crop=CropImage((50,80),'not_center')
    img_out=crop(img)
    img_out.show()



 