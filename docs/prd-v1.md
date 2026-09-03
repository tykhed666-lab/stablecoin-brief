# PRD v1 — Stablecoin Brief

Status: draft  
Owner:  
Date: 2026-09-01

## 1. Problem

Who uses it:

Internal staff who need to write stablecoin briefs or weekly reports (analysts / PMs), 
not retail investors opening an app ready to place an order.

How it is done now:

When writing materials, they have to manually open the issuer's official website, news, and trading pages, 
and copy the numbers and rules into the document.

Failure points:

1. Sentences lack links, making them impossible to verify later.
2. "1:1" is easily misunderstood as: any user can immediately redeem it for $1 in cash directly from the issuer.
3. When using AI to write the first draft, definitive statements are often read as "should buy / should sell" recommendations.

Evidence:
You once thought that a stablecoin stating "1:1" meant you could personally redeem it for USD with the company at any time, 
only to realize later that individuals can usually only buy and sell them on exchanges.
- 
- 

## 2. User

Primary: internal analyst / PM writing a weekly stablecoin memo.  
Not: retail user placing a trade.

## 3. Goal

Cut time-to-first-draft of a sourced memo, without increasing the chance that a reader treats the text as a buy/sell signal.

## 4. In scope (v1)

- One question or URL in
- Fixed output template: conclusion / sourced facts / product options / unverified lines
- Manual source allowlist (you paste links; the tool does not crawl the open web)

## 5. Out of scope

v1 不做下面这些事。做了就算出了这个项目的范围：

- 不预测价格，不写涨跌判断
- 句子里不出现：买、卖、加仓、开单、买入建议
- 不做成给普通用户用的网页或 App
- 不连接交易所下单，不接 Agent OS
- 不训练、不微调任何模型

## 6. Output contract

Every answer must contain:

1. Conclusion (≤3 sentences)
2. Facts (each line has a URL)
3. Product options A / B / C
4. Unverified sentences marked
5. Metric hypothesis

If a fact has no URL, the tool must label it `UNVERIFIED` or refuse to keep it in the Facts block.

## 7. Acceptance criteria

- [√] Running `python src/brief.py` produces the five blocks above
- [√] Three fixture questions in README can be completed without crashing
- [√] Output contains the string `not a trade recommendation` or `不是交易建议`
- [√] A sentence without a URL cannot sit in the Facts block unmarked
- [√] A reviewer can finish one task in 10 minutes
- [ ] 在项目根目录运行 `python .\src\brief.py`，能出现 Question 并打印五段（结论 / 事实 / 选项 / 未验证 / 指标）
- [ ] 五段里的「事实」每一行都带 http 链接；没有链接的句子只能放在「未验证」
- [ ] 输出里有一句：Not a trade recommendation. 或 不是交易建议。
- [ ] 用指定问题「为什么有的地区现货还能交易 USDT，有的地区更常看到 USDC？」时，可以在 10 分钟内只靠对比表填完「事实」，不靠记忆编数字

## 8. Metrics (see docs/metrics.md)

- Task completion
- Treated-as-trade-advice rate
- Human edit rate
- Unsourced sentence count

## 9. Risks

- Model hallucinates reserve numbers
- Reader ignores the disclaimer
- Sources go stale after regulation changes

## 10.Trust design

- 事实源：compare-table.md 里已填且带 URL 的格子；币安上架以用户打开的 support 公告原文为准。
- 模型不得覆盖事实源。
- 源打不开或过期：该句进 UNVERIFIED，或拒绝写进 Facts。
- 对客储备/赎回/牌照表述 = 单向门，v1 不对客发布。

## 11.Model permission
- v1 = 检索引用 + 人工起草（ladder 第 1–3 档）。
- 不做：建议下单、沙盒执行、真实下单。
