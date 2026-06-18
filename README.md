# AI 聊天机器人

基于 DeepSeek API 的命令行聊天程序，支持多轮对话。

## 功能

- 调用 DeepSeek API 实现智能对话
- 支持多轮对话，自动保持上下文
- 输入"退出"结束对话
- 输入"清空"清除对话历史

## 使用方法

```bash
# 安装依赖
pip install requests

# 运行
python chatbot.py
```

## 项目结构

```
ai-chatbot/
├── chatbot.py    # 主程序
└── README.md     # 项目说明
```

## 技术栈

- Python 3
- DeepSeek API (OpenAI 兼容格式)
- requests 库
