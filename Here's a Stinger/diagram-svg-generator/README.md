# Diagram SVG Generator

> **Language / 语言**: [English](#english) | [中文](#中文)

---

<a id="english"></a>

## 🇬🇧 English

### Overview

**Diagram SVG Generator** is an interactive Agent Skill (following the [Agent Skills Specification](https://agentskills.io)) that generates production-ready SVG diagrams through a guided conversational workflow. It asks users about diagram size, color scheme, information density, layout direction, and connector style before generating clean, accessible SVG code.

### Skill Structure

```
diagram-svg-generator/
├── SKILL.md                          # REQUIRED: Metadata (YAML frontmatter) + instructions
├── references/
│   ├── svg-templates.md              # Detailed SVG templates for all 7 diagram types
│   └── interaction-flow.md           # Complete interaction flow reference
├── assets/
│   ├── color-schemes.md              # 6 color scheme definitions with hex values
│   ├── density-presets.md            # 4 density level parameter tables
│   ├── svg-base-template.md          # Base SVG wrapper template
│   └── examples/
│       ├── example-flowchart.svg     # Example: User login flowchart
│       └── example-mindmap.svg       # Example: Project management mind map
└── README.md                         # This documentation file
```

### Supported Diagram Types

| # | Type | Description |
|---|------|-------------|
| 1 | Flowchart | Process flows with decisions, loops, and branches |
| 2 | Sequence Diagram | Actor interactions over time |
| 3 | Mind Map | Radial topic exploration from a central idea |
| 4 | Org Chart | Hierarchical organization structures |
| 5 | Timeline | Chronological events on a horizontal axis |
| 6 | ER Diagram | Entity-relationship models for databases |
| 7 | State Diagram | State machines with transitions |

### Interactive Configuration

The skill guides users through 5 configuration steps before generating:

| Step | Setting | Options | Default |
|------|---------|---------|---------|
| 1 | 📏 Size | Small (600×400) / **Medium (1000×700)** / Large (1400×1000) / XL (1920×1080) / Custom | ⭐ Medium |
| 2 | 🎨 Color Scheme | **Corporate Blue** / Nature Green / Sunset Warm / Dark Mode / Monochrome / Ocean Breeze / Custom | ⭐ Corporate Blue |
| 3 | 📝 Info Density | Minimal / **Standard** / Detailed / Compact | ⭐ Standard |
| 4 | 🧭 Direction | **Top→Bottom** / Left→Right / Bottom→Top / Right→Left | ⭐ Top→Bottom |
| 5 | 🔗 Connectors | Straight / Curved / **Orthogonal** / Dashed | ⭐ Orthogonal |

> **Quick Mode**: Say `"use defaults"` or `"快速生成"` to skip all configuration and use recommended defaults.

### Smart Recommendations

The skill auto-recommends settings based on content:
- **Size**: Based on node count (≤5 → Small, 6–15 → Medium, 16–30 → Large, 31+ → XL)
- **Color**: Based on topic (business → Blue, tech → Dark, print → Mono)
- **Direction**: Based on diagram type (flowchart → TB, timeline → LR)

### How to Use

1. **Activate**: Load the skill via `SKILL.md`
2. **Describe**: Tell the agent what you want to visualize
3. **Configure**: Answer 5 quick preference questions (or say "use defaults")
4. **Receive**: Get production-ready SVG code
5. **Refine**: Iterate on style, content, or layout as needed

### SVG Output Quality

All generated SVGs follow these standards:
- ✅ Valid XML with proper `xmlns` namespace
- ✅ Accessible: `<title>`, `<desc>`, `role="img"`, `aria-labelledby`
- ✅ Responsive: `viewBox` attribute for infinite scaling
- ✅ Clean: CSS classes in `<defs><style>`, no inline styles
- ✅ Semantic: `<g>` groups with meaningful `id` attributes
- ✅ Commented: XML comments for major sections

### Color Scheme Preview

| Scheme | Primary | Secondary | Background | Best For |
|--------|---------|-----------|------------|----------|
| 💼 Corporate Blue | `#1A73E8` | `#4285F4` | `#FFFFFF` | Business, professional |
| 🌿 Nature Green | `#2E7D32` | `#4CAF50` | `#FAFAFA` | Ecology, health |
| 🌅 Sunset Warm | `#E65100` | `#FF6D00` | `#FFF8E1` | Creative, marketing |
| 🌙 Dark Mode | `#BB86FC` | `#03DAC6` | `#121212` | Technical, dev |
| ⚫ Monochrome | `#212121` | `#616161` | `#FFFFFF` | Print, academic |
| 🌊 Ocean Breeze | `#0077B6` | `#00B4D8` | `#CAF0F8` | Education, calm |

### Examples

- **Login Flowchart**: `assets/examples/example-flowchart.svg` — Authentication process with 2FA and lockout
- **Mind Map**: `assets/examples/example-mindmap.svg` — Project management with 4 branches and sub-topics

### Technical Info

| Property | Value |
|----------|-------|
| Spec Version | Agent Skills v1 |
| Output Format | SVG (XML, UTF-8) |
| Dependencies | None |
| Languages | English + Chinese |
| Interaction | Multi-turn conversational |
| License | MIT |

---

<a id="中文"></a>

## 🇨🇳 中文

### 概述

**Diagram SVG Generator（图表 SVG 生成器）** 是一个遵循 [Agent Skills 规范](https://agentskills.io) 的交互式 Agent Skill。它通过引导式对话工作流生成生产级 SVG 图表，在生成前会询问用户关于图表尺寸、配色方案、信息密度、布局方向和连接线样式的偏好。

### Skill 结构

```
diagram-svg-generator/
├── SKILL.md                          # 必需：元数据（YAML frontmatter）+ 指令
├── references/
│   ├── svg-templates.md              # 7 种图表类型的详细 SVG 模板
│   └── interaction-flow.md           # 完整交互流程参考
├── assets/
│   ├── color-schemes.md              # 6 种配色方案定义（含十六进制色值）
│   ├── density-presets.md            # 4 种密度级别参数表
│   ├── svg-base-template.md          # 基础 SVG 包装模板
│   └── examples/
│       ├── example-flowchart.svg     # 示例：用户登录流程图
│       └── example-mindmap.svg       # 示例：项目管理思维导图
└── README.md                         # 本文档
```

### 支持的图表类型

| # | 类型 | 说明 |
|---|------|------|
| 1 | 流程图 (Flowchart) | 包含判断、循环和分支的流程 |
| 2 | 时序图 (Sequence) | 参与者之间的时序交互 |
| 3 | 思维导图 (Mind Map) | 从中心主题向外辐射的思维发散 |
| 4 | 组织架构图 (Org Chart) | 层级式组织结构 |
| 5 | 时间线 (Timeline) | 水平轴上的时间顺序事件 |
| 6 | ER 图 (ER Diagram) | 数据库实体关系模型 |
| 7 | 状态图 (State Diagram) | 带状态转换的状态机 |

### 交互式配置

Skill 会在生成前引导用户完成 5 步配置：

| 步骤 | 设置项 | 选项 | 默认值 |
|------|--------|------|--------|
| 1 | 📏 规格 | 小 (600×400) / **中 (1000×700)** / 大 (1400×1000) / 超大 (1920×1080) / 自定义 | ⭐ 中等 |
| 2 | 🎨 配色 | **商务蓝** / 自然绿 / 暖日落 / 暗色 / 单色 / 海洋微风 / 自定义 | ⭐ 商务蓝 |
| 3 | 📝 密度 | 极简 / **标准** / 详细 / 紧凑 | ⭐ 标准 |
| 4 | 🧭 方向 | **上→下** / 左→右 / 下→上 / 右→左 | ⭐ 上→下 |
| 5 | 🔗 连线 | 直线 / 曲线 / **直角折线** / 虚线 | ⭐ 直角折线 |

> **快速模式**：说 `"使用默认"` 或 `"快速生成"` 即可跳过配置，使用全部推荐默认值。

### 智能推荐

Skill 会根据内容自动推荐设置：
- **尺寸**：根据节点数量（≤5 → 小，6–15 → 中，16–30 → 大，31+ → 超大）
- **配色**：根据主题（商务 → 蓝，技术 → 暗色，打印 → 单色）
- **方向**：根据图表类型（流程图 → 上下，时间线 → 左右）

### 使用方法

1. **激活**：通过 `SKILL.md` 加载 Skill
2. **描述**：告诉 Agent 你想可视化什么
3. **配置**：回答 5 个快速偏好问题（或说"使用默认"）
4. **接收**：获取生产级 SVG 代码
5. **优化**：按需迭代样式、内容或布局

### SVG 输出质量

所有生成的 SVG 遵循以下标准：
- ✅ 有效 XML，正确的 `xmlns` 命名空间
- ✅ 可访问：`<title>`、`<desc>`、`role="img"`、`aria-labelledby`
- ✅ 响应式：`viewBox` 属性支持无限缩放
- ✅ 整洁：CSS 类定义在 `<defs><style>` 中，无内联样式
- ✅ 语义化：`<g>` 分组带有有意义的 `id` 属性
- ✅ 有注释：主要部分包含 XML 注释

### 配色方案预览

| 方案 | 主色 | 辅色 | 背景色 | 适用场景 |
|------|------|------|--------|----------|
| 💼 商务蓝 | `#1A73E8` | `#4285F4` | `#FFFFFF` | 商务、专业 |
| 🌿 自然绿 | `#2E7D32` | `#4CAF50` | `#FAFAFA` | 生态、健康 |
| 🌅 暖日落 | `#E65100` | `#FF6D00` | `#FFF8E1` | 创意、营销 |
| 🌙 暗色模式 | `#BB86FC` | `#03DAC6` | `#121212` | 技术、开发 |
| ⚫ 单色 | `#212121` | `#616161` | `#FFFFFF` | 打印、学术 |
| 🌊 海洋微风 | `#0077B6` | `#00B4D8` | `#CAF0F8` | 教育、清新 |

### 示例

- **登录流程图**：`assets/examples/example-flowchart.svg` — 包含双因素认证和账户锁定的认证流程
- **思维导图**：`assets/examples/example-mindmap.svg` — 项目管理的 4 个分支及子主题

### 技术信息

| 属性 | 值 |
|------|-----|
| 规范版本 | Agent Skills v1 |
| 输出格式 | SVG (XML, UTF-8) |
| 依赖项 | 无 |
| 支持语言 | 英文 + 中文 |
| 交互模式 | 多轮对话式 |
| 许可证 | MIT |

---

## License / 许可证

MIT License

## Contributing / 贡献

Issues and pull requests are welcome. / 欢迎提交 Issue 和 Pull Request。