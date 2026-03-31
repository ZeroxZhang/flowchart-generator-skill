# SVG Diagram Templates Reference

Detailed SVG template patterns for each of the 7 supported diagram types. The agent should use these as structural foundations and adapt them based on user configuration.

All templates use `{{variable}}` placeholders that are resolved from the user's chosen configuration (color scheme, density, size, etc.).

---

## 1. Flowchart / 流程图

**Node types**: Start (rounded pill), Process (rectangle), Decision (diamond), End (rounded pill)

```xml
<g id="flowchart" transform="translate({{offset_x}}, {{offset_y}})">
  <!-- START NODE: pill shape -->
  <g id="node-start" transform="translate({{x}}, {{y}})">
    <rect class="node-start" x="-60" y="-20" width="120" height="40" rx="20" ry="20" />
    <text class="node-text-light" text-anchor="middle" dominant-baseline="central">Start</text>
  </g>

  <!-- PROCESS NODE: rounded rectangle -->
  <g id="node-process-1" transform="translate({{x}}, {{y}})">
    <rect class="node-rect" x="-80" y="-25" width="160" height="50" rx="8" ry="8" />
    <text class="node-text" text-anchor="middle" dominant-baseline="central">{{label}}</text>
  </g>

  <!-- DECISION NODE: diamond via polygon -->
  <g id="node-decision-1" transform="translate({{x}}, {{y}})">
    <polygon class="node-decision" points="0,-35 70,0 0,35 -70,0" />
    <text class="node-text-light" text-anchor="middle" dominant-baseline="central">{{label}}</text>
  </g>

  <!-- END NODE: pill shape -->
  <g id="node-end" transform="translate({{x}}, {{y}})">
    <rect class="node-end" x="-60" y="-20" width="120" height="40" rx="20" ry="20" />
    <text class="node-text-light" text-anchor="middle" dominant-baseline="central">End</text>
  </g>

  <!-- CONNECTORS -->
  <!-- Straight -->
  <line class="connector" x1="{{x1}}" y1="{{y1}}" x2="{{x2}}" y2="{{y2}}" />
  <!-- Orthogonal (L-shaped) -->
  <polyline class="connector" points="{{x1}},{{y1}} {{x1}},{{mid}} {{x2}},{{mid}} {{x2}},{{y2}}" />
  <!-- Curved -->
  <path class="connector" d="M {{x1}},{{y1}} C {{cx1}},{{cy1}} {{cx2}},{{cy2}} {{x2}},{{y2}}" />

  <!-- Edge labels -->
  <text class="label" x="{{lx}}" y="{{ly}}">Yes</text>
  <text class="label" x="{{lx}}" y="{{ly}}">No</text>
</g>
```

**Layout rules (top-to-bottom):**
- Center-align nodes on the main vertical axis
- Decision branches go left (No) and continue down (Yes) by convention
- Spacing between rows = `node_spacing` from density preset
- Node width adapts to text length with minimum 120px

---

## 2. Mind Map / 思维导图

**Node types**: Central (large, primary color), Branch L1 (secondary), Leaf L2 (light fill)

```xml
<g id="mindmap" transform="translate({{center_x}}, {{center_y}})">
  <!-- Central node -->
  <rect class="central-node" x="-75" y="-25" width="150" height="50" rx="15" />
  <text class="text-center">{{central_topic}}</text>

  <!-- Branch: curved connector + rounded rect -->
  <path class="branch-line" d="M 75,0 C 140,0 140,-100 210,-100" />
  <g transform="translate(270, -100)">
    <rect class="branch-l1" x="-55" y="-18" width="110" height="36" rx="10" />
    <text class="text-branch">{{branch}}</text>
  </g>

  <!-- Leaf -->
  <path class="leaf-line" d="M 325,-100 C 365,-100 365,-140 405,-140" />
  <g transform="translate(460, -140)">
    <rect class="leaf" x="-50" y="-14" width="100" height="28" rx="8" />
    <text class="text-leaf">{{leaf}}</text>
  </g>
</g>
```

**Layout rules:**
- Central node at canvas center
- Branches radiate outward: top-right, bottom-right, top-left, bottom-left
- Use curved bezier connectors for organic feel
- Each branch gets a distinct color from the palette

---

## 3. Sequence Diagram / 时序图

```xml
<g id="sequence-diagram" transform="translate({{offset_x}}, {{offset_y}})">
  <!-- Actor header box -->
  <g class="actor" id="actor-1">
    <rect class="actor-box" x="{{x-40}}" y="20" width="80" height="36" rx="6" />
    <text class="actor-text" x="{{x}}" y="38">{{name}}</text>
    <line class="lifeline" x1="{{x}}" y1="56" x2="{{x}}" y2="{{bottom}}" />
  </g>

  <!-- Solid message arrow -->
  <line class="message-line" x1="{{from}}" y1="{{y}}" x2="{{to}}" y2="{{y}}" />
  <text class="message-text" x="{{mid}}" y="{{y-8}}">{{message}}</text>

  <!-- Dashed return arrow -->
  <line class="message-line-dashed" x1="{{from}}" y1="{{y}}" x2="{{to}}" y2="{{y}}" />

  <!-- Activation bar -->
  <rect class="activation" x="{{x-6}}" y="{{start}}" width="12" height="{{h}}" />
</g>
```

