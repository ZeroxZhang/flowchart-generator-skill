*Thinking...*

> The user wants me to create a complete skill file package for generating flowcharts from user input. Let me break down the workflow:
> 
> 1. Identify user input content
> 2. Optimize user input into a polished text description
> 3. Analyze and decompose the content into flowchart dimensions, levels, elements, links, titles, notes, etc.
> 4. Generate a text-based 2D flowchart (plaintext wireframe)
> 5. Generate styling specifications (color scheme, layout, fonts, etc.)
> 6. Use steps 4 and 5 to generate an SVG flowchart
> 
> Let me think about how to optimize this workflow and create a comprehensive skill package.
> 
> 
> Now I'm planning the package structure with a directory layout, core skill.md file, individual processing scripts, asset templates and examples, plus documentation. The architecture is essentially a text-to-flowchart pipeline that takes raw input, refines it into a structured description, extracts the flowchart structure with nodes and edges, generates a text-based layout, applies styling specifications, and renders the final SVG visualization.
> 
> Setting up the project files...
> 
> I'm reconsidering the structure since this is designed as an LLM skill rather than a traditional automation tool—the scripts should probably be instruction prompts rather than executable code, though I could also use Python files for actual processing logic.
> 
> Since the user is communicating in Chinese, I should write all the documentation and content in Chinese to make it practical and usable for them.
> 
> Now I'm reconsidering the architecture—for an LLM skill, the "scripts" are really prompt modules that guide each processing step rather than traditional automation scripts. I'll structure this as a comprehensive skill package with a core instruction file, modular prompts for each of the six steps, and supporting templates and examples.
> 
> Organizing the directory structure...
> 
> I'm seeing the rest of the templates and reference files that support the workflow—style templates, SVG base templates, color palettes, layout rules, and component documentation. Now I need to write out the skill.md file with metadata, skill description, and input/output specifications.
> 
> I'm refining the processing pipeline to make sure it's optimized. The six-step approach covers input recognition and analysis, content refinement and text drafting, then moves into flow structure and visualization generation. Now I'm organizing the project structure with a clear directory layout for the flowchart generator, including documentation, examples, templates, and reference materials that will support the implementation.
> 
> I need to think through what makes this genuinely useful—the skill prompt needs to guide an LLM through the complete pipeline, the templates should define clear schemas for each stage, examples should demonstrate the full workflow, and references should provide reusable design components like SVG shapes and color schemes.
> 
> Let me start writing out all the files now, focusing on practical utility and immediate usability. I'm mapping out the visual design system with five color palettes—business blue, tech green, warm tones, high contrast, and minimal gray—and defining seven node types for the flowchart including start/end ovals, process rectangles, decision diamonds, I/O parallelograms, sub-process boxes, document waves, and database cylinders.
> 
> For the layout structure, I'm considering three main modes: top-to-bottom flow, left-to-right orientation, and mixed layouts for more complex diagrams. Now I'm thinking through how to organize the documentation—I want to create a comprehensive skill guide as the foundation, then build clean templates and one detailed example that demonstrates the full workflow, along with essential reference materials.
> 
> Writing the wireframe notation...
> 
> Defining the layout structure with YAML... Now I'm settling on a clear pipeline where each step produces distinct output—the JSON structure defines the nodes and edges, then an ASCII wireframe helps visualize the layout before styling, and finally everything combines into the SVG. Let me start building this out by setting up the directory structure and writing each component file.
> 
> I'm reconsidering whether to include Python scripts since the skill framework handles all the processing through the LLM instructions themselves, but I'll keep the structure minimal and focus on making skill.md comprehensive enough to guide the entire workflow without external dependencies. scripts for input validation and SVG output validation that could be useful for pipeline integration. Now I'm laying out the complete directory structure and starting to write the actual skill.md file with all the key sections including metadata, input/output specs, and the six-phase execution pipeline.
> 
> I'm also thinking through what makes a flowchart truly beautiful, neat, and standardized—harmonious colors and consistent styling for aesthetics, grid-aligned nodes with orthogonal routing for neatness, and proper flowchart symbols with clear decision diamonds for standardization.
> 
> Now I'm organizing the full response with directory structure, complete file contents, and usage instructions, making sure the SVG generation produces high-quality output with rounded rectangles for processes, diamonds for decisions, pill shapes for start/end nodes, proper arrow markers, and shadow filters for visual polish. Building the ASCII flowchart...
> 
> I'm shifting to a more structured approach where I define the diagram in a machine-readable format first—using JSON or YAML to specify all the nodes, edges, and positioning—then generate the SVG from that specification, with the ASCII art serving as a human-readable verification step.
> 
> Now I'm ready to start writing the actual output. I'll begin with skill.md since that's the foundation, then move through the templates, examples, and supporting files. The user wants everything in one response, so this will be substantial, but I'm aiming for clear, focused content in each section.
> 
> One thing I'm realizing: the user's mention of "calling a large model" in step 6 suggests the SVG generation might be delegated to a separate LLM call, so I should structure the skill in a way that makes that handoff clear and straightforward.
> 
> For the visual design, I'm settling on standard flowchart dimensions—process boxes around 160×60 pixels, decision diamonds at 120×80, with consistent spacing and orthogonal connection lines that have arrow markers and labels for branches.
> 
> Let me start writing now.
> 
> I should keep this tool flexible enough to work with different LLMs, though I'll optimize it for Claude. I'll structure the skill package with a clear directory layout including the core skill instructions, validation scripts for both structure and SVG output, and example files to guide users.
> 
> Setting up the project structure... Now I'm deciding on the scope for each file—the README needs practical usage guidance, the skill documentation should be thorough and comprehensive since it's the foundation, the validation scripts can be concise, and the demo files should show complete working examples. I'll structure the output clearly, presenting each file in order. I'm continuing to flesh out the specification for this skill, detailing the output requirements like SVG format and default dimensions, then moving into constraints around node count and when to split complex flows into separate diagrams. 现在我在定义第二阶段的目标和执行步骤，要将用户的输入转化为结构清晰、表述准确的流程文字稿，消除歧义并补充缺失的细节。
> 
> 我需要统一术语、明确判断条件、添加角色职责和详细的步骤说明。
> 
> 现在进入第三阶段，我要把文字稿转化为结构化的流程数据，定义所有节点和连接关系，确保流程的完整性和逻辑的严密性。
> 
> 接下来第四阶段需要规划流程图的空间布局，计算节点位置并优化整体的视觉平衡，最后在第五阶段为流程图应用专业的视觉设计方案。
> 
> 第六阶段则是基于这些结构和设计数据生成最终的 SVG 代码。
> 
> 我需要初始化画布、注入样式定义，然后依次渲染节点、连接线、文本和标签，最后添加标题和图例。生成完成后还要确保所有文字清晰可读、节点均匀分布、连接线最少交叉，并通过质量检查清单验证节点文字完整性、对齐一致性等细节。
> 
> 如果用户输入信息不足或流程节点过多，我会列出已识别的信息、指出缺失部分，或建议将复杂流程分解成多个子图。
> 
> 对于存在多种理解方式的流程，我会列举可能的解读并选择最合理的默认方案。我还需要遵守一些约束：只生成静态SVG流程图，单次节点数不超过30个，不支持三维或动态交互式图表，也不嵌入外部资源。
> 
> 现在我要开始编写实际的文件内容。
> 
> skill.md的框架已经确定了，接下来我需要为structure_schema.json创建一个完整的模板，定义元数据、配置参数和节点结构...
> 
> Defining the JSON schema template... Defining the style schema with a business-blue color palette and typography settings... Defining node styling properties... Finishing up the configuration with edge styling, layout parameters, and visual effects like shadows and hover states. Now I'm ready to write out a complete example using a user registration flow that demonstrates all six phases. I'm debating whether to include the full SVG code in the example—it'll be substantial at 200-300 lines, but showing the actual output would be really valuable for demonstrating the complete pipeline. I've decided to include it to make the example comprehensive. Now I'm organizing the full response structure with all the key files and documentation sections I need to present. I've been overthinking this—time to just write out all the files. I'll keep the smaller ones compact and combine related reference files where it makes sense, then wrap up with some practical usage notes.

# 智能流程图生成器 — 完整 Skill 文件包

下面是我根据你的需求优化后的完整 skill 文件包。我做了以下优化：

1. 将 Phase 3（结构拆解）的输出改为 **结构化 JSON**，便于后续步骤精确引用
2. Phase 4 采用 **网格定位 + ASCII 线框双输出**，兼顾机器解析与人类可读
3. Phase 6 内置了 **SVG 组件库**，确保输出质量稳定可控
4. 增加了 **质量检查清单** 和 **错误兜底机制**

---

## 📁 目录结构

```
skill-flowchart-generator/
├── README.md                                  # 使用说明与快速上手
├── skill.md                                   # 核心技能指令文件（必选）
├── scripts/
│   ├── validate_structure.py                  # 结构数据校验脚本
│   └── validate_svg.py                        # SVG 输出校验脚本
└── assets/
    ├── examples/
    │   └── full_pipeline_demo.md              # 完整六阶段流水线演示
    ├── templates/
    │   ├── structure_schema.json              # Phase3 输出 JSON 模板
    │   ├── style_schema.json                  # Phase5 输出 JSON 模板
    │   └── svg_skeleton.md                    # SVG 骨架与组件使用说明
    └── references/
        ├── color_palettes.json                # 预设配色方案库
        ├── node_types.md                      # 标准节点类型与符号定义
        └── layout_rules.md                    # 布局规则与最佳实践
```

