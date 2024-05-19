
from PIL import Image
from PyPDF2 import PdfFileReader
from fpdf import FPDF

# import BytesIO


# ----- PIL Image ----- # 

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


# ----- pypdf2 ----- # 
def obtain_first_page(path: str):
    with open(path, "rb") as pdf_file:
        pdf_reader = PdfFileReader(pdf_file)
        pag_1 = pdf_reader.getPage(0)
    return pag_1



def pdf2png(path: str):
    pass


def generatePDF():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('helvetica', size=12)
    pdf.cell(text="hello world")

    pdf.ln(4)
    pdf.multi_cell(0, 5, text='aaaaaaaaaaaaaaaaaaaa')

    pdf.ln(4)
    pdf.image(fr'app\assets\svg\logo_ingenuity.svg',y = 60, w=30)

    pdf.output("hello_world.pdf")



def main():
    # path = fr'C:\dtertre59\Documents\3_PROGRAMACION\Python\image-converter\app\assets\userInfo.jpg'
    # img = image(path)
    # img2 = i_resize(img, 465, verbose= True)
    # i_size(img2, verbose=True)
    # i_save(img2, './app/assets/userInfo2.jpg')
    generatePDF()



if __name__ == '__main__':
    main()