# Test videos

Videos storage path:

+ original  videos: ./vids/inp
+ generated videos: ./vids/out


The corresponding videos in the two dirs should have the same name, same size and same number of frames

## 1. PSNR

PSNR code is in the dir ./PSNR

run the following code to evaluate PSNR value:

```shell
cd PSNR

python video_psnr.py
```

## 2. SSIM

SSIM code is in the dir ./SSIM
run the following code to evaluate SSIM value:

```shell
cd SSIM

python video_ssim.py
```

## 3. LPIPS

LPIPS code is in the dir ./PerceptualSimilarity

run the following code to evaluate LPIPS value:

```shell
cd PerceptualSimilarity

# take the distance between 2 specific videos
python lpips_2vids.py

# all corresponding pairs of videos in 2 directories
python lpips_2vid_dirs.py
```

## 4. $E^*_{warp}$


## 5. DOVER

DOVER code is in the dir ./DOVER

(1) download the pretrained model from [**DOVER**](https://github.com/QualityAssessment/DOVER/releases/download/v0.1.0/DOVER.pth), and remove DOVER.pth to ./DOVBER/pretrained_weights

(2) run the code to evaluate DOVER value:

```shell
cd DOVER

# python evaluate_a_set_of_videos.py -in $YOUR_SPECIFIED_DIR$ -out $OUTPUT_CSV_PATH$
# default YOUR_SPECIFIED_DIR is '../vids/out'
# default OUTPUT_CSV_PATH is '../vids/dover.csv'
python evaluate_a_set_of_videos.py
```

## 6. MUSIQ

MUSIQ code is in the dir ./MUSIQ

(1) This code is based on tensorflow framework. So first you need to install the packages following requirments.txt

(2) Download the model checkpoints from:
[gcloud directory link](https://console.cloud.google.com/storage/browser/gresearch/musiq)

- **ava_ckpt.npz**: Trained on AVA dataset. (not recommended)
- **koniq_ckpt.npz**: Trained on KonIQ dataset.
- **paq2piq_ckpt.npz**: Trained on PaQ2PiQ dataset.
- **spaq_ckpt.npz**: Trained on SPAQ dataset.
- **imagenet_pretrain.npz**: Pretrained checkpoint on ImageNet. (not recommended)

In our evalutaion, we use koniq_ckpt.npz