---

## 📄 `README.md`

```markdown
# 🧩 Skill: 智能流程图生成器 (Smart Flowchart Generator)

> 将自然语言、列表、伪代码等任意形式的流程描述，自动转化为专业美观的 SVG 流程图。

## 快速开始

### 1. 基本用法

将本 skill 文件夹放置于你的 prompt 工程项目中，在系统提示词中引用 `skill.md` 即可。

**最简调用示例：**
```
请根据以下描述生成流程图：
用户提交订单后，系统检查库存。库存充足则生成订单并通知仓库发货；
库存不足则通知用户缺货，用户可选择等待补货或取消订单。
```

### 2. 文件说明

| 文件 | 必选 | 说明 |
|------|------|------|
| `skill.md` | ✅ | 核心指令文件，定义完整的六阶段流水线 |
| `scripts/validate_structure.py` | ❌ | 校验 Phase3 输出的结构 JSON 是否合规 |
| `scripts/validate_svg.py` | ❌ | 校验最终 SVG 输出的完整性 |
| `assets/templates/` | ✅ | JSON Schema 模板 + SVG 组件说明 |
| `assets/examples/` | 推荐 | 完整流水线演示，供参考和调试 |
| `assets/references/` | 推荐 | 配色库、节点类型、布局规则 |

### 3. 六阶段流水线

```
用户输入 → [P1]输入分析 → [P2]内容优化 → [P3]结构拆解 → [P4]文本线框 → [P5]视觉设计 → [P6]SVG生成
```

每个阶段产出独立的中间产物，支持分步调试和复用。

### 4. 适用场景

- 业务流程图（审批流、注册流、下单流等）
- 技术流程图（部署流、CI/CD、数据处理管线）
- 决策流程图（风控策略、诊断流程）
- 产品交互流程（用户旅程、功能流转）

### 5. 限制

- 仅输出静态 SVG，不支持交互式或动态流程图
- 单次生成建议不超过 30 个核心节点，超出建议拆分子流程
- 不支持三维流程或嵌入外部图片
- SVG 中文字体依赖系统环境，建议优先使用通用字体族

### 6. 定制

- 修改 `assets/references/color_palettes.json` 可自定义配色方案
- 修改 `assets/references/node_types.md` 可扩展节点类型
- 修改 `assets/references/layout_rules.md` 可调整布局策略
```

---

## 📄 `skill.md`（核心指令文件）

```markdown
# Skill: 智能流程图生成器 (Smart Flowchart Generator)

## META
- skill_id: flowchart-generator
- version: 1.0.0
- output_format: SVG
- language: zh-CN / en (auto-detect)
- max_nodes: 30
- min_steps: 2

---

## 技能概述

你是一个专业的流程图生成引擎。你的任务是将用户提供的任意形式的流程描述（自然语言、列表、伪代码、文档片段等），通过严格的六阶段流水线，转化为 **专业、美观、规整、规范** 的 SVG 流程图。

你必须严格按照以下六个阶段顺序执行，每个阶段产出明确的中间产物。不可跳过任何阶段。

---

## 输入规范

### 接受的输入类型
- 自然语言段落描述
- 编号/无序列表
- 伪代码 / 逻辑描述
- 已有流程文档的摘要
- 关键词 + 关系描述的组合

### 输入约束
- 必须包含至少 2 个可识别的流程步骤
- 如果输入不足以生成有意义的流程图，执行「错误处理 - 输入不足」策略
- 如果超过 30 个核心节点，执行「错误处理 - 复杂度过高」策略

---

## 输出规范

### 最终输出
- 完整的 SVG 代码块，可直接保存为 `.svg` 文件
- UTF-8 编码
- 使用 viewBox 实现响应式缩放
- 默认画布宽度 800–1200px，高度自适应

### 中间产物（可选展示）
用户未要求时可折叠/省略中间产物，但内部必须完整执行每个阶段。
如用户要求「显示过程」或「分步展示」，则输出每个阶段的中间产物。

---

## ═══════════════════════════════════════
## 执行流水线（六阶段）
## ═══════════════════════════════════════

---

### Phase 1: 输入识别与分析

**目标**：全面理解用户意图，提取核心信息，评估输入质量。

**执行步骤**：

1. **类型判断**：识别输入属于自然语言 / 列表 / 伪代码 / 文档 / 混合类型
2. **实体提取**：
   - 动作/操作（如：提交、审核、发送）
   - 对象/状态（如：订单、邮件、账户）
   - 角色/主体（如：用户、系统、管理员）
   - 条件/规则（如：如果库存充足、当金额>1000）
3. **关系识别**：
   - 顺序关系（A → B）
   - 条件分支（if/else）
   - 并行关系（同时进行）
   - 循环关系（重复直到）
   - 汇聚关系（多条路径合并）
4. **领域分类**：业务流程 / 技术流程 / 决策流程 / 交互流程
5. **完整度评估**：
   - 是否有明确的起点和终点
   - 是否所有分支都有归宿
   - 是否存在歧义或缺失环节

**输出格式**：

```
## Phase 1 分析报告

- 输入类型：[自然语言描述]
- 领域分类：[业务流程]
- 识别实体：[N] 个动作，[N] 个对象，[N] 个角色，[N] 个条件
- 关系类型：顺序 ✓ | 分支 ✓ | 并行 ✗ | 循环 ✗ | 汇聚 ✓
- 完整度：[4/5]
- 缺失/待确认项：
  - [具体描述]
- 领域关键词：[keyword1, keyword2, ...]
```

---

### Phase 2: 内容优化与文字稿生成

**目标**：将原始输入转化为完整、清晰、无歧义的结构化流程文字稿。

**执行规则**：

1. **补全**：
   - 必须有明确的「开始」触发条件
   - 必须有明确的「结束」状态
   - 每个判断分支必须有完整的是/否（或多条件）路径
   - 补充合理的异常处理路径（如果原始输入遗漏）
2. **统一**：
   - 同一概念使用统一术语
   - 动作描述使用「动词 + 宾语」结构
   - 条件描述使用「当...时」或「如果...则」结构
3. **精简**：
   - 每个步骤描述不超过 15 字（用于节点标签）
   - 详细描述放入步骤说明中
4. **排序**：
   - 按实际执行顺序排列
   - 分支路径缩进标注

**输出格式**：

```markdown
## Phase 2 优化文字稿

### 流程名称：[名称]
### 流程概述：[一句话描述]

### 参与角色
| 角色 | 职责 |
|------|------|
| [角色] | [职责描述] |

### 流程步骤

**1. [步骤名称]**（节点标签：[≤15字的精简标签]）
- 描述：[详细描述]
- 角色：[执行角色]
- 输入：[所需输入]
- 输出：[产出结果]

**2. [判断名称]**（节点标签：[≤15字]）
- 类型：条件判断
- 条件：[判断条件]
  - ✅ 是 → 转到步骤 [N]
  - ❌ 否 → 转到步骤 [N]

...（依次列出所有步骤）

### 异常处理
| 异常场景 | 处理方式 |
|----------|----------|
| [场景] | [处理] |

### 补充说明
- [说明事项]
```

---

### Phase 3: 流程结构拆解

**目标**：将文字稿转化为结构化 JSON 数据，精确定义所有节点和连接。

**执行规则**：

1. **节点定义**：
   - 每个节点必须有唯一 `id`（格式：`node_01`, `node_02`, ...）
   - 节点类型必须从以下选取：`terminal`（开始/结束）、`process`（处理）、`decision`（判断）、`io`（输入/输出）、`subprocess`（子流程）
   - `label` 不超过 15 个中文字符或 30 个英文字符
   - 开始节点 label 固定为「开始」，结束节点 label 固定为「结束」（或对应英文）

2. **边定义**：
   - 每条边必须有 `from` 和 `to`，指向有效的节点 id
   - 条件分支的边必须有 `label`（如「是」「否」）
   - 普通顺序边 `label` 留空

3. **位置规划**：
   - 使用 `row`/`col` 网格定位（从 0 开始）
   - 主流程走中间列（通常 col=1 或 col=2）
   - 分支向两侧展开
   - 同一层级的节点在同一行

4. **元数据**：
   - 必须包含 `title`（流程名称）
   - 可选 `subtitle`（概述）和 `footnote`（备注）

**输出格式**：严格遵循 `assets/templates/structure_schema.json` 的 schema。

---

### Phase 4: 文本线框图生成

**目标**：基于 Phase 3 的结构数据，生成可视化的文本线框布局。

**执行规则**：

1. **流向选择**：
   - 默认使用 TB（自上而下）
   - 如果流程是线性且步骤较多（>8步），考虑 LR（从左到右）
   - 如果存在复杂的并行分支，使用 TB

2. **ASCII 线框规范**：
   - 使用 `[ ]` 表示处理节点
   - 使用 `(( ))` 表示开始/结束节点
   - 使用 `{ }` 表示判断节点
   - 使用 `│ ─ ┌ ┐ └ ┘ ├ ┤ ┬ ┴ ┼` 绘制连接线
   - 使用 `▼ ▶ ◀ ▲` 表示流向箭头
   - 使用 `[是]` `[否]` 标注分支条件

3. **布局检查**：
   - 确认无节点重叠
   - 确认连接线无不必要的交叉
   - 确认整体布局左右均衡

**输出格式**：

```
## Phase 4 文本线框图

