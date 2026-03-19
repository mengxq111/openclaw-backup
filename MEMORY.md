# MEMORY.md - 大脑袋的笔记

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
