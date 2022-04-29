# yapf:disable
log_config = dict(
    interval=50,
    hooks=[
        dict(type="TextLoggerHook", by_epoch=True),
        dict(
            type="WandbLoggerHook",
            init_kwargs=dict(
                project="seg-mmseg",
                name="Upernet_SwinB_p4_w12",
                entity="level2-cv-09",
            ),
        ),
    ],
)
# yapf:enable
dist_params = dict(backend="nccl")
log_level = "INFO"
load_from = None
resume_from = None
workflow = [("train", 1)]
cudnn_benchmark = True
