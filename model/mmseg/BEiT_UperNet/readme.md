# BEiT-UperNet
## 설치
- NVIDIA의 apex설치
```
git clone https://github.com/NVIDIA/apex
cd apex
python setup.py install
```
- mmcv-full 설치
```
pip install mmcv-full==1.5.0
```

- mmsegmentation 설치
```
pip install mmsegmentation==0.23.0
```
- scipy, timm 설치
```
pip install scipy timm
```
<br/>

<br/>



## 실행예시

### Download Pretrained Model Link

- [beit_large_patch16_224_pt22k_ft22k.pth](https://unilm.blob.core.windows.net/beit/beit_large_patch16_224_pt22k_ft22k.pth)

<br/>



1. pretrained model 받기
```
wget {Download Pretrained Model Link}
```
2. pretrained model 변환
```
# 경로 예시
{PRETRAIN_PATH}: ./pretrained/*.pth 
{STORE_PATH}: ./cvt_pretrained/*.pth

python tools/model_converters/beit2mmseg.py {PRETRAIN_PATH} {STORE_PATH}
```
3. ```default_runtime.py```에서 wandb experiment name 설정 및 ```dataset.py```에서 fold number 설정
4. 학습
```
python tools/train.py {CONFIG_PATH} --work-dir {WORK_DIR} --seed {SEED}
```