---
name: diagram-svg-generator
description: >
  Interactively generates production-ready SVG diagrams including flowcharts, sequence diagrams, mind maps, org charts, timelines, ER diagrams, and state diagrams. Use when the user wants to create, visualize, or export any kind of diagram, flowchart, process map, or visual representation of relationships and workflows. Guides users through selecting diagram size, color scheme, information density, layout direction, and connector style before generating clean, accessible SVG code.
license: MIT
compatibility: No external dependencies required. Works with any agent that supports file output.
metadata:
  author: zeroxzhang.cc
  version: "1.0"
  tags: "diagram svg flowchart mindmap visualization interactive"
---

# Diagram SVG Generator

An interactive skill that generates professional SVG diagrams through a guided conversational workflow.

## When to Use This Skill

Activate this skill when the user:
- Wants to create a flowchart, process diagram, or workflow visualization
- Asks for a mind map, org chart, timeline, ER diagram, or state diagram
- Mentions generating, drawing, or exporting SVG diagrams
- Needs to visualize relationships, hierarchies, or sequential processes

## Interaction Protocol

This is an **interactive skill**. Do NOT generate a diagram immediately. Follow these steps:

### Step 1: Parse User Intent

From the user's description, identify:
- **Diagram type**: flowchart / sequence / mindmap / org-chart / timeline / er-diagram / state-diagram
- **Content elements**: nodes, relationships, labels
- **Complexity**: count of nodes/edges to inform recommendations

If ambiguous, ask the user to clarify the diagram type.

### Step 2: Ask Configuration Preferences (REQUIRED)

Present all 5 options as a numbered menu. Mark recommended defaults with ⭐.

> **Quick mode**: If the user says "use defaults", "快速生成", or "just make it", skip to Step 4 using all ⭐ defaults.

#### 2a. Diagram Size

```
📏 Step 1/5: Diagram Size / 图表规格
1. 📱 Small (600×400) — inline/embedded use
2. ⭐ 📊 Medium (1000×700) — standard presentations [RECOMMENDED]
3. 🖥️ Large (1400×1000) — complex diagrams
4. 📺 Extra Large (1920×1080) — full HD display
5. 🔧 Custom — specify your own dimensions
```

**Auto-recommendation logic:**
- ≤5 nodes → Small
- 6–15 nodes → Medium
- 16–30 nodes → Large
- 31+ nodes → Extra Large

#### 2b. Color Scheme

```
🎨 Step 2/5: Color Scheme / 配色方案
1. ⭐ 💼 Corporate Blue — professional, trustworthy [RECOMMENDED]
2. 🌿 Nature Green — fresh, ecological
3. 🌅 Sunset Warm — energetic, creative
4. 🌙 Dark Mode — modern, eye-friendly
5. ⚫ Monochrome — minimalist, print-friendly
6. 🌊 Ocean Breeze — calm, refreshing
7. 🎨 Custom — define your own palette
```

See [assets/color-schemes.md](assets/color-schemes.md) for full color values.

**Auto-recommendation logic:**
- Business/process → Corporate Blue
- Environmental/health → Nature Green
- Creative/marketing → Sunset Warm
- Technical/dev → Dark Mode
- Print/academic → Monochrome

#### 2c. Information Density

```
📝 Step 3/5: Information Density / 信息密度
1. 🔹 Minimal — key info only, maximum whitespace
2. ⭐ 🔸 Standard — balanced layout, moderate detail [RECOMMENDED]
3. 🔶 Detailed — full descriptions and annotations
4. 🔷 Compact — maximum info in minimum space
```

See [assets/density-presets.md](assets/density-presets.md) for parameter values.

#### 2d. Layout Direction

```
🧭 Step 4/5: Layout Direction / 布局方向
1. ⭐ ⬇️ Top to Bottom [RECOMMENDED for flowcharts/hierarchies]
2. ➡️ Left to Right [RECOMMENDED for timelines/processes]
3. ⬆️ Bottom to Top
4. ⬅️ Right to Left
```

#### 2e. Connector Style

```
🔗 Step 5/5: Connector Style / 连接线样式
1. ➖ Straight lines
2. 〰️ Curved lines
3. ⭐ 📐 Orthogonal / right-angle lines [RECOMMENDED]
4. ➗ Dashed lines
```

### Step 3: Confirm Configuration

Summarize all choices in a table and ask the user to confirm:

```
✅ Configuration Summary / 配置摘要

| Setting        | Value                |
|---------------|----------------------|
| 📏 Size        | {selection}          |
| 🎨 Colors      | {selection}          |
| 📝 Density     | {selection}          |
| 🧭 Direction   | {selection}          |
| 🔗 Connectors  | {selection}          |
| 📊 Type        | {diagram_type}       |
| 🔢 Elements    | {n} nodes, {m} edges |

Proceed? (yes / no / modify)
```

### Step 4: Generate SVG

Generate the SVG following these **mandatory rules**:

1. **Valid SVG**: Well-formed XML with `xmlns="http://www.w3.org/2000/svg"`
2. **Accessible**: Include `<title>`, `<desc>`, and `role="img"` with `aria-labelledby`
3. **Responsive**: Always use `viewBox` attribute
4. **CSS classes**: Use `<style>` inside `<defs>`, not inline styles
5. **Grouped**: Use `<g>` elements with meaningful `id` and `class`
6. **Arrow markers**: Define in `<defs>` with proper `<marker>` elements
7. **Font fallbacks**: Always include fallback fonts (e.g. `Arial, sans-serif`)
8. **Comments**: Add brief XML comments for major sections

Use the SVG structure template from [assets/svg-base-template.md](assets/svg-base-template.md).
Use diagram-specific templates from [references/svg-templates.md](references/svg-templates.md).

### Step 5: Offer Refinement

After delivering the SVG, present:

```
🔄 What next? / 接下来？
1. ✅ Done — satisfied
2. ✏️ Edit content — modify nodes/connections
3. 🎨 Change style — adjust colors/fonts
4. 📏 Resize — change dimensions
5. 🔄 Regenerate — start fresh
```

Loop back to the relevant step based on the user's choice.

## Error Handling

- **Ambiguous input**: Ask for process steps, elements, and connections
- **Too many elements**: Warn and recommend larger size, compact density, or splitting into multiple diagrams
- **Invalid custom colors**: Validate hex format, suggest closest preset

## Language Support

All prompts support English and Chinese. Detect the user's language from their input and respond accordingly. Bilingual labels are used in the menu options above.