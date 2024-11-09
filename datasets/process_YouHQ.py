import os
import shutil
from tqdm import tqdm
from moviepy.editor import VideoFileClip, concatenate_videoclips
from moviepy.video import fx


def duplicate_images(input_folder, output_folder):
    # 确保输出文件夹存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    in_list = os.listdir(input_folder)
    for dir in tqdm(in_list, desc=f"处理文件夹{input_folder}"):    
        # 获取输入文件夹中所有符合格式的文件，文件名需匹配 "0000.jpg" 的格式
        original_files = os.listdir(os.path.join(input_folder, dir))

        # 生成正序、逆序、正序的顺序列表
        new_files = original_files + original_files[::-1] + original_files

        # 将文件复制到输出文件夹，并重命名
        for i, filename in enumerate(new_files):
            src_path = os.path.join(input_folder, dir, filename)
            dest_path = os.path.join(output_folder, dir, f"{i:04}.jpg")
            if os.path.exists(src_path):  # 检查源文件是否存在
                os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                shutil.copy(src_path, dest_path)
            else:
                print(f"文件 {src_path} 不存在，跳过该文件。")


def create_looped_video(input_video_path, output_video_path):
    if not os.path.exists(os.path.dirname(output_video_path)):
        os.makedirs(os.path.dirname(output_video_path))
    
    in_list = os.listdir(input_video_path)
    for file in in_list:
        # 获取输入文件夹中所有符合格式的文件，文件名需匹配 "0000.jpg" 的格式
        input_video_name = os.path.join(input_video_path, file)
        output_video_name = os.path.join(output_video_path, file)

        # 加载原始视频
        clip = VideoFileClip(input_video_name)
        
        # 创建倒放的视频
        reverse_clip = clip.fx(fx.all.time_mirror)
        
        # 将视频按正序、倒序、正序拼接
        final_clip = concatenate_videoclips([clip, reverse_clip, clip])
        
        # 输出合成视频
        final_clip.write_videofile(output_video_name, codec="mpeg4")
        # clip.reader.close()
        # clip.audio.reader.close_proc()


if __name__ == "__main__":
    # 图像文件处理
    input_folder = "YouHQ40/test"
    output_folder = "YouHQ40/test_new"
    # duplicate_images(input_folder, output_folder)

    # 视频文件处理
    input_video_path = "YouHQ40/train"
    output_video_path = "YouHQ40/train_new"
    create_looped_video(input_video_path, output_video_path)