# PluginDocAI

llama.cpp を利用して プラグインの説明を連続で生成する

プラグインの名前と説明が書かれたjsonを作成する

```sh
python3 getPluginDoc.py
```

プラグインの名前と説明が書かれたjsonからMarkdownを生成する

```sh
python3 toMarkdown.py
```

初期設定では resultディレクトリに json と md ファイルが生成されます。

config.pyでGGUFファイルのパス などを設定できます。
