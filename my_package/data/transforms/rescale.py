#Imports
from PIL import Image

class RescaleImage(object):
    '''
        Rescales the image to a given size.
    '''

    def __init__(self, output_size):
        '''
            Arguments:
            output_size (tuple or int): Desired output size. If tuple, output is
            matched to output_size. If int, smaller of image edges is matched
            to output_size keeping aspect ratio the same.
        '''
        self.type=isinstance(output_size,tuple)
        self.scale=output_size


    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)

            Note: You do not need to resize the bounding boxes. ONLY RESIZE THE IMAGE.
        '''

        #handing numpy array image
        # if not isinstance(image,PIL.Image.Image): # if given as numpy array, then convert into PIL Image
        #     image = Image.fromarray(image)
        #end of handling numpy image

        if self.type :
            return image.resize(self.scale)
        
        width,height=image.size
        
        if width < height :
            width_new=self.scale
            height_new=width_new*height//width
        else :
            height_new=self.scale
            width_new=height_new*width//height

        new_size=(width_new,height_new)
        return image.resize(new_size)

if __name__=='__main__' :
    img=Image.open("/home/hp/Downloads/download.png")
    rescale=RescaleImage((178,100))
    img_out=rescale(img)
    img_out.show()