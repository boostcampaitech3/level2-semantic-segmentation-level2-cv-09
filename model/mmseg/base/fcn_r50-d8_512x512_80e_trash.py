# 다른 모델을 쓰기 위해서 dataset과 epoch, num_classes를 바꿔줘야 함

_base_ = [
    '../_base_/models/fcn_r50-d8.py', '../_base_/datasets/dataset.py',
    '../_base_/default_runtime.py', '../_base_/schedules/epoch.py'
]

model = dict(
    decode_head=dict(num_classes=11), auxiliary_head=dict(num_classes=11))
