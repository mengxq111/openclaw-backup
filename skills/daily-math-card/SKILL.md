---
name: daily-math-card
description: Generate daily math problem cards for a first-year middle school student (初一) in Hangzhou, targeting common carelessness traps. Use when: (1) user asks for 每日数学题/数学每日一题, (2) setting up or running a daily math reminder task, (3) user wants to help 窝窝 improve math accuracy and avoid careless mistakes. Creates HTML cards with problem, hint, solution, and error analysis aligned with 浙教版七年级下 curriculum and Hangzhou 中考 requirements.
---

# Daily Math Card Generator (初一·杭州中考版)

Generates a daily math problem card targeting 窝窝's specific weak points: carelessness (粗心), poor reading comprehension (审题不仔细), and sign errors (符号处理).

## 窝窝档案

| 维度 | 情况 |
|------|------|
| 年级 | 初一（七年级下学期）|
| 教材 | 浙教版七年级下 |
| 能力 | 中上，运算能力强 |
| **核心短板** | **粗心（！！！）**、审题不仔细、符号处理易错 |

### 已发现薄弱点

1. **审题不仔细**（2026-03-21）
   - 表现：把 (2a+b)×(a+b) 看成 (a+b)×(a+b)，几何图形长宽看错
   - 针对训练：几何面积类题目，做前先标出所有已知长度

2. **去括号符号**（2026-03-21）
   - 表现：-(x-2)(3x+1) 展开时漏变号
   - 正确处理：-(x-2)(3x+1) = -3x² - x + 6x + 2（注意最后是+2不是-2）
   - 针对训练：复杂多项式化简题

## Card Structure

```
顶部色带（蓝色系 #4a7fb5）
├─ 期数 + 日期
├─ 主题标签（如：整式乘法/几何面积/整体代换）

题目区
├─ 今日题目（带详细题干）
├─ 陷阱提示（🎯 标注本题易错点）
├─ 答案与解析
└─ 错误分析（针对本题的粗心陷阱说明）
```

## 输出路径

HTML: `/Users/wowo/Documents/学习辅导/数学/每日一题/数学_卡片_YYYYMMDD.html`
PDF: `~/.openclaw/workspace/数学_卡片_YYYYMMDD.pdf`（用于飞书发送）

## 选题策略

### 每7天轮换主题（对接七年级下浙教版）

| 天 | 主题 | 对应考点 | 示例题目 |
|---|---|---|---|
| 1 | 整式乘法 | 乘法公式、符号处理 | (2x+3)(x-1) 展开 |
| 2 | 完全平方 | 公式变形、配方法 | (a+b)² = a²+2ab+b² 逆用 |
| 3 | 平方差 | 识别结构、速算 | (x+3)(x-3) = x²-9 |
| 4 | 几何面积 | 审题训练、图形标注 | 长方形面积→代数式 |
| 5 | 整体代换 | 换元思想、运算律 | 已知 x+y=3, 求 2x+2y |
| 6 | 去括号综合 | 符号处理、多层嵌套 | -(x-2)(3x+1) 展开 |
| 7 | 易错综合 | 综合训练、陷阱识别 | 混合运算大题 |

### 选题核心原则

**必须包含的粗心陷阱元素：**
1. **审题陷阱**：题目问"长"算"宽"、单位不一致、关键词看漏
2. **符号陷阱**：括号前负号变号、去括号漏乘、符号分配错误
3. **计算陷阱**：移项变号错误、合并同类项失误、幂运算错误
4. **格式陷阱**：答案漏写单位、多项式降幂排列缺失

**禁止出现：**
- 超纲知识点（七年级下范围）
- 纯计算无思维含量题目
- 与中考常见陈旧题重复（如简单完全平方直接套公式）

## Prompt for Cron Task

```
你是大脑袋，现在要给杭州初一学生"窝窝"生成数学每日一题卡片。

窝窝的薄弱点：
- 审题不仔细（几何图形长宽看错、关键词漏看）
- 去括号符号处理易错（括号前负号漏变号）
- 运算能力强但粗心

要求：
1. 出一道七年级下浙教版范围的题目（侧重整式乘法、乘法公式）
2. 题目必须包含至少1个粗心陷阱（审题/符号/计算/格式）
3. 卡片结构：
   - 今日题目（带详细题干）
   - 🎯 陷阱提示（标注本题易错点，2-3句话）
   - 答案与完整解析（分步写清楚）
   - 错误分析（针对本题的粗心陷阱做说明）
4. 仿写题目可选（选做）
5. 保存路径：/Users/wowo/Documents/学习辅导/数学/每日一题/数学_卡片.html
6. 配色：蓝色系（#4a7fb5），宽度720px，模板参考：~/.openclaw/workspace/skills/daily-math-card/assets/math-problem-template.html
```

## 完整流程（定时任务用）

### Step 1: 生成 HTML 卡片

按上方 Prompt 生成 HTML，保存到：
`/Users/wowo/Documents/学习辅导/数学/每日一题/数学_卡片.html`

### Step 2: HTML 转 PDF

```bash
# 先把 HTML 复制到 workspace 目录
cp "/Users/wowo/Documents/学习辅导/数学/每日一题/数学_卡片.html" \
   "/Users/wowo/.openclaw/workspace/数学_卡片_temp.html"

# 用 openclaw browser 打开并导出 PDF
openclaw browser open "file:///Users/wowo/.openclaw/workspace/数学_卡片_temp.html"
# 等待页面加载后：
openclaw browser pdf --target-id <tab-id>
# PDF 保存后重命名为带日期的名称
mv ~/Downloads/*.pdf "/Users/wowo/.openclaw/workspace/数学_YYYYMMDD.pdf"
```

**注意**：PDF 文件需要放在 `~/.openclaw/workspace/` 目录下才能被飞书发送。

### Step 3: 发送 PDF 到飞书群

群组 ID: `oc_f89abf0190161756b79dd73c8c5eab8a`

```bash
openclaw message send \
  --account main \
  --channel feishu \
  --target oc_f89abf0190161756b79dd73c8c5eab8a \
  --media "/Users/wowo/.openclaw/workspace/数学_YYYYMMDD.pdf" \
  --message "📐 数学每日一题 · 第X期"
```

### Cron 定时任务配置

- **时间**: 每天上午 11:00 (Asia/Shanghai)
- **Session**: isolated
- **执行内容**: 生成HTML → 转PDF → 发送飞书群（三步连续执行）

如需配置定时任务：
```bash
openclaw cron add \
  --name "数学每日一题" \
  --schedule "0 11 * * *" \
  --timezone "Asia/Shanghai" \
  --agent main \
  --task "生成数学每日一题卡片并发送飞书群"
```

## 模板文件

模板位置：`~/.openclaw/workspace/skills/daily-math-card/assets/math-problem-template.html`

模板变量：
- `{{issue}}` - 期数
- `{{date}}` - 日期
- `{{day_of_week}}` - 星期几
- `{{topic}}` - 主题标签
- `{{problem_content}}` - 题目内容
- `{{hint_content}}` - 思路提示
- `{{solution_content}}` - 答案与解析
