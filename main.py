import requests
import re

def ali_vpn_collector():
    # لیست چندین منبع مختلف برای اطمینان بیشتر
    sources = [
        "https://raw.githubusercontent.com/mahdibland/V2RayAggregator/master/Eternity",
        "https://raw.githubusercontent.com/barry-far/V2RAY-CONFIGS/main/Warp_Config.txt",
        "https://raw.githubusercontent.com/IranianCypherpunks/sub/main/config",
        "https://raw.githubusercontent.com/LalatinaHub/Mineralhearth/main/Lists/Proxies/V2Ray.txt"
    ]
    
    all_configs = []
    print("🛰️ Connecting to multiple sources...")
    
    for url in sources:
        try:
            response = requests.get(url, timeout=10)
            # پیدا کردن انواع لینک‌ها (vless, vmess, ss, trojan)
            configs = re.findall(r'(vless|vmess|ss|trojan)://[^\s]+', response.text)
            # استخراج کل لینک
            full_configs = re.findall(r'(?:vless|vmess|ss|trojan)://[^\s]+', response.text)
            all_configs.extend(full_configs)
        except:
            continue
            
    # حذف تکراری‌ها و ذخیره ۲۰ تای اول
    unique_configs = list(set(all_configs))
    
    with open("ali_list.txt", "w") as f:
        for link in unique_configs[:20]:
            f.write(link + "\n")
    
    print(f"✅ Success! {len(unique_configs[:20])} configs saved.")

if __name__ == "__main__":
    ali_vpn_collector()
