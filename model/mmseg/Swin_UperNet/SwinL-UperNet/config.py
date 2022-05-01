_base_ = [
    "upernet_swin.py",
    "dataset.py",
    "default_runtime.py",
    "epoch.py",
]

model = dict(
    pretrained="/opt/ml/input/code/mmsegmentation/pretrain/swin_large_patch4_window12_384_22k.pth",
    backbone=dict(
        pretrain_img_size=384,
        embed_dims=192,
        depths=[2, 2, 18, 2],
        num_heads=[6, 12, 24, 48],
        window_size=12,
        use_abs_pos_embed=False,
        drop_path_rate=0.3,
        patch_norm=True,
    ),
    decode_head=dict(in_channels=[192, 384, 768, 1536], num_classes=11),
    auxiliary_head=dict(in_channels=768, num_classes=11),
)


# AdamW optimizer, no weight decay for position embedding & layer norm
# in backbone
optimizer = dict(
    _delete_=True,
    type="AdamW",
    lr=0.00006,
    betas=(0.9, 0.999),
    weight_decay=0.01,
    paramwise_cfg=dict(
        custom_keys={
            "absolute_pos_embed": dict(decay_mult=0.0),
            "relative_position_bias_table": dict(decay_mult=0.0),
            "norm": dict(decay_mult=0.0),
            "head": dict(lr_mult=2.0),
        }
    ),
)

lr_config = dict(
    _delete_=True,
    policy="CosineRestart",
    periods=[30000, 50000],
    restart_weights=[1.0, 0.3],
    warmup="linear",
    warmup_iters=500,
    warmup_ratio=0.1,
    min_lr=0,
    by_epoch=False,
)

# lr = 1e-4 /2  # max learning rate
# optimizer = dict(type='AdamW', lr=lr, weight_decay=0.01)
# optimizer_config = dict(grad_clip=dict(max_norm=10, norm_type=2))
# lr_config = dict(
#     policy='CosineAnnealing',
#     warmup='linear',
#     warmup_iters=300,
#     warmup_ratio=0.1,
#     min_lr_ratio=7e-6
# )

# By default, models are trained on 8 GPUs with 2 images per GPU
data = dict(samples_per_gpu=4)
seed = 42