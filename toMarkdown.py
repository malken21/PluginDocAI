import util

FILE_JSON = "PluginDoc.json"

FILE_MD = "result/PluginDoc.md"


# json 読み込み
PL_DOC = util.readJSON(FILE_JSON)
print(f"Load : {FILE_JSON}")

# Markdow 作成
MarkdowList = ["# プラグインの説明"]
for pl, doc in PL_DOC.items():
    print(f"OK : {pl}")
    MarkdowList.extend(["", f"## {pl}", "", doc])
MarkdowList.append("")
Markdow = "\n".join(MarkdowList)

# md 保存
util.save(FILE_MD, Markdow)
print(f"Create : {FILE_MD}")

# Enter が押されるまでここで待機
input("Enterを押して終了")
