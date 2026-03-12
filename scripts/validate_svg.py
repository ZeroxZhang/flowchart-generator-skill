#!/usr/bin/env python3
"""
validate_svg.py
校验输出的 SVG 文件是否合法且包含必要元素。
用法：python validate_svg.py output.svg
"""

import sys
import xml.etree.ElementTree as ET


def validate_svg(filepath: str) -> list[str]:
    errors = []

    try:
        tree = ET.parse(filepath)
        root = tree.getroot()
    except ET.ParseError as e:
        return [f"SVG XML 解析失败: {e}"]

    ns = {"svg": "http://www.w3.org/2000/svg"}
    tag = root.tag
    if not tag.endswith("svg"):
        errors.append(f"根元素应为 <svg>，实际为: {tag}")
        return errors

    # viewBox 检查
    viewbox = root.get("viewBox")
    if not viewbox:
        errors.append("缺少 viewBox 属性（影响响应式缩放）")
    else:
        parts = viewbox.split()
        if len(parts) != 4:
            errors.append(f"viewBox 格式异常: {viewbox}")

    # xmlns 检查
    xmlns = root.get("xmlns", "")
    if "w3.org/2000/svg" not in xmlns:
        errors.append("缺少 xmlns 声明")

    # font-family 检查
    font = root.get("font-family", "")
    has_font = bool(font)
    if not has_font:
        # 检查 style 标签中是否定义了 font-family
        for style in root.iter():
            if style.tag.endswith("style") and style.text and "font-family" in style.text:
                has_font = True
                break
    if not has_font:
        errors.append("建议在 <svg> 或 <style> 中定义 font-family")

    # defs 检查
    defs = root.find("svg:defs", ns) or root.find("defs")
    if defs is None:
        errors.append("缺少 <defs> 区域（建议定义 marker/filter）")

    # 节点检查（至少有 rect 或 polygon）
    shapes = list(root.iter())
    has_rect = any(el.tag.endswith("rect") for el in shapes)
    has_polygon = any(el.tag.endswith("polygon") for el in shapes)
    has_path = any(el.tag.endswith("path") for el in shapes)
    has_text = any(el.tag.endswith("text") for el in shapes)

    if not (has_rect or has_polygon):
        errors.append("未检测到节点图形（rect 或 polygon）")
    if not has_path:
        errors.append("未检测到连接线（path）")
    if not has_text:
        errors.append("未检测到文字元素（text）")

    # 文字内容非空检查
    empty_text_count = 0
    for el in shapes:
        if el.tag.endswith("text"):
            content = (el.text or "").strip()
            children = list(el)
            child_text = "".join((c.text or "") for c in children).strip()
            if not content and not child_text:
                empty_text_count += 1
    if empty_text_count > 0:
        errors.append(f"发现 {empty_text_count} 个空文字元素")

    return errors


def main():
    if len(sys.argv) < 2:
        print("用法: python validate_svg.py <output.svg>")
        sys.exit(1)

    filepath = sys.argv[1]
    errors = validate_svg(filepath)
    if errors:
        print(f"⚠️ 校验发现 {len(errors)} 个问题：")
        for err in errors:
            print(f"   • {err}")
        sys.exit(1)
    else:
        print("✅ SVG 校验通过")
        sys.exit(0)


if __name__ == "__main__":
    main()
