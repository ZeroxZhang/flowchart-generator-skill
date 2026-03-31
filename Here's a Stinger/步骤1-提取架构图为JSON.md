# 任务：将架构图提取为 JSON 格式

请仔细分析当前项目。基于您的深入研究，生成详细的架构图。

## 预期的 JSON 结构

```json
{
  "diagram": {
    "title": "string",
    "layers": [
      {
        "id": "string",
        "name": "string",
        "level": number,
        "components": [
          {
            "id": "string",
            "name": "string",
            "type": "string",
            "module": "string (可选)",
            "provider": "string (可选)",
            "dependencies": ["string array (可选)"],
            "contains": [/* 嵌套组件 - 最多 3-4 层 */]
          }
        ]
      }
    ],
    "relationships": [
      {
        "from": "component-id",
        "to": "component-id",
        "type": "calls | uses | depends-on | integrates-with | supports"
      }
    ]
  }
}
```

## 提取规则

### 1. 识别层级（水平分区）

- 寻找将组件水平分组的虚线框
- 每个层级都有一个名称（通常在左侧，带有图标）
- 指定层级：1（顶部）→ 2（中间）→ 3（底部）

### 2. 提取组件

- 组件名称：框内的粗体文字
- 组件类型：名称下方括号中的文字（如 "ui-module"、"framework"）
- 对于嵌套组件（如"工具集"包含多个工具），使用 `contains` 数组
- **重要：最大嵌套深度为 3-4 层**
- 从组件名称生成 kebab-case 格式的 ID

### 3. 嵌套结构指南

- 层级 1：Layer（如 "Console UI"、"Agentic System"）
- 层级 2：主要组件（如 "Components"、"Tools"）
- 层级 3：子组件（如 "File System Toolset"、"Text Editor Tool"）
- 层级 4（如需要）：详细的子项（如特定工具函数）
- **最多到层级 4 - 不要继续嵌套**

### 4. 识别关系

- 组件之间的箭头表示关系
- 双向箭头（↔）= "integrates-with"
- 向下箭头（↓）= "depends-on"
- 指向特定组件的箭头 = "calls" 或 "uses"

### 5. 特殊情况

- 如果组件包含一系列项目（如"工具集"包含"文件系统工具集"、"文本编辑器工具"等），请将它们放在 `contains` 数组中
- 保持图表中的确切命名
- 对于括号中的模块名称，将其添加为 `module` 字段
- 如果遇到更深的嵌套结构，请将其扁平化至最多 4 层

## 嵌套示例

```json
{
  "layers": [                           // 层级 1
    {
      "components": [                   // 层级 2
        {
          "id": "tools",
          "name": "Tools",
          "contains": [                 // 层级 3
            {
              "id": "filesystem-tool",
              "name": "File System Toolset",
              "contains": [             // 层级 4（最大）
                {
                  "id": "read-file",
                  "name": "Read File"
                }
              ]
            }
          ]
        }
      ]
    }
  ]
}
```

## 输出

请提供：

1. 完整的 JSON 结构（遵守最多 3-4 层嵌套）
2. 参考文档位于 `doc` 文件夹和 README.md（如果存在）
3. 简要总结：
   - 层级数量
   - 组件数量
   - 使用的最大嵌套深度
   - 关系数量
4. 如果您需要扁平化任何结构，请说明简化了什么
