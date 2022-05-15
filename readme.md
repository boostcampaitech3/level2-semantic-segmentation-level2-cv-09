

</br>

![image](https://user-images.githubusercontent.com/82289435/161487725-cb433d95-1c59-47eb-b305-218a8c42ea46.png)

### 🚢 Members

[전다운](https://github.com/updaun)|[박정재](https://github.com/jeongjae96)|[김규민](https://github.com/km9mn)|[이융희](https://github.com/yoonghee)|[서경국](https://github.com/tjrudrnr2)|
:-:|:-:|:-:|:-:|:-:|
![image1][image1]|![image2][image2]|![image3][image3]|![image4][image4]|![image5][image5]|

[image1]: https://user-images.githubusercontent.com/82289435/161474965-fde57430-c7d8-4a8b-b042-a60e553cfb4e.png
[image2]: https://user-images.githubusercontent.com/82289435/161475112-33b5e095-c2f1-4ed8-90cb-c3ae9f6296ba.png
[image3]: https://user-images.githubusercontent.com/82289435/161475194-7b2f9f11-98fa-4c10-b3fa-ef986e8775d5.png
[image4]: https://user-images.githubusercontent.com/82289435/161475112-33b5e095-c2f1-4ed8-90cb-c3ae9f6296ba.png
[image5]: https://user-images.githubusercontent.com/82289435/161475256-bc796065-f8f8-4bdc-9d43-05b684a73d7d.png



### 🔥 Contribution  
- `전다운` &nbsp; ConvNeXt • BEiT • Model Experiment • Git management 
- `박정재` &nbsp; Data Preprocessing • SwinL • Model Experiment • Pseudo Labeling • Stratified Kfold • Ensemble   
- `김규민` &nbsp; Model Experiment • Loss • Hyper Parameter Tuning
- `이융희` &nbsp; Model Experiment • BEiT • SwinL • Ensemble 
- `서경국` &nbsp; Model Experiment • UNet++ • Segformerm • HRNetV2 • SwinL • Pseudo Labeling

</br>

### 🏆 LB Score

- Public LB: 0.8250 mIoU(2등/19팀)
- Private LB: 0.7476 mIoU(8등/19팀) 

![output](https://user-images.githubusercontent.com/82289435/168489577-80ff9933-1234-4328-b09f-09ef103bf569.png)


</br>

## 🔎 Semantic Segmentation for sorting recycled items ♻️

</br>

![image](https://user-images.githubusercontent.com/82289435/168489562-b411a976-eea4-4f45-88ef-de24c98e9777.png)

### 문제 정의 ❓

- 바야흐로 **대량 생산, 대량 소비**의 시대. 우리는 많은 물건이 대량으로 생산되고 소비되는 시대를 삶에 따라 **쓰레기 대란, 매립지 부족**과 같은 사회 문제 발생
- 버려지는 쓰레기 중 잘 분리배출 된 쓰레기는 자원으로서 가치를 인정받아 재활용되지만, 잘못 분리배출 되면 그대로 폐기물로 분류되어 매립 또는 소각되기 때문에 분리수거는 사회적 환경 부담 문제를 줄일 수 있는 방법
- Deep Learning을 통해 쓰레기들을 자동으로 분류할 수 있는 모델 개발 

</br>


### ⚙ Development Environment
- GPU : Nvidia Tesla V100
- OS : Linux Ubuntu 18.04
- Runtime : Python 3.8.5
- Main Dependency : Yolov5, MMdetection, Detectron2, Pytorch 1.7.1, OpenCV 4.5.1

</br>

### 💾 Dataset
![image](https://user-images.githubusercontent.com/82289435/161486061-946f9820-1580-4d0f-a14a-90a9a56181de.png)

- 전체 이미지 개수 : 3272장
- 11 class : Background, General trash, Paper, Paper pack, Metal, Glass, Plastic, Styrofoam, Plastic bag, Battery, Clothing
- 이미지 크기 : (512, 512)
- 평가 데이터 958개 노출 이슈
- 학습데이터는 2617(+958)장, 검증데이터는 655장, 평가데이터는 624장으로 무작위 선정

### 📐 Metrics
- Test set의 mIoU (Mean Intersection over Union)로 평가
![image](https://user-images.githubusercontent.com/82289435/168489941-31def4f1-d4e4-41c5-a5bd-0bbb6d314927.png)
- Example of IoU
![image](https://user-images.githubusercontent.com/82289435/168489956-0a33ccbc-27f5-4c61-88a2-52e58b079225.png)
- Example of mIoU (경진대회에서의 "C=11")
![image](https://user-images.githubusercontent.com/82289435/168489969-31ca0504-6640-44f3-b378-9dc188675286.png)

[참고사항]

- model로부터 예측된 mask의 size는 512 x 512 지만, 대회의 원활한 운영을 위해 output을 일괄적으로 256 x 256 으로 변경하여 score를 반영하게 되었습니다.

- mIoU (Mean Intersection over Union)
    - Semantic Segmentation에서 사용하는 대표적인 성능 측정 방법

</br>

### 🧪 Model Experiments 
### [![Notion](https://img.shields.io/badge/Notion-%23000000.svg?style=for-the-badge&logo=notion&logoColor=white)](https://seemly-newsstand-e49.notion.site/f627f43d19a848848f6183ce0b2b78cd?v=b089e7beafa242b38fbe2afa21762a8c)



### 🔬 Ensemble Experiments
### [![Notion](https://img.shields.io/badge/Notion-%23000000.svg?style=for-the-badge&logo=notion&logoColor=white)](https://seemly-newsstand-e49.notion.site/ba09f5ece32241eeb6c875abd2ee3fb0?v=b9d8bd7e497e410492ae546c9f35ef85)



### 🎶 Ensemble Candidate
### [![Notion](https://img.shields.io/badge/Notion-%23000000.svg?style=for-the-badge&logo=notion&logoColor=white)](https://seemly-newsstand-e49.notion.site/fa7f348203a3415aa2641cbebc34824a?v=0e1061cc856142659e0773fd0dc0a044)



### ✂ Data Denoising
### [![Notion](https://img.shields.io/badge/Notion-%23000000.svg?style=for-the-badge&logo=notion&logoColor=white)](https://seemly-newsstand-e49.notion.site/3305dac046bd400f895189bee0a0ed9e?v=da7f4136486c4da5b69217e7d6af252a)

</br>


### 📢 Presentation
[하이파이프_발표자료.pdf](https://drive.google.com/file/d/1sp5rvDz67RQ17p_tXO1a50L4snxF-QWX/view?usp=sharing)

</br>

<hr>

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