### 布局参数
- 流向：TB（自上而下）
- 网格：[行数] 行 × [列数] 列
- 节点数：[N]
- 连接数：[N]

### ASCII 线框

（在此绘制 ASCII 线框图）
```

---

### Phase 5: 视觉设计方案

**目标**：为流程图设计专业的视觉样式，确保美观和可读性。

**执行规则**：

1. **配色选择**：
   - 根据领域类型从 `assets/references/color_palettes.json` 中选取配色方案
   - 也可根据用户指定的风格自定义
   - 必须确保文字与背景的对比度 ≥ 4.5:1（WCAG AA 标准）

2. **排版规则**：
   - 字体族：`"PingFang SC", "Microsoft YaHei", "Helvetica Neue", Arial, sans-serif`
   - 节点标签字号：13–14px，font-weight: 500
   - 边标签字号：11–12px
   - 标题字号：20–24px，font-weight: 700
   - 备注字号：12px，斜体

3. **节点样式**：
   - 圆角半径：处理节点 8px，开始/结束节点 25px（胶囊形）
   - 阴影：`drop-shadow(0 2px 4px rgba(0,0,0,0.1))`
   - 内边距：水平 20px，垂直 12px
   - 节点宽度根据文字内容自适应，但同类节点保持统一宽度

4. **连接线样式**：
   - 线宽：1.5–2px
   - 颜色：中性灰色（与节点边框色协调）
   - 转角使用圆弧（radius 4-6px）
   - 箭头：实心三角形，大小 8px

5. **间距规则**：
   - 垂直间距（TB模式）：60–80px
   - 水平间距：50–70px
   - 画布内边距：40–60px

**输出格式**：严格遵循 `assets/templates/style_schema.json` 的 schema。

---

### Phase 6: SVG 代码生成

**目标**：综合 Phase 3–5 的全部数据，生成最终的 SVG 代码。

**SVG 代码结构**（按此顺序构建）：

```xml
<svg xmlns="..." viewBox="..." font-family="...">
  <!-- 1. 定义区：滤镜、渐变、箭头标记 -->
  <defs>
    <filter id="shadow">...</filter>
    <marker id="arrowhead">...</marker>
  </defs>

  <!-- 2. 背景层 -->
  <rect class="canvas-bg" ... />

  <!-- 3. 标题区 -->
  <text class="title">...</text>
  <text class="subtitle">...</text>

  <!-- 4. 连接线层（先渲染，使其位于节点下方） -->
  <g class="edges">
    <path ... />
    <text class="edge-label">...</text>
  </g>

  <!-- 5. 节点层 -->
  <g class="nodes">
    <g class="node" id="node_01">
      <rect ... />
      <text>...</text>
    </g>
  </g>

  <!-- 6. 标注层 -->
  <g class="annotations">...</g>

  <!-- 7. 备注/脚注 -->
  <text class="footnote">...</text>
</svg>
```

**生成规则**：

1. **画布**：
   - 使用 `viewBox`，不硬编码 `width/height`，确保响应式
   - 实际输出可添加 `width="100%"` 便于嵌入

2. **节点渲染**：
   - `terminal` 节点：圆角矩形（rx 等于高度一半），实心填充
   - `process` 节点：圆角矩形，白底 + 彩色边框
   - `decision` 节点：用 `<polygon>` 或旋转45°的 `<rect>` 绘制菱形
   - 所有文字使用 `<text>` 并设置 `text-anchor="middle"` + `dominant-baseline="central"`

3. **连接线渲染**：
   - 优先使用正交折线（直角转弯），用 `<path>` 的 L/H/V 命令
   - 如需圆角转弯，使用 Q（二次贝塞尔）
   - 箭头通过 `marker-end="url(#arrowhead)"` 引用
   - 分支标签放在连接线起始端附近

4. **坐标计算**：
   - 根据 Phase 3 的 `row/col` + Phase 5 的间距参数计算实际 x/y
   - 公式：`x = padding + col * (nodeWidth + gapH) + nodeWidth/2`
   - 公式：`y = titleAreaHeight + padding + row * (nodeHeight + gapV) + nodeHeight/2`
   - 连接线的起止点对齐到节点的边缘中心点

5. **文字处理**：
   - 超过节点宽度的文字需要折行（使用多个 `<tspan>`）
   - 中文按字符数估算宽度（每字符约 14px × fontSize 比例）

6. **质量检查**（生成后自检）：
   - ✅ 所有节点文字完整可见，未被截断
   - ✅ 节点之间无重叠
   - ✅ 连接线箭头方向正确
   - ✅ 判断分支的「是/否」标签清晰
   - ✅ 整体布局均衡，无明显偏移
   - ✅ viewBox 尺寸正确包含所有元素
   - ✅ 配色和谐，文字可读

---

## 错误处理

### 场景1：输入不足
当用户输入无法识别出 ≥ 2 个流程步骤时：
1. 说明当前识别到的信息
2. 提出 2-3 个引导问题帮助用户补充
3. 不生成流程图

### 场景2：复杂度过高
当识别到的核心节点 > 30 个时：
1. 建议将流程拆分为主流程 + 子流程
2. 提供拆分方案（列出建议的子流程边界）
3. 先生成高层概览图，子流程标注为 subprocess 节点

### 场景3：存在歧义
当流程存在多种合理理解时：
1. 列出不同的理解方式
2. 选择最常见/最合理的作为默认
3. 在流程图 footnote 中标注「注：此处存在 [N] 种理解，本图采用 [具体方案]」

### 场景4：用户指定风格
如用户指定了配色、风格、品牌色等：
- 在 Phase 5 中优先使用用户指定的方案
- 确保自定义配色仍满足对比度标准

---

## 约束与边界

1. 仅输出静态 SVG 文件，不含 JavaScript 交互
2. 不嵌入外部图片或字体文件（使用系统字体族）
3. SVG 代码必须是合法的 XML，可通过标准 SVG 验证
4. 所有中文内容使用 UTF-8 编码
5. 每个阶段不可省略，但中间产物可按需展示/隐藏
```

---

## 📄 `scripts/validate_structure.py`

```python
#!/usr/bin/env python3
"""
validate_structure.py
校验 Phase 3 输出的流程结构 JSON 是否符合规范。
用法：python validate_structure.py structure.json
"""

import json
import sys
from typing import Any

REQUIRED_TOP_KEYS = {"metadata", "config", "nodes", "edges"}
REQUIRED_NODE_KEYS = {"id", "type", "label", "position"}
REQUIRED_EDGE_KEYS = {"id", "from", "to"}
VALID_NODE_TYPES = {"terminal", "process", "decision", "io", "subprocess"}
VALID_DIRECTIONS = {"TB", "LR", "BT", "RL"}


def validate(data: dict[str, Any]) -> list[str]:
    errors = []

    # 顶层结构
    for key in REQUIRED_TOP_KEYS:
        if key not in data:
            errors.append(f"缺少顶层字段: {key}")

    if errors:
        return errors

    # metadata
    meta = data.get("metadata", {})
    if not meta.get("title"):
        errors.append("metadata.title 不可为空")

    # config
    config = data.get("config", {})
    direction = config.get("direction", "TB")
    if direction not in VALID_DIRECTIONS:
        errors.append(f"config.direction 无效: {direction}，可选值: {VALID_DIRECTIONS}")

    # nodes
    nodes = data.get("nodes", [])
    if len(nodes) < 2:
        errors.append(f"节点数不足: {len(nodes)}，至少需要 2 个节点")

    node_ids = set()
    has_terminal_start = False
    has_terminal_end = False

    for i, node in enumerate(nodes):
        for key in REQUIRED_NODE_KEYS:
            if key not in node:
                errors.append(f"nodes[{i}] 缺少字段: {key}")

        nid = node.get("id", "")
        if nid in node_ids:
            errors.append(f"节点 ID 重复: {nid}")
        node_ids.add(nid)

        ntype = node.get("type", "")
        if ntype not in VALID_NODE_TYPES:
            errors.append(f"nodes[{i}] ({nid}) 类型无效: {ntype}")

        if ntype == "terminal":
            label = node.get("label", "").lower()
            if label in ("开始", "start", "begin"):
                has_terminal_start = True
            elif label in ("结束", "end", "finish"):
                has_terminal_end = True

        label = node.get("label", "")
        if len(label) > 15 and all(ord(c) > 127 for c in label):
            errors.append(f"nodes[{i}] ({nid}) 标签过长: {len(label)} 字符（建议 ≤15）")

    if not has_terminal_start:
        errors.append("缺少「开始」终端节点")
    if not has_terminal_end:
        errors.append("缺少「结束」终端节点")

    # edges
    edges = data.get("edges", [])
    for i, edge in enumerate(edges):
        for key in REQUIRED_EDGE_KEYS:
            if key not in edge:
                errors.append(f"edges[{i}] 缺少字段: {key}")

        src = edge.get("from", "")
        tgt = edge.get("to", "")
        if src and src not in node_ids:
            errors.append(f"edges[{i}] from 指向不存在的节点: {src}")
        if tgt and tgt not in node_ids:
            errors.append(f"edges[{i}] to 指向不存在的节点: {tgt}")

    # 孤立节点检查
    connected = set()
    for edge in edges:
        connected.add(edge.get("from", ""))
        connected.add(edge.get("to", ""))
    orphans = node_ids - connected
    if orphans:
        errors.append(f"存在孤立节点（未被任何边连接）: {orphans}")

    return errors


def main():
    if len(sys.argv) < 2:
        print("用法: python validate_structure.py <structure.json>")
        sys.exit(1)

    filepath = sys.argv[1]
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError) as e:
        print(f"❌ 文件读取失败: {e}")
        sys.exit(1)

    errors = validate(data)
    if errors:
        print(f"❌ 校验失败，发现 {len(errors)} 个问题：")
        for err in errors:
            print(f"   • {err}")
        sys.exit(1)
    else:
        print(f"✅ 校验通过：{len(data['nodes'])} 个节点，{len(data['edges'])} 条边")
        sys.exit(0)


if __name__ == "__main__":
    main()
```

