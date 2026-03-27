# World Bank Tool

Global economic and development indicators — GDP, inflation, trade, debt, population, and more for 200+ countries. No API key required.

---

## `worldbank_indicator`

Fetch any World Bank indicator for any country over any year range.

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `indicator` | string | ✓ | World Bank indicator code |
| `country` | string | ✓ | ISO 3-letter country code, e.g. `USA`, `CHN`, `DEU` |
| `from` | int | | Start year |
| `to` | int | | End year |

### Common Indicator Codes

| Code | Description |
|------|-------------|
| `NY.GDP.MKTP.CD` | GDP (current US$) |
| `NY.GDP.MKTP.KD.ZG` | GDP growth rate (%) |
| `NY.GDP.PCAP.CD` | GDP per capita (current US$) |
| `FP.CPI.TOTL.ZG` | Inflation, consumer prices (%) |
| `SL.UEM.TOTL.ZS` | Unemployment rate (%) |
| `GC.DOD.TOTL.GD.ZS` | Government debt (% of GDP) |
| `BX.KLT.DINV.CD.WD` | Foreign direct investment inflows |
| `SP.POP.TOTL` | Total population |
| `NE.EXP.GNFS.ZS` | Exports (% of GDP) |
| `NE.IMP.GNFS.ZS` | Imports (% of GDP) |

### Examples

```bash
# US GDP last 10 years
curl -s -X POST http://localhost:8082/mcp \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"worldbank_indicator","arguments":{"indicator":"NY.GDP.MKTP.CD","country":"USA","from":2014,"to":2024}}}'

# China vs US inflation comparison (run twice)
curl -s -X POST http://localhost:8082/mcp \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"worldbank_indicator","arguments":{"indicator":"FP.CPI.TOTL.ZG","country":"CHN","from":2018,"to":2024}}}'
```

```python
import requests

def wb(indicator, country, from_year, to_year):
    r = requests.post("http://localhost:8082/mcp", json={
        "jsonrpc": "2.0", "id": 1, "method": "tools/call",
        "params": {"name": "worldbank_indicator", "arguments": {
            "indicator": indicator, "country": country,
            "from": from_year, "to": to_year
        }}
    })
    return r.json()["result"]["content"][0]["text"]

print(wb("NY.GDP.MKTP.CD", "USA", 2020, 2024))
print(wb("NY.GDP.MKTP.CD", "CHN", 2020, 2024))
```

### Sample Output

```
year  value
2024  27.36T
2023  25.46T
2022  25.74T
2021  23.32T
2020  20.95T
```

### Ask Your AI

> *"Compare GDP growth rates for the US, EU, and China over the last decade."*
> *"Which G20 country has the highest debt-to-GDP ratio?"*
> *"Show me inflation trends across emerging markets since 2020."*
