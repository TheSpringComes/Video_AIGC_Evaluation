from psnr import psnr
import os
import argparse
from tqdm import tqdm
import cv2
import numpy as np
from tqdm import tqdm
# X: (N,3,H,W) a batch of non-negative RGB images (0~255)
# Y: (N,3,H,W)  

parser = argparse.ArgumentParser()
parser.add_argument(
    "-x",
    "--input_video_dir",
    type=str,
    default="../vids/inp",
    help="the input video dir",
)

parser.add_argument(
    "-y",
    "--output_video_dir",
    type=str,
    default="../vids/out",
    help="the input video dir",
)

opt = parser.parse_args()

files = os.listdir(opt.input_video_dir)

psnr_vals = []  # psnrs for videos in the two directories
for file in tqdm(files):
    if os.path.exists(os.path.join(opt.output_video_dir, file)):
        videoCapture_x = cv2.VideoCapture(os.path.join(opt.input_video_dir, file))
        videoCapture_y = cv2.VideoCapture(os.path.join(opt.output_video_dir, file))

        frames_x = int(videoCapture_x.get(cv2.CAP_PROP_FRAME_COUNT))
        frames_y = int(videoCapture_y.get(cv2.CAP_PROP_FRAME_COUNT))
        if frames_x != frames_y:
            print(f"The number of frames ({frames_x} and {frames_y}) in the two videos are not equal. Exiting...")
            exit()

        psnr_val = []  # psnr for the corresponding video in the two directories
        # Get the frames
        for i in range(frames_x):
            retx, framex = videoCapture_x.read()
            rety, framey = videoCapture_y.read()
            if not retx or not rety:
                print(f"Error reading frames from {file}")
        
            psnr_val.append(psnr(framex, framey))
        
        psnr_vals.append(np.array(psnr_val).mean())
    else:
        print(f"File {file} does not exist in {opt.output_video_dir}, please ensure the files in the two directories have the same names")

print(f"Mean PSNR: {np.mean(psnr_vals):.4f}")