---

## 📄 `scripts/validate_svg.py`

```python
#!/usr/bin/env python3
"""
validate_svg.py
校验输出的 SVG 文件是否合法且包含必要元素。
用法：python validate_svg.py output.svg
"""

import sys
import xml.etree.ElementTree as ET


def validate_svg(filepath: str) -> list[str]:
    errors = []

    try:
        tree = ET.parse(filepath)
        root = tree.getroot()
    except ET.ParseError as e:
        return [f"SVG XML 解析失败: {e}"]

    ns = {"svg": "http://www.w3.org/2000/svg"}
    tag = root.tag
    if not tag.endswith("svg"):
        errors.append(f"根元素应为 <svg>，实际为: {tag}")
        return errors

    # viewBox 检查
    viewbox = root.get("viewBox")
    if not viewbox:
        errors.append("缺少 viewBox 属性（影响响应式缩放）")
    else:
        parts = viewbox.split()
        if len(parts) != 4:
            errors.append(f"viewBox 格式异常: {viewbox}")

    # xmlns 检查
    xmlns = root.get("xmlns", "")
    if "w3.org/2000/svg" not in xmlns:
        errors.append("缺少 xmlns 声明")

    # font-family 检查
    font = root.get("font-family", "")
    has_font = bool(font)
    if not has_font:
        # 检查 style 标签中是否定义了 font-family
        for style in root.iter():
            if style.tag.endswith("style") and style.text and "font-family" in style.text:
                has_font = True
                break
    if not has_font:
        errors.append("建议在 <svg> 或 <style> 中定义 font-family")

    # defs 检查
    defs = root.find("svg:defs", ns) or root.find("defs")
    if defs is None:
        errors.append("缺少 <defs> 区域（建议定义 marker/filter）")

    # 节点检查（至少有 rect 或 polygon）
    shapes = list(root.iter())
    has_rect = any(el.tag.endswith("rect") for el in shapes)
    has_polygon = any(el.tag.endswith("polygon") for el in shapes)
    has_path = any(el.tag.endswith("path") for el in shapes)
    has_text = any(el.tag.endswith("text") for el in shapes)

    if not (has_rect or has_polygon):
        errors.append("未检测到节点图形（rect 或 polygon）")
    if not has_path:
        errors.append("未检测到连接线（path）")
    if not has_text:
        errors.append("未检测到文字元素（text）")

    # 文字内容非空检查
    empty_text_count = 0
    for el in shapes:
        if el.tag.endswith("text"):
            content = (el.text or "").strip()
            children = list(el)
            child_text = "".join((c.text or "") for c in children).strip()
            if not content and not child_text:
                empty_text_count += 1
    if empty_text_count > 0:
        errors.append(f"发现 {empty_text_count} 个空文字元素")

    return errors


def main():
    if len(sys.argv) < 2:
        print("用法: python validate_svg.py <output.svg>")
        sys.exit(1)

    filepath = sys.argv[1]
    errors = validate_svg(filepath)
    if errors:
        print(f"⚠️ 校验发现 {len(errors)} 个问题：")
        for err in errors:
            print(f"   • {err}")
        sys.exit(1)
    else:
        print("✅ SVG 校验通过")
        sys.exit(0)


if __name__ == "__main__":
    main()
```

---

## 📄 `assets/templates/structure_schema.json`

```json
{
  "_comment": "Phase 3 输出模板 — 流程结构数据 JSON Schema",
  "_version": "1.0.0",

  "metadata": {
    "title": "流程名称（必填）",
    "subtitle": "一句话概述（可选）",
    "footnote": "备注说明（可选）",
    "author": "",
    "date": ""
  },

  "config": {
    "direction": "TB | LR",
    "total_nodes": 0,
    "total_edges": 0,
    "has_branch": false,
    "has_loop": false,
    "has_parallel": false,
    "grid_rows": 0,
    "grid_cols": 0
  },

  "nodes": [
    {
      "id": "node_01",
      "type": "terminal | process | decision | io | subprocess",
      "label": "节点标签（≤15中文字符）",
      "description": "详细描述（可选，不会渲染到图中）",
      "group": "分组名称（可选，用于泳道或分区）",
      "position": {
        "row": 0,
        "col": 0
      }
    }
  ],

  "edges": [
    {
      "id": "edge_01",
      "from": "node_01",
      "to": "node_02",
      "label": "分支条件标签（顺序边留空）",
      "type": "normal | conditional",
      "line_style": "solid | dashed"
    }
  ],

  "annotations": [
    {
      "id": "anno_01",
      "target_node": "node_03",
      "text": "注释文字",
      "position": "right | left | top | bottom"
    }
  ]
}
```

---

## 📄 `assets/templates/style_schema.json`

```json
{
  "_comment": "Phase 5 输出模板 — 视觉设计方案 JSON Schema",
  "_version": "1.0.0",

  "canvas": {
    "background": "#FFFFFF",
    "padding": 50
  },

  "palette": {
    "name": "方案名称",
    "primary": "#3B82F6",
    "primary_light": "#EFF6FF",
    "secondary": "#10B981",
    "secondary_light": "#ECFDF5",
    "accent": "#F59E0B",
    "accent_light": "#FEF3C7",
    "neutral": "#64748B",
    "neutral_light": "#F1F5F9",
    "text_dark": "#1E293B",
    "text_medium": "#475569",
    "text_light": "#94A3B8",
    "border": "#CBD5E1",
    "connector": "#94A3B8",
    "shadow": "rgba(0, 0, 0, 0.08)"
  },

  "typography": {
    "font_family": "'PingFang SC', 'Microsoft YaHei', 'Helvetica Neue', Arial, sans-serif",
    "title": {
      "font_size": 22,
      "font_weight": 700,
      "color": "palette.text_dark",
      "letter_spacing": 1
    },
    "subtitle": {
      "font_size": 13,
      "font_weight": 400,
      "color": "palette.text_light"
    },
    "node_label": {
      "font_size": 13,
      "font_weight": 500,
      "color": "palette.text_dark"
    },
    "edge_label": {
      "font_size": 11,
      "font_weight": 500,
      "color": "palette.text_medium"
    },
    "footnote": {
      "font_size": 11,
      "font_weight": 400,
      "color": "palette.text_light",
      "font_style": "italic"
    }
  },

  "node_styles": {
    "terminal": {
      "min_width": 120,
      "height": 44,
      "rx": 22,
      "fill": "palette.primary",
      "stroke": "none",
      "stroke_width": 0,
      "text_color": "#FFFFFF",
      "shadow": true,
      "padding_h": 24,
      "padding_v": 10
    },
    "process": {
      "min_width": 150,
      "height": 52,
      "rx": 8,
      "fill": "#FFFFFF",
      "stroke": "palette.primary",
      "stroke_width": 1.5,
      "text_color": "palette.text_dark",
      "shadow": true,
      "padding_h": 20,
      "padding_v": 12
    },
    "decision": {
      "min_width": 110,
      "height": 70,
      "fill": "palette.accent_light",
      "stroke": "palette.accent",
      "stroke_width": 1.5,
      "text_color": "#92400E",
      "shadow": true,
      "shape": "diamond"
    },
    "io": {
      "min_width": 150,
      "height": 52,
      "skew_offset": 12,
      "fill": "palette.secondary_light",
      "stroke": "palette.secondary",
      "stroke_width": 1.5,
      "text_color": "#065F46",
      "shadow": true,
      "shape": "parallelogram"
    },
    "subprocess": {
      "min_width": 150,
      "height": 52,
      "rx": 8,
      "fill": "palette.primary_light",
      "stroke": "palette.primary",
      "stroke_width": 1.5,
      "text_color": "#1E40AF",
      "shadow": true,
      "inner_border": true,
      "inner_border_offset": 6
    }
  },

  "edge_styles": {
    "stroke_width": 1.5,
    "stroke_color": "palette.connector",
    "marker_size": 7,
    "marker_fill": "palette.connector",
    "routing": "orthogonal",
    "corner_radius": 5,
    "label_bg": "#FFFFFF",
    "label_bg_padding": 3
  },

  "layout": {
    "direction": "TB",
    "node_gap_vertical": 70,
    "node_gap_horizontal": 60,
    "title_margin_bottom": 30,
    "footnote_margin_top": 30,
    "group_padding": 20
  },

  "effects": {
    "shadow_filter": {
      "dx": 0,
      "dy": 2,
      "std_deviation": 4,
      "flood_color": "palette.shadow"
    }
  }
}
```

---

## 📄 `assets/templates/svg_skeleton.md`

````markdown
# SVG 骨架与组件使用说明

本文件定义了 Phase 6 生成 SVG 时必须遵循的代码结构和可复用的组件代码。

---

## 1. SVG 整体骨架

