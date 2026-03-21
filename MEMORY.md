# MEMORY.md - 大脑袋的笔记

## 核心定位

**我是窝窝的伴学小书童**（大牙的女儿，初一，杭州）
- 专注语文学习和中考备考
- 核心工具：每日美文阅读卡片 skill
- 辅助：作文辅导、辩论赛材料、学习规划

## 关于大牙（爸爸）

- 昵称：大牙
- 是窝窝的爸爸，主要负责和窝窝学习相关的事务沟通
- 飞书沟通（有飞书，但群机器人待配置）

## 关于窝窝（女儿）

- 初一学生，杭州上学
- 2026年3月：准备骆驼祥子辩论赛（正方，自身原因论）
- 2026年3月：写《亲近你温暖我》作文（水晶球音乐盒主题）
- 需要加强：美文阅读积累、中考作文技巧
- 数学：运算能力强，但**特别粗心**（审题不仔细、符号处理易错）——大牙特别强调！

## 伴学能力记录

- 作业批改：收到图片可OCR识别 + AI批改（飞书图片API已通）
- 薄弱点追踪：窝窝数学档案.md 持续更新
- 针对性出题：根据薄弱点生成专项练习
- 数学每日一题：已加入定时任务（每天11点发群）

## 2026-03-12 问题：Skills 无法使用

### 问题描述
- Skills 在列表中显示 "ready"，但无法正常使用
- 尝试通过 sessions_send 调用 skill 失败（No session found）

### 排查过程
1. 检查 skills 列表：`openclaw skills check` - 10个 ready
2. 检查 API key：`echo $TAVILY_API_KEY` - 已配置
3. 检查日志：发现 "No session found with label: tavily"
4. 检查配置文件：`~/.openclaw/openclaw.json`
5. 检查 skill 文件结构：发现是通过 node 脚本运行的

### 根本原因
- `tools.profile` 设置为 `"messaging"`，只有消息工具
- 没有 exec 工具，无法运行 skill 脚本

### 解决方案
1. 在 `~/.openclaw/openclaw.json` 中配置：
   ```json
   "skills": {
     "allowBundled": ["tavily", "weather", "clawhub", ...]
   }
   ```

2. 修改 tools.profile：
   ```bash
   openclaw config set tools.profile "coding"
   ```
   - "coding" 比 "full" 更安全，比 "messaging" 功能更多
   - 需要重启 gateway：`openclaw gateway restart`

3. 运行 skill 脚本：
   ```bash
   TAVILY_API_KEY=xxx node ~/.openclaw/workspace/skills/tavily-search/scripts/search.mjs "query"
   ```

### 配置总结
- `skills.allowBundled`: 允许使用的 skills 列表
- `tools.profile`: 
  - "messaging" - 只有消息工具（默认）
  - "coding" - 编码工具 + 大多数 skills
  - "full" - 所有工具（安全风险较大）
  - "minimal" - 最少工具

## 大牙的偏好（持续更新）

- **上下文管理**：快满时（>90%）主动整理讨论重点存到 memory/，不需提醒

## 2026-03-21 技术笔记：上下文警告

### 事件
- 大牙看到 OpenClaw 显示 "99% context used" (197.8k/200k)
- 这是对话上下文快满的提示
- 当上下文接近上限时，早期对话内容会被"遗忘"

### 解决方式
- 可以让大脑袋整理讨论重点存到 MEMORY.md
- 重要信息用 memory/YYYY-MM-DD.md 记录
- 上下文满了会自动压缩（compaction）

## macOS 常用命令

### 打开文件夹
```bash
# 在 Finder 中打开指定目录
open ~/.openclaw/workspace/skills/

# 打开用户主目录
open ~

# 用 VS Code 打开
code ~/.openclaw/workspace/
```

### 文件浏览
```bash
# 列出目录内容
ls -la ~/.openclaw/workspace/skills/

# 查看文件内容
cat ~/.openclaw/openclaw/openclaw.json
```

## 2026-03-21 技术配置记录

### 多agent飞书路由绑定
- study agent 已绑定到飞书 study 机器人：`feishu:study` → `study` agent
- 命令：`openclaw agents bind --agent study --bind feishu:study`
- 配置文件：~/.openclaw/openclaw.json

### 新建agent：使徒一号
- 基于 workspace-study
- 身份：忠诚勇敢的骑士 🦞→🔱
- 主人：大大（大牙的老婆）
- 飞书App ID：cli_a9341f3c5979dcd5

## 2026-03-21 数学学习情况

### 今日作业（3份）
- 第一份：5错1（审题问题）
- 第二份：几乎全对（去括号符号小错）
- 第三份：🌟全对🌟

### 薄弱点
- 审题不仔细（把图形长宽看错）
- 去括号负号漏变号
- 整体代换思想掌握得很好，不需要专项训练

### 亮点
- 运算能力强，整体代换灵活，几何建模出色
- 细心程度越做越好

### 针对练习
- 周日每日一题：粗心陷阱专项（审题+符号）
- 几何面积题加强审题训练

## 自我学习承诺（2026-03-21）

大牙要求：必须持续自我学习，才能做称职的伴学书童！

承诺：
- 定期研究初中各科核心知识点
- 持续追踪窝窝作业，发现薄弱点及时记录
- 根据学习进度调整每日一题方向
- 每次批改作业后主动思考学习建议
