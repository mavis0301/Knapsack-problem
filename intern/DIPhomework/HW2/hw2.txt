B083040031邱歆惠

python版本:3.8.10
ubuntu :20.04

open()/save():開啟/儲存檔案

partA partB 分左右兩區塊

partA:
	1.auto level function (histogram()): 使用Histogram Equalization 盡量平均每個灰階的量(0~255)，
		會彈出histogram長條圖，左邊是原始，右邊是新的
	2.bit plane (bitPlane()): 輸入0~7顯示該plane，0是二進位中最右邊的bit
	3.smoothing (smoothmean())/sharpening(laplacian()) : 輸入整數以建立不同大小的filter，
	  smoothing是取filter平均，sharpening是用laplacian做邊緣偵測，再疊加原圖
partB:
	1.average mask (partBavg()) : 同partA smoothing，使用3*3 mask
	  	a,b兩圖做出來其實長得有點像，可能是因為兩圖雜訊顏色都有差異，所以取平均沒辦法直接取到最正確的顏色，會有點偏差
	2.median filter (partBmed()) : 使用3*3 filter，取中位數
		a圖做得比b圖還要好，猜測可能是因為a圖的雜訊比b圖還要再分散一點，所以用3*3filter的話，比較容易選到與附近多數相似的顏色。
	3.laplacian (partBlap()) : 選用median filter做出來的圖，再用laplacian做邊緣偵測
		a圖因為整體圖已經變平滑，所以比較容易找出邊緣，不會像b圖一樣因為還有雜訊導致邊緣偵測時連同雜訊也偵測到了