```xml
<svg
  xmlns="http://www.w3.org/2000/svg"
  viewBox="0 0 {WIDTH} {HEIGHT}"
  font-family="'PingFang SC', 'Microsoft YaHei', 'Helvetica Neue', Arial, sans-serif"
>
  <!-- ===== DEFS: 滤镜、标记、渐变 ===== -->
  <defs>
    {SHADOW_FILTER}
    {ARROW_MARKER}
  </defs>

  <!-- ===== 背景 ===== -->
  <rect width="100%" height="100%" fill="{BG_COLOR}" rx="0"/>

  <!-- ===== 标题区 ===== -->
  <text x="{TITLE_X}" y="{TITLE_Y}" font-size="{TITLE_SIZE}" font-weight="700"
        fill="{TITLE_COLOR}" text-anchor="middle">{TITLE}</text>
  <text x="{TITLE_X}" y="{SUBTITLE_Y}" font-size="{SUBTITLE_SIZE}" font-weight="400"
        fill="{SUBTITLE_COLOR}" text-anchor="middle">{SUBTITLE}</text>

  <!-- ===== 连接线层 ===== -->
  <g class="edges">
    {EDGE_ELEMENTS}
  </g>

  <!-- ===== 节点层 ===== -->
  <g class="nodes">
    {NODE_ELEMENTS}
  </g>

  <!-- ===== 注释层 ===== -->
  <g class="annotations">
    {ANNOTATION_ELEMENTS}
  </g>

  <!-- ===== 脚注 ===== -->
  <text x="{FN_X}" y="{FN_Y}" font-size="{FN_SIZE}" fill="{FN_COLOR}"
        text-anchor="middle" font-style="italic">{FOOTNOTE}</text>
</svg>
```

---

## 2. 组件模板

### 2.1 阴影滤镜
```xml
<filter id="shadow" x="-10%" y="-10%" width="130%" height="140%">
  <feDropShadow dx="0" dy="2" stdDeviation="4" flood-color="rgba(0,0,0,0.08)" flood-opacity="1"/>
</filter>
```

### 2.2 箭头标记
```xml
<marker id="arrowhead" viewBox="0 0 10 10" refX="10" refY="5"
        markerWidth="7" markerHeight="7" orient="auto-start-reverse" fill="{CONNECTOR_COLOR}">
  <path d="M 0 0 L 10 5 L 0 10 Z"/>
</marker>
```

### 2.3 终端节点（开始/结束）
```xml
<g filter="url(#shadow)">
  <rect x="{X}" y="{Y}" width="{W}" height="{H}" rx="{H/2}"
        fill="{FILL}" stroke="none"/>
  <text x="{CX}" y="{CY}" text-anchor="middle" dominant-baseline="central"
        font-size="13" font-weight="500" fill="#FFFFFF">{LABEL}</text>
</g>
```

### 2.4 处理节点
```xml
<g filter="url(#shadow)">
  <rect x="{X}" y="{Y}" width="{W}" height="{H}" rx="8"
        fill="#FFFFFF" stroke="{BORDER_COLOR}" stroke-width="1.5"/>
  <text x="{CX}" y="{CY}" text-anchor="middle" dominant-baseline="central"
        font-size="13" font-weight="500" fill="{TEXT_COLOR}">{LABEL}</text>
</g>
```

### 2.5 判断节点（菱形）
```xml
<g filter="url(#shadow)">
  <polygon points="{CX},{Y} {X+W},{CY} {CX},{Y+H} {X},{CY}"
           fill="{FILL}" stroke="{BORDER_COLOR}" stroke-width="1.5"/>
  <text x="{CX}" y="{CY}" text-anchor="middle" dominant-baseline="central"
        font-size="12" font-weight="500" fill="{TEXT_COLOR}">{LABEL}</text>
</g>
```

> 菱形坐标说明：  
> - 上顶点：(CX, Y)  
> - 右顶点：(X+W, CY)  
> - 下顶点：(CX, Y+H)  
> - 左顶点：(X, CY)  
> 其中 CX = X + W/2，CY = Y + H/2

### 2.6 子流程节点（双边框）
```xml
<g filter="url(#shadow)">
  <rect x="{X}" y="{Y}" width="{W}" height="{H}" rx="8"
        fill="{FILL}" stroke="{BORDER_COLOR}" stroke-width="1.5"/>
  <line x1="{X+6}" y1="{Y}" x2="{X+6}" y2="{Y+H}"
        stroke="{BORDER_COLOR}" stroke-width="1"/>
  <line x1="{X+W-6}" y1="{Y}" x2="{X+W-6}" y2="{Y+H}"
        stroke="{BORDER_COLOR}" stroke-width="1"/>
  <text x="{CX}" y="{CY}" text-anchor="middle" dominant-baseline="central"
        font-size="13" font-weight="500" fill="{TEXT_COLOR}">{LABEL}</text>
</g>
```

### 2.7 正交连接线（直角折线）

**直线连接（同列上下相邻）：**
```xml
<path d="M {FROM_CX},{FROM_BOTTOM} L {TO_CX},{TO_TOP}"
      fill="none" stroke="{COLOR}" stroke-width="1.5" marker-end="url(#arrowhead)"/>
```

**折线连接（不同列）：**
```xml
<path d="M {FROM_CX},{FROM_BOTTOM}
         L {FROM_CX},{MID_Y}
         Q {FROM_CX},{MID_Y+R} {FROM_CX+R},{MID_Y+R}
         L {TO_CX-R},{MID_Y+R}
         Q {TO_CX},{MID_Y+R} {TO_CX},{MID_Y+2R}
         L {TO_CX},{TO_TOP}"
      fill="none" stroke="{COLOR}" stroke-width="1.5" marker-end="url(#arrowhead)"/>
```

> MID_Y = (FROM_BOTTOM + TO_TOP) / 2，R = corner_radius

### 2.8 连接线标签（分支条件）
```xml
<rect x="{LX-PD}" y="{LY-12}" width="{LW+PD*2}" height="18" rx="3"
      fill="#FFFFFF" stroke="none"/>
<text x="{LX}" y="{LY}" font-size="11" font-weight="500"
      fill="{LABEL_COLOR}" text-anchor="middle" dominant-baseline="central">{LABEL}</text>
```

---

## 3. 坐标计算公式

### TB（自上而下）模式

```
TITLE_Y       = padding
SUBTITLE_Y    = TITLE_Y + 28
CONTENT_TOP   = SUBTITLE_Y + title_margin_bottom

对于 position (row, col) 的节点:
  CX = padding + col × (max_node_width + gap_h) + max_node_width / 2
  CY = CONTENT_TOP + row × (max_node_height + gap_v) + max_node_height / 2
  X  = CX - node_width / 2
  Y  = CY - node_height / 2

画布总宽 = padding × 2 + grid_cols × max_node_width + (grid_cols - 1) × gap_h
画布总高 = CONTENT_TOP + grid_rows × max_node_height + (grid_rows - 1) × gap_v + padding + footnote_area
```

### 连接点位置
```
节点上中: (CX, Y)
节点下中: (CX, Y + H)
节点左中: (X, CY)
节点右中: (X + W, CY)
```

---

## 4. 文字折行处理

当标签文字宽度超过节点内部可用宽度时，使用 `<tspan>` 折行：

```xml
<text x="{CX}" y="{CY}" text-anchor="middle" font-size="13">
  <tspan x="{CX}" dy="-0.6em">第一行文字</tspan>
  <tspan x="{CX}" dy="1.2em">第二行文字</tspan>
</text>
```

> 中文字符宽度估算：约为 font_size × 1.05  
> 英文字符宽度估算：约为 font_size × 0.55  
> 可用宽度 = node_width - padding_h × 2
````

---

## 📄 `assets/references/color_palettes.json`

