---
name: "flowchart-generator"
description: "Generates high-quality 2D flowcharts from text descriptions using a structured 6-step process (Identify, Optimize, Deconstruct, Wireframe, Style, SVG). Invoke when user mentions 'flowchart', 'process map', or 'framework diagram'."
---

# Flowchart Generator

This skill converts user text input into a professional 2D flowchart and generates an SVG file through a rigorous step-by-step process.

## Workflow

The skill MUST follow these steps sequentially. For each step, use the provided prompt to guide the generation.

### Step 1: Identify User Input
**Goal**: Understand the user's intent and raw content.
**Prompt**:
> "Analyze the user's input to identify the core request, the subject matter, and any specific constraints or preferences provided. Determine if the input is a process description, a structural hierarchy, or a relationship map. Extract the raw entities and actions."

### Step 2: Optimize User Input
**Goal**: Refine and expand the content into a complete narrative.
**Prompt**:
> "Based on the identified subject matter from Step 1, optimize and expand the user's input. Fill in missing logical links, clarify ambiguous terms, and structure the content into a coherent, comprehensive text description. Ensure the narrative flows logically and covers all necessary steps for a complete flowchart."

### Step 3: Deconstruct Content
**Goal**: Break down the narrative into flowchart components.
**Prompt**:
> "Based on the optimized description from Step 2, deconstruct the content into structured data points required for a flowchart. explicitly identify:
> - **Dimensions**: The scope, boundaries, and swimlanes (if applicable).
> - **Hierarchy**: The levels of information and nesting structure.
> - **Elements**: The specific nodes (Start/End, Process, Decision, Input/Output).
> - **Links**: The connections and relationships (source, target, direction, label).
> - **Metadata**: The chart title, legend, notes, and supplementary explanations."

### Step 4: Generate Plaintext Wireframe
**Goal**: Create a structural blueprint of the flowchart.
**Prompt**:
> "Using the deconstructed content from Step 3, generate a **text-based 2D flowchart (plaintext wireframe)**.
> - Use ASCII characters or a grid-based text layout to visualize the spatial arrangement.
> - Ensure clear separation between nodes.
> - Represent connections with lines and arrows (e.g., `-->`, `===`).
> - Verify that the logic flows correctly (e.g., no dead ends, clear decision branches).
> - **Output this wireframe to the user for verification.**"

### Step 5: Generate Style Scheme
**Goal**: Define the visual aesthetics.
**Prompt**:
> "Based on the content nature (Step 2-4), generate a tailored design scheme:
> - **Color Palette**: Define specific hex codes for background, nodes (primary, secondary, decision), lines, and text. Ensure high contrast and visual harmony.
> - **Layout Mode**: Determine the optimal orientation (Portrait vs. Landscape) and node spacing (compact vs. spacious).
> - **Typography**: Select font families (serif/sans-serif/monospace) and font sizes for titles, labels, and notes."

### Step 6: Generate SVG
**Goal**: Produce the final image file.
**Prompt**:
> "Synthesize the Wireframe (Step 4) and the Style Scheme (Step 5) to generate the complete **SVG code**.
> - Write valid, standalone SVG XML.
> - accurately render the geometry defined in the wireframe.
> - Apply the color palette, stroke widths, and font styles defined in the style scheme.
> - Ensure the SVG is responsive or has appropriate viewbox dimensions.
> - **Save the SVG code to a file (e.g., `flowchart.svg`) and present it to the user.**"

## Triggers

- User mentions "flowchart" (流程图).
- User mentions "process map" (流程映射).
- User mentions "framework diagram" (框架图).
- User asks to visualize a complex process.
