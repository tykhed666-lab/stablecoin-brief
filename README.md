# Stablecoin Brief

Internal research assistant for stablecoin product decisions.  
内部稳定币研究助手。输出是带出处的研究笔记，**不是交易建议**。

**Not a trading product.** The model must not say buy / sell / add size / 加仓.

## What this is

A small loop for a product internship portfolio:

1. PRD
2. Clickable (or runnable) prototype
3. 5-user test notes
4. Bilingual decision memo
5. Post-launch metric definitions

## Who it is for

Internal analyst / PM writing a decision memo. Not retail traders.

## Quick start

```bash
cd src
python brief.py
```

Paste a question such as:

- Why is USDT spot restricted for some EU users?
- How do USDC and USDT reserves differ?
- Should a yield number appear on a new-user earn page?

The script prints a fixed template. You must delete or mark any sentence without a URL.

## Repo map

| Path | Purpose |
|---|---|
| `docs/prd-v1.md` | First PRD before tests |
| `docs/prd-v2.md` | PRD after 5-user test |
| `docs/memo-zh.md` | Decision memo, Chinese |
| `docs/memo-en.md` | Decision memo, English |
| `docs/usability-notes.md` | Raw notes from 5 testers |
| `docs/metrics.md` | Launch metrics, even if traffic is only 5 people |
| `docs/compare-table.md` | USDT vs USDC facts with sources |
| `src/brief.py` | Minimal prototype |
| `assets/` | Demo recording, screenshots |

## Out of scope

- Price prediction
- Order placement
- Agent OS trading permissions as v1
- Training or fine-tuning a model
