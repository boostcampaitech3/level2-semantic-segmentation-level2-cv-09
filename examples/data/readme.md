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