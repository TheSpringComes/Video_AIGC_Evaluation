import argparse
import os
import lpips
import cv2
import numpy as np
from tqdm import tqdm

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-d0','--dir0', type=str, default='../vids/inp')
parser.add_argument('-d1','--dir1', type=str, default='../vids/out')
parser.add_argument('-o','--out', type=str, default='../vids/dists.txt')
parser.add_argument('-v','--version', type=str, default='0.1')
parser.add_argument('--use_gpu', action='store_true', help='turn on flag to use GPU')

opt = parser.parse_args()

## Initializing the model
loss_fn = lpips.LPIPS(net='alex',version=opt.version)
if(opt.use_gpu):
	loss_fn.cuda()

# crawl directories
f = open(opt.out,'w')
files = os.listdir(opt.dir0)

dists_dirs = [] # to store the distances between the videos in the two directories
for file in tqdm(files):
	if(os.path.exists(os.path.join(opt.dir1,file))): # files in 2 dirs have the same name
		# Load videos
		videoCapture0 = cv2.VideoCapture(os.path.join(opt.dir0,file))
		videoCapture1 = cv2.VideoCapture(os.path.join(opt.dir1,file))

		# Get the number of frames
		frames0 = int(videoCapture0.get(cv2.CAP_PROP_FRAME_COUNT))
		frames1 = int(videoCapture1.get(cv2.CAP_PROP_FRAME_COUNT))
		if frames0 != frames1:
			print(f'The number of frames ({frames0} and {frames1}) in the two videos are not equal. Exiting...')
			exit()

		# Get the frames
		dists = []
		for i in range(frames0):
			ret0, frame0 = videoCapture0.read()
			ret1, frame1 = videoCapture1.read()
			# Convert the frames to tensors
			img0 = lpips.im2tensor(frame0)
			img1 = lpips.im2tensor(frame1)

			if(opt.use_gpu):
				img0 = img0.cuda()
				img1 = img1.cuda()

			# Compute distance
			dists.append(loss_fn.forward(img0, img1).detach().cpu().numpy())
			
		distances = np.array(dists).mean()
		f.writelines('%s: %.6f\n'%(file,distances))
		dists_dirs.append(distances)
		
	else:
		print(f'{file} does not exist in {opt.dir1}, please ensure the files in the two directories have the same names')

print('Mean distance: %.4f'%np.array(dists_dirs).mean())
f.close()
