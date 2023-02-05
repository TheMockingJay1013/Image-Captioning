#Imports
from PIL import Image

class FlipImage(object):
    '''
        Flips the image.
    '''

    def __init__(self, flip_type='horizontal'):
        '''
            Arguments:
            flip_type: 'horizontal' or 'vertical' Default: 'horizontal'
        '''
        self.type=flip_type

    def __call__(self, image):
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

        if self.type=='horizontal' : 
            img_out=image.transpose(Image.FLIP_LEFT_RIGHT)
        else :
            img_out=image.transpose(Image.FLIP_TOP_BOTTOM)
        return img_out

if __name__=="__main__":
    img=Image.open("/home/hp/Downloads/download.png")
    flip=FlipImage('vertical')
    img_out=flip(img)
    img_out.show()
