import fasttext
import os
#https://towardsdatascience.com/benchmarking-language-detection-for-nlp-8250ea8b67c
#https://github.com/ageitgey/fastText-windows-binaries/releases/tag/v0.9.1
path_to_pretrained_model_compressed = 'assets/lid.176.ftz'

path_to_pretrained_model = 'assets/lid.176.bin'
def loadModel():
    if os.path.exists(path_to_pretrained_model):
        fmodel = fasttext.load_model(path_to_pretrained_model)
    else:
        fmodel = fasttext.load_model(path_to_pretrained_model_compressed)
    return fmodel    
def prediction(text,fmodel):
    text = text.replace('\n', '')
    text = text.replace('\\r', '')

    return fmodel.predict([text])[0][0][0].split('__')[-1]  # ([['__label__en']], [array([0.9331119], dtype=float32)]
    
# text ="never forget about china"
# print(prediction(text))