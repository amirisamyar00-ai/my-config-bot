import requests
import re

def ali_vpn_collector():
    # آدرس منبع کانفیگ‌ها
    url = "https://raw.githubusercontent.com/mahdibland/V2RayAggregator/master/Eternity"
    print("🛰️ Connecting to source...")
    
    try:
        response = requests.get(url, timeout=15)
        # پیدا کردن لینک‌های vless
        configs = re.findall(r'vless://[^\s]+', response.text)
        
        # ذخیره ۱۰ تای اول در یک فایل ساده
        with open("ali_list.txt", "w") as f:
            for link in configs[:10]:
                f.write(link + "\n")
        
        print(f"✅ Success! {len(configs[:10])} configs saved in ali_list.txt")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    ali_vpn_collector()
