#!/usr/bin/env python3
"""
生成每日美文阅读卡片 HTML

用法:
  python3 generate_card.py --output /path/to/output.html \
    --issue 1 \
    --date "2026年3月21日" \
    --dow "六" \
    --title "《春》节选" \
    --author "朱自清" \
    --essay "<p>原文内容...</p>" \
    --background "背景内容" \
    --appreciation "赏析内容" \
    --vocab "词语1,词语2,词语3" \
    --sentence "精彩句子及赏析" \
    --examples "写作范例1|写作范例2"

所有参数均可省略（使用默认值），output 是必填
"""

import argparse
import re
from pathlib import Path

def read_template():
    template_path = Path(__file__).parent.parent / "assets" / "card-template.html"
    return template_path.read_text(encoding="utf-8")

def build_vocab_tags(vocab_str):
    """将逗号分隔的词语转换为标签 HTML"""
    words = [w.strip() for w in vocab_str.split(",") if w.strip()]
    tags = "".join(f'<span class="word-tag">{w}</span>' for w in words)
    return f'<div class="word-list">{tags}</div>'

def build_writing_examples(examples_str):
    """构建写作应用区块 HTML"""
    if not examples_str:
        return ""
    
    blocks = []
    for i, ex in enumerate(examples_str.split("|"), 1):
        if "::" in ex:
            label, content = ex.split("::", 1)
        else:
            label, content = f"技法{i}", ex
        blocks.append(f'''
    <div class="writing-section" style="margin-top: 12px;">
      <div class="box-title"><span class="emoji">💡</span> {label.strip()}</div>
      <div class="explain">{content.strip()}</div>
    </div>''')
    return "".join(blocks)

def main():
    parser = argparse.ArgumentParser(description="生成每日美文阅读卡片")
    parser.add_argument("--output", required=True, help="输出 HTML 路径")
    parser.add_argument("--issue", default="1", help="期数")
    parser.add_argument("--date", default="", help="日期")
    parser.add_argument("--dow", default="", help="星期几")
    parser.add_argument("--title", default="", help="文章标题")
    parser.add_argument("--author", default="", help="作者")
    parser.add_argument("--essay", default="", help="原文 HTML")
    parser.add_argument("--background", default="", help="背景")
    parser.add_argument("--appreciation", default="", help="赏析")
    parser.add_argument("--vocab", default="", help="好词（逗号分隔）")
    parser.add_argument("--sentence", default="", help="精彩句子")
    parser.add_argument("--examples", default="", help="写作范例（用 | 分隔各范例，用 :: 分隔标题和内容）")
    
    args = parser.parse_args()
    
    template = read_template()
    
    # 替换占位符
    replacements = {
        "{{issue}}": args.issue,
        "{{date}}": args.date,
        "{{day_of_week}}": args.dow,
        "{{title}}": args.title,
        "{{author}}": args.author,
        "{{essay_content}}": args.essay,
        "{{background}}": args.background,
        "{{appreciation}}": args.appreciation,
        "{{vocabulary_tags}}": build_vocab_tags(args.vocab),
        "{{best_sentence}}": args.sentence,
        "{{writing_examples}}": build_writing_examples(args.examples),
    }
    
    for placeholder, value in replacements.items():
        template = template.replace(placeholder, value)
    
    # 清理未替换的占位符
    template = re.sub(r"\{\{[^}]+\}\}", "", template)
    
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(template, encoding="utf-8")
    
    print(f"✅ 卡片已生成: {output_path}")

if __name__ == "__main__":
    main()
