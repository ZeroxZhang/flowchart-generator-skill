step3-审查和修改

常见的优化场景

场景 1：语言混用问题
修改要求：
- 将所有非专有名词（如 layer, component）改为中文
- 保留技术栈名称为英文（如 Next.js, FastAPI）
- 组件类型保持英文（frontend-app, backend-api）便于后续处理

场景 2：层级过深或过浅
修改要求：
- 当前有 4 层，太多了，将"工具层"合并到"基础设施层"
- 或：当前只有 2 层，太粗糙，将"业务层"拆分为"编排层"和"执行层"

场景 3：遗漏关键组件
修改要求：
- 添加 `src/middleware/` 目录中的"认证中间件"组件
- 补充"消息队列"组件，它连接"API 层"和"Worker 层"
- 添加"监控告警"模块到"基础设施层"

场景 4：关系不准确
修改要求：
- "Web UI" 和 "API Server" 应该是双向集成关系（integrates-with），不是单向调用
- "研究员 Agent" 应该依赖（depends-on）"搜索工具"，而不是调用（calls）
- 补充"LLM Gateway"与所有 Agent 的关系

迭代技巧
一次性列出所有修改（推荐方式）：
请按照以下要求修改 JSON：

1. 语言规范：
   - 层级名称改为中文："Access Layer" → "访问层"
   - 组件名称改为中文："Coordinator" → "协调器"
   - 保留技术栈英文：Next.js, FastAPI 等

2. 结构调整：
   - 合并"搜索工具"和"数据工具"到统一的"工具集"组件
   - 将"监控模块"从"业务层"移到"基础设施层"

3. 补充内容：
   - 在"基础设施层"添加"Redis 缓存"组件（module: src/cache/）
   - 添加"配置中心"组件（provider: Consul）

4. 关系修正：
   - "API Server" → "Coordinator" 改为 depends-on
   - 补充"所有 Agent" → "LLM Gateway" 的 uses 关系

渐进式修改（如果改动较大）：
第一轮：先调整层级结构
第二轮：优化组件命名和类型
第三轮：补充遗漏的组件
第四轮：修正关系