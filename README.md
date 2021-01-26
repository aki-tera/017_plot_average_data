# 017_plot_average_data
![](https://img.shields.io/badge/type-python3-brightgreen)  ![](https://img.shields.io/badge/windows%20build-passing-brightgreen) ![](https://img.shields.io/badge/license-MIT-brightgreen) 

## DEMO
**Output Data  <-**  
<img src="https://user-images.githubusercontent.com/44888139/105790143-14fa2300-5fc7-11eb-821f-5e803d164bfe.png" width="400px">  
**INPUT Data  ->**   
<img src="https://user-images.githubusercontent.com/44888139/105789589-0fe8a400-5fc6-11eb-83bb-00fda47ff499.png" width="750px">  
  
## Features
You can create graphs and result's csv files from original csv files.

### specification
- You get the median of each from the ranges which you want for each period.
- You can change the settings according to the logger type in original csv files.
### original csv files
- You should assume file(s) which output from a logger.
- The files must contain the date(yyyy/mm/dd), data1, data2.
- The data must have stable data for a certain period.
### output data
- You can get the results which are csv files and graphs.

## Requirement 
Python 3
 - I ran this program with the following execution environment.
   - Python 3.8
   - Windows 10

Python Library
  - re
  - numpy
  - statistics
  - matplotlib
  - glob
  - os

## Usage
1. You place the csv files in the same folder as this program.
1. Run this program.
1. Display graphs plotting the median.
1. And then generate result's csv files.  
   But it will not be generated if results already exists.
## Note
Nothing in particular

## License
This program is under MIT license.
# 【日本語】


## 機能
元のcsvファイルからグラフとcsvファイルを作成する
- 仕様
  - 一定の値を取る部分から中央値を取得する
  - 元のcsvファイルに記載されているロガー型式で設定を変更する
- 元のcsvファイル
  - ロガーから出力されたファイルを想定
  - フォーマットは日付、データ1、データ2があるもの
  - 一定期間の安定した領域があるデータであること
- 出力する内容
  - 中央値をまとめてcsvファイルに出力（画像、csvファイル）する

## 必要なもの
Python 3
- このプログラムは、Python 3.8とWindows10で動作確認しています。

## 使い方
1. 本プログラムと同じフォルダにcsvファイル（複数可能）を置きます。
1. 本プログラムを実行します。
1. 中央値をプロットしたグラフが表示されます。
1. 同時に、result_が先頭に付いたcsvファイルが生成されます。  
   但し、すでにファイルがあれば生成されません


## 備考
特に無し

## ライセンス
本プログラムは、MITライセンスです。
