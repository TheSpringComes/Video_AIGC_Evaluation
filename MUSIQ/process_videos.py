import os
import cv2
from tqdm import tqdm
import argparse


def save_video_frames(video_path, output_folder):
    # 确保输出文件夹存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 打开视频文件
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print("Error: Could not open video.")
        return
    
    frame_count = 0
    while True:
        # 读取视频帧
        ret, frame = cap.read()
        
        if not ret:
            break  # 视频结束
        
        # 设置输出文件名（例如：0001.jpg, 0002.jpg）
        frame_filename = os.path.join(output_folder, f"{frame_count:04d}.jpg")
        
        # 保存帧
        cv2.imwrite(frame_filename, frame)
        frame_count += 1

    return frame_count


if __name__ == '__main__':
    argparse = argparse.ArgumentParser()
    argparse.add_argument('--video_paths', type=str, default='../vids/out')
    argparse.add_argument('--images_path', type=str, default='../vids/out_imgs')
    args = argparse.parse_args()

    files = os.listdir(args.video_paths)
    for file in tqdm(files, desc='Slicing videos to images'):
        if file.endswith('.mp4'):
            video_path = os.path.join(args.video_paths, file)
            output_folder = os.path.join(args.images_path, file.split('.')[0])
            save_video_frames(video_path, output_folder)
        else:
            print(f"Error: Could not find video file: {args.video_paths}")
