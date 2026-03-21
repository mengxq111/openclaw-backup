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

## Card Structure (per card)

```
顶部色带（绿色系）
├─ 期数 + 日期
├─ 文章标题
└─ 作者

内容区
├─ 原文选读（带缩进 + 引文装饰）  ← 600-900字
├─ 出处与赏析（背景 + 写作手法分析）
├─ 中考对应考点（🎯 标注）
├─ 好词好句（2列：词语标签 + 精彩句子）
└─ 写作应用（2个技法，各配仿写例子） ← 对应中考评分维度
```

## Output Location

`/Users/wowo/Documents/学习辅导/语文/阅读赏析/每日美文_卡片.html`

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
