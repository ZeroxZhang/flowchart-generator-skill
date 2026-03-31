# SVG Base Template

The foundational SVG wrapper structure that all diagram types share. Every generated SVG must follow this structure.

---

## Template

```xml
<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg"
     viewBox="0 0 {{width}} {{height}}"
     width="{{width}}"
     height="{{height}}"
     role="img"
     aria-labelledby="diagram-title diagram-desc">

  <title id="diagram-title">{{title}}</title>
  <desc id="diagram-desc">{{description}}</desc>

  <defs>
    <style>
      /* === Base Styles === */
      .bg { fill: {{background}}; }

      /* === Node Styles === */
      .node-rect { fill: {{node_fill}}; stroke: {{border}}; stroke-width: 2; rx: 8; ry: 8; }
      .node-start { fill: {{primary}}; stroke: {{primary}}; rx: 20; ry: 20; }
      .node-end { fill: {{accent}}; stroke: {{accent}}; rx: 20; ry: 20; }
      .node-decision { fill: {{secondary}}; stroke: {{secondary}}; }

      /* === Text Styles === */
      .node-text {
        fill: {{text}};
        font-family: {{font_family}};
        font-size: {{font_size_body}}px;
        text-anchor: middle;
        dominant-baseline: central;
      }
      .node-text-light {
        fill: #FFFFFF;
        font-family: {{font_family}};
        font-size: {{font_size_body}}px;
        text-anchor: middle;
        dominant-baseline: central;
      }
      .title-text {
        fill: {{primary}};
        font-family: {{font_family}};
        font-size: {{font_size_title}}px;
        font-weight: bold;
      }
      .label {
        fill: {{text}};
        font-family: {{font_family}};
        font-size: {{font_size_small}}px;
        text-anchor: middle;
      }

      /* === Connector Styles === */
      .connector {
        stroke: {{connector}};
        stroke-width: 2;
        fill: none;
        marker-end: url(#arrowhead);
      }
      .connector-dashed {
        stroke: {{connector}};
        stroke-width: 2;
        fill: none;
        stroke-dasharray: 6,3;
        marker-end: url(#arrowhead);
      }
    </style>

    <!-- Arrow marker definition -->
    <marker id="arrowhead"
            markerWidth="10" markerHeight="7"
            refX="10" refY="3.5"
            orient="auto"
            fill="{{connector}}">
      <polygon points="0 0, 10 3.5, 0 7" />
    </marker>
  </defs>

  <!-- Background -->
  <rect class="bg" width="100%" height="100%" />

  <!-- Diagram Title -->
  <text class="title-text" x="{{width/2}}" y="35" text-anchor="middle">{{title}}</text>

  <!-- Diagram Content -->
  <g id="diagram-content" transform="translate({{content_offset_x}}, {{content_offset_y}})">
    <!-- Diagram-specific nodes and connectors go here -->
    <!-- Use templates from references/svg-templates.md -->
  </g>

  <!-- Optional: Legend -->
  <g id="legend" transform="translate(30, {{height - 50}})">
    <!-- Legend items -->
  </g>

</svg>
```

---

## Variable Resolution

| Placeholder | Source | Example |
|------------|--------|---------|
| `{{width}}` | Size preset | `1000` |
| `{{height}}` | Size preset | `700` |
| `{{title}}` | User input | `"Login Process"` |
| `{{description}}` | Auto-generated from content | `"A flowchart showing..."` |
| `{{background}}` | Color scheme → `background` | `#FFFFFF` |
| `{{primary}}` | Color scheme → `primary` | `#1A73E8` |
| `{{secondary}}` | Color scheme → `secondary` | `#4285F4` |
| `{{accent}}` | Color scheme → `accent` | `#EA4335` |
| `{{text}}` | Color scheme → `text` | `#202124` |
| `{{border}}` | Color scheme → `border` | `#DADCE0` |
| `{{node_fill}}` | Color scheme → `node_fill` | `#E8F0FE` |
| `{{connector}}` | Color scheme → `connector` | `#5F6368` |
| `{{font_family}}` | Font setting | `Arial, sans-serif` |
| `{{font_size_title}}` | Density → `font_size_title` | `16` |
| `{{font_size_body}}` | Density → `font_size_body` | `13` |
| `{{font_size_small}}` | `font_size_body - 2` | `11` |
| `{{content_offset_x}}` | Calculated from size | `50` |
| `{{content_offset_y}}` | `55` (below title) | `55` |

---

## Mandatory SVG Rules

1. Always include `<?xml version="1.0" encoding="UTF-8"?>` declaration
2. Always include `xmlns="http://www.w3.org/2000/svg"` on the `<svg>` element
3. Always include `viewBox` for responsive scaling
4. Always include `<title>` and `<desc>` for accessibility
5. Always use `role="img"` and `aria-labelledby`
6. Define all styles in `<defs><style>` — avoid inline styles
7. Define all markers in `<defs>`
8. Use `<g>` groups with meaningful `id` attributes
9. Add XML comments for major sections
10. Include font-family fallbacks (e.g., `Arial, sans-serif`)