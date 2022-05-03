### data_concat_img_exclude.ipynb

- train_all.json에 data.json에서 유출된 annotation을 추가하는 코드입니다.
- concat 시, category가 0인 annotation이 있는 이미지를 제외합니다.

---

### data_concat_anno_exclude.ipynb

- train_all.json에 data.json에서 유출된 annotation을 추가하는 코드입니다.
- concat 시, category가 0인 annotation을 제외합니다.

---

### stratified_kfold.py

- Stratified K-fold validation set을 만드는 코드입니다.

---

### convert_mmseg.ipynb

- 원본 데이터를 mmsegmentation 형식에 맞추어 변환하는 코드입니다.

---

### data_cleansing.ipynb

- noise가 있는 데이터를 제외하는 코드입니다.
- ```data_cleansing.ipynb```는 이미지만 제외하는 코드입니다.
- ```data_cleansing_ver3.ipynb```는 이미지 제외 및 category를 변경할 수 있는 annotation은 category를 변경하는 코드입니다.
- ```data_cleasing_visualize.ipynb```는 전처리가 어떻게 돼가고 있는지 시각화 할 수 있도록 했습니다.