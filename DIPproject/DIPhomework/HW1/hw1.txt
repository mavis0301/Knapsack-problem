B083040031邱歆惠

python版本:3.8.10
ubuntu :20.04

open()/save():開啟/儲存檔案

底下四排參數:
	1.(1)做linearly : y=ax+b
	  (2)做exponentially : e^(ax+b)  ，a要小不然很容易超過255(全白)
	  (3)做logarithmically : ln(ax+b) ,ln裡面數字再大都還是很小(全黑)
		，所以我改成ln((ax+b)/255)*255，使裡面數字再小也能看得到圖
	2.放大縮小:
		使用f (x ', y') = λ(µ f (x + 1, y + 1) + (1− µ)f (x + 1, y))
		+ (1− λ)(µ f (x, y + 1) + (1− µ)f (x, y))
		，先抓到四個角的點，再用Bilinear interpolation算出真正點的灰階值
	3.rotate:
		先製作旋轉矩陣，再將原圖array乘旋轉矩陣
	4.gray level:
		使用者選擇顯示灰階值的範圍，然後有分original 和 black 模式，
		original就是保留未選擇區域的灰階值，black就是將為選擇區域變黑色

確定鍵(confirm):
	點選後會執行以上四步驟，並顯示圖片
