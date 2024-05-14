
from PIL import Image
# import BytesIO


def image(path: str) -> Image.Image:
    img = Image.open(path)
    return img

def i_size(img: Image.Image, verbose: bool = False) -> tuple[int, int]:
    weight, height = img.size
    if verbose:
        print('weight: ', weight, '\nheight: ', height)
    return weight, height

def i_resize(img: Image.Image, new_weight: int, verbose: bool = False) -> Image.Image:
    weight, height = i_size(img, verbose)
    scale = new_weight/weight
    new_height = int(height*scale)
    img_resized = img.resize((new_weight, new_height))
    return img_resized


def i_save(img: Image.Image, path: str):
    img.save(path)

def pdf2png(path: str):
    pass






def main():
    path = fr'C:\dtertre59\Documents\3_PROGRAMACION\Python\image-converter\app\assets\userInfo.jpg'
    img = image(path)
    img2 = i_resize(img, 465, verbose= True)
    i_size(img2, verbose=True)
    i_save(img2, './app/assets/userInfo2.png')



if __name__ == '__main__':
    main()