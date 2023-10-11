import discord
import os
from dotenv import load_dotenv
import sys

if not os.path.exists('.env'):
    with open('.env', 'w') as env_file:
        env_file.write('# ここに環境変数を設定\nDISCORD_TOKEN=')
    print('環境変数ファイルを作成しました。必要な情報を入力してください')
    sys.exit(1)


load_dotenv()


