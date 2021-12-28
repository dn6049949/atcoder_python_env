# atcoder_python_env

Python で AtCoder をやるときに便利な諸々を用意したやつ
- [コンテスト用フォルダの作成](#コンテスト用フォルダの作成)
- [セットアップ](#セットアップ)
- [自動テスト](#自動テスト)
- [自動提出](#自動提出)


## 必要なモジュールのインストール

[online-judge-tools](https://github.com/online-judge-tools/oj) と [atcoder-cli](https://github.com/Tatamo/atcoder-cli) を使います

```
$ pip3 install -r requirements.txt
$ npm install -g atcoder-cli
```


## コンテスト用フォルダの作成

例えば下記コマンドで `abc/abc100` フォルダが作成されます

```
$ python3 build_contest_env.py abc/abc100
```

階層は以下のようになります
```
.
├── abc
│   └── abc100
│       ├── a.py
│       ├── b.py
│       ├── c.py
│       ├── d.py
│       ├── e.py
│       ├── f.py
│       ├── g.py
│       ├── h.py
│       ├── judge.py
│       ├── setup.py
│       └── submit.py
├── temp
│   ├── judge.py
│   ├── setup.py
│   ├── submit.py
│   └── temp.py
├── .gitignore
├── README.md
├── build_contest_env.py
└── requirements.txt
```

`a.py` ~ `h.py` がそれぞれの問題を解くためのファイルで、 `temp/temp.py` の内容をコピーしたものです。なので自分のテンプレファイルを使いたい場合は `temp/temp.py` を変更してください

なお、フォルダ名は自由で大丈夫ですが、セットアップの際にフォルダのパスの末尾をデフォルトのコンテストIDとして認識するように設定してあるので末尾はコンテストIDにしておくと便利です
- コンテストID: AtCoder のコンテストのトップページのURLの末尾
  - 例： ABC100(https://atcoder.jp/contests/abc100) のコンテストIDはabc100

オプションがいくつかあるので詳しくは下記コマンドによりヘルプを参照してください

```
$ python3 build_contest_env.py -h
```


## セットアップ

セットアップでは全問題のサンプルケースのダウンロードと自動テスト・自動提出のための設定を行います

自動テストと自動提出を行う前に必ず実行してください

上記で作成したディレクトリに移動します

```
$ cd abc/abc100
```

下記コマンドによりセットアップを行います

```
$ python3 setup.py -c abc100
```

`-c` オプションによりコンテストIDを指定します

なおデフォルトではカレントディレクトリの末尾をコンテストIDと認識するようになっているので、今回の例では下記コマンドでも大丈夫です

```
$ python3 setup.py
```

初回実行時は自動テスト・自動提出のために online-judge-tools と atcoder-cli のそれぞれから AtCoder にログインするため2回続けてログインを要求します

2回目の実行以降はログインなしで実行可能です


## 自動テスト

`abc/abc100` ディレクトリにおいて、例えば下記コマンドにより A 問題のサンプルケースを自動でテストします

```
$ python3 judge.py a
```

`-s` オプションをつけて実行するとサンプルが全て一致していたら自動で提出も行います

```
$ python3 judge.py a -s
```

他にもオプションがいくつかあるので詳しくは下記コマンドによりヘルプを参照してください

```
$ python3 judge.py -h
```


## 自動提出

`abc/abc100` ディレクトリにおいて、例えば下記コマンドにより A 問題に自動で提出します

```
$ python3 submit.py a
```

`-l` オプションにより pypy で提出するか python で提出するか選べます、デフォルトは pypy です

```
$ python3 submit.py a -l python
```

詳しくは下記コマンドによりヘルプを参照してください

```
$ python3 submit.py -h
```
