import re,yaml
from core.facts import Signal
with open("rules/india_patterns.yaml",encoding="utf-8") as f:
    data = yaml.safe_load(f)
def analyze_text(text):
    signals=[]
    for rule in data["rules"]:
        for pattern in rule["patterns"]:
            if re.search(pattern,text,re.IGNORECASE):
                signals.append(Signal(rule["id"], rule["category"], rule["weight"], rule["reason"]))
                break
    return signals