```json
{
  "_comment": "预设配色方案库，按领域分类",

  "palettes": [
    {
      "id": "business-blue",
      "name": "商务蓝",
      "suitable_for": ["业务流程", "审批流程", "通用"],
      "primary": "#3B82F6",
      "primary_light": "#EFF6FF",
      "secondary": "#10B981",
      "secondary_light": "#ECFDF5",
      "accent": "#F59E0B",
      "accent_light": "#FEF3C7",
      "text_dark": "#1E293B",
      "text_medium": "#475569",
      "text_light": "#94A3B8",
      "border": "#CBD5E1",
      "connector": "#94A3B8",
      "canvas_bg": "#FFFFFF",
      "shadow": "rgba(0,0,0,0.08)"
    },
    {
      "id": "tech-indigo",
      "name": "科技靛蓝",
      "suitable_for": ["技术流程", "系统架构", "CI/CD"],
      "primary": "#6366F1",
      "primary_light": "#EEF2FF",
      "secondary": "#06B6D4",
      "secondary_light": "#ECFEFF",
      "accent": "#EC4899",
      "accent_light": "#FDF2F8",
      "text_dark": "#1E1B4B",
      "text_medium": "#4338CA",
      "text_light": "#A5B4FC",
      "border": "#C7D2FE",
      "connector": "#A5B4FC",
      "canvas_bg": "#FAFAFE",
      "shadow": "rgba(99,102,241,0.1)"
    },
    {
      "id": "nature-green",
      "name": "自然绿",
      "suitable_for": ["产品流程", "用户旅程", "教育"],
      "primary": "#059669",
      "primary_light": "#ECFDF5",
      "secondary": "#0891B2",
      "secondary_light": "#ECFEFF",
      "accent": "#D97706",
      "accent_light": "#FFFBEB",
      "text_dark": "#064E3B",
      "text_medium": "#047857",
      "text_light": "#6EE7B7",
      "border": "#A7F3D0",
      "connector": "#6EE7B7",
      "canvas_bg": "#F0FDF4",
      "shadow": "rgba(5,150,105,0.08)"
    },
    {
      "id": "warm-coral",
      "name": "暖珊瑚",
      "suitable_for": ["营销流程", "客户服务", "创意流程"],
      "primary": "#F43F5E",
      "primary_light": "#FFF1F2",
      "secondary": "#8B5CF6",
      "secondary_light": "#F5F3FF",
      "accent": "#F59E0B",
      "accent_light": "#FEF3C7",
      "text_dark": "#881337",
      "text_medium": "#E11D48",
      "text_light": "#FDA4AF",
      "border": "#FECDD3",
      "connector": "#FDA4AF",
      "canvas_bg": "#FFFBFB",
      "shadow": "rgba(244,63,94,0.08)"
    },
    {
      "id": "minimal-slate",
      "name": "极简灰",
      "suitable_for": ["通用", "正式文档", "高对比度"],
      "primary": "#334155",
      "primary_light": "#F1F5F9",
      "secondary": "#475569",
      "secondary_light": "#F8FAFC",
      "accent": "#0EA5E9",
      "accent_light": "#F0F9FF",
      "text_dark": "#0F172A",
      "text_medium": "#334155",
      "text_light": "#94A3B8",
      "border": "#CBD5E1",
      "connector": "#94A3B8",
      "canvas_bg": "#FFFFFF",
      "shadow": "rgba(0,0,0,0.06)"
    },
    {
      "id": "dark-mode",
      "name": "暗色模式",
      "suitable_for": ["技术文档", "演示文稿（深色背景）"],
      "primary": "#60A5FA",
      "primary_light": "#1E3A5F",
      "secondary": "#34D399",
      "secondary_light": "#0D3B2E",
      "accent": "#FBBF24",
      "accent_light": "#3D3100",
      "text_dark": "#F1F5F9",
      "text_medium": "#CBD5E1",
      "text_light": "#64748B",
      "border": "#475569",
      "connector": "#64748B",
      "canvas_bg": "#0F172A",
      "shadow": "rgba(0,0,0,0.3)"
    }
  ]
}
```

---

## 📄 `assets/references/node_types.md`

````markdown
# 标准节点类型定义

本文件定义了流程图中支持的所有节点类型，包含其语义、形状和使用场景。

---

## 节点类型一览

| type        | 中文名   | 形状       | 用途                         |
|-------------|----------|------------|------------------------------|
| terminal    | 终端     | 胶囊/椭圆  | 流程的开始和结束               |
| process     | 处理     | 圆角矩形   | 具体的操作步骤或动作           |
| decision    | 判断     | 菱形       | 条件分支判断                   |
| io          | 输入/输出 | 平行四边形  | 数据的输入或输出               |
| subprocess  | 子流程   | 双边框矩形  | 引用其他已定义的流程           |

---

## 各类型详细说明

### terminal（终端节点）

- **用途**：标记流程的起点和终点
- **标签规范**：
  - 开始节点：「开始」「Start」或具体触发条件（如「收到请求」）
  - 结束节点：「结束」「End」或具体结束状态（如「流程完成」）
- **数量规则**：
  - 每个流程必须有且仅有 1 个开始节点
  - 可以有 1 个或多个结束节点（多出口流程）
- **SVG 形状**：rx = height / 2 的圆角矩形（胶囊形）
- **默认配色**：实心填充主色，白色文字

### process（处理节点）

- **用途**：表示一个具体的操作、动作或处理步骤
- **标签规范**：使用「动词 + 宾语」结构，如「审核订单」「发送邮件」
- **SVG 形状**：rx = 8 的圆角矩形
- **默认配色**：白底 + 主色边框 + 深色文字

### decision（判断节点）

- **用途**：表示一个条件判断，产生 2 个或多个分支
- **标签规范**：
  - 使用问句形式：如「库存充足？」「金额>1000？」
  - 或简短条件词：如「审核结果」
- **分支规则**：
  - 必须有至少 2 条出边
  - 每条出边必须有标签（如「是/否」「通过/拒绝」「>1000/≤1000」）
  - TB 模式下：「是」通常向下，「否」通常向右或向左
- **SVG 形状**：菱形（polygon 四个顶点）
- **默认配色**：浅色填充（accent_light）+ 强调色边框

### io（输入/输出节点）

- **用途**：表示数据的输入来源或输出目标
- **标签规范**：如「用户输入表单」「输出报告」「读取数据库」
- **SVG 形状**：平行四边形（polygon 四个偏移顶点）
- **默认配色**：浅绿底 + 绿色边框

### subprocess（子流程节点）

- **用途**：引用另一个已定义的流程，避免当前图过于复杂
- **标签规范**：子流程的名称，如「支付处理流程」「身份验证流程」
- **SVG 形状**：圆角矩形 + 内部两侧竖线
- **默认配色**：浅主色底 + 主色边框

---

## 连接线类型

| 类型         | 线型   | 用途                    |
|-------------|--------|------------------------|
| normal      | 实线    | 顺序流转（默认）         |
| conditional | 实线    | 条件分支（带标签）       |
| association | 虚线    | 关联注释或补充说明       |

---

## 特殊约定

1. **判断节点的出边方向**（TB 模式）：
   - 主路径（通常为「是」）：向下
   - 备选路径（通常为「否」）：向左或向右
   - 如有多条件：按逻辑优先级向下、右、左排列

2. **节点标签长度**：
   - 硬限制：≤ 15 个中文字符 或 ≤ 30 个英文字符
   - 超长时在节点内自动折行（最多 2 行）

3. **节点 ID 命名**：
   - 格式：`node_01`, `node_02`, ..., `node_99`
   - 按流程执行顺序编号
   - 分支上的节点紧跟在判断节点后编号
````

---

## 📄 `assets/references/layout_rules.md`

````markdown
# 布局规则与最佳实践

---

## 1. 流向选择策略

| 条件 | 推荐流向 | 原因 |
|------|---------|------|
| 步骤数 ≤ 10，有分支 | TB（自上而下） | 分支左右展开，直观清晰 |
| 步骤数 > 10，线性为主 | LR（从左到右） | 避免纵向过长 |
| 大量并行分支 | TB | 并行横向排列更自然 |
| 泳道/角色区分明显 | LR | 泳道纵向分隔，横向流转 |

**默认**：除非有明确理由，一律使用 TB。

---

## 2. 网格定位规则

### TB 模式（自上而下）

```
        col=0      col=1      col=2      col=3
row=0              [开始]
row=1              [步骤1]
row=2              {判断?}
row=3   [否路径]              [是路径]
row=4   [处理A]               [处理B]
row=5              [汇合]
row=6              [结束]
```

**规则**：
- 主流程走 col=1（居中列）
- 分支向 col=0（左）和 col=2（右）展开
- 二次分支可用 col=3 或更多列
- 汇合节点回到主流程列
- 同层级节点在同一 row

### LR 模式（从左到右）

```
        row=0     [开始] → [步骤1] → {判断?} → [是路径] → [结束]
        row=1                           ↓
                                    [否路径] → [处理] ──→ ↑
```

**规则**：
- 主流程走 row=0
- 分支向 row=1, row=2 展开
- 回路通过底部绕回

---

## 3. 间距规范

| 参数 | TB 模式 | LR 模式 | 说明 |
|------|---------|---------|------|
| node_gap_vertical | 70px | 50px | 节点垂直间距 |
| node_gap_horizontal | 60px | 80px | 节点水平间距 |
| canvas_padding | 50px | 50px | 画布内边距 |
| title_margin_bottom | 30px | 30px | 标题与内容间距 |
| footnote_margin_top | 30px | 30px | 内容与脚注间距 |

---

## 4. 节点尺寸规范

| 节点类型 | 最小宽度 | 高度 | 备注 |
|---------|---------|------|------|
| terminal | 120px | 44px | 胶囊形 |
| process | 150px | 52px | 圆角矩形 |
| decision | 120px | 70px | 菱形（宽×高） |
| io | 150px | 52px | 平行四边形 |
| subprocess | 150px | 52px | 双边框矩形 |

**自适应规则**：
- 节点宽度 = max(min_width, 文字宽度 + padding_h × 2)
- 同类型节点取最大宽度统一（保持视觉整齐）
- 同一行的节点高度统一

---

## 5. 连接线路由规则

### 优先级策略

1. **直线优先**：同列上下相邻节点用直线连接
2. **单折线次之**：不同列节点用 L 形折线（先垂直再水平，或先水平再垂直）
3. **双折线兜底**：需要绕过障碍时用 Z 形双折线

### 避免交叉

- 调整分支节点的左右位置，使连接线不交叉
- 如无法避免交叉，使主流程连线在上层（先渲染分支线）

### 回路处理

- 循环回路从目标节点的左侧绕行
- 使用虚线或不同颜色区分回路

---

## 6. 视觉层次

```
最底层    画布背景
   ↑      分组/泳道背景
   ↑      连接线
   ↑      节点图形（含阴影）
   ↑      节点文字
   ↑      连接线标签（带白色背景遮挡）
最顶层    标题 / 脚注 / 注释
```

---

## 7. 标题与备注布局

