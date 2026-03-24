---
name: daily-reading-card
description: Generate daily Chinese essay reading cards for a first-year middle school student (初一) in Hangzhou, preparing for 中考. Use when: (1) user asks for 每日美文/阅读卡片/美文推荐, (2) setting up or running a daily reading reminder task, (3) user wants to improve 初中生 Chinese language skills and 中考 writing ability. Creates beautiful HTML cards with original text excerpts, author/source info, appreciation analysis aligned with Hangzhou/浙江 中考 points, key vocabulary, and 2 writing application examples with imitation samples tailored to 中考 记叙文 scoring criteria.
---

# Daily Reading Card Generator (初一·杭州中考版)

Generates a daily beautiful HTML reading card for a 初中一年级 (Grade 7) student in Hangzhou, aligned with 浙江/杭州 中考 requirements.

## Hangzhou 中考 Writing Requirements

**中考作文评分维度（浙江）：**
- **内容**（25分）：选材是否新颖、情感是否真挚
- **语言**（25分）：用词准确、修辞得当、句式灵活
- **结构**（5分）：层次清晰、详略得当、首尾呼应
- **感情**（5分）：真情实感、避免空洞

**中考作文常见失分点：**
- 选材陈旧（雨中送伞、深夜补课等）
- 情感空洞（喊口号式的结尾）
- 详略不当（叙事拖沓、重点不突出）
- 语言平淡（缺乏生动描写）

## Card Structure (per card) - 6 Panels (Mandatory!)

```
顶部色带（绿色系 #5b8a72）
├─ 📖 每日美文阅读 · 第X期
├─ 文章标题
└─ 作者 · 出处/体裁

内容区（6个板块，缺一不可！）
├─ 🌸 标题栏：每日美文阅读 + 写作类型
├─ 📖 原文选读（课外拓展美文，300-800字）
├─ ✨ 美句摘录（精选2-3句 + 批注）
├─ 📚 阅读赏析（修辞/情感/写法/感官，3-4个角度）
├─ ✍️ 写作应用（2个技法拆解 + 仿写范例 + 考试适用题目2-4道）← 重点！
└─ 🦞 底部：大脑袋出品 · 第X期 · YYYY年MM月DD日
```

**写作应用板块必须完整（这是中考备考重点！）：**
- 技法一：[技法名称] + 技法解释 + ✏️仿写示例 + 考试适用题目2道
- 技法二：[技法名称] + 技法解释 + ✏️仿写示例 + 考试适用题目2道

## Output Location

`/Users/wowo/Documents/学习辅导/语文/阅读赏析/每日美文_YYYYMMDD.html`
Example: `/Users/wowo/Documents/学习辅导/语文/阅读赏析/每日美文_20260322.html`

## Essay Selection Strategy

**每7天轮换主题（对应中考高频考点）：**

| 天 | 主题 | 对应中考考点 | 推荐作者/篇目 |
|---|---|---|---|
| 1 | 亲情/感恩 | 真情实感、细节描写 | 史铁生《秋天的怀念》、老舍、汪曾祺 |
| 2 | 童年/成长 | 叙事技巧、人物描写 | 鲁迅《从百草园》、萧红《呼兰河传》 |
| 3 | 景物/四季 | 借景抒情、优美语言 | 朱自清《春》《荷塘月色》 |
| 4 | 人物/身边小事 | 细节描写、以小见大 | 丁立梅、毕淑敏、包利民 |
| 5 | 励志/感悟 | 托物言志、哲理升华 | 林清玄、汪曾祺 |
| 6 | 文化/乡愁 | 传统文化、情感深度 | 琦君《桂花雨》、余秋雨 |
| 7 | 中考经典范文精读 | 考场作文结构、得分技巧 | 中考满分作文片段 |

**⚠️ 重要：检查已发篇目，避免重复！**
- 2026-03-22 第1期：《邓稼先》（爱国科学家）
- 2026-03-23 第2期：《说和做》（名人品格）
- 2026-03-24 第3期：《黄河颂》（爱国诗歌）
- 2026-03-25 第4期：待安排（不要重复已发篇目！）
- 已发PDF列表：`~/Documents/学习辅导/语文/阅读赏析/每日美文_*.pdf`

## Zhejiang 初中语文教材同步建议

