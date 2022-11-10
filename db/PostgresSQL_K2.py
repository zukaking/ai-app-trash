import psycopg2

def main():
    ansLabel = "003_can"

    gomiRes = GetTrashResult(ansLabel)

    print('result = {}'.format(gomiRes))


def GetTrashResult(label):
    #接続
    connector =  psycopg2.connect('postgresql://{user}:{password}@{host}:{port}/{dbname}'.format( 
                user="postgres",        #ユーザ
                password="passw0rd",     #パスワード
                host="localhost",       #ホスト名
                port="5432",            #ポート
                dbname="plismdb"))    #データベース名

    #カーソル取得
    cursor = connector.cursor()

    cursor.execute("SELECT result FROM trash_result where predict_label = '{}'".format(label))
    res = cursor.fetchall()

    return res[0][0]


if __name__ == "__main__":
    main()
