import json
import pathlib
import os


def createPrompt(message: str, history: list[str], system_message: str):
    input_prompt = f"\n{system_message}\n"
    for interaction in history:
        input_prompt = input_prompt + "\nUSER: " + \
            str(interaction[0]) + "\nASSISTANT: " + str(interaction[1])
    input_prompt = input_prompt + "\nUSER: " + str(message) + "\nASSISTANT: "
    return input_prompt


def createCompletion(llm, prompt: str):
    return llm.create_completion(
        prompt,
        temperature=0.7,
        top_p=0.3,
        top_k=40,
        repeat_penalty=1.1,
        max_tokens=1024,
        stop=[
            "ASSISTANT:",
            "USER:",
            "SYSTEM:",
        ],
    )["choices"][0]["text"].strip()


# 書き込み
def save(path, data: str):
    dirname = os.path.dirname(os)
    pathlib.Path(dirname).mkdir(parents=True, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as file:
        file.write(data)


# 書き込み
def saveJSON(path, data):
    dirname = os.path.dirname(os)
    pathlib.Path(dirname).mkdir(parents=True, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


# 読み込み
def readJSON(path):
    with open(path, 'r', encoding="utf-8") as file:
        return json.load(file)
