from albumentations import Compose, HorizontalFlip, VerticalFlip, Normalize
from albumentations.pytorch import ToTensorV2
import albumentations as albu
import cv2


class CustomAugmentation:
    def __init__(self, train=True, mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225)):
        self.mean = mean
        self.std = std
        if train:
           self.transform = Compose([
                                    HorizontalFlip(p=0.5),
                                    # VerticalFlip(p=0.5),
                                    # albu.ShiftScaleRotate(shift_limit=0.4, 
                                    #                   scale_limit=(0.5, 0.9), 
                                    #                   rotate_limit=90, 
                                    #                   p=1, 
                                    #                   border_mode=cv2.BORDER_REPLICATE),
                                    albu.ShiftScaleRotate(shift_limit=0.0625, 
                                                    scale_limit=0.2, 
                                                    rotate_limit=15),
                                    albu.RandomBrightnessContrast(p=0.5),
                                    # Normalize(self.mean,
                                    #     self.std),
                                    ToTensorV2()
                                    ])
        else:
            self.transform = Compose([
                                    # Normalize(self.mean,
                                    #     self.std),
                                    ToTensorV2()
                                    ])

    def __call__(self, image, mask=None):
        if mask is not None:
            return self.transform(image=image, mask=mask)
        else:
            return self.transform(image=image)


# aug reference
# https://lcyking.tistory.com/80