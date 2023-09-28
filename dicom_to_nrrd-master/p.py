from radiomics import featureextractor
import six
import sys, os

#Set up a pyradiomics directory variable:

dataDir = '/path/to/pyradiomics'
#You will find sample data files brain1_image.nrrd and brain1_label.nrrd in that directory.

#Store the path of your image and mask in two variables:

imageName = os.path.join(dataDir, "data", 'brain1_image.nrrd')
maskName = os.path.join(dataDir, "data",  'brain1_label.nrrd')
#Also store the path to the file containing the extraction settings:

params = os.path.join(dataDir, "bin", "Params.yaml")
#Instantiate the feature extractor class with the parameter file:

extractor = featureextractor.RadiomicsFeaturesExtractor(params)
#Calculate the features:

result = extractor.execute(imageName, maskName)
for key, val in six.iteritems(result):
    print("\t%s: %s" %(key, val))