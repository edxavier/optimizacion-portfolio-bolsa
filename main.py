import pandas as pd
import yfinance as yf

tickers = [
    "VWRA.L",  # Vanguard FTSE All-World UCITS ETF (renta variable global, acumulación)
    "AGGU.L",  # iShares Core Global Aggregate Bond UCITS ETF (renta fija global, hedged USD)
    "ZPRV.DE",  # SPDR MSCI USA Small Cap Value Weighted UCITS ETF (small caps value EE.UU.)
    "FUSD.L",  # Fidelity US Quality Income UCITS ETF (calidad/dividendos EE.UU.)
    "EIMI.L",  # iShares Core MSCI Emerging Markets IMI UCITS ETF (mercados emergentes)
    "SMGB.L",  # VanEck Semiconductor UCITS ETF (sector semiconductores)
]


def get_prices(
    tickers,
):
    df = yf.download(
        tickers, start="2021-01-01", end="2026-01-01", interval="1mo", auto_adjust=True
    )

    prices = df["Close"]
    if isinstance(prices.columns, pd.MultiIndex):
        prices.columns = prices.columns.get_level_values(0)
    prices.columns = prices.columns.str.upper()
    prices.index = prices.index.normalize()
    return prices


def main():
    prices = get_prices(tickers)
    prices.to_csv("precios_mensuales.csv")
    print(prices.tail(10))
    print(f"\nShape: {prices.shape}")
    print(f"Rango: {prices.index[0].date()} -> {prices.index[-1].date()}")


if __name__ == "__main__":
    main()
