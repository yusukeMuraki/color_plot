# color-plot

## インストール

`pip install color-plot`

## データの準備

用意するもの
- 町丁目shapeファイル
- 表示する統計データ

#### 町丁目shapeファイル

[こちら](https://www.e-stat.go.jp/gis/statmap-search?page=1&type=2&aggregateUnitForBoundary=A&toukeiCode=00200521&toukeiYear=2015&serveyId=A002005212015&coordsys=1&format=shape)から目的の区域のシェイプファイルをダウンロード

#### 統計データ
以下の形でデータを用意(.csv or .xlsx)

(※必須)`町丁目名`
| 町丁目名 | データ1 | データ2・・・ |
|:-----------|------------|:------------|
| 本町一丁目       | 23       | 3         |
| 本町二丁目   | 45      | 2       |
|  三月町      | 12        | 1         |
|    立花町     | 33          | 4           |



## サンプルコード

```
import color_plot

shape_file_name = '/path/to/file/data.shp'
data_file_name = '/path/to/file/data.xlsx'
column = 'データ1' # plotするデータのカラム名

color_plot.color_plot(shape_file_name, data_file_name, column)
```