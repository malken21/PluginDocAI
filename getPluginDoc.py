from llama_cpp import Llama
import util
from config import FILE_JSON, MODEL_PATH, PLUGINS, system_message


# LLMの準備
llm = Llama(MODEL_PATH, n_gpu_layers=40, n_ctx=2048)


# 文字生成
def generate_text(message: str, history: list[str]):
    prompt = util.createPrompt(message, history, system_message)
    text = util.createCompletion(llm, prompt)
    history.append([message, text])
    return {"text": text, "history": history}


PluginDoc = {}
for pl in PLUGINS:
    # 文字生成
    text = generate_text(pl, [])["text"]
    print(pl)
    print(text)
    PluginDoc[pl] = text

# json 保存
util.saveJSON(FILE_JSON, PluginDoc)
