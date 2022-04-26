import json
import argparse
import numpy as np
import funcy
from sklearn.model_selection import StratifiedGroupKFold
import os

parser = argparse.ArgumentParser(description='Splits COCO annotations file for cross validation.')
parser.add_argument('--path', type=str, default='/opt/ml/input/data/', help='Path to dataset')
parser.add_argument('-n', dest='split', type=int,  default=5,
                    help="A number of split for cross validation")

args = parser.parse_args()

def save_coco(file, info, licenses, images, annotations, categories):
    with open(file, 'w', encoding='UTF-8') as coco:
        json.dump({ 'info': info, 'licenses': licenses, 'images': images, 
            'annotations': annotations, 'categories': categories}, coco, indent=2)


def filter_annotations(annotations, images):
    image_ids = funcy.lmap(lambda i: int(i['id']), images)
    return funcy.lfilter(lambda a: int(a['image_id']) in image_ids, annotations)


def main(args):
    with open(f'{args.path}new_train_all.json', 'r', encoding='UTF-8') as annotations:
        coco = json.load(annotations)
        info = coco['info']
        licenses = coco['licenses']
        images = coco['images']
        annotations = coco['annotations']
        categories = coco['categories']
        
        var = [(ann['image_id'], ann['category_id']) for ann in coco['annotations']]

        groups = np.array([v[0] for v in var])
        y = np.array([v[1] for v in var])

        cv = StratifiedGroupKFold(n_splits=args.split, shuffle=True, random_state=411)

        images = np.array(images)

        for i, (train_idx, val_idx) in enumerate(cv.split(groups, y, groups)):

            train_idx = np.unique(groups[train_idx])
            val_idx = np.unique(groups[val_idx])

            if not os.path.isdir(os.path.join(args.path, 'stratified_kfold')):
                os.mkdir(os.path.join(args.path, 'stratified_kfold'))

            save_coco(os.path.join(args.path, f'stratified_kfold/train{i}.json'), info, licenses, list(images[train_idx]), filter_annotations(annotations, list(images[train_idx])), categories)
            save_coco(os.path.join(args.path, f'stratified_kfold/val{i}.json'), info, licenses, list(images[val_idx]), filter_annotations(annotations, list(images[val_idx])), categories)

            print(f'***cv{i}***')
            print(f'saved {len(images[train_idx])} images & {len(filter_annotations(annotations, list(images[train_idx])))} annotations in train set.')
            print(f'saved {len(images[val_idx])} images & {len(filter_annotations(annotations, list(images[val_idx])))} annotations in validation set.')
            print()


if __name__ == "__main__":
    main(args)