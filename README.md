# scraping

## scrap/spiders
クロール対象のサイトへのリクエスト、レスポンスのパース処理を記述。
どのようにサイトを辿って、ページの内容をどうパースするかのロジックを書く。
- spiderの作成
`scrapy genspider -t crawl {spider_name} {request_url}`
- spiderの実行
`scrapy crawl {spider_name}`

## scrap/items.py
スクレイピングで取得したデータを格納する入れ物。

## scrap/middlewares.py
リクエストとレスポンスに関連する追加の処理を拡張するためにロジックを記述する場所。
①SpiderMiddleware : webサイトへのリクエストやレスポンスに関連する処理を拡張
②DownloaderMiddleware : webサイトからページのダウンロードに関連する処理を拡張

## scrap/piplines.py
webサイトから取得したデータのクレンジング、チェック、DBへの更新などの処理を記述

## scrap/settings.py
パラメーターで各種設定を行うためのファイル