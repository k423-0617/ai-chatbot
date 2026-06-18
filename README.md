# AI 聊天机器人

基于 DeepSeek API 的命令行聊天程序，支持多轮对话。

## 功能

- 调用 DeepSeek API 实现智能对话
- 支持多轮对话，自动保持上下文
- 输入"退出"结束对话
- 输入"清空"清除对话历史

## 快速开始

### 1. 克隆项目

```bash
git clone https://github.com/k423-0617/ai-chatbot.git
cd ai-chatbot
```

### 2. 安装依赖

```bash
pip install requests
```

### 3. 配置密钥

打开 `chatbot.py`，找到第 12 行：

```python
API_KEY = "your-api-key-here"
```

把 `your-api-key-here` 替换成你的 DeepSeek API 密钥：

```python
API_KEY = "sk-你的密钥"
```

> 密钥获取地址：https://platform.deepseek.com/api_keys

### 4. 运行

```bash
python chatbot.py
```

## 使用示例

```
==================================================
  AI 聊天机器人 (Powered by DeepSeek)
  输入 '退出' 结束对话
  输入 '清空' 清除对话历史
==================================================

你: 你好，介绍一下你自己
AI: 你好！我是DeepSeek，一个由深度求索公司开发的AI助手...

你: 退出
再见！
```

## 项目结构

```
ai-chatbot/
├── chatbot.py    # 主程序
├── README.md     # 项目说明
└── .gitignore    # Git忽略文件
```

## 技术栈

- Python 3
- DeepSeek API（OpenAI 兼容格式）
- requests 库

## 注意事项

- 需要有效的 DeepSeek API 密钥才能运行
- API 调用会消耗账户余额，请注意用量
- 密钥不要分享给他人或上传到公开仓库
