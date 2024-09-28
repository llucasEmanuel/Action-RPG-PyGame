# Arquivo usado para fazer resize em sprites e texturas
import cv2
import os

def resize_png(file_path:str = None, scale:int = 1):
    # Lê o arquivo da imagem e mantém o png sem fundo
    img = cv2.imread(file_path, cv2.IMREAD_UNCHANGED)
   
    # Garante que o file_path existe
    assert img is not None, "File does not exist"

    # Cálculo das novas dimensões da imagem
    (new_w, new_h) = (img.shape[1] * scale, img.shape[0] * scale)

    # Faz o resize da imagem
    new_img = cv2.resize(img, (new_w, new_h), interpolation=cv2.INTER_NEAREST)

    # Mostra como a imagem ficou em comparação com a original
    cv2.imshow("Original image", img)
    cv2.imshow("New image", new_img)
   
    # Conta quantos arquivos tem na pasta para determinar o nome do novo arquivo
    save_path = "tools/images/"
    file_list = os.listdir(save_path)
    num_files = len(file_list)

    # salva a imagem em uma pasta especial
    cv2.imwrite(f"{save_path}new_image_{num_files + 1}.png", new_img)
   
    cv2.waitKey()
    cv2.destroyAllWindows()


# Substituir as variáveis para selecionar o arquivo e escala corretos
file_path = "assets/tittle.png"
scale = 3
if __name__ == "__main__":
    resize_png(file_path, scale)
