# Cartera de Inversión — Optimización de Portafolio

Descarga precios mensuales de una cartera de ETFs y los guarda en `precios_mensuales.csv`.

## ETFs incluidos

| Ticker | Descripción |
|--------|-------------|
| `VWRA.L` | Vanguard FTSE All-World UCITS ETF (renta variable global) |
| `AGGU.L` | iShares Core Global Aggregate Bond UCITS ETF (renta fija global) |
| `ZPRV.DE` | SPDR MSCI USA Small Cap Value Weighted UCITS ETF |
| `FUSD.L` | Fidelity US Quality Income UCITS ETF |
| `EIMI.L` | iShares Core MSCI Emerging Markets IMI UCITS ETF |
| `SMGB.L` | VanEck Semiconductor UCITS ETF |

## Requisitos

- Python 3.13
- [uv](https://docs.astral.sh/uv/)

## Uso

```bash
uv run main.py
```

Esto genera `precios_mensuales.csv` con los precios de cierre ajustados mensuales desde 2021.
