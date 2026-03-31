# Interaction Flow Reference / 交互流程参考

Detailed reference for the 5-step interactive conversation flow.

---

## Flow Overview

```
[User Input] → [Parse Intent] → [Ask 5 Preferences] → [Confirm] → [Generate SVG] → [Refinement Loop]
     ↑                                                                                      │
     └──────────────────────── [User requests changes] ←────────────────────────────────────┘
```

---

## Quick Mode Triggers

Skip all configuration and use defaults when the user says any of:

| English | Chinese |
|---------|---------|
| "use defaults" | "使用默认" |
| "quick generate" | "快速生成" |
| "just make it" | "直接生成" |
| "default settings" | "默认设置" |

Default configuration: Medium / Corporate Blue / Standard / Top-to-Bottom / Orthogonal

---

## Recommendation Logic Table

### Size Recommendation

| Node Count | Recommended Size | Rationale |
|-----------|-----------------|-----------|
| 1–5 | Small (600×400) | Simple diagram, minimal content |
| 6–15 | Medium (1000×700) | Standard complexity |
| 16–30 | Large (1400×1000) | Many elements need space |
| 31+ | Extra Large (1920×1080) | Complex diagram, needs room |

### Color Recommendation by Context

| Content Type | Recommended Scheme | Rationale |
|-------------|-------------------|-----------|
| Business process, workflow | Corporate Blue | Professional, trustworthy |
| Environment, health, biology | Nature Green | Organic, natural feel |
| Marketing, creative, brainstorm | Sunset Warm | Energetic, attention-grabbing |
| Software architecture, API, tech | Dark Mode | Developer-friendly |
| Academic paper, print document | Monochrome | Clean, universally printable |
| Education, tutorial, training | Ocean Breeze | Calm, approachable |

### Direction Recommendation by Diagram Type

| Diagram Type | Recommended Direction | Rationale |
|-------------|----------------------|-----------|
| Flowchart | Top → Bottom | Natural reading flow |
| Mind Map | Radial (N/A) | Branches spread from center |
| Sequence Diagram | Top → Bottom | Chronological top-down |
| Org Chart | Top → Bottom | Hierarchy flows downward |
| Timeline | Left → Right | Chronological left-right |
| ER Diagram | Left → Right | Entities side by side |
| State Diagram | Left → Right | State progression |

---

## Error Messages

### Ambiguous Input

```
I need more information to create your diagram. Could you provide:
1. What process or concept are you trying to visualize?
2. What are the key steps or elements?
3. How are they connected?

需要更多信息来创建图表，请提供：
1. 您想要可视化什么流程/概念？
2. 关键步骤或元素是什么？
3. 它们之间如何连接？
```

### Complexity Warning

```
⚠️ Your diagram has {n} elements, which may be hard to read at {size} size.
Suggestions:
- Upgrade to {larger_size}
- Use "Compact" density
- Split into multiple diagrams

⚠️ 您的图表有 {n} 个元素，在 {size} 尺寸下可能难以阅读。
建议：
- 升级到 {larger_size} 尺寸
- 使用"紧凑"信息密度
- 拆分为多个图表
```