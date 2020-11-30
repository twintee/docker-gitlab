# docker-gitlab

## 🌏 検証環境

require
- ubuntu :18.* or later

## ⚙ 使用手順
1. .env設定スクリプト実行
    ```
    sudo python3 ./config.py
    ```
    - DOMAIN:  
        gitlabのバーチャルホストの識別用  
        (初期値exampleの場合、gitlab.example / registory.example / mattermost.exampleとなる)
    - PORT_EXTERNAL: gitlabの使用ポート
    - MEM: gitlabのメモリ使用量

1. gitlabイメージのビルド
    ```
    docker-compose build
    ```

1. コンテナ初期化スクリプト実行.
    ```
    sudo python3 ./init.py
    ```
