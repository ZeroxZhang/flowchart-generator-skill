#!/usr/bin/env python3
"""
validate_structure.py
校验 Phase 3 输出的流程结构 JSON 是否符合规范。
用法：python validate_structure.py structure.json
"""

import json
import sys
from typing import Any

REQUIRED_TOP_KEYS = {"metadata", "config", "nodes", "edges"}
REQUIRED_NODE_KEYS = {"id", "type", "label", "position"}
REQUIRED_EDGE_KEYS = {"id", "from", "to"}
VALID_NODE_TYPES = {"terminal", "process", "decision", "io", "subprocess"}
VALID_DIRECTIONS = {"TB", "LR", "BT", "RL"}


def validate(data: dict[str, Any]) -> list[str]:
    errors = []

    # 顶层结构
    for key in REQUIRED_TOP_KEYS:
        if key not in data:
            errors.append(f"缺少顶层字段: {key}")

    if errors:
        return errors

    # metadata
    meta = data.get("metadata", {})
    if not meta.get("title"):
        errors.append("metadata.title 不可为空")

    # config
    config = data.get("config", {})
    direction = config.get("direction", "TB")
    if direction not in VALID_DIRECTIONS:
        errors.append(f"config.direction 无效: {direction}，可选值: {VALID_DIRECTIONS}")

    # nodes
    nodes = data.get("nodes", [])
    if len(nodes) < 2:
        errors.append(f"节点数不足: {len(nodes)}，至少需要 2 个节点")

    node_ids = set()
    has_terminal_start = False
    has_terminal_end = False

    for i, node in enumerate(nodes):
        for key in REQUIRED_NODE_KEYS:
            if key not in node:
                errors.append(f"nodes[{i}] 缺少字段: {key}")

        nid = node.get("id", "")
        if nid in node_ids:
            errors.append(f"节点 ID 重复: {nid}")
        node_ids.add(nid)

        ntype = node.get("type", "")
        if ntype not in VALID_NODE_TYPES:
            errors.append(f"nodes[{i}] ({nid}) 类型无效: {ntype}")

        if ntype == "terminal":
            label = node.get("label", "").lower()
            if label in ("开始", "start", "begin"):
                has_terminal_start = True
            elif label in ("结束", "end", "finish"):
                has_terminal_end = True

        label = node.get("label", "")
        if len(label) > 15 and all(ord(c) > 127 for c in label):
            errors.append(f"nodes[{i}] ({nid}) 标签过长: {len(label)} 字符（建议 ≤15）")

    if not has_terminal_start:
        errors.append("缺少「开始」终端节点")
    if not has_terminal_end:
        errors.append("缺少「结束」终端节点")

    # edges
    edges = data.get("edges", [])
    for i, edge in enumerate(edges):
        for key in REQUIRED_EDGE_KEYS:
            if key not in edge:
                errors.append(f"edges[{i}] 缺少字段: {key}")

        src = edge.get("from", "")
        tgt = edge.get("to", "")
        if src and src not in node_ids:
            errors.append(f"edges[{i}] from 指向不存在的节点: {src}")
        if tgt and tgt not in node_ids:
            errors.append(f"edges[{i}] to 指向不存在的节点: {tgt}")

    # 孤立节点检查
    connected = set()
    for edge in edges:
        connected.add(edge.get("from", ""))
        connected.add(edge.get("to", ""))
    orphans = node_ids - connected
    if orphans:
        errors.append(f"存在孤立节点（未被任何边连接）: {orphans}")

    return errors


def main():
    if len(sys.argv) < 2:
        print("用法: python validate_structure.py <structure.json>")
        sys.exit(1)

    filepath = sys.argv[1]
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError) as e:
        print(f"❌ 文件读取失败: {e}")
        sys.exit(1)

    errors = validate(data)
    if errors:
        print(f"❌ 校验失败，发现 {len(errors)} 个问题：")
        for err in errors:
            print(f"   • {err}")
        sys.exit(1)
    else:
        print(f"✅ 校验通过：{len(data['nodes'])} 个节点，{len(data['edges'])} 条边")
        sys.exit(0)


if __name__ == "__main__":
    main()
