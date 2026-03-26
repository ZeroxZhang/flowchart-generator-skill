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

---

## 使用说明总结

**最小化使用**：只需将 `skill.md` 引入你的系统提示词，模型即可按照六阶段流水线处理用户的流程描述请求。

**完整使用**：将整个 `skill-flowchart-generator/` 文件夹作为上下文提供给模型，可获得更稳定、更高质量的输出——模板文件提供了结构约束，参考文件提供了设计素材库，示例文件提供了 few-shot 学习样本。

**调试技巧**：如果输出不符合预期，可以要求模型「显示所有中间步骤」，然后定位问题出在哪个 Phase，针对性修正。
