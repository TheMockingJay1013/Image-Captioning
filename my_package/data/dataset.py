#Imports
import jsonlines
from PIL import Image
import os
import numpy as np

class Dataset(object):
    '''
        A class for the dataset that will return data items as per the given index
    '''

    def __init__(self, annotation_file, transforms=None):
        '''
            Arguments:
            annotation_file: path to the annotation file
            transforms: list of transforms (class instances)
                        For instance, [<class 'RandomCrop'>, <class 'Rotate'>]
        '''
        self.transform=transforms

        #opening annotation file and reading it
        with jsonlines.open(annotation_file,'r') as jsonFile :
            self.jsonlist=[obj for obj in jsonFile]
        

    def __len__(self):
        '''
            return the number of data points in the dataset
        '''
        return len(self.jsonlist)

    
    def __getann__(self, idx):
        '''
            return the data items for the index idx as an object
        '''
        self.idx=idx
        dataidx=self.jsonlist[idx]
        return dataidx
        

    def __transformitem__(self, path):
        '''
            return transformed PIL Image object for the image in the given path
        '''
        img=Image.open(path)
        if not isinstance(img,Image.Image) :
            img=Image.fromarray(img)
        
        if self.transform is not None :
            for transform in self.transform :
                img = transform(img)
        return img


