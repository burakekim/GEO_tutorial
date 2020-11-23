#import uuid
import argparse
import glob
import os
import tifffile
import numpy as np

#Example usage: 
#python im2npy.py --source_dir="C:\Users\PROCOMP11-PC\Desktop\PanColorGAN\PanColorGAN-master\PanColorGAN-master\dataset\PAN\tif" --save_to="C:\Users\PROCOMP11-PC\Desktop\PanColorGAN\PanColorGAN-master\PanColorGAN-master\dataset\PAN\all_pan"

parse = argparse.ArgumentParser(description= 'Converts image into numpy array.')
parse.add_argument('--save_to', help = '[DIRECTORY] - Where to save the numpy array?')
parse.add_argument('--extension', help = 'Image extension', default = 'tif')
args = parse.parse_args()
parse.add_argument('--extension', help = 'Image extension', default = 'tif')

args = pare.parse_args()

def get_image_ID_generator(source_dir,extension): 

    IDs = []
    for ims in range(len(os.listdir(source_dir))):

        images = glob.glob(source_dir + "\*.{}".format(extension))
        base_name = os.path.splitext(images[ims])[0]
        data_split = base_name.split("_")
        data_ID = data_split[-2] + '_' + data_split[-1]
        IDs.append(data_ID)
        yield IDs

def im2npy(source_dir,save_to,image_extension):

    if not os.path.exists(save_to):
        raise NameError("[WARNING] Could not find the target directory : [save_to]. Check if the directory is readable")

    images = glob.glob(source_dir + '\*.{}'.format(image_extension))
    print("\n[INFO] There are {} images in the folder that meets the searching criteria.".format(len(images)))

    IDs = get_image_ID_generator(source_dir = source_dir, extension = image_extension)
    iter_IDs = iter(IDs)

    for i,image in enumerate(images):


        image =tifffile.imread(image) #sonradan ekledim. görüntüyü açıp doğru okuduğundan emin ol!

        ID = next(iter_IDs)
        #run_ID = str(uuid.uuid4())
        np_img = np.asarray(image)

        np.save(save_to + '\\np-' + ID[-1] + '.npy', np_img)

    print("[INFO] ENDED. {} numpy arrrays are created in total.".format(i + 1))

im2npy(source_dir = args.source_dir, save_to = args.save_to, image_extension = args.extension)
