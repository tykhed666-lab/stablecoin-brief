# PRD v1 — Stablecoin Brief

Status: draft  
Owner:  
Date: 2026-09-01

## 1. Problem

（用 5–8 句写：谁、在做什么、卡在哪、你见过的证据。不要写「AI 很重要」。）

Evidence:

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

- Buy / sell / target price language
- On-chain trading or Agent OS execution
- Auto-publishing to users
- Multi-language UI (docs are bilingual; the tool UI can stay Chinese or English only)

## 6. Output contract

Every answer must contain:

1. Conclusion (≤3 sentences)
2. Facts (each line has a URL)
3. Product options A / B / C
4. Unverified sentences marked
5. Metric hypothesis

If a fact has no URL, the tool must label it `UNVERIFIED` or refuse to keep it in the Facts block.

## 7. Acceptance criteria

- [ ] Running `python src/brief.py` produces the five blocks above
- [ ] Three fixture questions in README can be completed without crashing
- [ ] Output contains the string `not a trade recommendation` or `不是交易建议`
- [ ] A sentence without a URL cannot sit in the Facts block unmarked
- [ ] A reviewer can finish one task in 10 minutes

## 8. Metrics (see docs/metrics.md)

- Task completion
- Treated-as-trade-advice rate
- Human edit rate
- Unsourced sentence count

## 9. Risks

- Model hallucinates reserve numbers
- Reader ignores the disclaimer
- Sources go stale after regulation changes