```
┌──────────────────────────────────────────┐
│  (padding)                               │
│         流程标题（居中，大号粗体）          │
│         副标题（居中，小号灰色）            │
│  (title_margin_bottom)                   │
│                                          │
│         ┌──────────────┐                 │
│         │   流程内容    │                 │
│         └──────────────┘                 │
│                                          │
│  (footnote_margin_top)                   │
│         脚注/备注（居中，小号斜体灰色）     │
│  (padding)                               │
└──────────────────────────────────────────┘
```

---

## 8. 常见反模式（避免）

| ❌ 反模式 | ✅ 正确做法 |
|-----------|------------|
| 节点大小不一致 | 同类型节点统一尺寸 |
| 间距不均匀 | 使用网格对齐 |
| 连接线斜着穿越多个节点 | 使用正交折线 |
| 判断分支没有标签 | 每条分支必须标注条件 |
| 文字溢出节点 | 缩短标签或自动折行 |
| 颜色过多 | 限制在配色方案的 3-5 种色 |
| 阴影过重 | 使用轻阴影 (blur ≤ 6, opacity ≤ 0.1) |
````

---

## 📄 `assets/examples/full_pipeline_demo.md`

````markdown
# 完整流水线演示：用户注册流程

---

## 用户原始输入

```
用户打开注册页面，填写用户名、邮箱和密码。系统检查邮箱是否已注册，
如果已注册提示用户换一个邮箱，如果没注册就发送验证邮件。
用户收到邮件点击验证链接，系统验证通过后创建账户，注册成功。
如果验证链接过期，用户需要重新申请验证邮件。
```

---

## Phase 1: 输入分析报告

```
- 输入类型：自然语言段落描述
- 领域分类：业务流程（用户注册）
- 识别实体：6 个动作，4 个对象，2 个角色，3 个条件
  - 动作：打开页面、填写信息、检查邮箱、发送邮件、点击链接、创建账户
  - 对象：注册页面、注册信息、验证邮件、账户
  - 角色：用户、系统
  - 条件：邮箱是否已注册、验证是否通过、链接是否过期
- 关系类型：顺序 ✓ | 分支 ✓ | 并行 ✗ | 循环 ✓（重新验证）| 汇聚 ✓
- 完整度：4/5
- 缺失项：
  - 密码格式校验未提及（补充为隐含步骤）
  - 验证邮件的有效期未明确（补充合理默认值）
```

---

## Phase 2: 优化文字稿

### 流程名称：用户注册流程
### 流程概述：新用户通过邮箱注册账户的完整流程

### 参与角色
| 角色 | 职责 |
|------|------|
| 用户 | 填写注册信息、验证邮箱 |
| 系统 | 校验信息、发送验证邮件、创建账户 |

### 流程步骤

**1. 开始**（节点标签：开始）
- 触发条件：用户访问注册页面

**2. 填写注册信息**（节点标签：填写注册信息）
- 描述：用户在注册页面填写用户名、邮箱地址和密码
- 角色：用户
- 输入：注册页面表单
- 输出：用户名、邮箱、密码

**3. 校验邮箱唯一性**（节点标签：邮箱已注册？）
- 类型：条件判断
- 条件：系统检查该邮箱是否已被注册
  - ✅ 是（已注册）→ 转到步骤 4
  - ❌ 否（未注册）→ 转到步骤 5

**4. 提示更换邮箱**（节点标签：提示更换邮箱）
- 描述：系统提示用户该邮箱已注册，建议更换
- 角色：系统
- → 返回步骤 2

**5. 发送验证邮件**（节点标签：发送验证邮件）
- 描述：系统向用户邮箱发送包含验证链接的邮件
- 角色：系统

**6. 点击验证链接**（节点标签：点击验证链接）
- 描述：用户打开邮件并点击验证链接
- 角色：用户

**7. 验证链接有效性**（节点标签：链接有效？）
- 类型：条件判断
- 条件：系统检查验证链接是否在有效期内
  - ✅ 是 → 转到步骤 8
  - ❌ 否（已过期）→ 转到步骤 5（重新发送）

**8. 创建账户**（节点标签：创建账户）
- 描述：系统创建新用户账户，注册完成
- 角色：系统

**9. 注册成功**（节点标签：结束）
- 结束状态：用户注册成功，可进行登录

### 补充说明
- 验证链接默认有效期为 24 小时
- 密码需满足最低安全要求（此处简化未展示）

---

## Phase 3: 结构数据 (JSON)

```json
{
  "metadata": {
    "title": "用户注册流程",
    "subtitle": "新用户通过邮箱注册账户的完整流程",
    "footnote": "验证链接有效期为 24 小时"
  },
  "config": {
    "direction": "TB",
    "total_nodes": 9,
    "total_edges": 10,
    "has_branch": true,
    "has_loop": true,
    "has_parallel": false,
    "grid_rows": 8,
    "grid_cols": 3
  },
  "nodes": [
    {"id": "node_01", "type": "terminal",  "label": "开始",         "position": {"row": 0, "col": 1}},
    {"id": "node_02", "type": "process",   "label": "填写注册信息",   "position": {"row": 1, "col": 1}},
    {"id": "node_03", "type": "decision",  "label": "邮箱已注册？",   "position": {"row": 2, "col": 1}},
    {"id": "node_04", "type": "process",   "label": "提示更换邮箱",   "position": {"row": 2, "col": 2}},
    {"id": "node_05", "type": "process",   "label": "发送验证邮件",   "position": {"row": 3, "col": 1}},
    {"id": "node_06", "type": "process",   "label": "点击验证链接",   "position": {"row": 4, "col": 1}},
    {"id": "node_07", "type": "decision",  "label": "链接有效？",     "position": {"row": 5, "col": 1}},
    {"id": "node_08", "type": "process",   "label": "创建账户",       "position": {"row": 6, "col": 1}},
    {"id": "node_09", "type": "terminal",  "label": "结束",         "position": {"row": 7, "col": 1}}
  ],
  "edges": [
    {"id": "edge_01", "from": "node_01", "to": "node_02", "label": "",       "type": "normal"},
    {"id": "edge_02", "from": "node_02", "to": "node_03", "label": "",       "type": "normal"},
    {"id": "edge_03", "from": "node_03", "to": "node_04", "label": "是",     "type": "conditional"},
    {"id": "edge_04", "from": "node_03", "to": "node_05", "label": "否",     "type": "conditional"},
    {"id": "edge_05", "from": "node_04", "to": "node_02", "label": "",       "type": "normal"},
    {"id": "edge_06", "from": "node_05", "to": "node_06", "label": "",       "type": "normal"},
    {"id": "edge_07", "from": "node_06", "to": "node_07", "label": "",       "type": "normal"},
    {"id": "edge_08", "from": "node_07", "to": "node_08", "label": "是",     "type": "conditional"},
    {"id": "edge_09", "from": "node_07", "to": "node_05", "label": "否",     "type": "conditional"},
    {"id": "edge_10", "from": "node_08", "to": "node_09", "label": "",       "type": "normal"}
  ],
  "annotations": []
}
```

---

## Phase 4: 文本线框图

### 布局参数
- 流向：TB（自上而下）
- 网格：8 行 × 3 列
- 节点数：9
- 连接数：10

### ASCII 线框

```
                  col=0          col=1            col=2

  row=0                      (( 开始 ))

                                  │
                                  ▼
  row=1                    [ 填写注册信息 ] ◄──────────┐
                                  │                    │
                                  ▼                    │
  row=2                    { 邮箱已注册？ } ──是──► [ 提示更换邮箱 ]
                                  │
                                 否
                                  │
                                  ▼
  row=3                    [ 发送验证邮件 ] ◄──┐
                                  │           │
                                  ▼           │
  row=4                    [ 点击验证链接 ]     │
                                  │           │
                                  ▼           │
  row=5                    { 链接有效？ } ─否──┘
                                  │
                                 是
                                  │
                                  ▼
  row=6                      [ 创建账户 ]

                                  │
                                  ▼
  row=7                      (( 结束 ))
```

---

## Phase 5: 视觉设计方案

```json
{
  "canvas": {
    "background": "#FFFFFF",
    "padding": 50
  },
  "palette": {
    "name": "business-blue",
    "primary": "#3B82F6",
    "primary_light": "#EFF6FF",
    "accent": "#F59E0B",
    "accent_light": "#FEF3C7",
    "text_dark": "#1E293B",
    "text_medium": "#475569",
    "text_light": "#94A3B8",
    "connector": "#94A3B8",
    "shadow": "rgba(0,0,0,0.08)"
  },
  "typography": {
    "font_family": "'PingFang SC', 'Microsoft YaHei', 'Helvetica Neue', Arial, sans-serif",
    "title": {"font_size": 22, "font_weight": 700, "color": "#1E293B"},
    "subtitle": {"font_size": 13, "font_weight": 400, "color": "#94A3B8"},
    "node_label": {"font_size": 13, "font_weight": 500},
    "edge_label": {"font_size": 11, "font_weight": 500, "color": "#475569"},
    "footnote": {"font_size": 11, "color": "#94A3B8", "font_style": "italic"}
  },
  "node_styles": {
    "terminal": {"width": 120, "height": 44, "rx": 22, "fill": "#3B82F6", "text_color": "#FFFFFF"},
    "process":  {"width": 160, "height": 52, "rx": 8,  "fill": "#FFFFFF", "stroke": "#3B82F6", "text_color": "#1E293B"},
    "decision": {"width": 130, "height": 76, "fill": "#FEF3C7", "stroke": "#F59E0B", "text_color": "#92400E"}
  },
  "edge_styles": {
    "stroke_width": 1.5,
    "stroke_color": "#94A3B8",
    "marker_size": 7,
    "corner_radius": 5
  },
  "layout": {
    "direction": "TB",
    "node_gap_vertical": 70,
    "node_gap_horizontal": 80,
    "title_margin_bottom": 30,
    "footnote_margin_top": 25
  }
}
```

