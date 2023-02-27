import psycopg2
#ゴミのIDをデータベースから取得(shiono)
def get_trashid(labels : list[str]):

    clss = []
    for label in labels:

        #接続
        connector =  psycopg2.connect('postgresql://{user}:{password}@{host}:{port}/{dbname}'.format(
                    user="postgres",        #ユーザ
                    password="passw0rd",     #パスワード
                    host="3.112.213.50",       #ホスト名
                    port="5432",            #ポート
                    dbname="plismdb"))    #データベース名

        #カーソル取得
        cursor = connector.cursor()

        cursor.execute("SELECT result FROM trash_result where predict_label = '{}'".format(label))
        res = cursor.fetchall()

        if len(res) > 0 and len(res[0]) > 0:
            clss.append(res[0][0])
        else:
            clss.append("other")

    return clss