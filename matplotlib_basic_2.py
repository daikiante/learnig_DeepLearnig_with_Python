import numpy as np
import matplotlib.pyplot as plt

"""
【pyplotの機能】
sin関数 / cos関数 / タイトルやラベル
"""

# 0から6まで0.1刻みで表示
x = np.arange(0, 6, 0.1)

y1 = np.sin(x)
y2 = np.cos(x)

# グラフの描画
plt.plot(x, y1, label='sin')

# 破線で描画
plt.plot(x, y2, linestyle='--', label='cos')

# x軸とy軸のラベル
plt.xlabel('x')
plt.ylabel('y')

# タイトル
plt.title('sin & cos')

plt.legend()

plt.show()