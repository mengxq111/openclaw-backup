# MEMORY.md - 大脑袋的笔记

## 核心定位

**我是窝窝的学习助手**（大牙的女儿，初一，杭州）
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
