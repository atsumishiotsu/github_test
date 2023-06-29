
# 修正しまいた。
# 修正２
# 修正３
# 修正６
import os,csv

#ファイル参照
with open('select_jira_links.csv', encoding="utf_8") as f_1:
    reader = csv.reader(f_1)
    
    # CSVファイルをループで上から順番に参照してrowへセット
    for row in reader:
        # CSVファイルの行全体を配列（リスト）で表示
        print(row)

print("=========")

with open('select_jira_links.csv', encoding="utf_8") as f_2:
    reader = csv.reader(f_2)

    # CSVファイルをループで上から順番に参照してrowへセット
    for row in reader:
        # CSVファイルの行の6番目の項目（DOCUMNET_ID）を表示
        print(row[5])

print("=========")

with open('select_jira_links.csv', encoding="utf_8") as f_3:
    reader = csv.reader(f_3)

    # CSVファイルをループで上から順番に参照してrowへセット
    for row in reader:
        # CSVファイルの行の5番目の項目（ISSUE_KEY）と6番目の項目（DOCUMNET_ID）を表示
        print("issue key=" + row[4] + "   " + "document id=" + row[5])
