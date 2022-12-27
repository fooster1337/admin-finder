import requests, os, sys
from requests.exceptions import ConnectionError
from colorama import Fore


version = "1.0"
program_name = sys.argv[0]
#domain = sys.argv[1]
lem = len(sys.argv)
result = 'result-scan-admin.txt'

g = Fore.GREEN
r = Fore.RED
reset = Fore.RESET

usage = (f"usage : python3 {program_name} <domain>")
banner = (f"""
             ;::::;                          
           ;::::; :;                          
         ;:::::'   :;                         
        ;:::::;     ;.                        
       ,:::::'       ;           OOO      
       ::::::;       ;          OOOOO    
       ;:::::;       ;         OOOOOOOO      
      ,;::::::;     ;'         / OOOOOOO      
    ;:::::::::`. ,,,;.        /  / DOOOOOO    
  .';:::::::::::::::::;,     /  /     DOOOO   
 ,::::::;::::::;;;;::::;,   /  /        DOOO  
;`::::::`'::::::;;;::::: ,#/  /          DOOO 
:`:::::::`;::::::;;::: ;::#  /            DOOO
::`:::::::`;:::::::: ;::::# /              DOO
`:`:::::::`;:::::: ;::::::#/               DOO
 :::`:::::::`;; ;:::::::::##                OO
 ::::`:::::::`;::::::::;:::#                OO
 `:::::`::::::::::::;'`:;::#                O 
  `:::::`::::::::;' /  / `:#                  
   ::::::`:::::;'  /  /   `#

{r}The Angel Of Death {reset}- {g}Admin Finder{reset}
Version : {version}
{usage}""")


def admin_checker():
	if lem != 2:
		print(banner)
		sys.exit(0)

	else:
		domain = sys.argv[1]
		get_wordlist = "https://fooster1337.github.io/assets/wordlist.txt"
		word = requests.get(get_wordlist)
		get_word = word.content.decode('utf-8')
		getStatus = requests.get(domain)
		getCode = getStatus.status_code
		#print(getCode)
		if getCode == 200:
			print(f"Scanning : {domain}")
			print(f"Result save on {result}")
			for i in get_word.splitlines():
				dom_pls = (f"{domain}/{i}")
				rq = requests.get(dom_pls)
				req = rq.status_code
				#print(f"{req} -> {dom_pls}")
				if req == 200:
					print(f"{g}[Found!] {reset}-> {dom_pls} [{g}{req}{reset}]")
					with open(result, 'a') as f:
						f.write(dom_pls)
						f.write("\n")
					f.close()
				elif req != 200:
					print(f"{r}[NoLuck] {reset}-> {dom_pls} [{r}{req}{reset}]")
		elif getCode != 200:
			print(f"Unknown Error : {getCode}\n{usage}")
			sys.exit(0)

if __name__ == "__main__":
	try:
		admin_checker()
	except ConnectionError as E:
		print(f"unable to catch {domain}\n{usage}")
	except KeyboardInterrupt:
		print(f"\n{r}Exit...{reset}")
		sys.exit(0)
	except ModuleNotFoundError:
		os.system("pip3 install requests && pip3 install colorama")
		admin_checker()