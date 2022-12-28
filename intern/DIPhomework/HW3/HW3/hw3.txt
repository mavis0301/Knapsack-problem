B083040031邱歆惠

python版本:3.8.10
ubuntu :20.04

GUI使用 :	主視窗是part1、part2、part3、part4的按鈕，可以分別跳出該題的視窗。
		part4中的第e題因為圖比較多，所以在part4視窗裡會多放一個前往第e題視窗的按鈕

part1 : 	原圖加4種smoothing sharping的圖片，mean filter會變模糊，7*7比3*3模糊；
		median filter會讓長條的短邊變圓弧狀，7*7比3*3圓弧。

part2 :	第a題的spectrum，用fourier transform轉換後取log，另外有乘上一個常數使圖片比較亮比較好觀察。
		第b題的兩張圖是取用magnitude-only image 和 phase-only image，分別將其作傅立葉逆轉換的圖。

part3 :	(1) 乘上(-1)^(x+y)會將座標x+y的pixel變負數，會使白色字上變黑白相間的點(看起來像灰色)
		(2) 做DFT，變頻域
		(3) 取共軛，改變虛數的正負，在虛實平面的角度改變
		(4) 做IDFT，變時域，圖片倒過來
		(5) 取實數去乘回(-1)^(x+y)

part4 :	(e)特別說明 : 	第一個row都是RGB，第一張原圖，後面兩個是smoothing(5*5 mean filter)和sharping(laplacian)，
					最右額外的兩圖分別是原圖跟smoothing比較，以及原圖跟sharping比較。
					第二個row是HSI，後面圖的做法都跟上面一樣，最後有轉成RGB的格式顯示出來。
					然後第三個row的兩張圖，是在看他們上面兩張的差異(RGB & HSI smoothing 和 RGB & HSI sharping)，
					
					

