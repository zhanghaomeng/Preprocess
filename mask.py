import numpy as np
import nibabel as nib
import os


file_path = "/Users/haomeng/Desktop/brainVolumeExtraction"
mask_file = os.path.join(file_path, "ribbon.mgz")
brain_file = os.path.join(file_path, "T1.mgz")


# flag: 'left', 'right' or 'entrie'
def mask(image, mask, out_path, flag):

	mask_file = nib.load(mask)
	mask_img = np.asarray(mask_file.get_data())
	image_file = nib.load(image)
	image_img = np.asarray(image_file.get_data())

	if flag == 'entire':
		out_file = os.path.join(out_path, "masked.nii.gz")
		entire_img = np.zeros_like(mask_img)
		entire_img[mask_img > 0] = 1.0

		entire_masked_img = nib.Nifti1Image(np.multiply(image_img, entire_img), image_file.affine, header=image_file.header)
		nib.save(entire_masked_img, out_file)

	elif flag == 'left':
		out_file = os.path.join(out_path, "masked.nii.gz")
		left_img = np.zeros_like(mask_img)
		left_img[mask_img > 1] = 1.0
		left_img[mask_img > 40] = 0.0

		left_masked_img = nib.Nifti1Image(np.multiply(image_img, left_img), image_file.affine, header=image_file.header)
		nib.save(left_masked_img, out_file)


	elif flag == 'right':
		out_file = os.path.join(out_path, "masked.nii.gz")
		right_img = np.zeros_like(mask_img)
		right_img[mask_img > 40] = 1.0

		right_masked_img = nib.Nifti1Image(np.multiply(image_img, right_img), image_file.affine, header=image_file.header)
		nib.save(right_masked_img, outfile)

	else:
		print('Please enter \'entire\', \'left\' or \'right\'')

mask(brain_file, mask_file, file_path, 'entire')
