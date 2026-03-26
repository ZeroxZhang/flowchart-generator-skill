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
