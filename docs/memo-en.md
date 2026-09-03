# Decision memo (English)

Date:  9.2
Audience: internal product / research

## Recommendation

1. Ship v1 as an internal research brief only.
2. Do not ship a retail summary or a trading agent in this version.
3. Tests: n readers; x treated the text as a reason to buy USDT; y thought they could redeem $1 with the issuer.

## Facts (URL on every line)

1.  Tether International, S.A. de C.V.
   Source: https://tether.to/en/legal/
2.  Official process (disclosure document of the El Salvador entity): Only KYC Verified Customers can subscribe/redeem directly on the official website at the pegged exchange rate (with reduced fees). Minimum transaction size is US$100,000. Redemption flow: the user sends tokens to Tether → tokens are removed from circulation → fiat is paid to the user’s bank account.
   Source:https://tether.to/public/Relevant_Information_Document_-_Tether_International,_S.A._de_C.V..pdf
3. Binance announcement: From 23:59 UTC on 31 March 2025, spot pairs of stablecoins that are not MiCA-compliant will be delisted for EEA users; the list includes USDT.
   Source: https://www.binance.com/en/square/post/21043822260465
## Product implications

- Likely user misread
- Listing / geo / compliance issue
- Most dangerous sentence if this ships to retail

## Options

- A Internal research only
- B Retail summary
- C Trading agent

## Measure and kill criteria

Pick:  A
Success: zero unsourced lines in Facts; zero buy/sell wording in the demo brief.
Kill: a later draft tells readers to buy/sell, or states that USDT is delisted worldwide.
Why not C: C moves account permissions and funds. That is a different product with a separate approval path.
