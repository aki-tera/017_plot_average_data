import re
import numpy as np
import statistics
from matplotlib.pyplot import figure
import matplotlib.pyplot as plt

import os
import glob

# 日本語フォント設定
from matplotlib import rc
jp_font = "Yu Gothic"
rc('font', family=jp_font)


class Gl220DataExtractor:
    def __init__(self, filename):
        # ファイル名
        self.filename = filename
        self.save_filename = "resutl_" + filename
        # データ取得用
        self.data_a = np.arange(0)
        self.data_b = np.arange(0)
        self.data_c = np.arange(0)
        # データの日付取得用
        self.data_start = ""
        self.data_end = ""

    def median_data(self):
        # 日付のチェック用
        check_code = re.compile(
            "[ 0-9]*,*[0-9]{4}/[0-9]{1,2}/[0-9]{1,2}")
        # 中央値の取得
        z1_mid = []
        z2_mid = []
        # ファイルからデータを取得する
        with open(self.filename) as f:
            for temp_line in f:
                # 日付のあるデータのみ抽出する
                if re.match(check_code, temp_line) is not None:
                    # 文字の場合、非数（nan）にして処理を続ける
                    try:
                        temp_z1 = float(temp_line.split(",")[3])
                    except ValueError:
                        temp_z1 = np.nan
                    try:
                        temp_z2 = float(temp_line.split(",")[4])
                    except ValueError:
                        temp_z2 = np.nan
   
                    # Z1の中央値を取得する
                    # -2より大きい数値の中央値とする
                    if -3 < temp_z1 < 10 and z1_mid == []:
                        z1_mid = [temp_z1]
                    elif -3 < temp_z1 < 10 and z1_mid != []:
                        z1_mid.append(temp_z1)
                    elif not(-3 < temp_z1 < 10) and z1_mid != []:
                        # Z1データの中央値をnumpy配列の代入
                        self.data_a = np.append(
                            self.data_a, statistics.median(z1_mid))
                        z1_mid = []

                    # Z2の中央値を取得する
                    if -3 < temp_z2 < 10 and z2_mid == []:
                        z2_mid = [temp_z2]
                    elif -3 < temp_z2 < 10 and z2_mid != []:
                        z2_mid.append(temp_z2)
                    elif not(-3 < temp_z2 < 10) and z2_mid != []:
                        # Z1データの中央値をnumpy配列の代入
                        self.data_b = np.append(
                            self.data_b, statistics.median(z2_mid))
                        z2_mid = []

                    # 開始時間を取得
                    if self.data_start == "":
                        self.data_start = temp_line.split(",")[1]
                        # 終了時間を取得
                        # 終わりが分からないので常時記録する
                        self.data_end = temp_line.split(",")[1]
        # データ数を取得する
        temp_ax = self.data_a.shape[0] + 1
        temp_bx = self.data_b.shape[0] + 1
        self.data_ax = np.arange(1, temp_ax)
        self.data_bx = np.arange(1, temp_bx)
      
        # 両者のデータが同じかどうかを確認する
        if temp_ax == temp_bx:
            if (os.path.exists(self.save_filename) is True):
                self.save_filename = "結果のファイルはすでにあります"
                return(False)
            else:
                return(True)
        else:
            self.save_filename = "Z1とZ2は、結果の数が異なるのでファイルは作成しません"
            return(False)

    def formatter_data(self):
        # 転置して出力するように変更
        np.savetxt(self.save_filename, np.array(
            [self.data_a, self.data_b]).T, fmt="%.4f", delimiter=",")

    def plot_data(self):
        # Figureオブジェクトを作成
        # ウインドウサイズを指定(横×縦)
        fig = figure(figsize=(8, 6))
        # 描画タイトルを表示
        fig.suptitle(
            self.save_filename +
            "\n" +
            self.data_start +
            " -> " +
            self.data_end,
            fontweight="bold")
        # figに属するAxesオブジェクトを作成
        ax = fig.add_subplot(1, 1, 1)
        # 散布図をプロット
        # sはプロットする点の大きさ
        ax.scatter(self.data_ax, self.data_a, s=5)
        ax.scatter(self.data_bx, self.data_b, s=5)
        # 凡例を表示
        ax.legend(["Z1", "Z2"], loc="best", fontsize=8)
        # grid表示ON
        ax.grid(True)
        # x範囲
        ax.set_xlim(left=1)
        # y範囲
        ax.set_ylim(bottom=-2, top=2)
        # X軸のラベル
        ax.set_xlabel("count number")
        # Y軸のラベル
        ax.set_ylabel("[mm]")


def main():
    filename = glob.glob("*.csv")
    for row in filename:
        if row[:7] == "resutl_":
            pass
        else:
            d = Gl220DataExtractor(row)
            if d.median_data() is True:
                d.formatter_data()
            else:
                print("結果ファイルが存在する、もしくは両者のデータが異なるで"
                      "ファイル保存は行いません")
            d.plot_data()

    # plt.show()


if __name__ == "__main__":
    main()
