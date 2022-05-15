# optimizer
optimizer = dict(type='SGD', lr=0.01, momentum=0.9, weight_decay=0.0005)
optimizer_config = dict()
# learning policy
lr_config = dict(policy='poly', power=0.9, min_lr=1e-4, by_epoch=True)
# runtime settings
runner = dict(type='EpochBasedRunner', max_epochs=80)
checkpoint_config = dict(by_epoch=True, interval=1, max_keep_ckpts=3)
evaluation = dict(save_best='mIoU', metric='mIoU', pre_eval=True)
