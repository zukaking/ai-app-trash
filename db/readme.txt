DB作成方法

1. docker上にpostgresを構築
    https://zenn.dev/re24_1986/articles/b76c3fd8f76aec

2. EC2上に.csvを作成

3. postgres環境に.csvをコピー
    docker cp trash_result.csv {CONTAINER ID}:/var

3. DBに接続
    docker exec -it postgres /bin/sh
    psql -h localhost -U postgres

4. .csvからDBを作成
    CREATE TABLE trash_result (predict_label varchar NOT NULL, result varchar NOT NULL, PRIMARY KEY (predict_label));
    \copy trash_result from '/var/trash_result.csv' with csv;

5. 作成したDB確認
    select * from trash_result;
