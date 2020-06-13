import requests
import sys

print ("Hazırlayan Mehmet Demirbas")
print ("twitter : @saltanatbekcisi")
print ("instagram : @root.mehmet")
def main():
	if len(sys.argv) < 2:
		print("kullanimi: python reverseip.py <domain>")
		sys.exit(1)

	url = "https://domains.yougetsignal.com/domains.php"
	payload = {
		"remoteAddress": sys.argv[1],
		"key": "",
		"_": ""
	}

	res = requests.post(url, data=payload, headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"})
	api = res.json()

	print("""
barindirdigi site sayisi {} Bulundu |{} ({}).
	""".format(api["domainCount"], api["remoteAddress"], api["remoteIpAddress"]))
	for lst in api.get("domainArray", []):
		print(lst[0])


if __name__ == "__main__":
	main()
