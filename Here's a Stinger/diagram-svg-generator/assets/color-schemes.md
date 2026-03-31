# Color Scheme Definitions

Complete color values for all 6 preset color schemes.

---

## 1. Corporate Blue / 商务蓝

| Role | Hex | Usage |
|------|-----|-------|
| `primary` | `#1A73E8` | Start/end nodes, titles, emphasis |
| `secondary` | `#4285F4` | Decision nodes, secondary elements |
| `accent` | `#EA4335` | Alerts, error states, highlights |
| `background` | `#FFFFFF` | Canvas background |
| `text` | `#202124` | Body text, labels |
| `border` | `#DADCE0` | Node borders, dividers |
| `node_fill` | `#E8F0FE` | Default node fill |
| `connector` | `#5F6368` | Lines, arrows |

## 2. Nature Green / 自然绿

| Role | Hex | Usage |
|------|-----|-------|
| `primary` | `#2E7D32` | Start/end nodes, titles |
| `secondary` | `#4CAF50` | Decision nodes |
| `accent` | `#FF9800` | Highlights |
| `background` | `#FAFAFA` | Canvas |
| `text` | `#1B5E20` | Body text |
| `border` | `#A5D6A7` | Borders |
| `node_fill` | `#E8F5E9` | Node fill |
| `connector` | `#66BB6A` | Lines |

## 3. Sunset Warm / 暖日落

| Role | Hex | Usage |
|------|-----|-------|
| `primary` | `#E65100` | Start/end nodes, titles |
| `secondary` | `#FF6D00` | Decision nodes |
| `accent` | `#FFD600` | Highlights |
| `background` | `#FFF8E1` | Canvas |
| `text` | `#3E2723` | Body text |
| `border` | `#FFCC80` | Borders |
| `node_fill` | `#FFF3E0` | Node fill |
| `connector` | `#FF8F00` | Lines |

## 4. Dark Mode / 暗色模式

| Role | Hex | Usage |
|------|-----|-------|
| `primary` | `#BB86FC` | Start/end nodes, titles |
| `secondary` | `#03DAC6` | Decision nodes |
| `accent` | `#CF6679` | Highlights |
| `background` | `#121212` | Canvas |
| `text` | `#E1E1E1` | Body text |
| `border` | `#333333` | Borders |
| `node_fill` | `#1E1E2E` | Node fill |
| `connector` | `#888888` | Lines |

## 5. Monochrome / 单色

| Role | Hex | Usage |
|------|-----|-------|
| `primary` | `#212121` | Start/end nodes, titles |
| `secondary` | `#616161` | Decision nodes |
| `accent` | `#9E9E9E` | Highlights |
| `background` | `#FFFFFF` | Canvas |
| `text` | `#212121` | Body text |
| `border` | `#BDBDBD` | Borders |
| `node_fill` | `#F5F5F5` | Node fill |
| `connector` | `#757575` | Lines |

## 6. Ocean Breeze / 海洋微风

| Role | Hex | Usage |
|------|-----|-------|
| `primary` | `#0077B6` | Start/end nodes, titles |
| `secondary` | `#00B4D8` | Decision nodes |
| `accent` | `#90E0EF` | Highlights |
| `background` | `#CAF0F8` | Canvas |
| `text` | `#03045E` | Body text |
| `border` | `#48CAE4` | Borders |
| `node_fill` | `#ADE8F4` | Node fill |
| `connector` | `#0096C7` | Lines |

---

## CSS Class Mapping

When generating SVG `<style>`, map scheme roles to CSS classes as follows:

```css
.bg             { fill: {{background}}; }
.node-rect      { fill: {{node_fill}}; stroke: {{border}}; stroke-width: 2; rx: 8; }
.node-start     { fill: {{primary}}; stroke: {{primary}}; rx: 20; }
.node-end       { fill: {{accent}}; stroke: {{accent}}; rx: 20; }
.node-decision  { fill: {{secondary}}; stroke: {{secondary}}; }
.node-text      { fill: {{text}}; font-family: {{font}}; font-size: {{body_size}}px; text-anchor: middle; dominant-baseline: central; }
.node-text-light{ fill: #FFFFFF; font-family: {{font}}; font-size: {{body_size}}px; text-anchor: middle; dominant-baseline: central; }
.connector      { stroke: {{connector}}; stroke-width: 2; fill: none; marker-end: url(#arrow); }
.label          { fill: {{text}}; font-family: {{font}}; font-size: {{small_size}}px; text-anchor: middle; }
.title-text     { fill: {{primary}}; font-family: {{font}}; font-size: {{title_size}}px; font-weight: bold; }
```