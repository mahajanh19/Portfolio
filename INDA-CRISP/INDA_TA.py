import yfinance as yf
import pandas_ta as ta
inda = yf.download("INDA", start="2021-01-01", end="2025-3-31")
inda.columns = [col[0] if isinstance(col, tuple) else col for col in inda.columns]
print(inda.head())
inda.ta.strategy("All",append=True, timed=True)