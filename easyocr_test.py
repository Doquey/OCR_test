import easyocr
import cv2
from beartype import beartype
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches



@beartype
def predict_image(img_path:str,languages:list=['en','pt'],detail:bool=True):
    """
    Essa função tem como objetivo receber um caminho para uma imagem, ler essa imagem usando o
    opencv e fazer a detecção e reconhecimento do texto nessa imagem utilizando o modelo easyocr.
    Passe 1 ou True para o argumento "detail" caso queira ver as bounding boxes da detecção do texto assim como o texto em si e tambem a confiança do modelo
    Passe 0 caso queira ver apenas o texto.
    """
    reader = easyocr.Reader(languages) 
    img = cv2.imread(img_path)
    assert img is not None, f'img not found!'
    results = reader.readtext(img,detail=detail)
    if detail:
        fig, ax = plt.subplots()
        ax.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        for ind,item in enumerate(results):
            bb = results[ind][0]
            polygon = patches.Polygon(bb, linewidth=2, edgecolor='r', facecolor='none')
            ax.add_patch(polygon)
            print(results[ind][1:])
        plt.show()
    
    

    return results
        
