# Swin-UperNet

## SwinB-UperNet

### Download Pretrained Model

- [_upernet_swin_base_patch4_window12_512x512_160k_ade20k_pretrain_384x384_22K_20210531_125459-429057bf.pth_](https://download.openmmlab.com/mmsegmentation/v0.5/swin/upernet_swin_base_patch4_window12_512x512_160k_ade20k_pretrain_384x384_22K/upernet_swin_base_patch4_window12_512x512_160k_ade20k_pretrain_384x384_22K_20210531_125459-429057bf.pth)

### 실행예시

1. [pretrained model 받기](#download-pretrained-model)
2. pretrained model 변환
```
# 경로 예시
{PRETRAIN_PATH}: ./pretrained/*.pth 
{STORE_PATH}: ./cvt_pretrained/*.pth

python tools/model_converters/swin2mmseg.py {PRETRAIN_PATH} {STORE_PATH}
```
3. ```default_runtime.py```에서 wandb experiment name 설정 및 ```dataset.py```에서 fold number 설정
4. 학습
```
python tools/train.py {CONFIG_PATH} --work-dir {WORK_DIR} --seed {SEED}
```