"""
参考
PythonでPDFを画像ファイル（JPEG、PNG）に変換する方法
https://gammasoft.jp/blog/convert-pdf-to-image-by-python/

Install の方法
【Python】PDFと画像の相互変換
https://algorithm.joho.info/programming/python/pdf-image-py/

conda install pdf2image, poppler 
でconda-forgeからインストールできる

https://github.com/Belval/pdf2image

結論
参考1のプログラムをにしなくても関数一つで同じことができる。


"""

from pathlib import Path

from pdf2image import convert_from_path

def pdf_image(pdf_file,img_path, fmt='jpeg', dpi=200):
    """
    pdf_file: 
    img_path: output holder name
    example:
    pdf_file="./data/abcd.pdf", img_path='./image"
    またはPathでもよい。
    
    """
    #pdf_fileをPathにする
    pdf_path = Path(pdf_file)
    image_dir = Path(img_path)
    
    # PDF -> Image に変換
    pages = convert_from_path(pdf_path, dpi)
    
    # 画像ファイルを１ページずつ保存
    for i, page in enumerate(pages):
        file_name = "{}_{:02d}.{}".format(pdf_path.stem,i+1,fmt)
        image_path = image_dir / file_name
        page.save(image_path, fmt)

        
if __name__ == "__main__":
    # PDFファイルのパス
    pdf_path = Path("./data/pdf3009p.pdf")
    img_path=Path("./image")
    
    pdf_image(pdf_file=pdf_path,img_path=img_path, fmt='jpeg', dpi=200)
    # convert_from_path(pdf_path, output_folder=img_path,fmt='jpeg',
    #                   output_file=pdf_path.stem)
    