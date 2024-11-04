import argparse
import lpips
import cv2
import numpy as np

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-p0','--path0', type=str, default='../vids/aigc01_inp.mp4')
parser.add_argument('-p1','--path1', type=str, default='../vids/aigc01_out.mp4')
parser.add_argument('-v','--version', type=str, default='0.1')
parser.add_argument('--use_gpu', action='store_true', help='turn on flag to use GPU')

opt = parser.parse_args()

## Initializing the model
loss_fn = lpips.LPIPS(net='alex',version=opt.version)

if(opt.use_gpu):
	loss_fn.cuda()

# Open the video files
videoCapture0 = cv2.VideoCapture(opt.path0)
videoCapture1 = cv2.VideoCapture(opt.path1)

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
	img0 = lpips.im2tensor(frame0) # RGB image from [-1,1]
	img1 = lpips.im2tensor(frame1)

	if(opt.use_gpu):
		img0 = img0.cuda()
		img1 = img1.cuda()

	# Compute distance
	dists.append(loss_fn.forward(img0, img1).detach().numpy())

print('Distance: %.3f'%np.array(dists).mean())