---

## Phase 6: SVG 输出

```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 620 920"
     font-family="'PingFang SC','Microsoft YaHei','Helvetica Neue',Arial,sans-serif">

  <defs>
    <filter id="shadow" x="-10%" y="-10%" width="130%" height="140%">
      <feDropShadow dx="0" dy="2" stdDeviation="4" flood-color="rgba(0,0,0,0.08)" flood-opacity="1"/>
    </filter>
    <marker id="arrowhead" viewBox="0 0 10 10" refX="10" refY="5"
            markerWidth="7" markerHeight="7" orient="auto-start-reverse" fill="#94A3B8">
      <path d="M 0 0 L 10 5 L 0 10 Z"/>
    </marker>
  </defs>

  <!-- 背景 -->
  <rect width="100%" height="100%" fill="#FFFFFF"/>

  <!-- 标题 -->
  <text x="310" y="38" text-anchor="middle" font-size="22" font-weight="700" fill="#1E293B">用户注册流程</text>
  <text x="310" y="58" text-anchor="middle" font-size="13" fill="#94A3B8">新用户通过邮箱注册账户的完整流程</text>

  <!-- ===== 连接线层 ===== -->
  <g class="edges">
    <!-- edge_01: 开始 → 填写注册信息 -->
    <path d="M 260,118 L 260,148" fill="none" stroke="#94A3B8" stroke-width="1.5" marker-end="url(#arrowhead)"/>

    <!-- edge_02: 填写注册信息 → 邮箱已注册？ -->
    <path d="M 260,200 L 260,240" fill="none" stroke="#94A3B8" stroke-width="1.5" marker-end="url(#arrowhead)"/>

    <!-- edge_03: 邮箱已注册？ →是→ 提示更换邮箱 -->
    <path d="M 325,278 L 420,278" fill="none" stroke="#94A3B8" stroke-width="1.5" marker-end="url(#arrowhead)"/>
    <rect x="350" y="268" width="24" height="18" rx="3" fill="#FFFFFF" stroke="none"/>
    <text x="362" y="280" text-anchor="middle" dominant-baseline="central" font-size="11" font-weight="500" fill="#475569">是</text>

    <!-- edge_04: 邮箱已注册？ →否→ 发送验证邮件 -->
    <path d="M 260,316 L 260,360" fill="none" stroke="#94A3B8" stroke-width="1.5" marker-end="url(#arrowhead)"/>
    <rect x="248" y="325" width="24" height="18" rx="3" fill="#FFFFFF" stroke="none"/>
    <text x="260" y="337" text-anchor="middle" dominant-baseline="central" font-size="11" font-weight="500" fill="#475569">否</text>

    <!-- edge_05: 提示更换邮箱 → 填写注册信息（回路） -->
    <path d="M 500,278 L 530,278 Q 540,278 540,268 L 540,174 Q 540,164 530,164 L 340,164"
          fill="none" stroke="#94A3B8" stroke-width="1.5" marker-end="url(#arrowhead)"/>

    <!-- edge_06: 发送验证邮件 → 点击验证链接 -->
    <path d="M 260,412 L 260,450" fill="none" stroke="#94A3B8" stroke-width="1.5" marker-end="url(#arrowhead)"/>

    <!-- edge_07: 点击验证链接 → 链接有效？ -->
    <path d="M 260,502 L 260,540" fill="none" stroke="#94A3B8" stroke-width="1.5" marker-end="url(#arrowhead)"/>

    <!-- edge_08: 链接有效？ →是→ 创建账户 -->
    <path d="M 260,616 L 260,660" fill="none" stroke="#94A3B8" stroke-width="1.5" marker-end="url(#arrowhead)"/>
    <rect x="248" y="625" width="24" height="18" rx="3" fill="#FFFFFF" stroke="none"/>
    <text x="260" y="637" text-anchor="middle" dominant-baseline="central" font-size="11" font-weight="500" fill="#475569">是</text>

    <!-- edge_09: 链接有效？ →否→ 发送验证邮件（回路） -->
    <path d="M 195,578 L 110,578 Q 100,578 100,568 L 100,386 Q 100,376 110,376 L 180,376"
          fill="none" stroke="#94A3B8" stroke-width="1.5" marker-end="url(#arrowhead)"/>
    <rect x="128" y="568" width="24" height="18" rx="3" fill="#FFFFFF" stroke="none"/>
    <text x="140" y="580" text-anchor="middle" dominant-baseline="central" font-size="11" font-weight="500" fill="#475569">否</text>

    <!-- edge_10: 创建账户 → 结束 -->
    <path d="M 260,712 L 260,750" fill="none" stroke="#94A3B8" stroke-width="1.5" marker-end="url(#arrowhead)"/>
  </g>

  <!-- ===== 节点层 ===== -->
  <g class="nodes">
    <!-- node_01: 开始 -->
    <g filter="url(#shadow)">
      <rect x="200" y="74" width="120" height="44" rx="22" fill="#3B82F6"/>
      <text x="260" y="96" text-anchor="middle" dominant-baseline="central"
            font-size="14" font-weight="500" fill="#FFFFFF">开始</text>
    </g>

    <!-- node_02: 填写注册信息 -->
    <g filter="url(#shadow)">
      <rect x="180" y="148" width="160" height="52" rx="8" fill="#FFFFFF" stroke="#3B82F6" stroke-width="1.5"/>
      <text x="260" y="174" text-anchor="middle" dominant-baseline="central"
            font-size="13" font-weight="500" fill="#1E293B">填写注册信息</text>
    </g>

    <!-- node_03: 邮箱已注册？（菱形） -->
    <g filter="url(#shadow)">
      <polygon points="260,240 325,278 260,316 195,278" fill="#FEF3C7" stroke="#F59E0B" stroke-width="1.5"/>
      <text x="260" y="278" text-anchor="middle" dominant-baseline="central"
            font-size="12" font-weight="500" fill="#92400E">邮箱已注册？</text>
    </g>

    <!-- node_04: 提示更换邮箱 -->
    <g filter="url(#shadow)">
      <rect x="420" y="252" width="160" height="52" rx="8" fill="#FFFFFF" stroke="#3B82F6" stroke-width="1.5"/>
      <text x="500" y="278" text-anchor="middle" dominant-baseline="central"
            font-size="13" font-weight="500" fill="#1E293B">提示更换邮箱</text>
    </g>

    <!-- node_05: 发送验证邮件 -->
    <g filter="url(#shadow)">
      <rect x="180" y="360" width="160" height="52" rx="8" fill="#FFFFFF" stroke="#3B82F6" stroke-width="1.5"/>
      <text x="260" y="386" text-anchor="middle" dominant-baseline="central"
            font-size="13" font-weight="500" fill="#1E293B">发送验证邮件</text>
    </g>

    <!-- node_06: 点击验证链接 -->
    <g filter="url(#shadow)">
      <rect x="180" y="450" width="160" height="52" rx="8" fill="#FFFFFF" stroke="#3B82F6" stroke-width="1.5"/>
      <text x="260" y="476" text-anchor="middle" dominant-baseline="central"
            font-size="13" font-weight="500" fill="#1E293B">点击验证链接</text>
    </g>

    <!-- node_07: 链接有效？（菱形） -->
    <g filter="url(#shadow)">
      <polygon points="260,540 325,578 260,616 195,578" fill="#FEF3C7" stroke="#F59E0B" stroke-width="1.5"/>
      <text x="260" y="578" text-anchor="middle" dominant-baseline="central"
            font-size="12" font-weight="500" fill="#92400E">链接有效？</text>
    </g>

    <!-- node_08: 创建账户 -->
    <g filter="url(#shadow)">
      <rect x="180" y="660" width="160" height="52" rx="8" fill="#FFFFFF" stroke="#3B82F6" stroke-width="1.5"/>
      <text x="260" y="686" text-anchor="middle" dominant-baseline="central"
            font-size="13" font-weight="500" fill="#1E293B">创建账户</text>
    </g>

    <!-- node_09: 结束 -->
    <g filter="url(#shadow)">
      <rect x="200" y="750" width="120" height="44" rx="22" fill="#3B82F6"/>
      <text x="260" y="772" text-anchor="middle" dominant-baseline="central"
            font-size="14" font-weight="500" fill="#FFFFFF">结束</text>
    </g>
  </g>

  <!-- 脚注 -->
  <text x="310" y="830" text-anchor="middle" font-size="11" fill="#94A3B8" font-style="italic">
    注：验证链接有效期为 24 小时
  </text>
</svg>
```

> 以上 SVG 代码可直接保存为 `.svg` 文件查看效果。

---

*演示结束。每个 Phase 的输出都是独立可复用的中间产物。*
````

---

## 使用说明总结

**最小化使用**：只需将 `skill.md` 引入你的系统提示词，模型即可按照六阶段流水线处理用户的流程描述请求。

**完整使用**：将整个 `skill-flowchart-generator/` 文件夹作为上下文提供给模型，可获得更稳定、更高质量的输出——模板文件提供了结构约束，参考文件提供了设计素材库，示例文件提供了 few-shot 学习样本。

**调试技巧**：如果输出不符合预期，可以要求模型「显示所有中间步骤」，然后定位问题出在哪个 Phase，针对性修正。