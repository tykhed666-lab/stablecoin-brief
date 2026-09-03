STABLECOIN BRIEF
Not a trade recommendation. 不是交易建议。
============================================================
QUESTION
内部研究助手和可交易 Agent 的权限边界应停在哪一档？

1. CONCLUSION (≤3 sentences)
- 本项目 v1 停在「检索引用 + 人工起草」，不执行交易。
- 可交易 Agent 会动用账户权限，属于另一产品，需要单独的授权、限额和合规，不能由研究助手顺手加上。
- 稳定币文案若对客承诺赎回或收益，属于单向门；v1 不对客、不下单。

2. FACTS (delete any line without a URL)
   - 本工具 v1 不对客、不执行交易 / Agent OS。https://raw.githubusercontent.com/tykhed666-lab/stablecoin-brief/main/docs/prd-v1.md）。
   - Circle Mint + 对客兑付风险，不合格者被导向交易所等二级渠道，而不是开 Mint 账户。https://www.circle.com/circle-mint
   - Set the permissions, accounts, and limits for each agent.https://www.binance.com/en/agent-os

3. PRODUCT OPTIONS
A. v1 仅内部起草，ladder 停在第 3 档
B. 先做对客摘要仍不下单
C. 做成可下单 Agent

4. UNVERIFIED (move leftover claims here)
- Agent 默认能否提现、亏损有无平台硬顶（未打开产品帮助中心原文）。
- Agent OS 与本内部助手是否同一套权限系统。

5. METRIC HYPOTHESIS
   If we shipped this, we would watch:
   -输出中是否出现下单/买入指令；目标为 0。
============================================================

Next: fill Facts from docs/compare-table.md only.