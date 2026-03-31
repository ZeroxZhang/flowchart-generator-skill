Generate a modern but minimalist style Architecture Diagram for DeerCode.

{
  "name": "DeerCode",
  "description": "DeerCode Architecture",
  "layers": [
    {
      "name": "Console UI",
      "type": "presentation",
      "components": [
        {
          "name": "App",
          "type": "ui-module"
        },
        {
          "name": "Theme",
          "type": "ui-module"
        },
        {
          "name": "Components",
          "type": "ui-module"
        }
      ]
    },
    {
      "name": "Agentic System",
      "type": "core",
      "components": [
        {
          "name": "Coding Agent",
          "type": "agent",
          "icon": "robot"
        },
        {
          "name": "Prompt Template",
          "type": "template",
          "icon": "template"
        },
        {
          "name": "Models",
          "type": "model-layer",
          "models": [
            {
              "name": "Doubao Seed 1.6",
              "provider": "bytedance"
            }
          ]
        },
        {
          "name": "Tools",
          "type": "tool-layer",
          "tools": [
            {
              "name": "File System Toolset",
              "category": "filesystem"
            },
            {
              "name": "Text Editor Tool",
              "category": "editor"
            },
            {
              "name": "Bash Tool",
              "category": "command"
            },
            {
              "name": "To-do List Tool",
              "category": "task"
            },
            {
              "name": "MCP Tool Loader",
              "category": "extension"
            }
          ]
        }
      ]
    },
    {
      "name": "Infrastructure",
      "type": "foundation",
      "components": [
        {
          "name": "LangChain",
          "type": "framework"
        },
        {
          "name": "LangGraph",
          "type": "framework"
        },
        {
          "name": "Textual UI",
          "type": "ui-framework"
        },
        {
          "name": "Rich UI",
          "type": "ui-framework"
        },
        {
          "name": "Config",
          "type": "configuration"
        }
      ]
    }
  ]
}