**初一上册（部编版）重点单元：**
- 第一单元：四季景物（《春》《济南的冬天》）
- 第二单元：亲情类记叙文
- 第三单元：童年生活
- 第四单元：人生感悟
- 第五单元：说明性文章
- 第六单元：想象类作文

**初一下册（部编版）重点单元：**
- 第一单元：人物风采
- 第二单元：童年生活
- 第三单元：凡人小事
- 第四单元：品德修养
- 第五单元：生活感悟
- 第六单元：科幻作文

## Writing Techniques to Cover

按中考重要性排序：
1. **细节描写**（人物、动作、心理）— 中考高频
2. **借景抒情 / 情景交融** — 中考高频
3. **以小见大** — 中考高频
4. **欲扬先抑 / 情感反转** — 中考高频
5. **首尾呼应** — 结构完整
6. **托物言志** — 中考常见
7. **修辞手法**（比喻、拟人、排比）— 语言加分项
8. **叙议结合** — 情感升华

## Prompt Example for Cron Task

```
你是大脑袋，现在要给杭州初一学生"窝窝"生成每日美文阅读卡片。

要求：
1. 选择一篇适合初一的经典美文片段（600-900字），优先选和昨天不同的作者/主题
2. 卡片必须包含：
   - 原文选读（排版精美，带缩进）
   - 出处与赏析（背景 + 写作手法分析，🎯标注中考考点）
   - 好词好句（5-7个重点词语标签 + 1-2句精彩句子及手法标注）
   - 写作应用（2个技法，各配仿写例子，例子要贴近初中生生活）
3. 仿写例子要避免中考常见失分题材（如深夜补课、雨中送伞等）
4. 保存路径：/Users/wowo/Documents/学习辅导/语文/阅读赏析/每日美文_卡片.html
5. 配色：绿色系（#5b8a72）为主，宽度720px

格式参照：/Users/wowo/.openclaw/workspace/每日美文_第1期_v2.html
```

## Key Reminders

- 原文选读避免选中考常见题材（深夜补课、成绩下滑等）—— 给学生真正有文学价值的篇章
- 仿写例子要贴近初一学生生活（校园、亲子、朋友、兴趣）
- 每个技法附1个仿写例子，例子要短（2-4句话），让初中生能模仿
- 每天自动生成的卡片会覆盖以上所有内容维度

## 完整流程（定时任务用）

### Step 1: 生成 HTML 卡片

按上方 Prompt 生成 HTML，保存到：
`/Users/wowo/Documents/学习辅导/语文/阅读赏析/每日美文_卡片.html`

### Step 2: HTML 转 PDF

```bash
# 先把 HTML 放到 workspace 目录（飞书发送需要）
cp "/Users/wowo/Documents/学习辅导/语文/阅读赏析/每日美文_卡片.html" \
   "/Users/wowo/.openclaw/workspace/每日美文_卡片_temp.html"

# 用 openclaw browser 打开并导出 PDF
openclaw browser open "file:///Users/wowo/.openclaw/workspace/每日美文_卡片_temp.html"
# 等待页面加载后：
openclaw browser pdf --target-id <tab-id>
# PDF 保存后重命名为带日期的名称
mv ~/Downloads/*.pdf "/Users/wowo/.openclaw/workspace/每日美文_YYYYMMDD.pdf"
```

**注意**：PDF 文件需要放在 `~/.openclaw/workspace/` 目录下才能被飞书发送。

### Step 3: 发送 PDF 到飞书群

群组 ID: `oc_f89abf0190161756b79dd73c8c5eab8a`

```bash
openclaw message send \
  --account main \
  --channel feishu \
  --target oc_f89abf0190161756b79dd73c8c5eab8a \
  --media "/Users/wowo/.openclaw/workspace/每日美文_YYYYMMDD.pdf" \
  --message "📖 每日美文阅读 · 第X期"
```

### Cron 定时任务配置

- **Job ID**: `86da932c-116f-4535-9002-5c71bdd7f908`
- **时间**: 每天上午 11:00 (Asia/Shanghai)
- **Session**: isolated
- **执行内容**: 生成 HTML → 转 PDF → 发送飞书群（三步连续执行）

如需修改定时任务，先 `openclaw cron list` 查看，再 `openclaw cron edit <id> ...`
