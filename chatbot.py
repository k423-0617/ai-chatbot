# -*- coding: utf-8 -*-
"""
AI 聊天机器人
调用 DeepSeek API 实现多轮对话
"""

import os
import requests
import json

# ============ 配置文件路径 ============
CONFIG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json")

def load_config():
    """加载配置，如果没有则提示用户输入"""
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)

    # 第一次运行，询问密钥
    print("=" * 50)
    print("  首次运行，请配置 DeepSeek API 密钥")
    print("  密钥获取地址：https://platform.deepseek.com/api_keys")
    print("=" * 50)
    api_key = input("\n请输入你的 DeepSeek API 密钥: ").strip()

    config = {"api_key": api_key}
    with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
        json.dump(config, f, ensure_ascii=False, indent=2)

    print("密钥已保存！下次运行无需重新输入。\n")
    return config

# ============ 加载配置 ============
config = load_config()
API_KEY = config["api_key"]
BASE_URL = "https://api.deepseek.com/v1/chat/completions"
MODEL = "deepseek-chat"

# ============ 对话历史 ============
messages = [
    {"role": "system", "content": "你是一个友好的AI助手，用中文回答问题。"}
]

def chat(user_input):
    """调用 DeepSeek API 进行对话"""
    messages.append({"role": "user", "content": user_input})

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    data = {
        "model": MODEL,
        "messages": messages,
        "temperature": 0.7,
        "max_tokens": 2000
    }

    try:
        response = requests.post(BASE_URL, headers=headers, json=data, timeout=30)
        response.raise_for_status()
        result = response.json()
        reply = result["choices"][0]["message"]["content"]
        messages.append({"role": "assistant", "content": reply})
        return reply
    except requests.exceptions.RequestException as e:
        return f"请求出错: {e}"
    except (KeyError, IndexError) as e:
        return f"解析响应出错: {e}"

def main():
    """主函数：命令行聊天循环"""
    print("=" * 50)
    print("  AI 聊天机器人 (Powered by DeepSeek)")
    print("  输入 '退出' 结束对话")
    print("  输入 '清空' 清除对话历史")
    print("=" * 50)
    print()

    while True:
        user_input = input("你: ").strip()

        if not user_input:
            continue

        if user_input in ["退出", "exit", "quit", "q"]:
            print("\n再见！")
            break

        if user_input in ["清空", "clear"]:
            messages.clear()
            messages.append({"role": "system", "content": "你是一个友好的AI助手，用中文回答问题。"})
            print("对话历史已清空。\n")
            continue

        print("AI: ", end="", flush=True)
        reply = chat(user_input)
        print(reply)
        print()

if __name__ == "__main__":
    main()
