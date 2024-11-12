import os
import cv2

def list_files_info(folder_path):
    # 检查文件夹是否存在
    if not os.path.isdir(folder_path):
        print("指定的路径不是文件夹或不存在。")
        return

    txt_file = open('satisfactory_video.txt', 'w')
    # 遍历文件夹下的所有文件
    cnt, cnt_new = 0, 0
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            cap = cv2.VideoCapture(file_path)
            if not cap.isOpened():
                print("无法打开视频文件。")
                return

            # 获取视频的帧数和分辨率
            frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))    # 视频总帧数
            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))          # 视频宽度
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))        # 视频高度

            # 输出视频信息
            # print(f"视频文件: {file_path}")
            # print(f"视频帧数: {frame_count}")
            # print(f"视频分辨率: {width}x{height}")
            if frame_count >= 77 and width*height >= 512*512:
                cnt_new += 1
                txt_file.write(f"{file_path}\n")
            cnt += 1
    print(f"共检测到 {cnt} 个视频文件，其中 {cnt_new} 个视频文件帧数大于等于 77 帧且 分辨率大于等于 512x512。")
    txt_file.close()
    print("视频信息已保存到 satisfactory_video.txt 文件。")

# 调用函数，替换 'your_folder_path' 为实际文件夹路径
list_files_info('./VideoGen-Eval1.0')
