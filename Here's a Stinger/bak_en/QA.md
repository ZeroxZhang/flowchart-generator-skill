QA

常见问题与解决方案
Q1：生成的图片中文文字有乱码或错误怎么办？
解决方案：
- 在 prompt 中明确指定 "Generate text in Simplified Chinese (简体中文)"
- 尽量使用 2k 输出，这需要你购买 Google Cloud 的账户
- 如果仍有问题，使用第二章 Step 5 的 PowerPoint 文本框覆盖法
- 尝试在 prompt 中提供完整的中文文本内容，而不是让 AI 自己生成
Q2：生成的架构图布局混乱，模块重叠？
解决方案：
- 在 architecture JSON 中更明确地指定层级关系
- 增加 spacing 参数的数值
- 尝试简化架构，分多张图展示（如前端架构图 + 后端架构图）
- 在 prompt 中添加："Ensure no overlapping modules, maintain clear visual hierarchy"
Q3：颜色不符合预期，对比度不够？
解决方案：
- 使用 HEX 色值而不是颜色名称（如 "#1E40AF" 而非 "blue"）
- 测试对比度：使用 WebAIM Contrast Checker 确保文字可读性
- 明确指定背景色和前景色的关系
- 在 prompt 中添加："Ensure WCAG AA contrast ratio for all text"
Q4：生成的图片尺寸不对，导出后模糊？
解决方案：
- 在 prompt 中明确指定分辨率："Resolution: 2560x1440 pixels"
- 如果需要打印，使用 4K 或更高分辨率
- 确保 Crate 中的设置与 prompt 一致
- 导出时选择最高质量，避免压缩
Q5：如何批量生成多个类似风格的图？
解决方案：
- 固定 style 和 theme JSON，只替换 architecture 部分
- 在 Crate 中创建一个模板节点，复用配置
- 使用变量占位符，批量替换内容
- 考虑编写简单的 Python 脚本自动化流程