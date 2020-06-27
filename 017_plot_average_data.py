import re
import numpy as np
import statistics
from matplotlib.pyplot import figure
import matplotlib.pyplot as plt

path = "test.csv"

check_code = re.compile("[0-9]{4}/[0-9]{2}/[0-9]{2}")

data_a = np.arange(0)
data_b = np.arange(0)
data_c = np.arange(0)
counter = 0

data_start = ""
data_end = ""

# 中央値の取得
z1_mid = []
z2_mid = []

with open(path) as f:
    for temp_line in f:
        # 日付のあるデータのみ抽出する
        if re.match(check_code, temp_line) is not None:
            temp_z1 = float(temp_line.split(",")[2])
            temp_z2 = float(temp_line.split(",")[3])

            # Z1の中央値を取得する
            if temp_z1 < 5 and z1_mid == []:
                z1_mid = [temp_z1]
            elif temp_z1 < 5 and z1_mid != []:
                z1_mid.append(temp_z1)
            elif temp_z1 > 5 and z1_mid != []:
                # Z1データの中央値をnumpy配列の代入
                data_a = np.append(data_a, statistics.median(z1_mid))
                z1_mid = []

            # Z2の中央値を取得する
            if temp_z2 < 5 and z2_mid == []:
                z2_mid = [temp_z2]
            elif temp_z2 < 5 and z2_mid != []:
                z2_mid.append(temp_z2)
            elif temp_z2 > 5 and z2_mid != []:
                # Z1データの中央値をnumpy配列の代入
                data_b = np.append(data_b, statistics.median(z2_mid))
                z2_mid = []

            # 開始時間を取得
            if data_start == "":
                data_start = temp_line.split(",")[0]
            # 終了時間を取得
            data_end = temp_line.split(",")[0]

data_ax = np.arange(1, data_a.shape[0]+1)
data_bx = np.arange(1, data_b.shape[0]+1)


print(data_a.shape[0])
print(data_b.shape[0])


np.savetxt("sample.csv", np.array([data_a, data_b]), fmt="%.4f", delimiter=",")

# Figureオブジェクトを作成
# ウインドウサイズを指定(横×縦)
fig = figure(figsize=(8, 4))
# 描画タイトルを表示
fig.suptitle(data_start+" -> "+data_end, fontweight="bold")

# figに属するAxesオブジェクトを作成
ax = fig.add_subplot(1, 1, 1)


ax.plot(data_ax, data_a)
ax.plot(data_bx, data_b)

# 凡例を表示
ax.legend(["Z1", "Z2"], loc="best", fontsize=8)
# grid表示ON
ax.grid(True)
# x範囲
ax.set_xlim(left=1)
# y範囲
ax.set_ylim(bottom=-1, top=2)
# X軸のラベル
ax.set_xlabel("count number")
# Y軸のラベル
ax.set_ylabel("[mm]")
# 表示指示
plt.show()
