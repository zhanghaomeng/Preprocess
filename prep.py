import os
import argparse
import sys

import utils


def main(args):
	func = args.func
	side = args.side

	if args.file_in != None and args.file_out != None and arg.mask != None:
		image_path = args.file_in
		out_path = args.file_out
		mask_path = args.mask

		mask_file = utils.read_file(mask_path)
		image_file = utils.read_file(image_path)

		masked = utils.mask(image_file[0], mask_file[0], side)

		if func == "mask":
			utils.save_file(masked, image_file[1], image_file[2], out_path)

		elif func == "normalize":
			normalized = utils.min_max_normalize(masked)
			utils.save_file(normalized, image_file[1], image_file[2], out_path)

		else:
			print('func error')

	elif args.folder_in != None :
		folder_in = args.folder_in

		if args.folder_out != None:
			folder_out = args.folder_out
		else:
			folder_out = folder_in

		image_folder = os.path.join(folder_in, 'image')
		mask_folder = os.path.join(folder_in, 'mask')

		image_files = []
		for file in os.listdir(image_folder):
			if file.endswith((".mgz", ".nii", ".nii.gz")):
				image_files.append(file)

		mask_files = []
		for file in os.listdir(mask_folder):
			if file.endswith((".mgz", ".nii", ".nii.gz")):
				mask_files.append(file)


		for file in image_files:
			image_path = os.path.join(image_folder, file)
			mask_path = os.path.join(mask_folder, file)

			image_file = utils.read_file(image_path)
			mask_file = utils.read_file(mask_path)

			masked = utils.mask(image_file[0], mask_file[0], side)

			if func == "mask":
				if file.endswith((".mgz", ".nii")):
					out_file = file[:-4] + '_masked.nii.gz'
				elif file.endswith([".nii.gz"]):
					out_file = file[:-7] + '_masked.nii.gz'
					
				out_path = os.path.join(folder_out, 'masked')
				if not os.path.exists(out_path):
					os.makedirs(out_path)
				out_path = os.path.join(out_path, out_file)
				utils.save_file(masked, image_file[1], image_file[2], out_path)

			elif func == "normalize":
				normalized = utils.min_max_normalize(masked)
				if file.endswith((".mgz", ".nii")):
					out_file = file[:-4] + '_normalized.nii.gz'
				elif file.endswith([".nii.gz"]):
					out_file = file[:-7] + '_normalized.nii.gz'
				out_path = os.path.join(folder_out, 'normalized')
				if not os.path.exists(out_path):
					os.makedirs(out_path)
				out_path = os.path.join(out_path, out_file)
				utils.save_file(normalized, image_file[1], image_file[2], out_path)

			else:
				print('func error')


	else:
		print('parameter error')



if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument('--infile', type=str, dest='file_in', help='input file')
	parser.add_argument('--mask', type=str, dest='mask', help='mask image file')
	parser.add_argument('--outfile', type=str, dest='file_out', help='output file')
	parser.add_argument('--infolder', type=str, dest='folder_in', help='input folder')
	parser.add_argument('--outfolder', type=str, dest='folder_out', help='output folder')
	parser.add_argument('--func', required=True, type=str, dest='func', help='mask or normalize')
	parser.add_argument('--side', required=True, type=str, dest='side', help='the brain side being masked')
	args = parser.parse_args()

	main(args)
