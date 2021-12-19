from json import loads, dumps
from datetime import datetime
from langlib1 import Colors
from os import system

system("clear")

print(f"""
{Colors['lred']}
████████╗███████╗ ██████╗██╗  ██╗ ██████╗ ██████╗ ██████╗ ██╗████████╗
╚══██╔══╝██╔════╝██╔════╝██║  ██║██╔═══██╗██╔══██╗██╔══██╗██║╚══██╔══╝
   ██║   █████╗  ██║     ███████║██║   ██║██████╔╝██████╔╝██║   ██║   
   ██║   ██╔══╝  ██║     ██╔══██║██║   ██║██╔══██╗██╔══██╗██║   ██║   
   ██║   ███████╗╚██████╗██║  ██║ ██████╔╝██║  ██║██████╔╝██║   ██║   
   ╚═╝   ╚══════╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚═╝   ╚═╝

  {Colors['lgreen']}=================================================================
  |                     > choose an item <                        |
  =================================================================\x1b[0m

        +———————————————————————————————————————————————————+
        |   \x1b[33m[1]\x1b[0m Add               ¦    \x1b[33m[2]\x1b[0m Delete           |
        |   \x1b[33m[3]\x1b[0m edit title/link   ¦    \x1b[33m[4]\x1b[0m styling lists    |
        |   \x1b[33m[5]\x1b[0m get DataBase      ¦    \x1b[33m[6]\x1b[0m get logcat       |
        |   \x1b[33m[7]\x1b[0m set warning       ¦    \x1b[33m[8]\x1b[0m get warnings     |
        |   \x1b[33m[9]\x1b[0m edit warnings     ¦    \x1b[33m[0]\x1b[0m exit             |
        +———————————————————————————————————————————————————+
""")

