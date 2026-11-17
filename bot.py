from tradingview_ta import TA_Handler, Interval
import requests
import json
import os

# قراءة مفتاح الـ API بأمان من أسرار GitHub
API_KEY = os.environ.get("GEMINI_API_KEY")

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

prompt = f"""
أنت محلل أسواق مالية خبير ومهندس استراتيجيات تداول آلية. 
إليك كافة بيانات التحليل الفني والمؤشرات اللحظية والمتقدمة المستخرجة بالكامل من منصة TradingView لزوج BTCUSDT على فاصل الساعة:

التوصية العامة للملخص: {summary}

قائمة كافة المؤشرات والقيم الحالية:
{all_indicators_text}

المطلوب بناءً على دراسة متعمقة لكافة هذه الأرقام والمؤشرات بدقة متناهية:
1. تقديم قراءة تحليلية شاملة ومفصلة لوضع السوق الحالي (الزخم، الاتجاه العام، حالات التشبع الشرائي أو البيعي).
2. بناء استراتيجية تداول احترافية وكاملة تتضمن:
   - نقطة الدخول المقترحة (Entry Price).
   - مستوى وقف الخسارة الدقيق (Stop Loss).
   - الأهداف السعرية المتوقعة بترتيبها (Take Profit 1, 2, 3).
   - المبررات الفنية والرياضية المستندة حصرياً للأرقام الواردة في القائمة أعلاه.
"""

url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"
headers = {'Content-Type': 'application/json'}
data = {
    "contents": [{
        "parts": [{"text": prompt}]
    }]
}

print("جاري إرسال كافة المعلومات والبيانات إلى Gemini للتحليل...")
response = requests.post(url, headers=headers, data=json.dumps(data))

if response.status_code == 200:
    result = response.json()
    analysis_result = result['candidates'][0]['content']['parts'][0]['text']
    print("\n" + "="*60)
    print("التحليل الاستراتيجي الشامل من Gemini:")
    print("="*60)
    print(analysis_result)
    print("="*60)
else:
    print(f"حدث خطأ في الاتصال مع جيمني: {response.text}")
