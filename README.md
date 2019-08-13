# challenges for InterKosenCTF2019

## 規約

- 問題に関する情報は全て `challenges.yaml` に書く
  - 問題サーバのIPアドレス/FQDN名は`{{host}}`とすると取得できることになっている
- 各問題のディレクトリ名は`問題名.replace(' ', '_').lower()`
- サーバを必要とする問題はDocker化し、`docker-compose.yaml`を設置する
  - コンテナ内で使用するファイルは全て `challenge`以下に配置する（これには特に理由はないけど）
- 配布するファイルは全て `distfiles` に置く
  - あとで自動圧縮するので生のファイルを置いておけば良い
  - 自動圧縮されたくないファイルは`distarchive`に置く
- 解法を `solution` ディレクトリに置いておくと :+1:
  - 解けるかどうかを自動でチェックするために使う
  - `solve.bash` というファイルを置いておいて、実行するとフラグを含む文字列を出力するようにしておく
  - `distfiles`、`distarchive` 内のファイルは勝手にコピーされてくるのである体で書いて良い
  - `CHALLENGE_HOST` という環境変数に問題サーバのIPアドレス/FQDN名が格納されていることになっている
