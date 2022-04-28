# Semantic Segmentation

## Working Directory (04/28 update)

```
.
|-- code (git)
|   |-- examples
|   |   |-- baseline_model_feat
|   |   |   |-- bestmIoU_baseline_fcn_resnet50.ipynb
|   |   |   `-- wandb_baseline_fcn_resnet50.ipynb
|   |   `-- data
|   |       |-- convert_mmseg.ipynb
|   |       |-- data_concat_anno_exclude.ipynb
|   |       |-- data_concat_img_exclude.ipynb
|   |       `-- stratified_kfold.py
|   |-- mmsegmentation
|   |-- model
|   |   `-- mmseg
|   |-- baseline_fcn_resnet50.ipynb
|   |-- requirements.txt
|   `-- utils.py
`-- data
    |-- batch_01_vt
    |   `-- 0002.jpg
    |-- batch_02_vt
    |   `-- 0001.jpg
    |-- batch_03
    |   `-- 0001.jpg
    |-- mmseg
    |   |-- ann_dir
    |   |    |-- train0~4
    |   |    |    `-- *.png
    |   |    `-- val0~4
    |   |         `-- *.png
    |   `-- img_dir
    |       |-- test
    |       |    `-- *.jpg
    |       |-- train0~4
    |       |    `-- *.jpg 
    |       `-- val0~4
    |              `-- *.jpg
    |-- stratified_kfold
    |   |-- train0~4.json
    |   `-- val0~4.json
    |-- new_train_all_anno_excluded.json
    |-- test.json
    |-- train.json
    |-- train_all.json
    `-- val.json
```

<br>

## MMSegmentation 설치

<br>

_설치 예시_
```
conda create -n open-mmlab python=3.10 -y
conda activate open-mmlab

conda install pytorch=1.11.0 torchvision cudatoolkit=11.3 -c pytorch

pip install mmcv-full -f https://download.openmmlab.com/mmcv/dist/cu113/torch1.11/index.html

# mmsegmentation을 설치할 경로 설정. 저는 저희 깃 폴더 내부에 설치했습니다.
cd ... code/

git clone https://github.com/open-mmlab/mmsegmentation.git
cd mmsegmentation
pip install -e .  # or "python setup.py develop"
```

<br>

## train_all.json과 data.json 합치기
- [_data_concat_anno_exclude.ipynb_](https://github.com/boostcampaitech3/level2-semantic-segmentation-level2-cv-09/blob/develop/examples/data/data_concat_anno_exclude.ipynb) 실행 : category가 'UNKNOWN'이거나 segmentation이 빈 annotation을 제외하고 concatenation이 진행된다.

<br>

## Train & Validation Split
1. 먼저 [train_all.json과 data.json 합치기](#trainalljson과-datajson-합치기)를 진행한다.
2. [_stratified_kfold.py_](https://github.com/boostcampaitech3/level2-semantic-segmentation-level2-cv-09/blob/develop/examples/data/stratified_kfold.py) 실행 : Stratified K-fold로 나누어진다. (default 5-fold)

<br>

## Convert to MMSegementation Format
1. 먼저 [Train & Validation Split](#train--validation-split)를 진행한다.
2. [_convert_mmseg.ipynb_](https://github.com/boostcampaitech3/level2-semantic-segmentation-level2-cv-09/blob/develop/examples/data/convert_mmseg.ipynb)를 실행한다.