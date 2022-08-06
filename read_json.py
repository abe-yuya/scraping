import json

with open('data/giita_trend_1d.json', encoding='utf-8') as f:
  qiita_data = json.load(f)
  # 辞書型でjsonファイル取得
  print(qiita_data[0])

  titles = qiita_data[0]['titles']

  urls = qiita_data[0]['urls']

for title, url in zip(titles, urls):
  # 記事タイトルとURLをペアで表示
  print(title, url)