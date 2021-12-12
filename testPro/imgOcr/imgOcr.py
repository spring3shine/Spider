import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'D:\myApps\Tesseract-OCR\tesseract.exe'

def img_ocr(img_path):
    pic = Image.open(img_path)

    # 模式L”为灰色图像，它的每个像素用8个bit表示，0表示黑，255表示白，其他数字表示不同的灰度。
    pic_gray = pic.convert('L')

    while True:

        # 设定阈值
        threshold = 200
        threshold = input("请输入0-255的整数，作为二值化的阈值，输入'-1'结束\n")
        threshold = int(threshold)
        if threshold == -1:
            break

        table = []
        for i in range(256):
            if i < threshold:
                table.append(1)
            else:
                table.append(0)
        # 图片二值化
        photo = pic_gray.point(table, '1')
        photo.show()

        # 解析图片，lang='chi_sim'表示识别简体中文，默认为English
        # 如果是只识别数字，可再加上参数config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789'
        content = pytesseract.image_to_string(photo, lang='chi_sim', config='--psm 7 --oem 3 -c tessedit_char_whitelist=0123456789')
        print(content)
        photo.save('二值化结果.png')



    # 解析图片，lang='chi_sim'表示识别简体中文，默认为English
    # 如果是只识别数字，可再加上参数config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789'
    content = pytesseract.image_to_string(photo, lang='chi_sim', config='--psm 0 --oem 3 -c tessedit_char_whitelist=0123456789')
    print(content)


if __name__ == '__main__':
    # img_ocr("7364.png")
    # img_ocr("2710386495.png")
    img_ocr("auc3.png")
    # img_ocr("2710386495屏幕截图.png")
    # img_ocr("知乎截图.png")
    # img_ocr("静夜思.png")
