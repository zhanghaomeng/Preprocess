import numpy as np
import os
import nibabel as nib
import matplotlib.pyplot as plt

import mask

SET_MIN = -1
SET_MAX = 1
percentiles = 5


file_path = "/Users/haomeng/Desktop/brainVolumeExtraction"

masked = os.path.join(file_path, "masked.nii.gz")
normalized = os.path.join(file_path, "normalized.nii.gz")


def max_min_normalize(image, affine, header, percentiles=0, set_min=-1, set_max=1):
	minimum = np.percentile(image, 0+percentiles)
	maximum = np.percentile(image, 100-percentiles)

	image = (np.divide((image-minimum), maximum-minimum)*(set_max-set_min)+set_min).copy()

	image[image < set_min] = set_min
	image[image > set_max] = set_max

	ni1 = nib.Nifti1Image(image, affine, header)

	nib.save(ni1, normalized)


def sum_normalize(image, affine, header):
	image_sum = np.sum(left_img, dtype=np.float32)
	image = np.divide(image, image_sum)

	ni1 = nib.Nifti1Image(image, affine, header)

	nib.save(ni1, normalized)

file = nib.load(masked)
affine = file.affine
header = file.header
image = np.asarray(nib.load(masked).get_data())

max_min_normalize(image, affine, header)





# entire_brain = nib.load(entire_masked_out_file)
# left_brain = nib.load(left_masked_out_file)
# right_brain = nib.load(right_masked_out_file)


# # read data in np.uint8
# entire_img = np.asarray(entire_brain.get_data())
# left_img = np.asarray(left_brain.get_data())
# right_img = np.asarray(right_brain.get_data())


# entire_sum = np.sum(entire_img, dtype=np.float32)
# left_sum = np.sum(left_img, dtype=np.float32)
# right_sum = np.sum(right_img, dtype=np.float32)


# entire_max = np.amax(entire_img)
# entire_min = np.amin(entire_img)

# left_max = np.amax(left_img)
# left_min = np.amin(left_img)

# right_max = np.amax(right_img)
# right_min = np.amin(right_img)

# print(np.sum(entire_img))

# entire_flat = entire_img.flatten()
# plt.hist(entire_flat, 152)
# plt.show()

# #entire_img = np.divide(entire_img, entire_sum)
# #left_img = np.divide(left_img, left_sum)
# #right_img = np.divide(right_img, right_sum)

# #entire_img = np.add(np.divide(np.multiply(np.subtract(entire_img, entire_min), (SET_MAX-SET_MIN)), (entire_max-entire_min)), SET_MIN)
# #left_img = np.add(np.divide(np.multiply(np.subtract(left_img, left_min), (SET_MAX-SET_MIN)), (left_max-left_min)), SET_MIN)
# #right_img = np.add(np.divide(np.multiply(np.subtract(right_img, right_min), (SET_MAX-SET_MIN)), (right_max-right_min)), SET_MIN)

# min_i = np.percentile(entire_img, 0+percentiles)
# max_i = np.percentile(entire_img, 100-percentiles)
# entire_img = (np.divide((entire_img-min_i), max_i-min_i)*(SET_MAX-SET_MIN)+SET_MIN).copy()
# entire_img[entire_img > SET_MAX] = SET_MAX
# entire_img[entire_img < SET_MIN] = SET_MIN

# print(np.sum(entire_img))


# entire_ni1 = nib.Nifti1Image(entire_img, entire_brain.affine, entire_brain.header)
# left_ni1 = nib.Nifti1Image(left_img, left_brain.affine, left_brain.header)
# right_ni1 = nib.Nifti1Image(right_img, right_brain.affine, right_brain.header)


# nib.save(entire_ni1, entire_normalized)
# nib.save(left_ni1, left_normalized)
# nib.save(right_ni1, right_normalized)