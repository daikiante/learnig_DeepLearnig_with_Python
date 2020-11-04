import numpy as np
import matplotlib.pyplot as plt

# matplotlibはグラフ描画のためのライブラリ


"""sin関数を描画する"""

# データの作成

# 0から6まで0.1刻みで生成
x = np.arange(0, 6, 0.1)
y = np.sin(x)

# グラフの描画
plt.plot(x, y)
plt.show()