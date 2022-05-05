### pseudo_labeling_to_mask_png.ipynb

- output.csv를 이용해 mask.png 형식의 pseudo label 이미지를 만드는 코드입니다.

---

### create_custom_coco_dataset.ipynb

- mask.png format을 coco format으로 바꾸는 코드입니다.
- _reference: https://github.com/chrise96/image-to-coco-json-converter_

### mmseg Pseudo labeling 만드는 법
1. 위 과정으로 png, pseudo.json 파일을 생성한다.
2. merge_json.ipynb로 train(ann_excluded든 revised든)과 pseudo.json 합친다.
3. stratified_kfold.py로 kfold
    기존 kfold랑 구분하고 싶으면 디렉토리 이름 변경 (저는 p_stratified_kfold)
4. convert_mmseg.ipynb로 img_dir, ann_dir 생성
    저는 mmseg랑 구분하고 싶으면 디렉토리 이름 변경 (저는 p_mmseg)
5. mmseg폴더를 따로 생성했으면 mmsegmentation의 dataset.py에서 data_dir 경로 바꿔주기