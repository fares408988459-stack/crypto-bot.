from tradingview_ta import TA_Handler, Interval

print("جاري جلب كافة بيانات المؤشرات والتحليل الفني بدقة من TradingView...")
handler = TA_Handler(
    symbol="BTCUSDT",
    screener="crypto",
    exchange="BINANCE",
    interval=Interval.INTERVAL_1_HOUR
)

analysis = handler.get_analysis()
summary = analysis.summary
indicators = analysis.indicators

all_indicators_text = ""
for key, value in indicators.items():
    all_indicators_text += f"- {key}: {value}\n"

print("\n" + "="*50)
print("تقرير التحليل الفني المباشر لزوج BTCUSDT (فاصل الساعة):")
print("="*50)
print(f"التوصية أو الملخص الفني العام: {summary}")
print("\nأبرز قراءات المؤشرات الفنية:")
print(f"- مؤشر القوة النسبية (RSI): {indicators.get('RSI', 'غير متوفر')}")
print(f"- المتوسط المتحرك البسيط (SMA 50): {indicators.get('SMA50', 'غير متوفر')}")
print(f"- المتوسط المتحرك البسيط (SMA 200): {indicators.get('SMA200', 'غير متوفر')}")
print(f"- مؤشر الماكدي (MACD.macd): {indicators.get('MACD.macd', 'غير متوفر')}")
print("="*50)
print("تم إتمام جمع ومعالجة البيانات الفنية بنجاح تام!")
