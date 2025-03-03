# 我獨自升級練等系統

# 發想
最近陪我妹看了幾集，發現劇情裡有它的每日訓練菜單  
就拿它做了個練等框架，希望自己可以努力運動(期許的部分)


# 架構與用法
整個程式主體是用在Obsidian上的可視化框架  
圖形視覺化主要靠Dataviewjs實現  
配合第三方外掛Dataview 跟 Contribution Graph(只有熱力圖)的部分  
從Obsidian下看會有以下幾個區塊  

![image](https://github.com/user-attachments/assets/f0b66683-dbda-42b3-b0ce-0aba213d3531)  
使用yaml屬性抓取數值  
show+"鍵名稱"的核取選向會抓取目的資料夾裡存在項目的鍵值，自動產生折線給累積圖  
這四個運動項目則是來自於獨自升級裡的設定，但要一般人每天跑10km太唬爛了我先5k就好  
使用者可以自己調整標準  


![image](https://github.com/user-attachments/assets/ac7f2756-6204-4b72-b0a4-8de96cf9dd04)  
熱力圖是按照第三方插件值接搬的，偵測的是日誌資料夾的檔案創建時間  
所以如果是每天創建檔案的話可以達到打卡的效果  
其實沒有辦法熱力(因為算的是檔案數而不是鍵值  
但如果是補打卡，由於建檔時間跟實際命名日期不一樣所以也沒有用  

![image](https://github.com/user-attachments/assets/a71c935c-0074-4369-8213-0b68500e6e47)  
等級區域，一個隨著你完成每日任務逐漸升級的框架  
每完成一個任務25EXP，一天總共可得100EXP  
每個等級需要EXP隨著等級線性提升  

懲罰：如果沒有完成所有每日，則扣除目前等級所需經驗的50%，有可能掉級  
但因為是偵測每份文件，所以偷懶連日記建檔都沒有的話就會沒事  

![image](https://github.com/user-attachments/assets/eab3c713-041d-4188-997d-6eb9f37c351d)  
各項目折線則是各個運動項目的統計圖表，  
如果擺爛導致等級掉光，至少還有一個數據可以安慰自己  


![image](https://github.com/user-attachments/assets/22f102e6-b1ff-49e5-b608-eb26137c1885)  
最後則是採計檔案的統計清單  
Created on 實際上是來自檔案名稱而不是建檔時間  


# 問題
等級折線圖的檔案有時候排序會亂掉，嘗試排序(使用日期或檔名)都小失敗  
目前還找不到原因  