**Layout rules:**
- Actors evenly spaced horizontally, each with a vertical dashed lifeline
- Messages go top to bottom in chronological order
- Row spacing = `node_spacing` from density preset
- Activation bars overlap the lifeline

---

## 4. Org Chart / 组织架构图

```xml
<g id="org-chart" transform="translate({{center_x}}, {{offset_y}})">
  <!-- Root node -->
  <g id="org-root">
    <rect class="org-node-l0" x="-80" y="-30" width="160" height="60" rx="8" />
    <text class="org-text-light org-title" y="-6">{{name}}</text>
    <text class="org-text-light org-subtitle" y="14">{{role}}</text>
  </g>

  <!-- Vertical + horizontal connectors -->
  <polyline class="org-connector" points="0,30 0,55 {{cx}},55 {{cx}},70" />

  <!-- Child node -->
  <g transform="translate({{cx}}, 100)">
    <rect class="org-node-l1" x="-70" y="-25" width="140" height="50" rx="8" />
    <text class="org-text-light org-title" y="-4">{{name}}</text>
    <text class="org-text-light org-subtitle" y="14">{{role}}</text>
  </g>
</g>
```

**Layout rules:**
- Top-to-bottom hierarchy
- Siblings centered under their parent
- Connector: vertical from parent → horizontal bar → vertical to each child
- Level 0 uses `primary`, Level 1 uses `secondary`, Level 2+ uses `node_fill`

---

## 5. Timeline / 时间线

```xml
<g id="timeline" transform="translate({{offset_x}}, {{center_y}})">
  <!-- Horizontal axis -->
  <line class="timeline-line" x1="30" y1="0" x2="{{end}}" y2="0" />

  <!-- Milestone (alternating above/below) -->
  <g transform="translate({{x}}, 0)">
    <circle class="milestone-dot" cx="0" cy="0" r="8" />
    <g transform="translate(0, {{card_y}})">
      <rect class="milestone-card" x="-70" y="-40" width="140" height="60" rx="6" />
      <text class="milestone-date" x="0" y="-22" text-anchor="middle">{{date}}</text>
      <text class="milestone-title" x="0" y="-4" text-anchor="middle">{{title}}</text>
      <text class="milestone-desc" x="0" y="12" text-anchor="middle">{{desc}}</text>
    </g>
  </g>
</g>
```

**Layout rules:**
- Left-to-right horizontal axis
- Milestone cards alternate above (-60) and below (+40) the axis
- Even spacing between milestones

---

## 6. ER Diagram / ER 图

```xml
<g id="er-diagram" transform="translate({{offset_x}}, {{offset_y}})">
  <!-- Entity -->
  <g transform="translate({{x}}, {{y}})">
    <rect class="entity-body" x="0" y="0" width="160" height="{{h}}" rx="6" />
    <rect class="entity-header" x="0" y="0" width="160" height="32" rx="6" />
    <text class="entity-title" x="80" y="16">{{name}}</text>
    <text class="attr-text attr-pk" x="12" y="52">🔑 {{pk}} : {{type}}</text>
    <text class="attr-text" x="12" y="72">    {{attr}} : {{type}}</text>
    <text class="attr-text attr-fk" x="12" y="92">🔗 {{fk}} : {{type}}</text>
  </g>

  <!-- Relationship line with cardinality -->
  <path class="relation-line" d="M {{x1}},{{y1}} L {{x2}},{{y2}}" />
  <text class="relation-text" x="{{near1}}" y="{{y1-8}}">1</text>
  <text class="relation-text" x="{{near2}}" y="{{y2-8}}">*</text>
</g>
```

---

## 7. State Diagram / 状态图

```xml
<g id="state-diagram" transform="translate({{offset_x}}, {{offset_y}})">
  <!-- Initial state: filled circle -->
  <circle class="initial-state" cx="{{x}}" cy="{{y}}" r="10" />

  <!-- State node: rounded rectangle -->
  <g transform="translate({{x}}, {{y}})">
    <rect class="state-node" x="-60" y="-22" width="120" height="44" rx="12" />
    <text class="state-text">{{name}}</text>
  </g>

  <!-- Final state: double circle -->
  <g transform="translate({{x}}, {{y}})">
    <circle class="final-outer" cx="0" cy="0" r="12" />
    <circle class="final-inner" cx="0" cy="0" r="7" />
  </g>

  <!-- Transition: curved arrow with label -->
  <path class="transition" d="M {{x1}},{{y1}} Q {{cx}},{{cy}} {{x2}},{{y2}}" />
  <text class="transition-label" x="{{lx}}" y="{{ly}}">{{event}} [{{guard}}]</text>
</g>
```