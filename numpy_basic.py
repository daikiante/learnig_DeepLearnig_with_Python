import numpy as np

"""Numpyの配列生成"""
x = np.array([1.0, 2.0, 3.0])
print(x)
print(type(x))


"""Numpyの算術計算"""
y = np.array([2.0, 4.0, 6.0])

print('x + y :', x + y)
print('x - y :', x - y)
print('x * y :', x * y)
print('x / y :', x / y)


"""NumpyのN次元配列"""

# Numpyは、1次元の配列(1列に並んだ配列)だけでなく、多次元配列も作成することができる。
A = np.array([[1, 2], [3, 4]])
B = np.array([[3, 0], [0, 6]])

print(A)

# 行列Aの形状
print('A.shape', A.shape)

# 行列Aの要素のデータ型
print('A.dtype', A.dtype)

print('A + B :', A + B)
print('A * B :', A * B)

# 行列に対してスカラ値(単一の数値)で算術を行うことも可能
print('A * 10 :', A * 10)



"""ブロードキャスト"""

A = np.array([[1, 2], [3, 4]])
B = np.array([10, 20])

# 形状の異なる配列同士も計算可能(これをブロードキャストと呼ぶ)
print('A * B : ', A * B)



"""要素へのアクセス"""

X = np.array([[51, 55], [14, 19], [0, 4]])

print('X : ', X)

print('X[0] : ', X[0])

print('X[0][1] : ', X[0][1])


# for文も使える
for row in X:
    print('row : ', row)


# Xを1次元配列へ変換
X = X.flatten()
print('X.flatten() : ', X)

# インデックスが0, 2, 4番目の要素を取得
print('X[np.array([0, 2, 4])] : ', X[np.array([0, 2, 4])])


# Xから15以上の値だけを抜き出す(Boolean)
print('X > 15 : ', X > 15)

# Xから15以上の値だけを抜き出す(Int)
print('X[X>15] : ', X[X>15])