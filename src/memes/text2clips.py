# https://github.com/jacebrowning/memegen

# https://github.com/nomad-software/meme




# https://github.com/xenox240/Aspace#meme-generators
# shuru 固定数量的句子 断句即可  自动选择合适的meme 模板 总共有180多个 
# 输出 图片
# 输出 gif


def text2staticimg()
def text2imggif()

def text2memeimg()
def text2memeimgparts()
def text2memegif()
def text2keywordvideo()
def text2compilationclip()

video dataset 


https://github.com/haofanwang/natural-language-joint-query-search
from pathlib import Path

# Create a folder for the precomputed features
!mkdir unsplash-dataset

# Download from Github Releases
if not Path('unsplash-dataset/photo_ids.csv').exists():
  !wget https://github.com/haltakov/natural-language-image-search/releases/download/1.0.0/photo_ids.csv -O unsplash-dataset/photo_ids.csv

if not Path('unsplash-dataset/features.npy').exists():
  !wget https://github.com/haltakov/natural-language-image-search/releases/download/1.0.0/features.npy -O unsplash-dataset/features.npy


import torch
import numpy as np
import pandas as pd
from PIL import Image

from CLIP.clip import clip

def encode_search_query(search_query):
    with torch.no_grad():
        text_encoded, weight = model.encode_text(clip.tokenize(search_query).to(device))
        text_encoded /= text_encoded.norm(dim=-1, keepdim=True)
        return text_encoded.cpu().numpy()

def find_best_matches(text_features, photo_features, photo_ids, results_count):
  similarities = (photo_features @ text_features.T).squeeze(1)
  best_photo_idx = (-similarities).argsort()
  return [photo_ids[i] for i in best_photo_idx[:results_count]]

device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load("ViT-B/32", device=device)

photo_ids = pd.read_csv("unsplash-dataset/photo_ids.csv")
photo_ids = list(photo_ids['photo_id'])
photo_features = np.load("unsplash-dataset/features.npy")

# text to image
search_query = "Tokyo Tower at night."
text_features = model.encode_search_query(search_query)
best_photo_ids = find_best_matches(text_features, photo_features, photo_ids, 5)
for photo_id in best_photo_ids:
  print("https://unsplash.com/photos/{}/download".format(photo_id))

# image to image
source_image = "images/borna-hrzina-8IPrifbjo-0-unsplash.jpg"
with torch.no_grad():
  image_feature = model.encode_image(preprocess(Image.open(source_image)).unsqueeze(0).to(device))
  image_feature = (image_feature / image_feature.norm(dim=-1, keepdim=True)).cpu().numpy()
best_photo_ids = find_best_matches(image_feature, photo_features, photo_ids, 5)
for photo_id in best_photo_ids:
  print("https://unsplash.com/photos/{}/download".format(photo_id))

# text+text to image
search_query = "red flower"
search_query_extra = "blue sky"
text_features = encode_search_query(search_query)
text_features_extra = encode_search_query(search_query_extra)
mixed_features = text_features + text_features_extra
best_photo_ids = find_best_matches(mixed_features, photo_features, photo_ids, 5)
for photo_id in best_photo_ids:
  print("https://unsplash.com/photos/{}/download".format(photo_id))

# image+text to image
search_image = "images/borna-hrzina-8IPrifbjo-0-unsplash.jpg"
search_text = "cars"
with torch.no_grad():
  image_feature = model.encode_image(preprocess(Image.open(search_image)).unsqueeze(0).to(device))
  image_feature = (image_feature / image_feature.norm(dim=-1, keepdim=True)).cpu().numpy()
text_feature = encode_search_query(search_text)
modified_feature = image_feature + text_feature
best_photo_ids = find_best_matches(modified_feature, photo_features, photo_ids, 5)
for photo_id in best_photo_ids:
  print("https://unsplash.com/photos/{}/download".format(photo_id))


