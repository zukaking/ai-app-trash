①フロントエンド、バックエンドの環境起動
docker-compose up -d

②コンテナに入る（node）
docker-compose exec node bash

③vueプロジェクトの生成
vue create ai-app-trash
-> vue3 / npmを選択

・サーバ立ち上げ確認
cd ai-app-trash
npm run serve


④axiosの追加
cd ai-app-trash
npm add axios

⑤TailwindCSS, DaisyUIの追加
npm install -D tailwindcss postcss autoprefixer
npm install daisyui
npx tailwindcss init -p

⑥node/ai-appフォルダから以下をコピー
cp -f ai-app/tailwind.config.js ai-app-trash/tailwind.config.js
cp -f ai-app/vue.config.js ai-app-trash/vue.config.js
cp -f ai-app/src/App.vue ai-app-trash/src/App.vue
cp -f ai-app/src/index.css ai-app-trash/src/index.css
cp -f ai-app/src/main.js ai-app-trash/src/main.js
cp -f ai-app/src/components/FileUp.vue ai-app-trash/src/components/FileUp.vue

⑦apiサーバのパスを必要に応じて書き換え
ai-app/src/components/FileUp.vue
の20行目

⑧デバッグ用のサーバ起動
npm run serve



