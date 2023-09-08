from llama_cpp import Llama
import util

FILE_JSON = "PluginDoc.json"

# プラグイン一覧
PLUGINS = [
    "BKCommonLib", "Armor_stand", "ArmorStandEditor", "Auto_message", "BanPlayerSheet", "BlocksHub", "BungeeGuard", "ClockItemTimer", "ClockPlugin", "CommandPanels",
    "CoreProtect", "DiscordSRV", "Dispenser_FallingBlock", "DispenserActions", "dynmap", "Dynmap-WorldGuard", "Effect_GUI", "Essentials", "EssentialsChat", "EssentialsProtect"
    "EssentialsSpawn", "EssKillPotionBack", "GSit", "HideNametagCMD", "HolographicDisplays", "ImageOnMap", "InfinityDispense", "ItemDropCooldown", "Lift", "LuckPerms"
    "LunaChat", "Multiverse-Core", "MyPet", "PlaceholderAPI", "RealScoreboard", "Shopkeepers", "TeleportSpectator", "Tps_log", "Train_Carts", "Vault",
    "Vehicles", "ViaVersion", "Warn_KillPotion", "WorldBorder", "WorldEdit", "WorldEditSelectionVisualizer", "WorldGuard", "WorldGuardExtraFlags"
]

# GGUFファイルのパス
MODEL_PATH = "models/ggml-model-q4_m.gguf"

# システムメッセージ
system_message = "これから発言するMinecraftのプラグインの説明を書いて"


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
