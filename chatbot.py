# -*- coding: utf-8 -*-
"""
AI 聊天机器人
调用 DeepSeek API 实现多轮对话
"""

import requests
import json
import os

# ============ 配置 ============
API_KEY = os.getenv("DEEPSEEK_API_KEY", "your-api-key-here")  # 请设置环境变量或直接填入你的密钥
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