while True:
	try:
		item = int(input("➜ item: ") or 0)
		db, chars = "db.json", [loads(open("theme.json").read())['charForTitle'], loads(open("theme.json").read())['charForID']]
	
		if item == 0 :
			exit()
	
		elif item == 1 :
			smallChannels, bigChannels, groups = loads(open(db).read()).get("smallChannels"), loads(open(db).read()).get("bigChannels"), loads(open(db).read()).get("groups")
	
			title = input("➜ title: ")
			link = input(f"➜ link: {Colors['underline']}{Colors['dblue']}")
			print("\x1b[0m", end="")
			members = int(input(f"➜ members: {Colors['bold']}{Colors['dyellow']}"))
			
			linkType = "group" if "joing/" in link else "channel"
		
			if linkType == "channel" and members < 500 :
				smallChannels.append({
					"title":title,
					"count":members,
					"link": link,
				})
			
			elif linkType == "channel" and members > 500 :
				bigChannels.append({
					"title":title,
					"count":members,
					"link": link,
				})
			
			else :
				groups.append({
					"title":title,
					"count":members,
					"link": link,
				})
			
			smallChannels.sort(key=lambda i:i["count"])
			bigChannels.sort(key=lambda i:i["count"])
			groups.sort(key=lambda i:i["count"])
			
			open(db,"w").write(dumps({
				"smallChannels": smallChannels,
				"bigChannels": bigChannels,
				"groups": groups
			},indent=4,ensure_ascii=False))
			open("warns.json","w").write(dumps({
				link:0
			},indent=4,ensure_ascii=True))
			
			print(f"{Colors['lgreen']}[✓] successfully added.\x1b[0m")
			open("logcat.txt","a+").write(f"\n{datetime.now().strftime('%m/%d')}:[+]:{link}")
		
		elif item == 2 :
			link = input(f"➜ link: {Colors['underline']}{Colors['dblue']}")
			print("\x1b[0m",end="")
			smallChannels, bigChannels, groups = loads(open(db).read()).get("smallChannels"), loads(open(db).read()).get("bigChannels"), loads(open(db).read()).get("groups")
			links = [i.get("link") for i in smallChannels+bigChannels+groups]
			
			if link in links :
				try: smallChannels.remove(smallChannels[links.index(link)])
				except:
					try: bigChannels.remove(bigChannels[links.index(link)])
					except: groups.remove(groups[links.index(link)])
				
				open(db,"w").write(dumps({
					"smallChannels": smallChannels,
					"bigChannels": bigChannels,
					"groups": groups
				},indent=4,ensure_ascii=True))
				print(f"{Colors['lgreen']}[✓] successfully deleted.\x1b[0m")
				open("logcat.txt","a+").write(f"\n{datetime.now().strftime('%m/%d')}:[-]:{link}")
			else :
				print(f"{Colors['dyellow']}[!] link is not exist.\x1b[0m")
	
		elif item == 3 :
			link = input(f"➜ link: {Colors['underline']}{Colors['dblue']}")
			print("\x1b[0m",end="")
			key,value = input("➜ what do you want to change?[title/count/link]: "), input("➜ new value: ")
			
			smallChannels, bigChannels, groups = loads(open(db).read()).get("smallChannels"), loads(open(db).read()).get("bigChannels"), loads(open(db).read()).get("groups")
			links = [i.get("link") for i in smallChannels+bigChannels+groups]
			
			if key.lower() == "count": value = int(value)
			ok = True
			try:
				smallChannels[links.index(link)][key],ok = value,True
			except:
				try:
					bigChannels[links.index(link)][key],ok = value,True
				except:
					try:
						groups[links.index(link)][key],ok = value,True
					except:
						print(f"{Colors['dyellow']}[!] link, key or value is not valid.\x1b[0m")
						ok = False
	
			if ok:
				open(db,"w").write(dumps({
					"smallChannels": smallChannels,
					"bigChannels": bigChannels,
					"groups": groups
				},indent=4,ensure_ascii=True))
				print(f"{Colors['lgreen']}[✓] successfully edited.\x1b[0m")
				open("logcat.txt","a+").write(f"\n{datetime.now().strftime('%m/%d')}:[*]:{link}")
	
		elif item == 4 :
			iChars = [input('➜ title’s character (empty for default): ') or  chars[0], input('➜ link’s character (empty for default): ') or chars[2]] #input characters
			chars = iChars
			if iChars[0] and iChars[1]:
				open("theme.json","w").write(dumps({
					'charForTitle': iChars[0],
					'charForID': iChars[1]
				},indent=4,ensure_ascii=False))
				print(f"{Colors['lgreen']}[+] successfully changed.\x1b[0m")
				open("logcat.txt","a+").write(f"\n{datetime.now().strftime('%m/%d')}:[*]:list style")

		elif item == 5 :
			smallChannels, bigChannels, groups = loads(open(db).read()).get("smallChannels"), loads(open(db).read()).get("bigChannels"), loads(open(db).read()).get("groups")

			smallChannels.reverse()
			bigChannels.reverse()
			groups.reverse()

			option = input("➜ which db do you want? [all/smallChannels/bigChannels/groups]: ").lower() or "all"
			method = input("➜ and do you want to copy?(write/copy/both): ").lower() or "both"

			sList, bList, gList = "", "", ""

			for s in smallChannels: sList += chars[0]+" "+s.get("title")+"\n"+chars[1]+" "+s.get("link")+"\n\n"
			for b in bigChannels: bList += chars[0]+" "+b.get("title")+"\n"+chars[1]+" "+b.get("link")+"\n\n"
			for g in groups: gList += chars[0]+" "+g.get("title")+"\n"+chars[1]+" "+g.get("link")+"\n\n"

			allList = sList+"\n\n"+bList+"\n\n"+gList

			if option == "smallchannels":
				if method == "write":
					print(sList)
				elif method == "copy":
					system(f"termux-clipboard-set '{sList}'")
				else:
					print(sList)
					system(f"termux-clipboard-set '{sList}'")
			elif option == "bigchannels":
				if method == "write":
					print(bList)
				elif method == "copy":
					system(f"termux-clipboard-set '{bList}'")
				else:
					print(bList)
					system(f"termux-clipboard-set '{bList}'")
			elif option == "groups":
				if method == "write":
					print(gList)
				elif method == "copy":
					system(f"termux-clipboard-set '{gList}'")
				else:
					print(gList)
					system(f"termux-clipboard-set '{gList}'")
			else:
				if method == "write":
					print(allList)
				elif method == "copy":
					system(f"termux-clipboard-set '{allList}'")
				else:
					print(allList)
					system(f"termux-clipboard-set '{allList}'")

		elif item == 6 :
			logcat = [i.split(":") for i in open("logcat.txt").read().splitlines()[4:]]
			for log in logcat: print(Colors['bold']+log[0],log[1],"\x1b[0m"+":".join(log[2:]))

		elif item == 7 :
			link = input(f"➜ link: {Colors['underline']}{Colors['dblue']}")
			print("\x1b[0m", end="")

			warns = loads(open("warns.json").read())
			
			try: warns[link] += 1
			except KeyError: warns[link] = 1
			open("warns.json","w").write(dumps(warns,indent=4,ensure_ascii=True))


		elif item == 8 :
			link = input(f"➜ link: {Colors['underline']}{Colors['dblue']}")
			print("\x1b[0m", end="")
			
			warns = loads(open("warns.json").read())
			
			try: print(warns[link])
			except KeyError: print(0)

		elif item == 9 :
			link = input(f"➜ link: {Colors['underline']}{Colors['dblue']}")
			print("\x1b[0m", end="")
			count = int(input(f"➜ new count: {Colors['lyellow']}"))
			print("\x1b[0m", end="")
			
			warns = loads(open("warns.json").read())

			warns[link] = count
			open("warns.json","w").write(dumps(warns,indent=4,ensure_ascii=True))

	except KeyboardInterrupt :
		exit()
		
		
		
# TODOs:
#1 : syncing logcat with 7,9