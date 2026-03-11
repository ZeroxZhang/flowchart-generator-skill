# Flowchart Generator Skill

**English** | [中文](#中文)

A powerful, universal AI skill designed to generate high-quality 2D flowcharts from natural language descriptions. This skill follows a rigorous 6-step process to ensure accuracy, clarity, and aesthetic appeal.

> **Universal Compatibility**: This skill is designed to work with **any AI Agent or Intelligent IDE** (e.g., Trae, Cursor, Windsurf, AutoGPT, etc.) that supports prompt-based skill execution or function calling.

---

## 🚀 Features

- **End-to-End Generation**: Converts raw text into a professional SVG flowchart.
- **Structured Workflow**: Uses a 6-step pipeline (Identify -> Optimize -> Deconstruct -> Wireframe -> Style -> SVG) to minimize errors.
- **Visual Validation**: Includes a text-based wireframe step for user verification before final rendering.
- **Adaptive Styling**: Automatically generates color palettes and layouts based on the content's context.

## 🛠 Workflow

The skill executes the following 6 steps sequentially:

1.  **Identify User Input**: Analyzes intent, subject matter, and constraints.
2.  **Optimize User Input**: Expands and structures the narrative logically.
3.  **Deconstruct Content**: Breaks down the narrative into dimensions, hierarchy, elements, and links.
4.  **Generate Plaintext Wireframe**: Creates a text-based ASCII/grid blueprint for structural verification.
5.  **Generate Style Scheme**: Defines colors, typography, and layout orientation.
6.  **Generate SVG**: Produces the final standalone SVG file.

## 📦 Installation & Usage

### For Trae / AI IDEs
1.  Clone this repository into your skills directory (e.g., `~/.trae/skills/flowchart-generator`).
2.  Reload your IDE or Agent.
3.  **Trigger**: Ask the AI to "create a flowchart", "draw a process map", or "visualize this framework".

### For General LLM Agents
You can copy the content of `SKILL.md` into your agent's system prompt or tool definition. The prompts within `SKILL.md` are designed to be model-agnostic.

---

<a name="中文"></a>
# 流程图生成技能 (Flowchart Generator Skill)

[English](#flowchart-generator-skill) | **中文**

一个强大的通用 AI 技能，旨在将自然语言描述转化为高质量的 2D 流程图。该技能遵循严谨的 6 步流程，以确保生成的图表准确、清晰且美观。

> **通用兼容性**：此技能专为**所有 AI 智能体 (Agent) 和智能 IDE**（如 Trae, Cursor, Windsurf, AutoGPT 等）设计，只要支持基于提示词的技能执行或函数调用即可使用。

## 🚀 特性

- **端到端生成**：将原始文本直接转化为专业的 SVG 流程图。
- **结构化工作流**：采用 6 步流水线（识别 -> 优化 -> 解构 -> 线框图 -> 样式 -> SVG），最大程度减少错误。
- **视觉验证**：包含基于文本的线框图步骤，供用户在最终渲染前进行结构验证。
- **自适应样式**：根据内容上下文自动生成配色方案和布局。

## 🛠 工作流程

该技能按顺序执行以下 6 个步骤：

1.  **识别用户输入 (Identify)**：分析用户意图、主题和约束条件。
2.  **优化用户输入 (Optimize)**：扩展并逻辑化梳理用户的叙述内容。
3.  **解构内容 (Deconstruct)**：将叙述拆解为维度、层级、元素和链路。
4.  **生成纯文本线框图 (Wireframe)**：创建基于 ASCII/网格的文本蓝图，用于结构验证。
5.  **生成样式方案 (Style)**：定义配色、排版和布局方向。
6.  **生成 SVG (Generate SVG)**：输出最终独立的 SVG 文件。

## 📦 安装与使用

### 对于 Trae / 智能 IDE
1.  将本仓库克隆到您的技能目录中（例如 `~/.trae/skills/flowchart-generator`）。
2.  重载您的 IDE 或 Agent。
3.  **触发方式**：直接让 AI “生成流程图”、“绘制流程映射”或“可视化这个框架”。

### 对于通用 LLM 智能体
您可以将 `SKILL.md` 的内容复制到您的 Agent 系统提示词 (System Prompt) 或工具定义中。`SKILL.md` 中的提示词设计为模型无关，可通用。
