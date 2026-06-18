# AI 聊天机器人

基于 DeepSeek API 的命令行聊天程序，支持多轮对话。

## 功能

- 调用 DeepSeek API 实现智能对话
- 支持多轮对话，自动保持上下文
- 输入"退出"结束对话
- 输入"清空"清除对话历史

## 前置条件

在使用本程序前，你需要：

1. **安装 Python 3**
   - 下载地址：https://www.python.org/downloads/
   - 安装时勾选 "Add Python to PATH"

2. **获取 DeepSeek API 密钥**
   - 注册地址：https://platform.deepseek.com
   - 注册后进入"API 密钥"页面，创建一个新密钥
   - 复制密钥（格式类似：sk-xxxxxxxxxxxxxxxx）

## 安装步骤

### 第一步：下载代码

打开命令行（Windows 按 Win+R 输入 cmd 回车），输入：

```
git clone https://github.com/k423-0617/ai-chatbot.git
cd ai-chatbot
```

如果没有 git 命令，可以直接在 GitHub 页面点击绿色的 "Code" 按钮，选 "Download ZIP"，解压后进入文件夹。

### 第二步：安装依赖

在命令行中输入以下任意一个（哪个能用就用哪个）：

```
pip install requests
```

或者：

```
py -3 -m pip install requests
```

或者：

```
python -m pip install requests
```

### 第三步：运行程序

```
py -3 chatbot.py
```

或者：

```
python chatbot.py
```

首次运行时，程序会提示你输入 DeepSeek API 密钥。输入后会自动保存，下次无需重新输入。

## 使用方法

1. 运行程序后，直接输入你想问的问题
2. AI 会自动回复
3. 输入"清空"可以清除对话历史
4. 输入"退出"结束程序

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

## 常见问题

**Q: 提示"pip 不是命令"怎么办？**
A: 试试 `python -m pip install requests`，或者检查 Python 是否安装正确。

**Q: 提示"python 不是命令"怎么办？**
A: 需要安装 Python 并勾选 "Add Python to PATH"。

**Q: 提示"请求出错 401"怎么办？**
A: API 密钥无效或过期，请检查密钥是否正确。

## 项目结构

```
ai-chatbot/
├── chatbot.py      # 主程序
├── config.json     # 配置文件（首次运行自动生成）
├── README.md       # 项目说明
└── .gitignore      # Git 忽略文件
```

## 技术栈

- Python 3
- DeepSeek API（OpenAI 兼容格式）
- requests 库

## 注意事项

- 需要有效的 DeepSeek API 密钥才能运行
- API 调用会消耗账户余额，请注意用量
- 密钥不要分享给他人或上传到公开仓库
