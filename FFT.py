from google.colab import files 
x=files.upload()
##ここで実行を行いコードを追加する。パソコン内でファイルを参照する
uploaded_file_name = next(iter(x))
##ここで実行を行いコードを追加する。アップロードした画像をイテレータで要素を取得し値で保存
import cv2
import numpy as np
src = cv2.imread(uploaded_file_name,0)#grayscaleで読み込むためimreadの第二引数は0にする
f = np.fft.fft2(src)#フーリエ変換を行う
fshift = np.fft.fftshift(f)#原点シフト
fsrc = np.log(np.abs(fshift))#複素数なので絶対値にlogをつける
##ここで実行を行いコードを追加する
from matplotlib import pyplot as plt
plt.imshow(fsrc)
##ここで実行を行いプロットして終了
