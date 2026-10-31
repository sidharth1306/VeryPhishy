from core.analyzers.text_analyzer import analyze_text

messages=[
    "Dear customer your SBI account will be blocked today. Update KYC immediately",
    "Your OTP is 136749, do not share it with anyone",
    "Your KYC is pending, please update your KYC",
    "Hi, are we still meeting at 5?"
]

for msg in messages:
    print(msg)
    for s in analyze_text(msg):
        print("   ->",s.id,s.weight,"|",s.reason)
    print()