---
name: daily-english-card
description: Generate daily English practice cards (3 questions) for a first-year middle school student (初一) in Hangzhou, aligned with PEP English textbook (人教版七年级下). Use when: (1) user asks for 每日英语三题/英语每日练习, (2) setting up or running a daily English reminder task, (3) user wants to help 窝窝 improve English grammar and vocabulary. Creates HTML cards with word form conversion, cloze/reading comprehension, and matching questions targeting identified weak points.
---

# Daily English Card Generator (初一·人教版七年级下)

Generates daily English practice cards (3 questions) for 窝窝, targeting her specific weak points identified from recent homework errors.

## 窝窝档案

| 维度 | 情况 |
|------|------|
| 年级 | 初一（七年级下学期）|
| 教材 | 人教版七年级下 |
| 英语整体水平 | 中上，基础扎实 |
| **核心短板** | 词形转换、主谓一致、匹配题逻辑、阅读审题 |

### 已发现薄弱点（按优先级排序）

1. **词形转换**（出现≥5次）
   - match/matches、needs/need、health/healthy、real/really 混淆
   - does homework 固定搭配写成 reading homework
   - 主谓一致规则不熟（复数主语用动词原形）

2. **匹配题·上下文逻辑**（出现3次）
   - 只看关键词不看整体语境，运动描述题选反
   - 对话流程理解不连贯

3. **阅读理解·审题**
   - 主旨题选细节而非整体
   - 问次数选地点（How many times → 数字不是地点）
   - 圈了单词但没选对应选项

## Card Structure

```
顶部色带（橙色系 #e67e22）
├─ 期数 + 日期 + Weekday
├─ 三道题目标题

题目区
├─ 📝 题1：词形转换（10分钟）
│   - 题目描述
│   - 留空答题区
│
├─ 📖 题2：完形/阅读（15分钟）
│   - 短文 + 选项
│   - 答题区
│
└─ 🎯 题3：匹配/语法综合（10分钟）
    - 题目描述
    - 答题区

答案折叠区（做完再对）
├─ 题1答案 + 解析
├─ 题2答案 + 解析
└─ 题3答案 + 解析
```

## 每周轮换主题（周一至周五）

### 第1天（周一）：Unit 1 词形转换专项
- 题1：词形转换 ×3（health/healthy, child/children, real/really）
- 题2：完形填空（行为动词/频率副词语境）
- 题3：匹配题（询问爱好/运动）

### 第2天（周二）：Unit 2 名词/代词专项
- 题1：词形转换 ×3（mine/ours, difference/different, belong/belongs）
- 题2：阅读理解（细节题训练）
- 题3：语法填空（主谓一致专项）

### 第3天（周三）：Unit 3 运动/健康专项
- 题1：词形转换 ×3（运动相关词汇）
- 题2：完形填空（健康话题）
- 题3：匹配题（食物/饮食习惯描述）

### 第4天（周四）：易错题综合
- 题1：词形转换综合（本周错题重组）
- 题2：阅读主旨题训练
- 题3：匹配题逻辑训练（对话流程）

### 第5天（周五）：词汇辨析专项
- 题1：易混词汇（volleyball/baseball, tennis/table tennis）
- 题2：完形（综合语境）
- 题3：本周错题同类练习

## 高频词形转换总结

| 原形 | →名词 | →形容词 | →副词 | →复数/三单 |
|------|-------|---------|-------|-----------|
| health | health | healthy | healthily | - |
| child | child | - | - | children |
| exercise | exercise | - | - | exercises |
| difference | difference | different | - | differences |
| real | - | real | really | - |
| mine | - | - | - | ours |
| belong | - | - | - | belongs |

## 常见错误警示

- ❌ match → matches（复数要加es或s）
- ❌ needs → need（Kids是复数，动词用原形）
- ❌ does homework → doing homework（固定搭配）
- ❌ volleyball → baseball（排球vs棒球）
- ❌ reading → doing（does some homework）

## 输出路径

HTML: `/Users/wowo/Documents/学习辅导/英语/每日三题/英语_三题_YYYYMMDD.html`
图片: `~/.openclaw/workspace/memory/英语每日三题_YYYYMMDD.png`（用于飞书发送）

## Prompt for Cron Task

```
你是大脑袋，给杭州初一学生窝窝生成每日英语三题练习卡片并发送到飞书群。

背景：
- 学生：初一七年级下学期，人教版英语
- 薄弱点：词形转换、主谓一致、匹配题逻辑、阅读审题
- 飞书群组ID：oc_f89abf0190161756b79dd73c8c5eab8a

步骤：
1. 根据当天星期确定考点主题（周一至周五轮换）
2. 生成3道题的HTML卡片
3. 用Python将HTML转为图片（宽1200px），保存为 ~/.openclaw/workspace/memory/英语每日三题_YYYYMMDD.png
4. 用 openclaw message send --channel feishu --account main --target oc_f89abf0190161756b79dd73c8c5eab8a --media ~/.openclaw/workspace/memory/英语每日三题_YYYYMMDD.png --message "🇬🇧 英语每日三题 · 第X期\n📝 题1：词形转换\n📖 题2：完形/阅读\n🎯 题3：匹配/语法\n💡 先做完再对答案哦～" 发送

【题目要求】
- 题1：词形转换 ×3空（答案折叠）
- 题2：完形填空或阅读理解（4选1）
- 题3：匹配题或语法综合
- 每题控制在3-5分钟，总时间30分钟内
- 贴近人教版七年级下单元话题
- 答案放在折叠区，做完再展开

【卡片格式】
- 橙色系（#e67e22），宽720px
- 三道题分开展示，有答题空间
- 答案折叠，做完对
- 标注星期和日期

参考：~/.openclaw/workspace/skills/daily-english-card/references/question-bank.md
```

## 完整流程（定时任务用）

### Step 1: 生成 HTML 卡片

按上方 Prompt 生成 HTML，保存到：
`/Users/wowo/Documents/学习辅导/英语/每日三题/英语_三题_卡片.html`

### Step 2: HTML 转图片

```bash
# 复制到 workspace
cp "/Users/wowo/Documents/学习辅导/英语/每日三题/英语_三题_卡片.html" \
   "/Users/wowo/.openclaw/workspace/英语_三题_temp.html"

# 用 openclaw browser 打开并截图
openclaw browser open "file:///Users/wowo/.openclaw/workspace/英语_三题_temp.html"
# 等待加载后截图保存

# 重命名为日期格式
mv ~/Downloads/*.png "/Users/wowo/.openclaw/workspace/memory/英语每日三题_YYYYMMDD.png"
```

### Step 3: 发送图片到飞书群

```bash
openclaw message send \
  --account main \
  --channel feishu \
  --target oc_f89abf0190161756b79dd73c8c5eab8a \
  --media "/Users/wowo/.openclaw/workspace/memory/英语每日三题_YYYYMMDD.png" \
  --message "🇬🇧 英语每日三题 · 第X期\n📝 题1：词形转换\n📖 题2：完形/阅读\n🎯 题3：匹配/语法"
```

### Cron 定时任务配置

- **时间**: 每天下午 15:30 (Asia/Shanghai)
- **Session**: isolated
- **执行内容**: 生成HTML → 转图片 → 发送飞书群

## 模板文件

模板位置：`~/.openclaw/workspace/skills/daily-english-card/assets/english-card-template.html`

## 题库参考

题库位置：`~/.openclaw/workspace/skills/daily-english-card/references/question-bank.md`
