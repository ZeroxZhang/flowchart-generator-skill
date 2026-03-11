# Flowchart Generator Skill for Trae

[English](#english) | [中文](#chinese)

<a name="english"></a>

## 🇬🇧 English

This is an AI Skill built for **Trae IDE**, designed to automatically generate clear 2D flowcharts (in SVG format) from simple natural language descriptions.

### ✨ Features

- **Text-Driven**: Simply describe your process in text—no manual dragging or drawing required.
- **Auto-Layout**: Generates flowcharts based on plaintext wireframes, ensuring logical and readable structures.
- **SVG Export**: Produces high-quality vector graphics, perfect for embedding in documents or websites.
- **Multi-Language Support**: Supports input in English, Chinese, and other languages. The text in the generated chart matches your input language.

### 🚀 How to Use

In the Trae IDE chat interface, you can trigger this skill using keywords like:

- **"Help me draw a flowchart for..."**
- **"Generate a framework diagram for..."**
- **"Visualize the process of..."**

#### Example

**User Input:**
> "Generate a user registration and login flowchart, including inputting credentials, validation, success redirect, and retry on failure."

**Skill Execution Flow:**
1. **Analyze Input**: Understands the user's intent and process logic.
2. **Generate Wireframe**: Outputs a text-based draft for confirmation.
3. **Generate SVG**: Creates the final SVG file based on the draft.
4. **Deliver Result**: Displays the generated file path directly in the chat.

### 🛠️ Installation & Configuration

To use this skill, clone this repository into your Trae skills directory (refer to the Trae official documentation for the specific path).

```bash
git clone https://github.com/ZeroxZhang/flowchart-generator-skill.git
```

### 📝 Skill Definition

The core definition of this skill is as follows (see `SKILL.md`):

```yaml
name: "flowchart-generator"
description: "Generates 2D flowcharts from text descriptions. Invoke when user mentions 'flowchart' or 'framework diagram'."
```

### 🤝 Contributing

Contributions via Issues or Pull Requests are welcome!

### 📄 License

MIT License

---

<a name="chinese"></a>

## 🇨🇳 中文

这是一个为 **Trae IDE** 打造的 AI 技能（Skill），旨在通过简单的自然语言描述，自动生成清晰的 2D 流程图（SVG 格式）。

### ✨ 功能特点

- **文本驱动**：只需输入文字描述，无需手动拖拽。
- **自动布局**：基于文本线框图（Plaintext Wireframe）生成，逻辑结构一目了然。
- **SVG 导出**：生成高质量的矢量图形，方便嵌入文档或网页。
- **多语言支持**：支持中文、英文等多种语言输入，生成的图表文字与输入语言保持一致。

### 🚀 如何使用

在 Trae IDE 的对话框中，你可以通过以下关键词触发此技能：

- **"帮我画一个...流程图"**
- **"生成一个...框架图"**
- **"可视化一下...的流程"**

#### 示例

**用户输入：**
> "生成一个用户注册登录的流程图，包含输入账号密码、验证、成功跳转和失败重试。"

**Skill 执行流程：**
1. **分析输入**：理解用户意图和流程逻辑。
2. **生成线框图**：先输出一个文本版的草图供确认。
3. **生成 SVG**：根据草图生成最终的 SVG 文件。
4. **交付结果**：直接在对话中展示生成的文件路径。

### 🛠️ 安装与配置

要使用此技能，请将本仓库克隆到你的 Trae 技能目录中（具体路径请参考 Trae 官方文档）。

```bash
git clone https://github.com/ZeroxZhang/flowchart-generator-skill.git
```

### 📝 技能定义 (Skill Definition)

该技能的核心定义如下（详见 `SKILL.md`）：

```yaml
name: "flowchart-generator"
description: "Generates 2D flowcharts from text descriptions. Invoke when user mentions 'flowchart' or 'framework diagram'."
```

### 🤝 贡献

欢迎提交 Issue 或 Pull Request 来改进此技能！

### 📄 许可证

MIT License
