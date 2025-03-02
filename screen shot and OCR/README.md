# 螢幕截圖與OCR

在網路上查資料的時候，很常遇到鎖複製文字、或者要從影片截文本的需求  
通常我會使用螢幕截圖再丟到google翻譯，透過顯示原文來取得文字文本  
這次想說寫個程式把這個流程做起來。

# 初步構想

在使用者使用 Win + Shift + S Windows 螢幕截圖時，自動執行程式監聽剪貼簿，  
當剪貼簿20秒以內有做更改時，詢問是否要進行OCR，  
若是則開啟pytesseract進行文字產生，並將文字存入剪貼簿，  
若20以內沒有更改剪貼簿，則自動關閉程式。  

# 環境建置

### **安裝 Tesseract OCR**

1. `pip install pytesseract`不會自動安裝OCR相關內容，仍然需要手動安裝

2. 下載並安裝 Tesseract：
    
    - 下載 Tesseract 安裝程式：[Tesseract OCR 官方 GitHub 頁面](https://github.com/tesseract-ocr/tesseract)
    - 或從這裡下載安裝檔案：[Tesseract 下載頁面](https://github.com/UB-Mannheim/tesseract/wiki) (Windows)

2. 安裝過程中，記得選擇將 `tesseract.exe` 添加到系統的 **PATH 環境變數**，這樣 `pytesseract` 就可以直接找到它。
	1. 路徑（通常是 `C:\Program Files\Tesseract-OCR\tesseract.exe`）
	2. 開啟使用者環境變數，在Path變數新增`C:\Program Files\Tesseract-OCR`，確定後並重啟電腦，這樣cmd才找得到環境變數
	  
3. 確認 Tesseract 安裝成功：
    
    - 打開命令提示字元 (cmd)，輸入：
        ```cmd
        tesseract --version
		```
    如果顯示 Tesseract 的版本號，則表示安裝成功。

### **Python 虛擬環境依賴庫安裝**

```anaconda prompt
pip install pyperclip
pip install pytesseract
```

### **Python 程式打包成 Windows 可執行檔**

1. 步驟 1: 安裝 `pyinstaller`
	1. 首先，安裝 `pyinstaller`，這是一個可以將 Python 程式打包成執行檔的工具。
 	2. 在虛擬環境中執行以下命令：
		`pip install pyinstaller`

2. 將.ipynb轉成.py，或者直接開一個.py把內容摳過去 
	`jupyter nbconvert --to script my_script.ipynb`
3. 打包
	`pyinstaller --onefile --windowed my_script.py`

### **語言擴充**

可以前往[Tesseract 的 GitHub 頁面](https://github.com/tesseract-ocr/tessdata)下載所需的語言檔案。如果沒有安裝，可以手動下載並放置在 tessdata 目錄下。

# 遇到的困難與解決(歷程記錄)

## 初步架構
[screenshot_debug.ipynb](data\screenshot_bebug.ipynb)

實現了基本的內容，當執行時開始監測圖像剪貼簿的內容，  
當內容進行變化時，觸發OCR，並將處理完的文本丟回剪貼簿。  

後續想法是串接快捷鍵，當快捷鍵事件觸發時自動執行打包的.exe檔案  
這樣才不需要一直在背景監聽  

## 監聽問題
嘗試了兩個方法但結果不盡人意，為了一個截圖功能一直開著監聽器似乎也不太合邏輯   
1. Windows 工作排程器：它似乎沒有單純監聽按鍵的觸發事件  
2. AutoHotKey ：使用小程式完成監聽，但我原本的設想是在 Win + Shift + S 觸發時使用，但AHK認為這個是不合理的觸發按鍵組合(猜測是Windows占用)  

## 結果
重新反思我需要的結果，其實只是在截圖後需要一個OCR的按鍵而已，   
這個主動使用OCR的工作可以把它綁在工具列上，我自己按就好。  
所以改變了設計想法，只需要做成一個將剪貼簿圖片OCR後轉存至剪貼簿文本就好  

[ocr_windows_bebug.ipynb](data/ocr_windows_bebug.ipynb) 實現了這個功能  
## 優化
使用提示框導致確認按鍵變多了，不太符合一個簡化的小程式設計，  
因此決定將訊息方式改成使用WIN 10/11的側欄通知，  
[ocr_toast_debug.ipynb](data/ocr_toast_debug.ipynb) 進行了改進  

## 後續討論
Tesseract 在繁中處理上效果不太好，但考慮到離線可用，就先將就一下。  
程式本身是按照預設路徑去找 Tesseract ，如果電腦本身沒有安裝或改路徑，.exe應該是沒辦法運行

## 打包問題
在打包後使用.exe後，遇到了與[這一篇討論](https://stackoverflow.com/questions/50758709/the-win10toast-distribution-was-not-found-is-displayed-while-i-execute-a-python)同樣的問題，  
```
toaster.show_toast(title, text, duration=10)  # 顯示通知，持續 10 秒
```
這一行的指令雖然運行上沒有問題，但當轉到執行檔時它會因為ICO圖檔的path設定而出錯，改成如下  
```
toaster.show_toast(title, text, icon_path="OCR_ICON.ico", duration=10)  # 顯示通知，持續 10 秒
```
存在了icon_path再去打包錯誤消失
當然icon要自己弄一個把它包一起 
最後我的打包指令如下
```
pyinstaller --onefile --icon=OCR_ICON.ico --windowed --add-data "OCR_ICON.ico;." ocr_toast.py
```




