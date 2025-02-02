# Custom sentiment score for stocks/finance terms in both news article and Reddit
new_words = {
    "moon": 3.5,
    "mooon": 3.5,
    "moooon": 3.5,
    "space": 3.5,
    "jupiter": 3.5,
    "mars": 3.5,
    "star": 3,
    "stars": 3,
    "bear": -2,
    "bearish": -3,
    "bull": 2,
    "bullish": 3,
    "surged": 2.5,
    "surges": 2.5,
    "leap": 2,
    "leaps": 2,
    "hold": 1,
    "holding": 1,
    "added": 2.5,
    "buy": 2,
    "buying": 2,
    "bought": 2,
    "sell": -2,
    "sells": -2,
    "selling": -2,
    "sell-off": -2,
    "sold": -2,
    "sale": 2,
    "discount": 2,
    "cheap": 2,
    "pump": 2,
    "pumps": 2,
    "dump": -2,
    "dumps": -2,
    "partner": 2,
    "partnership": 2,
    "participate": 2,
    "green": 1.5,
    "red": -1.5,
    "rip": -2,
    "go": 1,
    "call": 1.5,
    "calls": 1.5,
    "puts": -1.5,
    "load": 1.5,
    "loading": 1.5,
    "rocket": 2.5,
    "rockets": 2.5,
    "rocketing": 2.5,
    "skyrocket": 2.5,
    "skyrockets": 2.5,
    "skyrocketing": 2.5,
    "soar": 2,
    "soars": 2,
    "soaring": 2,
    "soared": 2,
    "wiped": -1.5,
    "fly": 2.5,
    "flying": 2.5,
    "rise": 2,
    "rises": 2,
    "rising": 2,
    "slip": -1.8,
    "slips": -1.8,
    "plunge": -2.5,
    "plunges": -2.5,
    "plunged": -2.5,
    "plummet": -2.5,
    "plummets": -2.5,
    "plummeted": -2.5,
    "dive": -2.2,
    "dives": -2.2,
    "diving": -2.2,
    "dividend": 1.5,
    "dividends": -1.5,
    "fall": -2,
    "falling": -2,
    "tumble": -3,
    "tumbles": -3,
    "tumbled": -3,
    "tumbling": -3,
    "gloom": -2,
    "gloomy": -2,
    "falls": -2,
    "fell": -2,
    "sink": -2,
    "sinks": -2,
    "sinking": -2,
    "sank": -2,
    "sunk": -2,
    "slide": -1.5,
    "sliding": -1.5,
    "target": 2,
    "shorting": -2.5,
    "short": -2.5,
    "shorted": -2.5,
    "dip": -2,
    "dips": -2,
    "dipping": -2,
    "drop": -2,
    "drops": -2,
    "dropping": -2,
    "dropped": -2,
    "break": 1.5,
    "squeeze": 2.5,
    "regulate": -2,
    "regulates": -2,
    "regulations": -2,
    "regulating": -2,
    "waking": 1.5,
    "sleeping": -1.5,
    "wake": 1,
    "sleep": -1,
    "printing": 1.5,
    "print": 1.5,
    "bleed": -1.5,
    "bleeding": -1.5,
    "undervalued": 2,
    "overvalued": -2,
    "underperform": -2,
    "underperforms": -2,
    "underperforming": -2,
    "underperformed": -2,
    "perk": 2,
    "perks": 2,
    "pop": 1.5,
    "jump": 2,
    "supercharge": 2.5,
    "jumped": 2,
    "popped": 1.5,
    "tank": -1.5,
    "tanked": -1.5,
    "shaved": -1.5,
    "tanking": -1.5,
    "all": 1.2,
    "gang": 1,
    "up": 2,
    "down": -2,
    "upgrade": 2,
    "downgrade": -2,
    "lost": -1.5,
    "lose": -1.5,
    "loses": -1.5,
    "losing": -1.5,
    "loser": -1.5,
    "losers": -1.5,
    "loss": -1.5,
    "losses": -1.5,
    "lawsuit": -1.5,
    "earn": 1.5,
    "multiplied": 1,
    "surge": 2.5,
    "surging": 2.5,
    "explode": 3,
    "exploded": 3,
    "bubble": -1.8,
    "collaborate": 1.5,
    "collaborating": 1.5,
    "merge": 1.5,
    "merging": 1.5,
    "merger": 1.5,
    "acquire": 1.5,
    "acquiring": 1.5,
    "acquisition": 1.5,
    "record": 2.5,
    "halted": -2.8,
    "diamond": 2.5,
    "shed": -1,
    "slipped": -1.8,
    "crash": -2.5,
    "crashed": -2.5,
    "crashing": -2.5,
    "invest": 1.5,
    "invests": 1.5,
    "investing": 1.5,
    "investment": 1.5,
    "inflow": 1.5,
    "inflows": 1.5,
    "outflow": -1.5,
    "outflows": -1.5,
    "double": 2,
    "dilution": -2.5,
    "bounce": 1.5,
    "bounces": 1.5,
    "hit": 1.5,
    "miss": -1.5,
    "blowout": 2.5,
    "rally": 1.5,
    "rallies": 1.5,
    "rallied": 1.5,
    "reverse": -1.5,
    "reverses": -1.5,
    "high": 2,
    "higher": 2,
    "low": -2,
    "lower": -2,
    "lowering": -2,
    "lowered": -2,
    "expansion": 2.5,
    "shortage": -2.5,
    "watchlist": 1.5,
    "watchlists": 1.5,
    "flat": -2,
    "sideway": -2,
    "sideways": -2,
    "outperform": 2,
    "outperforms": 2,
    "outperformed": 2,
    "outperforming": 2,
    "outpace": 2,
    "outpaces": 2,
    "outpacing": 2,
    "inflation": -2,
    "antitrust": -2,
    "cut": -2,
    "cuts": -2,
    "cutting": -2,
    "launch": 1.5,
    "launching": 1.5,
    "launches": 1.5,
    "launched": 1.5,
}
