

</br>

![image](https://user-images.githubusercontent.com/82289435/161487725-cb433d95-1c59-47eb-b305-218a8c42ea46.png)

### π’ Members

[μ λ€μ΄](https://github.com/updaun)|[λ°μ μ¬](https://github.com/jeongjae96)|[κΉκ·λ―Ό](https://github.com/km9mn)|[μ΄μ΅ν¬](https://github.com/yoonghee)|[μκ²½κ΅­](https://github.com/tjrudrnr2)|
:-:|:-:|:-:|:-:|:-:|
![image1][image1]|![image2][image2]|![image3][image3]|![image4][image4]|![image5][image5]|

[image1]: https://user-images.githubusercontent.com/82289435/161474965-fde57430-c7d8-4a8b-b042-a60e553cfb4e.png
[image2]: https://user-images.githubusercontent.com/82289435/161475112-33b5e095-c2f1-4ed8-90cb-c3ae9f6296ba.png
[image3]: https://user-images.githubusercontent.com/82289435/161475194-7b2f9f11-98fa-4c10-b3fa-ef986e8775d5.png
[image4]: https://user-images.githubusercontent.com/82289435/161475112-33b5e095-c2f1-4ed8-90cb-c3ae9f6296ba.png
[image5]: https://user-images.githubusercontent.com/82289435/161475256-bc796065-f8f8-4bdc-9d43-05b684a73d7d.png



### π₯ Contribution  
- `μ λ€μ΄` &nbsp; ConvNeXt β’ BEiT β’ Model Experiment β’ Git management 
- `λ°μ μ¬` &nbsp; Data Preprocessing β’ SwinL β’ Model Experiment β’ Pseudo Labeling β’ Stratified Kfold β’ Ensemble   
- `κΉκ·λ―Ό` &nbsp; Model Experiment β’ Loss β’ Hyper Parameter Tuning
- `μ΄μ΅ν¬` &nbsp; Model Experiment β’ BEiT β’ SwinL β’ Ensemble 
- `μκ²½κ΅­` &nbsp; Model Experiment β’ UNet++ β’ Segformerm β’ HRNetV2 β’ SwinL β’ Pseudo Labeling

</br>

### π LB Score

- Public LB: 0.8250 mIoU(2λ±/19ν)
- Private LB: 0.7476 mIoU(8λ±/19ν) 

![output](https://user-images.githubusercontent.com/82289435/168489577-80ff9933-1234-4328-b09f-09ef103bf569.png)


</br>

## π Semantic Segmentation for sorting recycled items β»οΈ

</br>

![image](https://user-images.githubusercontent.com/82289435/168489562-b411a976-eea4-4f45-88ef-de24c98e9777.png)

### λ¬Έμ  μ μ β

- λ°μΌνλ‘ **λλ μμ°, λλ μλΉ**μ μλ. μ°λ¦¬λ λ§μ λ¬Όκ±΄μ΄ λλμΌλ‘ μμ°λκ³  μλΉλλ μλλ₯Ό μΆμ λ°λΌ **μ°λ κΈ° λλ, λ§€λ¦½μ§ λΆμ‘±**κ³Ό κ°μ μ¬ν λ¬Έμ  λ°μ
- λ²λ €μ§λ μ°λ κΈ° μ€ μ λΆλ¦¬λ°°μΆ λ μ°λ κΈ°λ μμμΌλ‘μ κ°μΉλ₯Ό μΈμ λ°μ μ¬νμ©λμ§λ§, μλͺ» λΆλ¦¬λ°°μΆ λλ©΄ κ·Έλλ‘ νκΈ°λ¬Όλ‘ λΆλ₯λμ΄ λ§€λ¦½ λλ μκ°λκΈ° λλ¬Έμ λΆλ¦¬μκ±°λ μ¬νμ  νκ²½ λΆλ΄ λ¬Έμ λ₯Ό μ€μΌ μ μλ λ°©λ²
- Deep Learningμ ν΅ν΄ μ°λ κΈ°λ€μ μλμΌλ‘ λΆλ₯ν  μ μλ λͺ¨λΈ κ°λ° 

</br>


### β Development Environment
- GPU : Nvidia Tesla V100
- OS : Linux Ubuntu 18.04
- Runtime : Python 3.8.5
- Main Dependency : Yolov5, MMdetection, Detectron2, Pytorch 1.7.1, OpenCV 4.5.1

</br>

### πΎ Dataset
![image](https://user-images.githubusercontent.com/82289435/161486061-946f9820-1580-4d0f-a14a-90a9a56181de.png)

- μ μ²΄ μ΄λ―Έμ§ κ°μ : 3272μ₯
- 11 class : Background, General trash, Paper, Paper pack, Metal, Glass, Plastic, Styrofoam, Plastic bag, Battery, Clothing
- μ΄λ―Έμ§ ν¬κΈ° : (512, 512)
- νκ° λ°μ΄ν° 958κ° λΈμΆ μ΄μ
- νμ΅λ°μ΄ν°λ 2617(+958)μ₯, κ²μ¦λ°μ΄ν°λ 655μ₯, νκ°λ°μ΄ν°λ 624μ₯μΌλ‘ λ¬΄μμ μ μ 

### π Metrics
- Test setμ mIoU (Mean Intersection over Union)λ‘ νκ°
![image](https://user-images.githubusercontent.com/82289435/168489941-31def4f1-d4e4-41c5-a5bd-0bbb6d314927.png)
- Example of IoU
![image](https://user-images.githubusercontent.com/82289435/168489956-0a33ccbc-27f5-4c61-88a2-52e58b079225.png)
- Example of mIoU (κ²½μ§λνμμμ "C=11")
![image](https://user-images.githubusercontent.com/82289435/168489969-31ca0504-6640-44f3-b378-9dc188675286.png)

[μ°Έκ³ μ¬ν­]

- modelλ‘λΆν° μμΈ‘λ maskμ sizeλ 512 x 512 μ§λ§, λνμ μνν μ΄μμ μν΄ outputμ μΌκ΄μ μΌλ‘ 256 x 256 μΌλ‘ λ³κ²½νμ¬ scoreλ₯Ό λ°μνκ² λμμ΅λλ€.

- mIoU (Mean Intersection over Union)
    - Semantic Segmentationμμ μ¬μ©νλ λνμ μΈ μ±λ₯ μΈ‘μ  λ°©λ²

</br>

### π§ͺ Model Experiments 
### [![Notion](https://img.shields.io/badge/Notion-%23000000.svg?style=for-the-badge&logo=notion&logoColor=white)](https://seemly-newsstand-e49.notion.site/f627f43d19a848848f6183ce0b2b78cd?v=b089e7beafa242b38fbe2afa21762a8c)



### π¬ Ensemble Experiments
### [![Notion](https://img.shields.io/badge/Notion-%23000000.svg?style=for-the-badge&logo=notion&logoColor=white)](https://seemly-newsstand-e49.notion.site/ba09f5ece32241eeb6c875abd2ee3fb0?v=b9d8bd7e497e410492ae546c9f35ef85)



### πΆ Ensemble Candidate
### [![Notion](https://img.shields.io/badge/Notion-%23000000.svg?style=for-the-badge&logo=notion&logoColor=white)](https://seemly-newsstand-e49.notion.site/fa7f348203a3415aa2641cbebc34824a?v=0e1061cc856142659e0773fd0dc0a044)



### β Data Denoising
### [![Notion](https://img.shields.io/badge/Notion-%23000000.svg?style=for-the-badge&logo=notion&logoColor=white)](https://seemly-newsstand-e49.notion.site/3305dac046bd400f895189bee0a0ed9e?v=da7f4136486c4da5b69217e7d6af252a)

</br>


### π’ Presentation
[νμ΄νμ΄ν_λ°νμλ£.pdf](https://drive.google.com/file/d/1sp5rvDz67RQ17p_tXO1a50L4snxF-QWX/view?usp=sharing)

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

## MMSegmentation μ€μΉ

<br>

_μ€μΉ μμ_
```
conda create -n open-mmlab python=3.10 -y
conda activate open-mmlab

conda install pytorch=1.11.0 torchvision cudatoolkit=11.3 -c pytorch

pip install mmcv-full -f https://download.openmmlab.com/mmcv/dist/cu113/torch1.11/index.html

# mmsegmentationμ μ€μΉν  κ²½λ‘ μ€μ . μ λ μ ν¬ κΉ ν΄λ λ΄λΆμ μ€μΉνμ΅λλ€.
cd ... code/

git clone https://github.com/open-mmlab/mmsegmentation.git
cd mmsegmentation
pip install -e .  # or "python setup.py develop"
```

<br>

## train_all.jsonκ³Ό data.json ν©μΉκΈ°
- [_data_concat_anno_exclude.ipynb_](https://github.com/boostcampaitech3/level2-semantic-segmentation-level2-cv-09/blob/develop/examples/data/data_concat_anno_exclude.ipynb) μ€ν : categoryκ° 'UNKNOWN'μ΄κ±°λ segmentationμ΄ λΉ annotationμ μ μΈνκ³  concatenationμ΄ μ§νλλ€.

<br>

## Train & Validation Split
1. λ¨Όμ  [train_all.jsonκ³Ό data.json ν©μΉκΈ°](#trainalljsonκ³Ό-datajson-ν©μΉκΈ°)λ₯Ό μ§ννλ€.
2. [_stratified_kfold.py_](https://github.com/boostcampaitech3/level2-semantic-segmentation-level2-cv-09/blob/develop/examples/data/stratified_kfold.py) μ€ν : Stratified K-foldλ‘ λλμ΄μ§λ€. (default 5-fold)

<br>

## Convert to MMSegementation Format
1. λ¨Όμ  [Train & Validation Split](#train--validation-split)λ₯Ό μ§ννλ€.
2. [_convert_mmseg.ipynb_](https://github.com/boostcampaitech3/level2-semantic-segmentation-level2-cv-09/blob/develop/examples/data/convert_mmseg.ipynb)λ₯Ό μ€ννλ€.
