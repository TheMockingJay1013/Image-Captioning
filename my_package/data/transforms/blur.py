#Imports
from PIL import Image, ImageFilter

class BlurImage(object):
    '''
        Applies Gaussian Blur on the image.
    '''

    def __init__(self, radius):
        '''
            Arguments:
            radius (int): radius to blur
        '''
        self.radius=radius
  

    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL Image)

            Returns:
            image (numpy array or PIL Image)
        '''
        #handing numpy array image
        # if not isinstance(image,PIL.Image.Image): # if given as numpy array, then convert into PIL Image
        #     image = Image.fromarray(image)
        #end of handling numpy image

        return image.filter(ImageFilter.GaussianBlur(self.radius))

if __name__=='__main__' :
    img=Image.open("/home/hp/Downloads/download.png")
    blur=BlurImage(2)
    img_out=blur(img)
    img_out.show()


