import pytesseract
from PIL import ImageGrab
import pyperclip
from win10toast import ToastNotifier
import time

# 設定 Tesseract OCR 路徑，請確認路徑正確
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def notify(title, text):
    """ 顯示側邊欄通知 """
    toaster = ToastNotifier()
    toaster.show_toast(title, text, icon_path="OCR_ICON.ico", duration=10)  # 顯示通知，持續 10 秒

def get_image_from_clipboard():
    """ 從剪貼簿中獲取圖片 """
    image = ImageGrab.grabclipboard()
    return image

def perform_ocr_on_image(image):
    """ 對圖片進行 OCR 辨識 """
    text = pytesseract.image_to_string(image, lang="chi_tra+eng")  # 可根據需要調整語言
    return text

def copy_text_to_clipboard(text):
    """ 將辨識出的文字複製到剪貼簿 """
    pyperclip.copy(text)

def main():
    """ 主程序邏輯 """
    print("開始處理剪貼簿中的圖片...")
    image = get_image_from_clipboard()

    if image is None:
        notify("錯誤", "剪貼簿中未發現圖片！")
        print("未發現圖片")
        return

    print("圖片獲取成功，開始進行 OCR 辨識...")
    text = perform_ocr_on_image(image)

    if text.strip():  # 檢查是否有辨識到文字
        print(f"OCR 辨識結果:\n{text}")
        copy_text_to_clipboard(text)  # 將文字複製到剪貼簿
        notify("OCR 完成", "已將辨識內容儲存至剪貼簿！")
    else:
        notify("OCR 失敗", "未能辨識出任何文字，請重試。")
        print("未能辨識出任何文字")

if __name__ == "__main__":
    main()