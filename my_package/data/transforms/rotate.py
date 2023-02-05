#Imports
from PIL import Image

class RotateImage(object):
    '''
        Rotates the image about the centre of the image.
    '''

    def __init__(self, degrees):
        '''
            Arguments:
            degrees: rotation degree.
        '''
        self.deg=degrees

    def __call__(self, sample):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)
        '''
        #handing numpy array image
        # if not isinstance(image,PIL.Image.Image): # if given as numpy array, then convert into PIL Image
        #     image = Image.fromarray(image)
        #end of handling numpy image

        img_out=sample.rotate(self.deg,0,1)
        return img_out

#testing
if __name__=='__main__':
    img=Image.open("/home/hp/Downloads/download.png")
    rotate=RotateImage(45)
    img_out=rotate(img)
    img_out.show()