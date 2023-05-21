import xml.etree.ElementTree as ET
import glob
import csv

# XMLファイル一覧取得
# 前提:同一階層のxmlsフォルダにxmlファイルを配置する
xmls = glob.glob('xmls/*.xml', recursive=True)

# 解析結果格納用リスト
cdata_list = []

# ファイルごとに解析する
for xml in xmls:
    # XMLファイルパース
    tree = ET.parse(xml)
    root = tree.getroot()
    print(root)
    for record in root:
        for child in record.iter():

            # 子要素の中身を解析
            if child.tag == 'Record':
                record_type = child.attrib['type']
                if record_type == 'HKQuantityTypeIdentifierHeartRate':
                    date = child.attrib['startDate']
                    value = child.attrib['value']

                    # 特定要素の抽出
                    if '2023-03-25' in date:
                        time = date[11:19]

                        #型、時刻、心拍数を出力
                        print(
                            f'{record_type}, {time}, {value}')
                        cdata = [time, value]
                        cdata_list.append(cdata)

# CSVファイルに保存
with open('result/cdata.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(cdata_list)