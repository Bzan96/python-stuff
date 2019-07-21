''' Visualisering för Gå-själv-program för åk 7-Gy i 100 Innovationer.
Programmet grundar sig i tankar om gamification och de teknologiträd som gärna återfinns i strategispel
som behandlar historia. Det här teknologiträdet går ut på att eleverna ska gå runt i utställningen och undersöka
olika innovationer. För att ge en liten morot ges spelaren (dvs. elevgrupperna) möjlighet att välja en av fyra
grundkulturer, som man skulle kunna hitta i verkligheten.
Därifrån utgår spelet från en akademisk idé om att innovationer uppstår på olika sätt, men exemplifierad på ett icke-
akademiskt sätt för att göra det lättare att förstå. Det kan finns ett starkt behov för en innovation som människan 
strävar efter att lösa, men en innovation kan också uppstå som en del i en större process, eller helt enkelt som en 
konsekvens av något annat. Poängen med det systemet är inte att vara full ut lärande, utan snarare för att få igång 
tankeverskamheten hos elever. Hur och varför kom den här innovationen till?
I samband med att de försöker välja en av tre innovationer i varje steg kan det vara en bra idé att röra sig runt i
utställningen och läsa på om innovationerna innan man gör sina val.

Teknologiträdet har 7 steg som alla går att återfinna i utställningen och som (2018-08-09) inbegriper 28 innovationer.
Det finns ingen helt genomtänkt idé om vilka innovationer som är utvalda, utan det är snarast en fråga om att få en 
spridning mellan behovs-, konsekvens- eller processinnovationer.
Det finns sedan ett poängsystem som följer valen, där de första valet automatiskt ger 10 poäng, men valen därefter 
ger 5 poäng för en behovsinnovation, 3 poäng för en innovation som kommer till som en del av en process, samt 1 poäng
för en innovation som mer eller mindre "råkar uppstå". Beroende på hur många poäng man sedan får delas man in en grupp
och man får en beskrivning av vilken tekniknördskategori man tillhör.'''

## Todo: Fysisk 'blankett' som eleverna kan använda för att skapa sitt träd. (substitut finns så länge)

import random

choices = []
points = 0
behov = "Det är en innovation som kommer till efter att man identifierat ett behov som man sedan lyckats fylla."
konsekvens = "Det är en innovation som kommer till som en konsekvens av att något hänt, t.ex. att en annan innovation misslyckats och en annan uppstått istället."
process = "Det är en innovation som kommer till som en del i en större process där man försökt utveckla tekniken i en riktning."


# Innovationer:
skor = "Skor är en fantastisk innovation, eller hur? Istället för att slita ut våra egna ömtåliga fötter kan vi konstruera en sorts ersättningsfötter som tål mycket mer och som inte gör ont om vi trampar på något vasst. Skor kan sägas vara en behovsinnovation. "
antibiotika = "Antibiotikan är en innovation som är lite lustig. Innan den kom till var det ingen som hade en tanke på att det skulle vara möjligt med något som stoppar så många sjukdomar. Efter uppfinnandet har vi använt det flitigt, men idag varnar forskare för att överanvändandet kan leda till att det inte längre fungerar. Antibiotika kan sägas vara en konsekvensinnovation. "
skriftspråket = "Skriftspråket är jämfört med människan inte alls gammalt, det har bara funnits i ca. 5000 år, men det är tack vare det som vi har möjlighet att ta del av och dela med oss av så stora mängder kunskap. Försök förställa dig en värld där ingen människa kan läsa. Hur skulle internet se ut utan text? Skriftspråket kan sägas vara en processinnovation. "
tändstickan = "Tändstickan löste ett mycket gammalt problem när den väl kom, dvs. hur man skulle göra upp eld. De första tändstickorna, som kom på 1600-talet, kunde självantända och det dröjde ända fram till mitten av 1800-talet innan säkerhetständstickan (som vi har idag) uppfanns. Tändstickan kan sägas vara en behovsinnovation. "
jordbruket = "För ca. 10000 år sedan skedde en stor förändring i människans livsstil, vi började bli bofasta. Fram tills dess hade vi jagat efter mat eller samlat bär, samtidigt som vi ständigt flyttat runt, men nu kunde vi bli bofasta och kunde därmed lägga tiden på att uppfinna nya saker. Jordbruket kan sägas vara en konsekvensinnovation. "
byggnadskonsten = "Att bygga saker har vi människor kunnat göra länge, redan för 500 000 år sedan byggde vi enkla saker som vindskydd. Det dröjde dock tills vi blev bofasta innan vi började bygga mer avancerade saker och grunden till de hus vi är så vana vid idag kom till. Idag kan vi ta hjälp av datorer för att kunna bygga högre och bättre. Byggnadskonsten kan sägas vara en processinnovation. "
propellern = "Tekniken bakom propellern (skruven) har funnits väldigt länge, så man skulle kunna tänka sig att också propellern funnits länge, men det dröjde faktiskt fram till 1800-talet innan den uppfanns. Den kom till när man letade efter något som kunde driva de stora nya ångdrivna fartygen. Propellern kan sägas vara en behovsinnovation. "
vattenkraft = "Vattenkraften har använts i ca. 2000 år och har fungerat som en avgörande innovation i människans historia eftersom det var första gången vi kunde ersätta muskelkraften hos människor eller djur. I slutet av 1800-talet gjordes en förbättring på hjulet så man kunde börja producera el. Vattenkraften kan sägas vara en konsekvensinnovation. "
cykeln = "Cykeln är idag en självklarhet för många, framförallt i i-länderna, men cykeln är inte alls så gammal som man kan tro. Cykeln blev dock en mycket viktig innovation när den väl kom på 1800-talet(!) eftersom den gjorde det möjligt för människor att arbeta långt ifrån där de bodde. Cykeln kan sägas vara en processinnovation. "
spikenochskruven = "Spiken & skruven har använts väldigt länge av människan, så länge faktiskt, att vi inte ens vet hur länge. I Sverige finns ordet 'spik' med i fornsvenskan, där det helt enkelt betyder 'spetsig'. Det dröjde fram till 1800-talet innan det kom en standardisering för spikar och skruvar. Spiken & skruven kan sägas vara en processinnovation. "
telegrafen = "Telegrafen kom in i samhället som en del i den industriella revolutionen och var en stark hjälp i att binda ihop de stora avstånden som fanns i den nya globala världen. Samuel Morse är den egentliga uppfinnaren av den, men i Sverige kopplar vi telegrafen mer till Lars Magnus Ericsson, som 1876 grundade företaget LM Ericsson - numera Ericsson, som finns över hela världen. Telegrafen kan sägas vara en konsekvensinnovation. "
ångmaskinen = "Ångmaskinen är en förutsättning för den industriella revolution och en av drivkrafterna bakom den. Tack vare den kunde vi ersätta den ineffektiva muskelkraften med maskiner, som kunde arbeta effektivare och utan pauser. Ångmaskinen kan sägas vara en behovsinnovation. "
förbränningsmotorn = "Förbränningsmotorn kom till som en förbättring på ångmaskinen eftersom man märkt att ångmaskinen, trots sin överlägsenhet mot muskelkraften, ändå var ganska ineffektiv. Den första riktiga förbränningsmotorn uppfanns av tysken Nikolaus Otto och den kallades därför för 'Ottomotorn', men idag pratar vi gärna om den som en 'bensinmotor', eller 'dieselmotor', som uppfanns av tysken Rudolf Diesel i slutet av 1800-talet. Förbränningsmotorn kan sägas vara en konsekvensinnovation. "
motorcykeln = "Motorcykeln är på sätt och vis en produkt av cykeln, förbränningsmotorn och bilen, då under samma tidsperiod tysken Gottleib Daimler arbetade med lite lättare förbränningsmotorer och fick för sig att testa att sätta en på en cykel, vilket gick ganska bra! Motorcykeln kan sägas vara en processinnovation. "
vapen = "Vapen är en mycket gammal innovation och har inte alltid använts till att döda andra människor. Det är under en mycket liten period som det använts till det, istället användes de av människor (och apor!) för att jaga och skaffa mat flera hundra tusen år tillbaka i tiden. Numera är dock vapen något vi ser negativt på, med all rätt, då framförallt atombomberna över Hiroshima och Nagasaki är exempel på hur destruktiva de kan vara, de dödade sammanlagt ca. 200 000 människor. Vapen kan sägas vara en processinnovation. "
dynamit = "Dynamiten är, till skillnad från vad man kan tro, inte en innovation som kom till för att döda människor. Svensken Alfred Nobel, som uppfann dynamiten, arbetade hela livet för att göra nitroglycerin mindre instabilt och kom till slut fram med dynamiten. Tragiskt nog dog hans bror i en olycka med nitroglycerin innan dynamiten uppfanns, men Alfred Nobel gav inte upp. Han drömde om att dynamiten skulle få slut på alla krig, men istället ersatte det krutet och gjorde krig ännu värre. Dynamiten kan sägas vara en behovsinnovation. "
sophantering = "Sophantering är en relativt ny innovation i människans historia, det är egentligen bara under lite drygt 100 år som vi verkligen försökt ta hand om våra sopor - innan dess har det inte behövts. Om man skulle ta hela Sveriges sopor under ett år skulle man kunna fylla Globen 48 gånger! Men vi är ändå inte värst, USA tidigare största soptipp tog som mest emot 500 ton skräp - varje timme! Sophanteringen kan sägas vara en behovsinnovation. "
avloppssystemet = "Avloppsystem har funnits väldigt länge i världen, där det förmodligen äldsta är 'cloaca maxima' under Rom, som byggdes på 200-talet före Kristus. I Sverige tog det dock väldigt lång tid innan vi kom på att vi kunde behöva ett sådant. Först på 1880-talet hade smuts och skräp som samlades när människor flyttat till städerna blivit ett så stort problem att man var tvungen att hitta en lösning. Avloppsystemet kan sägas vara en konsekvensinnovation. "
glödlampan = "De flesta idag kan nog koppla ihop glödlampan med Thomas Edison, men det är en smått orättvis koppling. Edison var nämligen långt ifrån den enda uppfinnaren som kom på glödlampan utan det var en hel drös med uppfinnare som kom fram med olika versioner av den. Edison var dock den första som fick patent på sin, som glödde i 40 timmar innan den slocknade. Glödlampan förändrade folks livsstil, människan var inte längre tvungen att rätta sig efter natt och dag, nu kunde man arbeta hela nätterna om man hade lust. Glödlampan kan sägas vara en behovsinnovation. "
robot = "Frågar man olika människor idag vad en robot är kommer man få väldigt olika svar, men i grund och botten är en robot en maskin som kan känna, tänka och göra på egen hand. Det finns idag många olika sorters robotar, de flesta snälla, men trots det tänker vi gärna på robotar som något elakt, mycket på grund av populärkulturen, där robotar gärna vill förgöra världen. Roboten kan sägas vara en konsekvensinnovation. "
flygplan = "Människan har under historiens lopp gjort många försök för att lära sig flyga, från misslyckade försök med att kopiera fåglars vingar till mer lyckade versioner som luftballongen. Men när flygplanet väl kom var det en blandning mellan kunskaperna från cykeltillverkning och starka förbränningsmotorer, det hjälpte till att binda ihop vår nya globala värld. Flygplanet kan sägas vara en konsekvensinnovation. "
vävstolen = "Tillsammans med t.ex. ångmaskinen är vävstolen än av de typiska drivande innovationerna i den industriella revolutionen. Det var inte att vävtekniken var ny - det äldsta tecknet på att någon vävt är ca. 9000 år gammalt (från Irak) - men vävstolen innebar att man kunde köra det snabbare och så småningom kunde man lägga in hålkort i maskinen för att massproducera saker! Vävstolen kan sägas vara en behovsinnovation. "
låset = "Låset är ca. 4000 år gammalt, bara hälften så gammalt som den tid vi varit bosatta. De första låsen var till och med gjorda av trä och det dröjde fram till romartiden innan man började tillverka lås i metall. Christopher Polhem i Sverige uppfann under 1700-talet ett finurligt lås som var väldigt svårt att bryta upp, det användes i flera hundra år! Låset kan sägas vara en behovsinnovation. "
vaccin = "Vaccin är ett sätt att bygga upp immunitet mot olika sjukdomar i kroppen genom att spruta in ofarliga versioner av sjukdomarna först. Det är en teknik som den engelske läkaren Edward Jenner kom på under 1700-talet när han sprutade in kokoppor i en 8-årig pojke (ofarligt för människor) och därefter smittkoppor (som dödade ca. 60 miljoner människor under 1700-talet!). Pojken överlevde! Vaccinet kan sägas vara en processinnovation. "


# Val #1

startUpChoice = input("Välj mellan att börja ditt teknologiträd i en havskultur: 'h', en krigskultur: 'k', en nomadkultur: 'n', eller en stadskultur: 's':\n")

if startUpChoice == "h":
	points += 10
	firstChoice = "båten"
	print("Båten är en av människans äldsta innovationer och en förutsättning för att havskulturer skulle kunna frodas. Visste du att forskare ha kommit fram till att befolkningen av Australien skedde med mycket enkla båtar för väldigt länge sedan? Du har valt att börja i en havskultur.")
elif startUpChoice == "k":
	points += 10
	firstChoice = "hjulet"
	print("Hjulet är en av människans äldsta innovationer och förmodligen också en av de viktigaste. Visste du att hjulet länge var en förutsättning för att kunna strida på häst? De antika egyptierna använde sig av vagnar fastspända bakom hästar för att kunna vara mer rörliga i strid. Du har valt att börja i en stridskultur.")
elif startUpChoice == "n":
	points += 10
	firstChoice = "eldstaden"
	print("Eldstaden är en innovation som vi idag gärna förknippar med ett landställe och mysiga sommarkvällar, men som historiskt sett fungerade som den centrala delen i ett hem. Eldstaden var länge den varmaste platsen i ett hushåll och därför var det en heder att få sitta eller sova så nära den som möjligt. Du har valt att börja i en nomadkultur.")
elif startUpChoice == "s":
	points += 10
	firstChoice = "smink"
	print("Smink är en mycket gammal företeelse i människans historia och med sin anknytning till den gamla egyptiska civilisationen är det något av en symbol för en civiliserad och urbaniserad kultur. Du har valt att börja i en stadskultur.")
else:
	randChoice = random.randrange(1,4)
	print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig kultur")
	if randChoice == 1:
		points += 10
		firstChoice = "båten"
		print("Du tilldelades: " + str(firstChoice) )
	elif randChoice == 2:
		points += 10
		firstChoice = "hjulet"
		print("Du tilldelades: " + str(firstChoice) )
	elif randChoice == 3:
		points += 10
		firstChoice = "eldstaden"
		print("Du tilldelades: " + str(firstChoice) )
	else:
		points += 10
		firstChoice = "smink"
		print("Du tilldelades: " + str(firstChoice) )

print("\n\n")		
		
# Val #2

# Smink
if firstChoice == "smink":
	sminkTier2 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är skor: 'sk', antibiotika: 'a', eller skriftspråket: 'ss':\n")

	if sminkTier2 == "sk":
		points += 5
		secondChoice = "skor"
		print(skor + behov)
	elif sminkTier2 == "a":
		points += 1
		secondChoice = "antibiotika"
		print(antibiotika + konsekvens)
	elif sminkTier2 == "ss":
		points += 3
		secondChoice = "skriftspråket"
		print(skriftspråket + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			secondChoice = "skor"
			print("Du tilldelades: " + str(secondChoice) )
		elif randChoice == 2:
			points += 1
			secondChoice = "antibiotika"
			print("Du tilldelades: " + str(secondChoice) )
		else:
			points += 3
			secondChoice = "skriftspråket"
			print("Du tilldelades: " + str(secondChoice) )

# Eldstaden			
elif firstChoice == "eldstaden":
	eldstadenTier2 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är tändstickan: 't', jordbruket: 'j', eller byggnadskonsten: 'b':\n")

	if eldstadenTier2 == "t":
		points += 5
		secondChoice = "tändstickan"
		print(tändstickan + behov)
	elif eldstadenTier2 == "j":
		points += 1
		secondChoice = "jordbruket"
		print(jordbruket + konsekvens)
	elif eldstadenTier2 == "b":
		points += 3
		secondChoice = "byggnadskonsten"
		print(byggnadskonsten + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			secondChoice = "tändstickan"
			print("Du tilldelades: " + str(secondChoice) )
		elif randChoice == 2:
			points += 1
			secondChoice = "jordbruket"
			print("Du tilldelades: " + str(secondChoice) )
		else:
			points += 3
			secondChoice = "byggnadskonsten"
			print("Du tilldelades: " + str(secondChoice) )

# Båten		
elif firstChoice == "båten":
	båtenTier2 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är propellern: 'p', vattenkraft: 'v', eller byggnadskonsten: 'b':\n")

	if båtenTier2 == "p":
		points += 5
		secondChoice = "propellern"
		print(propellern + behov)
	elif båtenTier2 == "v":
		points += 1
		secondChoice = "vattenkraft"
		print(vattenkraft + konsekvens)
	elif båtenTier2 == "b":
		points += 3
		secondChoice = "byggnadskonsten"
		print(byggnadskonsten + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			secondChoice = "propellern"
			print("Du tilldelades: " + str(secondChoice) )
		elif randChoice == 2:
			points += 1
			secondChoice = "vattenkraft"
			print("Du tilldelades: " + str(secondChoice) )
		else:
			points += 3
			secondChoice = "byggnadskonsten"
			print("Du tilldelades: " + str(secondChoice) )

# Hjulet
elif firstChoice == "hjulet":
	hjuletTier2 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är propellern: 'p', vattenkraft: 'v', eller cykeln: 'c':\n")
	
	if hjuletTier2 == "p":
		points += 5
		secondChoice = "propellern"
		print(propellern + behov)
	elif hjuletTier2 == "v":
		points += 1
		secondChoice = "vattenkraft"
		print(vattenkraft + konsekvens)
	elif hjuletTier2 == "c":
		points += 3
		secondChoice = "cykeln"
		print(cykeln + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			secondChoice = "propellern"
			print("Du tilldelades: " + str(secondChoice) )
		elif randChoice == 2:
			points += 1
			secondChoice = "vattenkraft"
			print("Du tilldelades: " + str(secondChoice) )
		else:
			points += 3
			secondChoice = "cykeln"
			print("Du tilldelades: " + str(secondChoice) )
		
print("\n\n")

# Val 3

# Skor
if secondChoice == "skor":
	skorTier3 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är vävstolen: 'v', roboten: 'r', eller spiken & skruven: 'ss':\n")
	
	if skorTier3 == "v":
		points += 5
		thirdChoice = "vävstolen"
		print(vävstolen + behov)
	elif skorTier3 == "r":
		points += 1
		thirdChoice = "robot"
		print(robot + konsekvens)
	elif skorTier3 == "ss":
		points += 3
		thirdChoice = "spiken & skruven"
		print(spikenochskruven + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			thirdChoice = "vävstolen"
			print("Du tilldelades: " + str(thirdChoice) )
		elif randChoice == 2:
			points += 1
			thirdChoice = "robot"
			print("Du tilldelades: " + str(thirdChoice) )
		else:
			points += 3
			thirdChoice = "spiken & skruven"
			print("Du tilldelades: " + str(thirdChoice) )

# Antibiotika
elif secondChoice == "antibiotika":
	antibiotikaTier3 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är sophantering: 's', avloppssystemet: 'a', eller vaccinet: 'v':\n")
	
	if antibiotikaTier3 == "s":
		points += 5
		thirdChoice = "sophantering"
		print(sophantering + behov)
	elif antibiotikaTier3 == "a":
		points += 1
		thirdChoice = "avloppssystemet"
		print(avloppssystemet + konsekvens)
	elif antibiotikaTier3 == "v":
		points += 3
		thirdChoice = "vaccin"
		print(vaccin + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			thirdChoice = "sophantering"
			print("Du tilldelades: " + str(thirdChoice) )
		elif randChoice == 2:
			points += 1
			thirdChoice = "avloppssystemet"
			print("Du tilldelades: " + str(thirdChoice) )
		else:
			points += 3
			thirdChoice = "vaccin"
			print("Du tilldelades: " + str(thirdChoice) )

# Tändstickan			
elif secondChoice == "tändstickan":
	tändstickanTier3 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är glödlampan: 'g', förbränningsmotorn: 'f', eller vapen: 'v':\n")
	
	if tändstickanTier3 == "g":
		points += 5
		thirdChoice = "glödlampan"
		print(glödlampan + behov)
	elif tändstickanTier3 == "f":
		points += 1
		thirdChoice = "förbränningsmotorn"
		print(vapen + konsekvens)
	elif tändstickanTier3 == "v":
		points += 3
		thirdChoice = "vapen"
		print(vapen + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			thirdChoice = "glödlampan"
			print("Du tilldelades: " + str(thirdChoice) )
		elif randChoice == 2:
			points += 1
			thirdChoice = "förbränningsmotorn"
			print("Du tilldelades: " + str(thirdChoice) )
		else:
			points += 3
			thirdChoice = "vapen"
			print("Du tilldelades: " + str(thirdChoice) )

# Jordbruket			
elif secondChoice == "jordbruket":
	jordbruketTier3 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är sophantering: 'sp', avloppssystemet: 'a', eller skriftspråket: 'ss':\n")
	
	if jordbruketTier3 == "sp":
		points += 5
		thirdChoice = "sophantering"
		print(sophantering + behov)
	elif jordbruketTier3 == "a":
		points += 1
		thirdChoice = "avloppssystemet"
		print(avloppssystemet + konsekvens)
	elif jordbruketTier3 == "ss":
		points += 3
		thirdChoice = "skriftspråket"
		print(skriftspråket + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			thirdChoice = "sophantering"
			print("Du tilldelades: " + str(thirdChoice) )
		elif randChoice == 2:
			points += 1
			thirdChoice = "avloppssystemet"
			print("Du tilldelades: " + str(thirdChoice) )
		else:
			points += 3
			thirdChoice = "skriftspråket"
			print("Du tilldelades: " + str(thirdChoice) )

# Propellern			
elif secondChoice == "propellern":
	propellernTier3 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är ångmaskinen: 'å', flygplan: 'f', eller vapen: 'v':\n")
	
	if propellernTier3 == "å":
		points += 5
		thirdChoice = "ångmaskinen"
		print(ångmaskinen + behov)
	elif propellernTier3 == "f":
		points += 1
		thirdChoice = "flygplan"
		print(flygplan + konsekvens)
	elif propellernTier3 == "v":
		points += 3
		thirdChoice = "vapen"
		print(vapen + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			thirdChoice = "ångmaskinen"
			print("Du tilldelades: " + str(thirdChoice) )
		elif randChoice == 2:
			points += 1
			thirdChoice = "flygplan"
			print("Du tilldelades: " + str(thirdChoice) )
		else:
			points += 3
			thirdChoice = "vapen"
			print("Du tilldelades: " + str(thirdChoice) )			
			
# Byggnadskonsten
elif secondChoice == "byggnadskonsten":
	byggkonstenTier3 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är dynamit: 'd', jordbruket: 'j', eller spiken & skruven: 'ss':\n")
	
	if byggkonstenTier3 == "d":
		points += 5
		thirdChoice = "dynamit"
		print(dynamit + behov)
	elif byggkonstenTier3 == "j":
		points += 1
		thirdChoice = "jordbruket"
		print(jordbruket + konsekvens)
	elif byggkonstenTier3 == "ss":
		points += 3
		thirdChoice = "spiken & skruven"
		print(spikenochskruven + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			thirdChoice = "dynamit"
			print("Du tilldelades: " + str(thirdChoice) )
		elif randChoice == 2:
			points += 1
			thirdChoice = "jordbruket"
			print("Du tilldelades: " + str(thirdChoice) )
		else:
			points += 3
			thirdChoice = "spiken & skruven"
			print("Du tilldelades: " + str(thirdChoice) )
			
# Skriftspråket
elif secondChoice == "skriftspråket":
	skriftspråketTier3 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är vävstolen: 'v', telegrafen: 't', eller byggnadskonsten: 'b':\n")
	
	if skriftspråketTier3 == "v":
		points += 5
		thirdChoice = "vävstolen"
		print(vävstolen + behov)
	elif skriftspråketTier3 == "t":
		points += 1
		thirdChoice = "telegrafen"
		print(telegrafen + konsekvens)
	elif skriftspråketTier3 == "b":
		points += 3
		thirdChoice = "byggnadskonsten"
		print(byggnadskonsten + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			thirdChoice = "vävstolen"
			print("Du tilldelades: " + str(thirdChoice) )
		elif randChoice == 2:
			points += 1
			thirdChoice = "telegrafen"
			print("Du tilldelades: " + str(thirdChoice) )
		else:
			points += 3
			thirdChoice = "byggnadskonsten"
			print("Du tilldelades: " + str(thirdChoice) )
			
# Vattenkraft
elif secondChoice == "vattenkraft":
	vattenkraftTier3 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är ångmaskinen: 'å', jordbruket: 'j', eller byggnadskonsten: 'b':\n")
	
	if vattenkraftTier3 == "å":
		points += 5
		thirdChoice = "ångmaskinen"
		print(ångmaskinen + behov)
	elif vattenkraftTier3 == "j":
		points += 1
		thirdChoice = "jordbruket"
		print(jordbruket + konsekvens)
	elif vattenkraftTier3 == "b":
		points += 3
		thirdChoice = "byggnadskonsten"
		print(byggnadskonsten + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			thirdChoice = "ångmaskinen"
			print("Du tilldelades: " + str(thirdChoice) )
		elif randChoice == 2:
			points += 1
			thirdChoice = "jordbruket"
			print("Du tilldelades: " + str(thirdChoice) )
		else:
			points += 3
			thirdChoice = "byggnadskonsten"
			print("Du tilldelades: " + str(thirdChoice) )
			
# Cykeln
elif secondChoice == "cykeln":
	cykelnTier3 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är låset: 'l', motorcykeln: 'm', eller förbränningsmotorn: 'f':\n")
	
	if cykelnTier3 == "l":
		points += 5
		thirdChoice = "låset"
		print(låset + behov)
	elif cykelnTier3 == "f":
		points += 1
		thirdChoice = "förbränningsmotorn"
		print(förbränningsmotorn + konsekvens)
	elif cykelnTier3 == "m":
		points += 3
		thirdChoice = "motorcykeln"
		print(motorcykeln + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			thirdChoice = "låset"
			print("Du tilldelades: " + str(thirdChoice) )
		elif randChoice == 2:
			points += 1
			thirdChoice = "förbränningsmotorn"
			print("Du tilldelades: " + str(thirdChoice) )
		else:
			points += 3
			thirdChoice = "motorcykeln"
			print("Du tilldelades: " + str(thirdChoice) )

print("\n\n")
			
#Val 4

# Vävstolen
if thirdChoice == "vävstolen":
	vävstolenTier4 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är ångmaskinen: 'å', roboten: 'r', eller spiken & skruven: 'ss':\n")
	
	if vävstolenTier4 == "å":
		points += 5
		fourthChoice = "ångmaskinen"
		print(ångmaskinen + behov)
	elif vävstolenTier4 == "r":
		points += 1
		fourthChoice = "robot"
		print(robot + konsekvens)
	elif vävstolenTier4 == "ss":
		points += 3
		fourthChoice = "spiken & skruven"
		print(spikenochskruven + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			fourthChoice = "ångmaskinen"
			print("Du tilldelades: " + str(fourthChoice) )
		elif randChoice == 2:
			points += 1
			fourthChoice = "robot"
			print("Du tilldelades: " + str(fourthChoice) )
		else:
			points += 3
			fourthChoice = "spiken & skruven"
			print("Du tilldelades: " + str(fourthChoice) )

# Sophanteringen
elif thirdChoice == "sophantering":
	sophanteringTier4 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är skor: 's', avloppssystemet: 'a', eller vaccin: 'v':\n")
	
	if sophanteringTier4 == "å":
		points += 5
		fourthChoice = "ångmaskinen"
		print(ångmaskinen + behov)
	elif sophanteringTier4 == "a":
		points += 1
		fourthChoice = "avloppssystemet"
		print(avloppssystemet + konsekvens)
	elif sophanteringTier4 == "v":
		points += 3
		fourthChoice = "vaccin"
		print(vaccin + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			fourthChoice = "ångmaskinen"
			print("Du tilldelades: " + str(fourthChoice) )
		elif randChoice == 2:
			points += 1
			fourthChoice = "avloppssystemet"
			print("Du tilldelades: " + str(fourthChoice) )
		else:
			points += 3
			fourthChoice = "vaccin"
			print("Du tilldelades: " + str(fourthChoice) )

# Glödlampan
elif thirdChoice == "glödlampan":
	glödlampanTier4 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är sophantering: 'sp', telegrafen: 't', eller skriftspråket: 'ss':\n")
	
	if glödlampanTier4 == "sp":
		points += 5
		fourthChoice = "sophantering"
		print(sophantering + behov)
	elif glödlampanTier4 == "t":
		points += 1
		fourthChoice = "telegrafen"
		print(telegrafen + konsekvens)
	elif glödlampanTier4 == "ss":
		points += 3
		fourthChoice = "skriftspråket"
		print(skriftspråket + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			fourthChoice = "sophantering"
			print("Du tilldelades: " + str(fourthChoice) )
		elif randChoice == 2:
			points += 1
			fourthChoice = "telegrafen"
			print("Du tilldelades: " + str(fourthChoice) )
		else:
			points += 3
			fourthChoice = "skriftspråket"
			print("Du tilldelades: " + str(fourthChoice) )

# Ångmaskinen
elif thirdChoice == "ångmaskinen":
	ångmaskinenTier4 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är dynamit: 'd', förbränningsmotorn: 'f', eller byggnadskonsten: 'b':\n")
	
	if ångmaskinenTier4 == "d":
		points += 5
		fourthChoice = "dynamit"
		print(dynamit + behov)
	elif ångmaskinenTier4 == "f":
		points += 1
		fourthChoice = "förbränningsmotorn"
		print(förbränningsmotorn + konsekvens)
	elif ångmaskinenTier4 == "b":
		points += 3
		fourthChoice = "byggnadskonsten"
		print(byggnadskonsten + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			fourthChoice = "dynamit"
			print("Du tilldelades: " + str(fourthChoice) )
		elif randChoice == 2:
			points += 1
			fourthChoice = "förbränningsmotorn"
			print("Du tilldelades: " + str(fourthChoice) )
		else:
			points += 3
			fourthChoice = "byggnadskonsten"
			print("Du tilldelades: " + str(fourthChoice) )			

# Dynamiten
elif thirdChoice == "dynamit":
	dynamitTier4 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är sophantering: 'sp', roboten: 'r', eller vapen: 'v':\n")
	
	if dynamitTier4 == "sp":
		points += 5
		fourthChoice = "sophantering"
		print(sophantering + behov)
	elif dynamitTier4 == "r":
		points += 1
		fourthChoice = "robot"
		print(robot + konsekvens)
	elif dynamitTier4 == "v":
		points += 3
		fourthChoice = "vapen"
		print(vapen + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			fourthChoice = "sophantering"
			print("Du tilldelades: " + str(fourthChoice) )
		elif randChoice == 2:
			points += 1
			fourthChoice = "robot"
			print("Du tilldelades: " + str(fourthChoice) )
		else:
			points += 3
			fourthChoice = "vapen"
			print("Du tilldelades: " + str(fourthChoice) )

# Låset
elif thirdChoice == "låset":
	låsetTier4 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är dynamit: 'd', jordbruket: 'j', eller spiken & skruven: 'ss':\n")
	
	if låsetTier4 == "d":
		points += 5
		fourthChoice = "dynamit"
		print(dynamit + behov)
	elif låsetTier4 == "j":
		points += 1
		fourthChoice = "jordbruket"
		print(jordbruket + konsekvens)
	elif låsetTier4 == "ss":
		points += 3
		fourthChoice = "spiken & skruven"
		print(spikenochskruven + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			fourthChoice = "dynamit"
			print("Du tilldelades: " + str(fourthChoice) )
		elif randChoice == 2:
			points += 1
			fourthChoice = "jordbruket"
			print("Du tilldelades: " + str(fourthChoice) )
		else:
			points += 3
			fourthChoice = "spiken & skruven"
			print("Du tilldelades: " + str(fourthChoice) )

# Telegrafen
elif thirdChoice == "telegraf":
	telegrafTier4 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är glödlampan: 'g', robot: 'r', eller vapen: 'v':\n")
	
	if telegrafTier4 == "g":
		points += 5
		fourthChoice = "glödlampan"
		print(glödlampan + behov)
	elif telegrafTier4 == "r":
		points += 1
		fourthChoice = "robot"
		print(robot + konsekvens)
	elif telegrafTier4 == "v":
		points += 3
		fourthChoice = "vapen"
		print(vapen + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			fourthChoice = "glödlampan"
			print("Du tilldelades: " + str(fourthChoice) )
		elif randChoice == 2:
			points += 1
			fourthChoice = "robot"
			print("Du tilldelades: " + str(fourthChoice) )
		else:
			points += 3
			fourthChoice = "vapen"
			print("Du tilldelades: " + str(fourthChoice) )

# Flygplanet
elif thirdChoice == "flygplan":
	flygplanTier4 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är låset: 'l', robot: 'r', eller byggnadskonsten: 'b':\n")
	
	if flygplanTier4 == "l":
		points += 5
		fourthChoice = "låset"
		print(låset + behov)
	elif flygplanTier4 == "r":
		points += 1
		fourthChoice = "robot"
		print(robot + konsekvens)
	elif flygplanTier4 == "b":
		points += 3
		fourthChoice = "byggnadskonsten"
		print(byggnadskonsten + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			fourthChoice = "låset"
			print("Du tilldelades: " + str(fourthChoice) )
		elif randChoice == 2:
			points += 1
			fourthChoice = "robot"
			print("Du tilldelades: " + str(fourthChoice) )
		else:
			points += 3
			fourthChoice = "byggnadskonsten"
			print("Du tilldelades: " + str(fourthChoice) )
			
# Förbränningsmotorn
elif thirdChoice == "förbränningsmotorn":
	förbränningsmotornTier4 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är ångmaskinen: 'å', flygplan: 'f', eller motorcykeln: 'm':\n")
	
	if förbränningsmotornTier4 == "å":
		points += 5
		fourthChoice = "ångmaskinen"
		print(ångmaskinen + behov)
	elif förbränningsmotornTier4 == "f":
		points += 1
		fourthChoice = "flygplan"
		print(flygplan + konsekvens)
	elif förbränningsmotornTier4 == "m":
		points += 3
		fourthChoice = "motorcykeln"
		print(motorcykeln + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			fourthChoice = "ångmaskinen"
			print("Du tilldelades: " + str(fourthChoice) )
		elif randChoice == 2:
			points += 1
			fourthChoice = "flygplan"
			print("Du tilldelades: " + str(fourthChoice) )
		else:
			points += 3
			fourthChoice = "motorcykeln"
			print("Du tilldelades: " + str(fourthChoice) )
			
# Avloppsystemet
elif thirdChoice == "avloppssystemet":
	avloppssystemetTier4 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är skor: 's', vattenkraft: 'v', eller byggnadskonsten: 'b':\n")
	
	if avloppssystemetTier4 == "s":
		points += 5
		fourthChoice = "skor"
		print(skor + behov)
	elif avloppssystemetTier4 == "v":
		points += 1
		fourthChoice = "vattenkraft"
		print(vattenkraft + konsekvens)
	elif avloppssystemetTier4 == "b":
		points += 3
		fourthChoice = "byggnadskonsten"
		print(byggnadskonsten + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			fourthChoice = "skor"
			print("Du tilldelades: " + str(fourthChoice) )
		elif randChoice == 2:
			points += 1
			fourthChoice = "vattenkraft"
			print("Du tilldelades: " + str(fourthChoice) )
		else:
			points += 3
			fourthChoice = "byggnadskonsten"
			print("Du tilldelades: " + str(fourthChoice) )
			
# Roboten
elif thirdChoice == "robot":
	robotTier4 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är sophantering: 'sp', förbränningsmotorn: 'f', eller vapen: 'v':\n")
	
	if robotTier4 == "sp":
		points += 5
		fourthChoice = "sophantering"
		print(sophantering + behov)
	elif robotTier4 == "f":
		points += 1
		fourthChoice = "förbränningsmotorn"
		print(förbränningsmotorn + konsekvens)
	elif robotTier4 == "v":
		points += 3
		fourthChoice = "vapen"
		print(vapen + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			fourthChoice = "sophantering"
			print("Du tilldelades: " + str(fourthChoice) )
		elif randChoice == 2:
			points += 1
			fourthChoice = "förbränningsmotorn"
			print("Du tilldelades: " + str(fourthChoice) )
		else:
			points += 3
			fourthChoice = "vapen"
			print("Du tilldelades: " + str(fourthChoice) )
			
# Spiken & skruven
elif thirdChoice == "spiken & skruven":
	spikenochskruvenTier4 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är propellern: 'p', vattenkraft: 'v', eller cykeln: 'v':\n")
	
	if spikenochskruvenTier4 == "p":
		points += 5
		fourthChoice = "propellern"
		print(propellern + behov)
	elif spikenochskruvenTier4 == "v":
		points += 1
		fourthChoice = "vapen"
		print(vapen + konsekvens)
	elif spikenochskruvenTier4 == "c":
		points += 3
		fourthChoice = "cykeln"
		print(cykeln + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			fourthChoice = "propellern"
			print("Du tilldelades: " + str(fourthChoice) )
		elif randChoice == 2:
			points += 1
			fourthChoice = "vapen"
			print("Du tilldelades: " + str(fourthChoice) )
		else:
			points += 3
			fourthChoice = "cykeln"
			print("Du tilldelades: " + str(fourthChoice) )
			
# Vaccinet
elif thirdChoice == "vaccin":
	vaccinTier4 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är sophantering: 'sp', jordbruket: 'j', eller vapen: 'v':\n")
	
	if vaccinTier4 == "sp":
		points += 5
		fourthChoice = "sophantering"
		print(sophantering + behov)
	elif vaccinTier4 == "j":
		points += 1
		fourthChoice = "jordbruket"
		print(jordbruket + konsekvens)
	elif vaccinTier4 == "v":
		points += 3
		fourthChoice = "vapen"
		print(vapen + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			fourthChoice = "sophantering"
			print("Du tilldelades: " + str(fourthChoice) )
		elif randChoice == 2:
			points += 1
			fourthChoice = "jordbruket"
			print("Du tilldelades: " + str(fourthChoice) )
		else:
			points += 3
			fourthChoice = "vapen"
			print("Du tilldelades: " + str(fourthChoice) )
			
# Vapen
elif thirdChoice == "vapen":
	vapenTier4 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är dynamit: 'd', robot: r', eller motorcykeln: 'm':\n")
	
	if vapenTier4 == "d":
		points += 5
		fourthChoice = "dynamit"
		print(dynamit + behov)
	elif vapenTier4 == "r":
		points += 1
		fourthChoice = "robot"
		print(robot + konsekvens)
	elif vapenTier4 == "m":
		points += 3
		fourthChoice = "motorcykeln"
		print(motorcykeln + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			fourthChoice = "dynamit"
			print("Du tilldelades: " + str(fourthChoice) )
		elif randChoice == 2:
			points += 1
			fourthChoice = "robot"
			print("Du tilldelades: " + str(fourthChoice) )
		else:
			points += 3
			fourthChoice = "motorcykeln"
			print("Du tilldelades: " + str(fourthChoice) )
			
# Motorcykeln
elif thirdChoice == "motorcykeln":
	motorcykelnTier4 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är låset: 'l', förbränningsmotorn: 'f', eller spiken & skruven: 'ss':\n")
	
	if motorcykelnTier4 == "l":
		points += 5
		fourthChoice = "låset"
		print(låset + behov)
	elif motorcykelnTier4 == "f":
		points += 1
		fourthChoice = "förbränningsmotorn"
		print(förbränningsmotorn + konsekvens)
	elif motorcykelnTier4 == "ss":
		points += 3
		fourthChoice = "spiken & skruven"
		print(spikenochskruven + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			fourthChoice = "låset"
			print("Du tilldelades: " + str(fourthChoice) )
		elif randChoice == 2:
			points += 1
			fourthChoice = "förbränningsmotorn"
			print("Du tilldelades: " + str(fourthChoice) )
		else:
			points += 3
			fourthChoice = "spiken & skruven"
			print("Du tilldelades: " + str(fourthChoice) )
			
# Byggnadskonsten
elif thirdChoice == "byggnadskonsten":
	byggkonstenTier4 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är dynamit: 'd', jordbruket: 'j', eller spiken & skruven: 'ss':\n")
	
	if byggkonstenTier4 == "d":
		points += 5
		fourthChoice = "dynamit"
		print(dynamit + behov)
	elif byggkonstenTier4 == "j":
		points += 1
		fourthChoice = "jordbruket"
		print(jordbruket + konsekvens)
	elif byggkonstenTier4 == "ss":
		points += 3
		fourthChoice = "spiken & skruven"
		print(spikenochskruven + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			fourthChoice = "dynamit"
			print("Du tilldelades: " + str(fourthChoice) )
		elif randChoice == 2:
			points += 1
			fourthChoice = "jordbruket"
			print("Du tilldelades: " + str(fourthChoice) )
		else:
			points += 3
			fourthChoice = "spiken & skruven"
			print("Du tilldelades: " + str(fourthChoice) )
			
# Skriftspråket
elif thirdChoice == "skriftspråket":
	skriftspråketTier4 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är vävstolen: 'v', telegrafen: 't', eller byggnadskonsten: 'b':\n")
	
	if skriftspråketTier4 == "v":
		points += 5
		fourthChoice = "vävstolen"
		print(vävstolen + behov)
	elif skriftspråketTier4 == "t":
		points += 1
		fourthChoice = "telegrafen"
		print(telegrafen + konsekvens)
	elif skriftspråketTier4 == "b":
		points += 3
		fourthChoice = "byggnadskonsten"
		print(byggnadskonsten + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			fourthChoice = "vävstolen"
			print("Du tilldelades: " + str(fourthChoice) )
		elif randChoice == 2:
			points += 1
			fourthChoice = "telegrafen"
			print("Du tilldelades: " + str(fourthChoice) )
		else:
			points += 3
			fourthChoice = "byggnadskonsten"
			print("Du tilldelades: " + str(fourthChoice) )
			
# Jordbruket			
elif thirdChoice == "jordbruket":
	jordbruketTier4 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är sophantering: 'sp', avloppssystemet: 'a', eller skriftspråket: 'ss':\n")
	
	if jordbruketTier4 == "sp":
		points += 5
		fourthChoice = "sophantering"
		print(sophantering + behov)
	elif jordbruketTier4 == "a":
		points += 1
		fourthChoice = "avloppssystemet"
		print(avloppssystemet + konsekvens)
	elif jordbruketTier4 == "ss":
		points += 3
		fourthChoice = "skriftspråket"
		print(skriftspråket + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			fourthChoice = "sophantering"
			print("Du tilldelades: " + str(fourthChoice) )
		elif randChoice == 2:
			points += 1
			fourthChoice = "avloppssystemet"
			print("Du tilldelades: " + str(fourthChoice) )
		else:
			points += 3
			fourthChoice = "skriftspråket"
			print("Du tilldelades: " + str(fourthChoice) )
			
print("\n\n")
			
# Val 5

# Sophanteringen
if fourthChoice == "sophantering":
	sophanteringTier5 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är skor: 's', avloppssystemet: 'a', eller vaccin: 'v':\n")
	
	if sophanteringTier5 == "å":
		points += 5
		fifthChoice = "ångmaskinen"
		print(ångmaskinen + behov)
	elif sophanteringTier5 == "a":
		points += 1
		fifthChoice = "avloppssystemet"
		print(avloppssystemet + konsekvens)
	elif sophanteringTier5 == "v":
		points += 3
		fifthChoice = "vaccin"
		print(vaccin + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			fifthChoice = "ångmaskinen"
			print("Du tilldelades: " + str(fifthChoice) )
		elif randChoice == 2:
			points += 1
			fifthChoice = "avloppssystemet"
			print("Du tilldelades: " + str(fifthChoice) )
		else:
			points += 3
			fifthChoice = "vaccin"
			print("Du tilldelades: " + str(fifthChoice) )

# Glödlampan
elif fourthChoice == "glödlampan":
	glödlampanTier5 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är sophantering: 'sp', telegrafen: 't', eller skriftspråket: 'ss':\n")
	
	if glödlampanTier5 == "sp":
		points += 5
		fifthChoice = "sophantering"
		print(sophantering + behov)
	elif glödlampanTier5 == "t":
		points += 1
		fifthChoice = "telegrafen"
		print(telegrafen + konsekvens)
	elif glödlampanTier5 == "ss":
		points += 3
		fifthChoice = "skriftspråket"
		print(skriftspråket + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			fifthChoice = "sophantering"
			print("Du tilldelades: " + str(fifthChoice) )
		elif randChoice == 2:
			points += 1
			fifthChoice = "telegrafen"
			print("Du tilldelades: " + str(fifthChoice) )
		else:
			points += 3
			fifthChoice = "skriftspråket"
			print("Du tilldelades: " + str(fifthChoice) )

# Ångmaskinen
elif fourthChoice == "ångmaskinen":
	ångmaskinenTier5 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är dynamit: 'd', förbränningsmotorn: 'f', eller byggnadskonsten: 'b':\n")
	
	if ångmaskinenTier5 == "d":
		points += 5
		fifthChoice = "dynamit"
		print(dynamit + behov)
	elif ångmaskinenTier5 == "f":
		points += 1
		fifthChoice = "förbränningsmotorn"
		print(förbränningsmotorn + konsekvens)
	elif ångmaskinenTier5 == "b":
		points += 3
		fifthChoice = "byggnadskonsten"
		print(byggnadskonsten + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			fifthChoice = "dynamit"
			print("Du tilldelades: " + str(fifthChoice) )
		elif randChoice == 2:
			points += 1
			fifthChoice = "förbränningsmotorn"
			print("Du tilldelades: " + str(fifthChoice) )
		else:
			points += 3
			fifthChoice = "byggnadskonsten"
			print("Du tilldelades: " + str(fifthChoice) )			

# Dynamiten
elif fourthChoice == "dynamit":
	dynamitTier5 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är sophantering: 'sp', roboten: 'r', eller vapen: 'v':\n")
	
	if dynamitTier5 == "sp":
		points += 5
		fifthChoice = "sophantering"
		print(sophantering + behov)
	elif dynamitTier5 == "r":
		points += 1
		fifthChoice = "robot"
		print(robot + konsekvens)
	elif dynamitTier5 == "v":
		points += 3
		fifthChoice = "vapen"
		print(vapen + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			fifthChoice = "sophantering"
			print("Du tilldelades: " + str(fifthChoice) )
		elif randChoice == 2:
			points += 1
			fifthChoice = "robot"
			print("Du tilldelades: " + str(fifthChoice) )
		else:
			points += 3
			fifthChoice = "vapen"
			print("Du tilldelades: " + str(fifthChoice) )

# Låset
elif fourthChoice == "låset":
	låsetTier5 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är dynamit: 'd', jordbruket: 'j', eller spiken & skruven: 'ss':\n")
	
	if låsetTier5 == "d":
		points += 5
		fifthChoice = "dynamit"
		print(dynamit + behov)
	elif låsetTier5 == "j":
		points += 1
		fifthChoice = "jordbruket"
		print(jordbruket + konsekvens)
	elif låsetTier5 == "ss":
		points += 3
		fifthChoice = "spiken & skruven"
		print(spikenochskruven + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			fifthChoice = "dynamit"
			print("Du tilldelades: " + str(fifthChoice) )
		elif randChoice == 2:
			points += 1
			fifthChoice = "jordbruket"
			print("Du tilldelades: " + str(fifthChoice) )
		else:
			points += 3
			fifthChoice = "spiken & skruven"
			print("Du tilldelades: " + str(fifthChoice) )

# Telegrafen
elif fourthChoice == "telegrafen":
	telegrafTier5 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är glödlampan: 'g', robot: 'r', eller vapen: 'v':\n")
	
	if telegrafTier5 == "g":
		points += 5
		fifthChoice = "glödlampan"
		print(glödlampan + behov)
	elif telegrafTier5 == "r":
		points += 1
		fifthChoice = "robot"
		print(robot + konsekvens)
	elif telegrafTier5 == "v":
		points += 3
		fifthChoice = "vapen"
		print(vapen + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			fifthChoice = "glödlampan"
			print("Du tilldelades: " + str(fifthChoice) )
		elif randChoice == 2:
			points += 1
			fifthChoice = "robot"
			print("Du tilldelades: " + str(fifthChoice) )
		else:
			points += 3
			fifthChoice = "vapen"
			print("Du tilldelades: " + str(fifthChoice) )

# Flygplanet
elif fourthChoice == "flygplan":
	flygplanTier5 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är låset: 'l', robot: 'r', eller byggnadskonsten: 'b':\n")
	
	if flygplanTier5 == "l":
		points += 5
		fifthChoice = "låset"
		print(låset + behov)
	elif flygplanTier5 == "r":
		points += 1
		fifthChoice = "robot"
		print(robot + konsekvens)
	elif flygplanTier5 == "b":
		points += 3
		fifthChoice = "byggnadskonsten"
		print(byggnadskonsten + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			fifthChoice = "låset"
			print("Du tilldelades: " + str(fifthChoice) )
		elif randChoice == 2:
			points += 1
			fifthChoice = "robot"
			print("Du tilldelades: " + str(fifthChoice) )
		else:
			points += 3
			fifthChoice = "byggnadskonsten"
			print("Du tilldelades: " + str(fifthChoice) )
			
# Förbränningsmotorn
elif fourthChoice == "förbränningsmotorn":
	förbränningsmotornTier5 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är ångmaskinen: 'å', flygplan: 'f', eller motorcykeln: 'm':\n")
	
	if förbränningsmotornTier5 == "å":
		points += 5
		fifthChoice = "ångmaskinen"
		print(ångmaskinen + behov)
	elif förbränningsmotornTier5 == "f":
		points += 1
		fifthChoice = "flygplan"
		print(flygplan + konsekvens)
	elif förbränningsmotornTier5 == "m":
		points += 3
		fifthChoice = "motorcykeln"
		print(motorcykeln + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			fifthChoice = "ångmaskinen"
			print("Du tilldelades: " + str(fifthChoice) )
		elif randChoice == 2:
			points += 1
			fifthChoice = "flygplan"
			print("Du tilldelades: " + str(fifthChoice) )
		else:
			points += 3
			fifthChoice = "motorcykeln"
			print("Du tilldelades: " + str(fifthChoice) )
			
# Avloppsystemet
elif fourthChoice == "avloppssystemet":
	avloppssystemetTier5 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är skor: 's', vattenkraft: 'v', eller byggnadskonsten: 'b':\n")
	
	if avloppssystemetTier5 == "s":
		points += 5
		fifthChoice = "skor"
		print(skor + behov)
	elif avloppssystemetTier5 == "v":
		points += 1
		fifthChoice = "vattenkraft"
		print(vattenkraft + konsekvens)
	elif avloppssystemetTier5 == "b":
		points += 3
		fifthChoice = "byggnadskonsten"
		print(byggnadskonsten + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			fifthChoice = "skor"
			print("Du tilldelades: " + str(fifthChoice) )
		elif randChoice == 2:
			points += 1
			fifthChoice = "vattenkraft"
			print("Du tilldelades: " + str(fifthChoice) )
		else:
			points += 3
			fifthChoice = "byggnadskonsten"
			print("Du tilldelades: " + str(fifthChoice) )
			
# Roboten
elif fourthChoice == "robot":
	robotTier5 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är sophantering: 'sp', förbränningsmotorn: 'f', eller vapen: 'v':\n")
	
	if robotTier5 == "sp":
		points += 5
		fifthChoice = "sophantering"
		print(sophantering + behov)
	elif robotTier5 == "f":
		points += 1
		fifthChoice = "förbränningsmotorn"
		print(förbränningsmotorn + konsekvens)
	elif robotTier5 == "v":
		points += 3
		fifthChoice = "vapen"
		print(vapen + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			fifthChoice = "sophantering"
			print("Du tilldelades: " + str(fifthChoice) )
		elif randChoice == 2:
			points += 1
			fifthChoice = "förbränningsmotorn"
			print("Du tilldelades: " + str(fifthChoice) )
		else:
			points += 3
			fifthChoice = "vapen"
			print("Du tilldelades: " + str(fifthChoice) )
			
# Spiken & skruven
elif fourthChoice == "spiken & skruven":
	spikenochskruvenTier5 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är propellern: 'p', vattenkraft: 'v', eller cykeln: 'v':\n")
	
	if spikenochskruvenTier5 == "p":
		points += 5
		fifthChoice = "propellern"
		print(propellern + behov)
	elif spikenochskruvenTier5 == "v":
		points += 1
		fifthChoice = "vapen"
		print(vapen + konsekvens)
	elif spikenochskruvenTier5 == "c":
		points += 3
		fifthChoice = "cykeln"
		print(cykeln + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			fifthChoice = "propellern"
			print("Du tilldelades: " + str(fifthChoice) )
		elif randChoice == 2:
			points += 1
			fifthChoice = "vapen"
			print("Du tilldelades: " + str(fifthChoice) )
		else:
			points += 3
			fifthChoice = "cykeln"
			print("Du tilldelades: " + str(fifthChoice) )
			
# Vaccinet
elif fourthChoice == "vaccin":
	vaccinTier5 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är sophantering: 'sp', jordbruket: 'j', eller vapen: 'v':\n")
	
	if vaccinTier5 == "sp":
		points += 5
		fifthChoice = "sophantering"
		print(sophantering + behov)
	elif vaccinTier5 == "j":
		points += 1
		fifthChoice = "jordbruket"
		print(jordbruket + konsekvens)
	elif vaccinTier5 == "v":
		points += 3
		fifthChoice = "vapen"
		print(vapen + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			fifthChoice = "sophantering"
			print("Du tilldelades: " + str(fifthChoice) )
		elif randChoice == 2:
			points += 1
			fifthChoice = "jordbruket"
			print("Du tilldelades: " + str(fifthChoice) )
		else:
			points += 3
			fifthChoice = "vapen"
			print("Du tilldelades: " + str(fifthChoice) )
			
# Vapen
elif fourthChoice == "vapen":
	vapenTier5 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är dynamit: 'd', robot: r', eller motorcykeln: 'm':\n")
	
	if vapenTier5 == "d":
		points += 5
		fifthChoice = "dynamit"
		print(dynamit + behov)
	elif vapenTier5 == "r":
		points += 1
		fifthChoice = "robot"
		print(robot + konsekvens)
	elif vapenTier5 == "m":
		points += 3
		fifthChoice = "motorcykeln"
		print(motorcykeln + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			fifthChoice = "dynamit"
			print("Du tilldelades: " + str(fifthChoice) )
		elif randChoice == 2:
			points += 1
			fifthChoice = "robot"
			print("Du tilldelades: " + str(fifthChoice) )
		else:
			points += 3
			fifthChoice = "motorcykeln"
			print("Du tilldelades: " + str(fifthChoice) )
			
# Motorcykeln
elif fourthChoice == "motorcykeln":
	motorcykelnTier5 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är låset: 'l', förbränningsmotorn: 'f', eller spiken & skruven: 'ss':\n")
	
	if motorcykelnTier5 == "l":
		points += 5
		fifthChoice = "låset"
		print(låset + behov)
	elif motorcykelnTier5 == "f":
		points += 1
		fifthChoice = "förbränningsmotorn"
		print(förbränningsmotorn + konsekvens)
	elif motorcykelnTier5 == "ss":
		points += 3
		fifthChoice = "spiken & skruven"
		print(spikenochskruven + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			fifthChoice = "låset"
			print("Du tilldelades: " + str(fifthChoice) )
		elif randChoice == 2:
			points += 1
			fifthChoice = "förbränningsmotorn"
			print("Du tilldelades: " + str(fifthChoice) )
		else:
			points += 3
			fifthChoice = "spiken & skruven"
			print("Du tilldelades: " + str(fifthChoice) )
			
# Byggnadskonsten
elif fourthChoice == "byggnadskonsten":
	byggkonstenTier5 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är dynamit: 'd', jordbruket: 'j', eller spiken & skruven: 'ss':\n")
	
	if byggkonstenTier5 == "d":
		points += 5
		fifthChoice = "dynamit"
		print(dynamit + behov)
	elif byggkonstenTier5 == "j":
		points += 1
		fifthChoice = "jordbruket"
		print(jordbruket + konsekvens)
	elif byggkonstenTier5 == "ss":
		points += 3
		fifthChoice = "spiken & skruven"
		print(spikenochskruven + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			fifthChoice = "dynamit"
			print("Du tilldelades: " + str(fifthChoice) )
		elif randChoice == 2:
			points += 1
			fifthChoice = "jordbruket"
			print("Du tilldelades: " + str(fifthChoice) )
		else:
			points += 3
			fifthChoice = "spiken & skruven"
			print("Du tilldelades: " + str(fifthChoice) )
			
# Skriftspråket
elif fourthChoice == "skriftspråket":
	skriftspråketTier5 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är vävstolen: 'v', telegrafen: 't', eller byggnadskonsten: 'b':\n")
	
	if skriftspråketTier5 == "v":
		points += 5
		fifthChoice = "vävstolen"
		print(vävstolen + behov)
	elif skriftspråketTier5 == "t":
		points += 1
		fifthChoice = "telegrafen"
		print(telegrafen + konsekvens)
	elif skriftspråketTier5 == "b":
		points += 3
		fifthChoice = "byggnadskonsten"
		print(byggnadskonsten + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			fifthChoice = "vävstolen"
			print("Du tilldelades: " + str(fifthChoice) )
		elif randChoice == 2:
			points += 1
			fifthChoice = "telegrafen"
			print("Du tilldelades: " + str(fifthChoice) )
		else:
			points += 3
			fifthChoice = "byggnadskonsten"
			print("Du tilldelades: " + str(fifthChoice) )
			
# Jordbruket			
elif fourthChoice == "jordbruket":
	jordbruketTier5 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är sophantering: 'sp', avloppssystemet: 'a', eller skriftspråket: 'ss':\n")
	
	if jordbruketTier5 == "sp":
		points += 5
		fifthChoice = "sophantering"
		print(sophantering + behov)
	elif jordbruketTier5 == "a":
		points += 1
		fifthChoice = "avloppssystemet"
		print(avloppssystemet + konsekvens)
	elif jordbruketTier5 == "ss":
		points += 3
		fifthChoice = "skriftspråket"
		print(skriftspråket + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			fifthChoice = "sophantering"
			print("Du tilldelades: " + str(fifthChoice) )
		elif randChoice == 2:
			points += 1
			fifthChoice = "avloppssystemet"
			print("Du tilldelades: " + str(fifthChoice) )
		else:
			points += 3
			fifthChoice = "skriftspråket"
			print("Du tilldelades: " + str(fifthChoice) )			

# Propellern			
elif fourthChoice == "propellern":
	propellerntier5 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är ångmaskinen: 'å', flygplan: 'f', eller vapen: 'v':\n")
	
	if propellerntier5 == "å":
		points += 5
		fifthChoice = "ångmaskinen"
		print(ångmaskinen + behov)
	elif propellerntier5 == "f":
		points += 1
		fifthChoice = "flygplan"
		print(flygplan + konsekvens)
	elif propellerntier5 == "v":
		points += 3
		fifthChoice = "vapen"
		print(vapen + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			fifthChoice = "ångmaskinen"
			print("Du tilldelades: " + str(fifthChoice) )
		elif randChoice == 2:
			points += 1
			fifthChoice = "flygplan"
			print("Du tilldelades: " + str(fifthChoice) )
		else:
			points += 3
			fifthChoice = "vapen"
			print("Du tilldelades: " + str(fifthChoice) )

# Vattenkraft
elif fourthChoice == "vattenkraft":
	vattenkrafttier5 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är ångmaskinen: 'å', jordbruket: 'j', eller byggnadskonsten: 'b':\n")
	
	if vattenkrafttier5 == "å":
		points += 5
		fifthChoice = "ångmaskinen"
		print(ångmaskinen + behov)
	elif vattenkrafttier5 == "j":
		points += 1
		fifthChoice = "jordbruket"
		print(jordbruket + konsekvens)
	elif vattenkrafttier5 == "b":
		points += 3
		fifthChoice = "byggnadskonsten"
		print(byggnadskonsten + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			fifthChoice = "ångmaskinen"
			print("Du tilldelades: " + str(fifthChoice) )
		elif randChoice == 2:
			points += 1
			fifthChoice = "jordbruket"
			print("Du tilldelades: " + str(fifthChoice) )
		else:
			points += 3
			fifthChoice = "byggnadskonsten"
			print("Du tilldelades: " + str(fifthChoice) )

# Skor
elif fourthChoice == "skor":
	skortier5 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är vävstolen: 'v', roboten: 'r', eller spiken & skruven: 'ss':\n")
	
	if skortier5 == "v":
		points += 5
		fifthChoice = "vävstolen"
		print(vävstolen + behov)
	elif skortier5 == "r":
		points += 1
		fifthChoice = "robot"
		print(robot + konsekvens)
	elif skortier5 == "ss":
		points += 3
		fifthChoice = "spiken & skruven"
		print(spikenochskruven + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			fifthChoice = "vävstolen"
			print("Du tilldelades: " + str(fifthChoice) )
		elif randChoice == 2:
			points += 1
			fifthChoice = "robot"
			print("Du tilldelades: " + str(fifthChoice) )
		else:
			points += 3
			fifthChoice = "spiken & skruven"
			print("Du tilldelades: " + str(fifthChoice) )
			
# Cykeln
elif fourthChoice == "cykeln":
	cykelntier5 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är låset: 'l', motorcykeln: 'm', eller förbränningsmotorn: 'f':\n")
	
	if cykelntier5 == "l":
		points += 5
		fifthChoice = "låset"
		print(låset + behov)
	elif cykelntier5 == "f":
		points += 1
		fifthChoice = "förbränningsmotorn"
		print(förbränningsmotorn + konsekvens)
	elif cykelntier5 == "m":
		points += 3
		fifthChoice = "motorcykeln"
		print(motorcykeln + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			fifthChoice = "låset"
			print("Du tilldelades: " + str(fifthChoice) )
		elif randChoice == 2:
			points += 1
			fifthChoice = "förbränningsmotorn"
			print("Du tilldelades: " + str(fifthChoice) )
		else:
			points += 3
			fifthChoice = "motorcykeln"
			print("Du tilldelades: " + str(fifthChoice) )
			
print("\n\n")

# Val 6

# Sophanteringen
if fifthChoice == "sophantering":
	sophanteringtier6 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är skor: 's', avloppssystemet: 'a', eller vaccin: 'v':\n")
	
	if sophanteringtier6 == "å":
		points += 5
		sixthChoice = "ångmaskinen"
		print(ångmaskinen + behov)
	elif sophanteringtier6 == "a":
		points += 1
		sixthChoice = "avloppssystemet"
		print(avloppssystemet + konsekvens)
	elif sophanteringtier6 == "v":
		points += 3
		sixthChoice = "vaccin"
		print(vaccin + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			sixthChoice = "ångmaskinen"
			print("Du tilldelades: " + str(sixthChoice) )
		elif randChoice == 2:
			points += 1
			sixthChoice = "avloppssystemet"
			print("Du tilldelades: " + str(sixthChoice) )
		else:
			points += 3
			sixthChoice = "vaccin"
			print("Du tilldelades: " + str(sixthChoice) )

# Glödlampan
elif fifthChoice == "glödlampan":
	glödlampantier6 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är sophantering: 'sp', telegrafen: 't', eller skriftspråket: 'ss':\n")
	
	if glödlampantier6 == "sp":
		points += 5
		sixthChoice = "sophantering"
		print(sophantering + behov)
	elif glödlampantier6 == "t":
		points += 1
		sixthChoice = "telegrafen"
		print(telegrafen + konsekvens)
	elif glödlampantier6 == "ss":
		points += 3
		sixthChoice = "skriftspråket"
		print(skriftspråket + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			sixthChoice = "sophantering"
			print("Du tilldelades: " + str(sixthChoice) )
		elif randChoice == 2:
			points += 1
			sixthChoice = "telegrafen"
			print("Du tilldelades: " + str(sixthChoice) )
		else:
			points += 3
			sixthChoice = "skriftspråket"
			print("Du tilldelades: " + str(sixthChoice) )

# Ångmaskinen
elif fifthChoice == "ångmaskinen":
	ångmaskinentier6 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är dynamit: 'd', förbränningsmotorn: 'f', eller byggnadskonsten: 'b':\n")
	
	if ångmaskinentier6 == "d":
		points += 5
		sixthChoice = "dynamit"
		print(dynamit + behov)
	elif ångmaskinentier6 == "f":
		points += 1
		sixthChoice = "förbränningsmotorn"
		print(förbränningsmotorn + konsekvens)
	elif ångmaskinentier6 == "b":
		points += 3
		sixthChoice = "byggnadskonsten"
		print(byggnadskonsten + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			sixthChoice = "dynamit"
			print("Du tilldelades: " + str(sixthChoice) )
		elif randChoice == 2:
			points += 1
			sixthChoice = "förbränningsmotorn"
			print("Du tilldelades: " + str(sixthChoice) )
		else:
			points += 3
			sixthChoice = "byggnadskonsten"
			print("Du tilldelades: " + str(sixthChoice) )			

# Dynamiten
elif fifthChoice == "dynamit":
	dynamittier6 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är sophantering: 'sp', roboten: 'r', eller vapen: 'v':\n")
	
	if dynamittier6 == "sp":
		points += 5
		sixthChoice = "sophantering"
		print(sophantering + behov)
	elif dynamittier6 == "r":
		points += 1
		sixthChoice = "robot"
		print(robot + konsekvens)
	elif dynamittier6 == "v":
		points += 3
		sixthChoice = "vapen"
		print(vapen + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			sixthChoice = "sophantering"
			print("Du tilldelades: " + str(sixthChoice) )
		elif randChoice == 2:
			points += 1
			sixthChoice = "robot"
			print("Du tilldelades: " + str(sixthChoice) )
		else:
			points += 3
			sixthChoice = "vapen"
			print("Du tilldelades: " + str(sixthChoice) )

# Låset
elif fifthChoice == "låset":
	låsettier6 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är dynamit: 'd', jordbruket: 'j', eller spiken & skruven: 'ss':\n")
	
	if låsettier6 == "d":
		points += 5
		sixthChoice = "dynamit"
		print(dynamit + behov)
	elif låsettier6 == "j":
		points += 1
		sixthChoice = "jordbruket"
		print(jordbruket + konsekvens)
	elif låsettier6 == "ss":
		points += 3
		sixthChoice = "spiken & skruven"
		print(spikenochskruven + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			sixthChoice = "dynamit"
			print("Du tilldelades: " + str(sixthChoice) )
		elif randChoice == 2:
			points += 1
			sixthChoice = "jordbruket"
			print("Du tilldelades: " + str(sixthChoice) )
		else:
			points += 3
			sixthChoice = "spiken & skruven"
			print("Du tilldelades: " + str(sixthChoice) )

# Telegrafen
elif fifthChoice == "telegrafen":
	telegraftier6 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är glödlampan: 'g', robot: 'r', eller vapen: 'v':\n")
	
	if telegraftier6 == "g":
		points += 5
		sixthChoice = "glödlampan"
		print(glödlampan + behov)
	elif telegraftier6 == "r":
		points += 1
		sixthChoice = "robot"
		print(robot + konsekvens)
	elif telegraftier6 == "v":
		points += 3
		sixthChoice = "vapen"
		print(vapen + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			sixthChoice = "glödlampan"
			print("Du tilldelades: " + str(sixthChoice) )
		elif randChoice == 2:
			points += 1
			sixthChoice = "robot"
			print("Du tilldelades: " + str(sixthChoice) )
		else:
			points += 3
			sixthChoice = "vapen"
			print("Du tilldelades: " + str(sixthChoice) )

# Flygplanet
elif fifthChoice == "flygplan":
	flygplantier6 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är låset: 'l', robot: 'r', eller byggnadskonsten: 'b':\n")
	
	if flygplantier6 == "l":
		points += 5
		sixthChoice = "låset"
		print(låset + behov)
	elif flygplantier6 == "r":
		points += 1
		sixthChoice = "robot"
		print(robot + konsekvens)
	elif flygplantier6 == "b":
		points += 3
		sixthChoice = "byggnadskonsten"
		print(byggnadskonsten + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			sixthChoice = "låset"
			print("Du tilldelades: " + str(sixthChoice) )
		elif randChoice == 2:
			points += 1
			sixthChoice = "robot"
			print("Du tilldelades: " + str(sixthChoice) )
		else:
			points += 3
			sixthChoice = "byggnadskonsten"
			print("Du tilldelades: " + str(sixthChoice) )
			
# Förbränningsmotorn
elif fifthChoice == "förbränningsmotorn":
	förbränningsmotorntier6 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är ångmaskinen: 'å', flygplan: 'f', eller motorcykeln: 'm':\n")
	
	if förbränningsmotorntier6 == "å":
		points += 5
		sixthChoice = "ångmaskinen"
		print(ångmaskinen + behov)
	elif förbränningsmotorntier6 == "f":
		points += 1
		sixthChoice = "flygplan"
		print(flygplan + konsekvens)
	elif förbränningsmotorntier6 == "m":
		points += 3
		sixthChoice = "motorcykeln"
		print(motorcykeln + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			sixthChoice = "ångmaskinen"
			print("Du tilldelades: " + str(sixthChoice) )
		elif randChoice == 2:
			points += 1
			sixthChoice = "flygplan"
			print("Du tilldelades: " + str(sixthChoice) )
		else:
			points += 3
			sixthChoice = "motorcykeln"
			print("Du tilldelades: " + str(sixthChoice) )
			
# Avloppsystemet
elif fifthChoice == "avloppssystemet":
	avloppssystemettier6 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är skor: 's', vattenkraft: 'v', eller byggnadskonsten: 'b':\n")
	
	if avloppssystemettier6 == "s":
		points += 5
		sixthChoice = "skor"
		print(skor + behov)
	elif avloppssystemettier6 == "v":
		points += 1
		sixthChoice = "vattenkraft"
		print(vattenkraft + konsekvens)
	elif avloppssystemettier6 == "b":
		points += 3
		sixthChoice = "byggnadskonsten"
		print(byggnadskonsten + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			sixthChoice = "skor"
			print("Du tilldelades: " + str(sixthChoice) )
		elif randChoice == 2:
			points += 1
			sixthChoice = "vattenkraft"
			print("Du tilldelades: " + str(sixthChoice) )
		else:
			points += 3
			sixthChoice = "byggnadskonsten"
			print("Du tilldelades: " + str(sixthChoice) )
			
# Roboten
elif fifthChoice == "robot":
	robottier6 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är sophantering: 'sp', förbränningsmotorn: 'f', eller vapen: 'v':\n")
	
	if robottier6 == "sp":
		points += 5
		sixthChoice = "sophantering"
		print(sophantering + behov)
	elif robottier6 == "f":
		points += 1
		sixthChoice = "förbränningsmotorn"
		print(förbränningsmotorn + konsekvens)
	elif robottier6 == "v":
		points += 3
		sixthChoice = "vapen"
		print(vapen + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			sixthChoice = "sophantering"
			print("Du tilldelades: " + str(sixthChoice) )
		elif randChoice == 2:
			points += 1
			sixthChoice = "förbränningsmotorn"
			print("Du tilldelades: " + str(sixthChoice) )
		else:
			points += 3
			sixthChoice = "vapen"
			print("Du tilldelades: " + str(sixthChoice) )
			
# Spiken & skruven
elif fifthChoice == "spiken & skruven":
	spikenochskruventier6 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är propellern: 'p', vattenkraft: 'v', eller cykeln: 'v':\n")
	
	if spikenochskruventier6 == "p":
		points += 5
		sixthChoice = "propellern"
		print(propellern + behov)
	elif spikenochskruventier6 == "v":
		points += 1
		sixthChoice = "vapen"
		print(vapen + konsekvens)
	elif spikenochskruventier6 == "c":
		points += 3
		sixthChoice = "cykeln"
		print(cykeln + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			sixthChoice = "propellern"
			print("Du tilldelades: " + str(sixthChoice) )
		elif randChoice == 2:
			points += 1
			sixthChoice = "vapen"
			print("Du tilldelades: " + str(sixthChoice) )
		else:
			points += 3
			sixthChoice = "cykeln"
			print("Du tilldelades: " + str(sixthChoice) )
			
# Vaccinet
elif fifthChoice == "vaccin":
	vaccintier6 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är sophantering: 'sp', jordbruket: 'j', eller vapen: 'v':\n")
	
	if vaccintier6 == "sp":
		points += 5
		sixthChoice = "sophantering"
		print(sophantering + behov)
	elif vaccintier6 == "j":
		points += 1
		sixthChoice = "jordbruket"
		print(jordbruket + konsekvens)
	elif vaccintier6 == "v":
		points += 3
		sixthChoice = "vapen"
		print(vapen + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			sixthChoice = "sophantering"
			print("Du tilldelades: " + str(sixthChoice) )
		elif randChoice == 2:
			points += 1
			sixthChoice = "jordbruket"
			print("Du tilldelades: " + str(sixthChoice) )
		else:
			points += 3
			sixthChoice = "vapen"
			print("Du tilldelades: " + str(sixthChoice) )
			
# Vapen
elif fifthChoice == "vapen":
	vapentier6 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är dynamit: 'd', robot: r', eller motorcykeln: 'm':\n")
	
	if vapentier6 == "d":
		points += 5
		sixthChoice = "dynamit"
		print(dynamit + behov)
	elif vapentier6 == "r":
		points += 1
		sixthChoice = "robot"
		print(robot + konsekvens)
	elif vapentier6 == "m":
		points += 3
		sixthChoice = "motorcykeln"
		print(motorcykeln + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			sixthChoice = "dynamit"
			print("Du tilldelades: " + str(sixthChoice) )
		elif randChoice == 2:
			points += 1
			sixthChoice = "robot"
			print("Du tilldelades: " + str(sixthChoice) )
		else:
			points += 3
			sixthChoice = "motorcykeln"
			print("Du tilldelades: " + str(sixthChoice) )
			
# Motorcykeln
elif fifthChoice == "motorcykeln":
	motorcykelntier6 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är låset: 'l', förbränningsmotorn: 'f', eller spiken & skruven: 'ss':\n")
	
	if motorcykelntier6 == "l":
		points += 5
		sixthChoice = "låset"
		print(låset + behov)
	elif motorcykelntier6 == "f":
		points += 1
		sixthChoice = "förbränningsmotorn"
		print(förbränningsmotorn + konsekvens)
	elif motorcykelntier6 == "ss":
		points += 3
		sixthChoice = "spiken & skruven"
		print(spikenochskruven + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			sixthChoice = "låset"
			print("Du tilldelades: " + str(sixthChoice) )
		elif randChoice == 2:
			points += 1
			sixthChoice = "förbränningsmotorn"
			print("Du tilldelades: " + str(sixthChoice) )
		else:
			points += 3
			sixthChoice = "spiken & skruven"
			print("Du tilldelades: " + str(sixthChoice) )
			
# Byggnadskonsten
elif fifthChoice == "byggnadskonsten":
	byggkonstentier6 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är dynamit: 'd', jordbruket: 'j', eller spiken & skruven: 'ss':\n")
	
	if byggkonstentier6 == "d":
		points += 5
		sixthChoice = "dynamit"
		print(dynamit + behov)
	elif byggkonstentier6 == "j":
		points += 1
		sixthChoice = "jordbruket"
		print(jordbruket + konsekvens)
	elif byggkonstentier6 == "ss":
		points += 3
		sixthChoice = "spiken & skruven"
		print(spikenochskruven + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			sixthChoice = "dynamit"
			print("Du tilldelades: " + str(sixthChoice) )
		elif randChoice == 2:
			points += 1
			sixthChoice = "jordbruket"
			print("Du tilldelades: " + str(sixthChoice) )
		else:
			points += 3
			sixthChoice = "spiken & skruven"
			print("Du tilldelades: " + str(sixthChoice) )
			
# Skriftspråket
elif fifthChoice == "skriftspråket":
	skriftspråkettier6 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är vävstolen: 'v', telegrafen: 't', eller byggnadskonsten: 'b':\n")
	
	if skriftspråkettier6 == "v":
		points += 5
		sixthChoice = "vävstolen"
		print(vävstolen + behov)
	elif skriftspråkettier6 == "t":
		points += 1
		sixthChoice = "telegrafen"
		print(telegrafen + konsekvens)
	elif skriftspråkettier6 == "b":
		points += 3
		sixthChoice = "byggnadskonsten"
		print(byggnadskonsten + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			sixthChoice = "vävstolen"
			print("Du tilldelades: " + str(sixthChoice) )
		elif randChoice == 2:
			points += 1
			sixthChoice = "telegrafen"
			print("Du tilldelades: " + str(sixthChoice) )
		else:
			points += 3
			sixthChoice = "byggnadskonsten"
			print("Du tilldelades: " + str(sixthChoice) )
			
# Jordbruket			
elif fifthChoice == "jordbruket":
	jordbrukettier6 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är sophantering: 'sp', avloppssystemet: 'a', eller skriftspråket: 'ss':\n")
	
	if jordbrukettier6 == "sp":
		points += 5
		sixthChoice = "sophantering"
		print(sophantering + behov)
	elif jordbrukettier6 == "a":
		points += 1
		sixthChoice = "avloppssystemet"
		print(avloppssystemet + konsekvens)
	elif jordbrukettier6 == "ss":
		points += 3
		sixthChoice = "skriftspråket"
		print(skriftspråket + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			sixthChoice = "sophantering"
			print("Du tilldelades: " + str(sixthChoice) )
		elif randChoice == 2:
			points += 1
			sixthChoice = "avloppssystemet"
			print("Du tilldelades: " + str(sixthChoice) )
		else:
			points += 3
			sixthChoice = "skriftspråket"
			print("Du tilldelades: " + str(sixthChoice) )			

# Propellern			
elif fifthChoice == "propellern":
	propellerntier6 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är ångmaskinen: 'å', flygplan: 'f', eller vapen: 'v':\n")
	
	if propellerntier6 == "å":
		points += 5
		sixthChoice = "ångmaskinen"
		print(ångmaskinen + behov)
	elif propellerntier6 == "f":
		points += 1
		sixthChoice = "flygplan"
		print(flygplan + konsekvens)
	elif propellerntier6 == "v":
		points += 3
		sixthChoice = "vapen"
		print(vapen + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			sixthChoice = "ångmaskinen"
			print("Du tilldelades: " + str(sixthChoice) )
		elif randChoice == 2:
			points += 1
			sixthChoice = "flygplan"
			print("Du tilldelades: " + str(sixthChoice) )
		else:
			points += 3
			sixthChoice = "vapen"
			print("Du tilldelades: " + str(sixthChoice) )

# Vattenkraft
elif fifthChoice == "vattenkraft":
	vattenkrafttier6 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är ångmaskinen: 'å', jordbruket: 'j', eller byggnadskonsten: 'b':\n")
	
	if vattenkrafttier6 == "å":
		points += 5
		sixthChoice = "ångmaskinen"
		print(ångmaskinen + behov)
	elif vattenkrafttier6 == "j":
		points += 1
		sixthChoice = "jordbruket"
		print(jordbruket + konsekvens)
	elif vattenkrafttier6 == "b":
		points += 3
		sixthChoice = "byggnadskonsten"
		print(byggnadskonsten + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			sixthChoice = "ångmaskinen"
			print("Du tilldelades: " + str(sixthChoice) )
		elif randChoice == 2:
			points += 1
			sixthChoice = "jordbruket"
			print("Du tilldelades: " + str(sixthChoice) )
		else:
			points += 3
			sixthChoice = "byggnadskonsten"
			print("Du tilldelades: " + str(sixthChoice) )

# Skor
elif fifthChoice == "skor":
	skortier6 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är vävstolen: 'v', roboten: 'r', eller spiken & skruven: 'ss':\n")
	
	if skortier6 == "v":
		points += 5
		sixthChoice = "vävstolen"
		print(vävstolen + behov)
	elif skortier6 == "r":
		points += 1
		sixthChoice = "robot"
		print(robot + konsekvens)
	elif skortier6 == "ss":
		points += 3
		sixthChoice = "spiken & skruven"
		print(spikenochskruven + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			sixthChoice = "vävstolen"
			print("Du tilldelades: " + str(sixthChoice) )
		elif randChoice == 2:
			points += 1
			sixthChoice = "robot"
			print("Du tilldelades: " + str(sixthChoice) )
		else:
			points += 3
			sixthChoice = "spiken & skruven"
			print("Du tilldelades: " + str(sixthChoice) )
			
# Cykeln
elif fifthChoice == "cykeln":
	cykelntier6 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är låset: 'l', motorcykeln: 'm', eller förbränningsmotorn: 'f':\n")
	
	if cykelntier6 == "l":
		points += 5
		sixthChoice = "låset"
		print(låset + behov)
	elif cykelntier6 == "f":
		points += 1
		sixthChoice = "förbränningsmotorn"
		print(förbränningsmotorn + konsekvens)
	elif cykelntier6 == "m":
		points += 3
		sixthChoice = "motorcykeln"
		print(motorcykeln + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			sixthChoice = "låset"
			print("Du tilldelades: " + str(sixthChoice) )
		elif randChoice == 2:
			points += 1
			sixthChoice = "förbränningsmotorn"
			print("Du tilldelades: " + str(sixthChoice) )
		else:
			points += 3
			sixthChoice = "motorcykeln"
			print("Du tilldelades: " + str(sixthChoice) )
			
# Vävstolen
elif fifthChoice == "vävstolen":
	vävstolentier6 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är ångmaskinen: 'å', roboten: 'r', eller spiken & skruven: 'ss':\n")
	
	if vävstolentier6 == "å":
		points += 5
		sixthChoice = "ångmaskinen"
		print(ångmaskinen + behov)
	elif vävstolentier6 == "r":
		points += 1
		sixthChoice = "robot"
		print(robot + konsekvens)
	elif vävstolentier6 == "ss":
		points += 3
		sixthChoice = "spiken & skruven"
		print(spikenochskruven + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			sixthChoice = "ångmaskinen"
			print("Du tilldelades: " + str(sixthChoice) )
		elif randChoice == 2:
			points += 1
			sixthChoice = "robot"
			print("Du tilldelades: " + str(sixthChoice) )
		else:
			points += 3
			sixthChoice = "spiken & skruven"
			print("Du tilldelades: " + str(sixthChoice) )

print("\n\n")

# Val 7

# Sophanteringen
if sixthChoice == "sophantering":
	sophanteringtier7 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är skor: 's', avloppssystemet: 'a', eller vaccin: 'v':\n")
	
	if sophanteringtier7 == "å":
		points += 5
		seventhChoice = "ångmaskinen"
		print(ångmaskinen + behov)
	elif sophanteringtier7 == "a":
		points += 1
		seventhChoice = "avloppssystemet"
		print(avloppssystemet + konsekvens)
	elif sophanteringtier7 == "v":
		points += 3
		seventhChoice = "vaccin"
		print(vaccin + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			seventhChoice = "ångmaskinen"
			print("Du tilldelades: " + str(seventhChoice) )
		elif randChoice == 2:
			points += 1
			seventhChoice = "avloppssystemet"
			print("Du tilldelades: " + str(seventhChoice) )
		else:
			points += 3
			seventhChoice = "vaccin"
			print("Du tilldelades: " + str(seventhChoice) )

# Glödlampan
elif sixthChoice == "glödlampan":
	glödlampantier7 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är sophantering: 'sp', telegrafen: 't', eller skriftspråket: 'ss':\n")
	
	if glödlampantier7 == "sp":
		points += 5
		seventhChoice = "sophantering"
		print(sophantering + behov)
	elif glödlampantier7 == "t":
		points += 1
		seventhChoice = "telegrafen"
		print(telegrafen + konsekvens)
	elif glödlampantier7 == "ss":
		points += 3
		seventhChoice = "skriftspråket"
		print(skriftspråket + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			seventhChoice = "sophantering"
			print("Du tilldelades: " + str(seventhChoice) )
		elif randChoice == 2:
			points += 1
			seventhChoice = "telegrafen"
			print("Du tilldelades: " + str(seventhChoice) )
		else:
			points += 3
			seventhChoice = "skriftspråket"
			print("Du tilldelades: " + str(seventhChoice) )

# Ångmaskinen
elif sixthChoice == "ångmaskinen":
	ångmaskinentier7 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är dynamit: 'd', förbränningsmotorn: 'f', eller byggnadskonsten: 'b':\n")
	
	if ångmaskinentier7 == "d":
		points += 5
		seventhChoice = "dynamit"
		print(dynamit + behov)
	elif ångmaskinentier7 == "f":
		points += 1
		seventhChoice = "förbränningsmotorn"
		print(förbränningsmotorn + konsekvens)
	elif ångmaskinentier7 == "b":
		points += 3
		seventhChoice = "byggnadskonsten"
		print(byggnadskonsten + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			seventhChoice = "dynamit"
			print("Du tilldelades: " + str(seventhChoice) )
		elif randChoice == 2:
			points += 1
			seventhChoice = "förbränningsmotorn"
			print("Du tilldelades: " + str(seventhChoice) )
		else:
			points += 3
			seventhChoice = "byggnadskonsten"
			print("Du tilldelades: " + str(seventhChoice) )			

# Dynamiten
elif sixthChoice == "dynamit":
	dynamittier7 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är sophantering: 'sp', roboten: 'r', eller vapen: 'v':\n")
	
	if dynamittier7 == "sp":
		points += 5
		seventhChoice = "sophantering"
		print(sophantering + behov)
	elif dynamittier7 == "r":
		points += 1
		seventhChoice = "robot"
		print(robot + konsekvens)
	elif dynamittier7 == "v":
		points += 3
		seventhChoice = "vapen"
		print(vapen + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			seventhChoice = "sophantering"
			print("Du tilldelades: " + str(seventhChoice) )
		elif randChoice == 2:
			points += 1
			seventhChoice = "robot"
			print("Du tilldelades: " + str(seventhChoice) )
		else:
			points += 3
			seventhChoice = "vapen"
			print("Du tilldelades: " + str(seventhChoice) )

# Låset
elif sixthChoice == "låset":
	låsettier7 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är dynamit: 'd', jordbruket: 'j', eller spiken & skruven: 'ss':\n")
	
	if låsettier7 == "d":
		points += 5
		seventhChoice = "dynamit"
		print(dynamit + behov)
	elif låsettier7 == "j":
		points += 1
		seventhChoice = "jordbruket"
		print(jordbruket + konsekvens)
	elif låsettier7 == "ss":
		points += 3
		seventhChoice = "spiken & skruven"
		print(spikenochskruven + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			seventhChoice = "dynamit"
			print("Du tilldelades: " + str(seventhChoice) )
		elif randChoice == 2:
			points += 1
			seventhChoice = "jordbruket"
			print("Du tilldelades: " + str(seventhChoice) )
		else:
			points += 3
			seventhChoice = "spiken & skruven"
			print("Du tilldelades: " + str(seventhChoice) )

# Telegrafen
elif sixthChoice == "telegraf":
	telegraftier7 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är glödlampan: 'g', robot: 'r', eller vapen: 'v':\n")
	
	if telegraftier7 == "g":
		points += 5
		seventhChoice = "glödlampan"
		print(glödlampan + behov)
	elif telegraftier7 == "r":
		points += 1
		seventhChoice = "robot"
		print(robot + konsekvens)
	elif telegraftier7 == "v":
		points += 3
		seventhChoice = "vapen"
		print(vapen + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			seventhChoice = "glödlampan"
			print("Du tilldelades: " + str(seventhChoice) )
		elif randChoice == 2:
			points += 1
			seventhChoice = "robot"
			print("Du tilldelades: " + str(seventhChoice) )
		else:
			points += 3
			seventhChoice = "vapen"
			print("Du tilldelades: " + str(seventhChoice) )

# Flygplanet
elif sixthChoice == "flygplan":
	flygplantier7 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är låset: 'l', robot: 'r', eller byggnadskonsten: 'b':\n")
	
	if flygplantier7 == "l":
		points += 5
		seventhChoice = "låset"
		print(låset + behov)
	elif flygplantier7 == "r":
		points += 1
		seventhChoice = "robot"
		print(robot + konsekvens)
	elif flygplantier7 == "b":
		points += 3
		seventhChoice = "byggnadskonsten"
		print(byggnadskonsten + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			seventhChoice = "låset"
			print("Du tilldelades: " + str(seventhChoice) )
		elif randChoice == 2:
			points += 1
			seventhChoice = "robot"
			print("Du tilldelades: " + str(seventhChoice) )
		else:
			points += 3
			seventhChoice = "byggnadskonsten"
			print("Du tilldelades: " + str(seventhChoice) )
			
# Förbränningsmotorn
elif sixthChoice == "förbränningsmotorn":
	förbränningsmotorntier7 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är ångmaskinen: 'å', flygplan: 'f', eller motorcykeln: 'm':\n")
	
	if förbränningsmotorntier7 == "å":
		points += 5
		seventhChoice = "ångmaskinen"
		print(ångmaskinen + behov)
	elif förbränningsmotorntier7 == "f":
		points += 1
		seventhChoice = "flygplan"
		print(flygplan + konsekvens)
	elif förbränningsmotorntier7 == "m":
		points += 3
		seventhChoice = "motorcykeln"
		print(motorcykeln + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			seventhChoice = "ångmaskinen"
			print("Du tilldelades: " + str(seventhChoice) )
		elif randChoice == 2:
			points += 1
			seventhChoice = "flygplan"
			print("Du tilldelades: " + str(seventhChoice) )
		else:
			points += 3
			seventhChoice = "motorcykeln"
			print("Du tilldelades: " + str(seventhChoice) )
			
# Avloppsystemet
elif sixthChoice == "avloppssystemet":
	avloppssystemettier7 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är skor: 's', vattenkraft: 'v', eller byggnadskonsten: 'b':\n")
	
	if avloppssystemettier7 == "s":
		points += 5
		seventhChoice = "skor"
		print(skor + behov)
	elif avloppssystemettier7 == "v":
		points += 1
		seventhChoice = "vattenkraft"
		print(vattenkraft + konsekvens)
	elif avloppssystemettier7 == "b":
		points += 3
		seventhChoice = "byggnadskonsten"
		print(byggnadskonsten + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			seventhChoice = "skor"
			print("Du tilldelades: " + str(seventhChoice) )
		elif randChoice == 2:
			points += 1
			seventhChoice = "vattenkraft"
			print("Du tilldelades: " + str(seventhChoice) )
		else:
			points += 3
			seventhChoice = "byggnadskonsten"
			print("Du tilldelades: " + str(seventhChoice) )
			
# Roboten
elif sixthChoice == "robot":
	robottier7 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är sophantering: 'sp', förbränningsmotorn: 'f', eller vapen: 'v':\n")
	
	if robottier7 == "sp":
		points += 5
		seventhChoice = "sophantering"
		print(sophantering + behov)
	elif robottier7 == "f":
		points += 1
		seventhChoice = "förbränningsmotorn"
		print(förbränningsmotorn + konsekvens)
	elif robottier7 == "v":
		points += 3
		seventhChoice = "vapen"
		print(vapen + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			seventhChoice = "sophantering"
			print("Du tilldelades: " + str(seventhChoice) )
		elif randChoice == 2:
			points += 1
			seventhChoice = "förbränningsmotorn"
			print("Du tilldelades: " + str(seventhChoice) )
		else:
			points += 3
			seventhChoice = "vapen"
			print("Du tilldelades: " + str(seventhChoice) )
			
# Spiken & skruven
elif sixthChoice == "spiken & skruven":
	spikenochskruventier7 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är propellern: 'p', vattenkraft: 'v', eller cykeln: 'c':\n")
	
	if spikenochskruventier7 == "p":
		points += 5
		seventhChoice = "propellern"
		print(propellern + behov)
	elif spikenochskruventier7 == "v":
		points += 1
		seventhChoice = "vapen"
		print(vapen + konsekvens)
	elif spikenochskruventier7 == "c":
		points += 3
		seventhChoice = "cykeln"
		print(cykeln + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			seventhChoice = "propellern"
			print("Du tilldelades: " + str(seventhChoice) )
		elif randChoice == 2:
			points += 1
			seventhChoice = "vapen"
			print("Du tilldelades: " + str(seventhChoice) )
		else:
			points += 3
			seventhChoice = "cykeln"
			print("Du tilldelades: " + str(seventhChoice) )
			
# Vaccinet
elif sixthChoice == "vaccin":
	vaccintier7 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är sophantering: 'sp', jordbruket: 'j', eller vapen: 'v':\n")
	
	if vaccintier7 == "sp":
		points += 5
		seventhChoice = "sophantering"
		print(sophantering + behov)
	elif vaccintier7 == "j":
		points += 1
		seventhChoice = "jordbruket"
		print(jordbruket + konsekvens)
	elif vaccintier7 == "v":
		points += 3
		seventhChoice = "vapen"
		print(vapen + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			seventhChoice = "sophantering"
			print("Du tilldelades: " + str(seventhChoice) )
		elif randChoice == 2:
			points += 1
			seventhChoice = "jordbruket"
			print("Du tilldelades: " + str(seventhChoice) )
		else:
			points += 3
			seventhChoice = "vapen"
			print("Du tilldelades: " + str(seventhChoice) )
			
# Vapen
elif sixthChoice == "vapen":
	vapentier7 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är dynamit: 'd', robot: r', eller motorcykeln: 'm':\n")
	
	if vapentier7 == "d":
		points += 5
		seventhChoice = "dynamit"
		print(dynamit + behov)
	elif vapentier7 == "r":
		points += 1
		seventhChoice = "robot"
		print(robot + konsekvens)
	elif vapentier7 == "m":
		points += 3
		seventhChoice = "motorcykeln"
		print(motorcykeln + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			seventhChoice = "dynamit"
			print("Du tilldelades: " + str(seventhChoice) )
		elif randChoice == 2:
			points += 1
			seventhChoice = "robot"
			print("Du tilldelades: " + str(seventhChoice) )
		else:
			points += 3
			seventhChoice = "motorcykeln"
			print("Du tilldelades: " + str(seventhChoice) )
			
# Motorcykeln
elif sixthChoice == "motorcykeln":
	motorcykelntier7 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är låset: 'l', förbränningsmotorn: 'f', eller spiken & skruven: 'ss':\n")
	
	if motorcykelntier7 == "l":
		points += 5
		seventhChoice = "låset"
		print(låset + behov)
	elif motorcykelntier7 == "f":
		points += 1
		seventhChoice = "förbränningsmotorn"
		print(förbränningsmotorn + konsekvens)
	elif motorcykelntier7 == "ss":
		points += 3
		seventhChoice = "spiken & skruven"
		print(spikenochskruven + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			seventhChoice = "låset"
			print("Du tilldelades: " + str(seventhChoice) )
		elif randChoice == 2:
			points += 1
			seventhChoice = "förbränningsmotorn"
			print("Du tilldelades: " + str(seventhChoice) )
		else:
			points += 3
			seventhChoice = "spiken & skruven"
			print("Du tilldelades: " + str(seventhChoice) )
			
# Byggnadskonsten
elif sixthChoice == "byggnadskonsten":
	byggkonstentier7 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är dynamit: 'd', jordbruket: 'j', eller spiken & skruven: 'ss':\n")
	
	if byggkonstentier7 == "d":
		points += 5
		seventhChoice = "dynamit"
		print(dynamit + behov)
	elif byggkonstentier7 == "j":
		points += 1
		seventhChoice = "jordbruket"
		print(jordbruket + konsekvens)
	elif byggkonstentier7 == "ss":
		points += 3
		seventhChoice = "spiken & skruven"
		print(spikenochskruven + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			seventhChoice = "dynamit"
			print("Du tilldelades: " + str(seventhChoice) )
		elif randChoice == 2:
			points += 1
			seventhChoice = "jordbruket"
			print("Du tilldelades: " + str(seventhChoice) )
		else:
			points += 3
			seventhChoice = "spiken & skruven"
			print("Du tilldelades: " + str(seventhChoice) )
			
# Skriftspråket
elif sixthChoice == "skriftspråket":
	skriftspråkettier7 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är vävstolen: 'v', telegrafen: 't', eller byggnadskonsten: 'b':\n")
	
	if skriftspråkettier7 == "v":
		points += 5
		seventhChoice = "vävstolen"
		print(vävstolen + behov)
	elif skriftspråkettier7 == "t":
		points += 1
		seventhChoice = "telegrafen"
		print(telegrafen + konsekvens)
	elif skriftspråkettier7 == "b":
		points += 3
		seventhChoice = "byggnadskonsten"
		print(byggnadskonsten + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			seventhChoice = "vävstolen"
			print("Du tilldelades: " + str(seventhChoice) )
		elif randChoice == 2:
			points += 1
			seventhChoice = "telegrafen"
			print("Du tilldelades: " + str(seventhChoice) )
		else:
			points += 3
			seventhChoice = "byggnadskonsten"
			print("Du tilldelades: " + str(seventhChoice) )
			
# Jordbruket			
elif sixthChoice == "jordbruket":
	jordbrukettier7 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är sophantering: 'sp', avloppssystemet: 'a', eller skriftspråket: 'ss':\n")
	
	if jordbrukettier7 == "sp":
		points += 5
		seventhChoice = "sophantering"
		print(sophantering + behov)
	elif jordbrukettier7 == "a":
		points += 1
		seventhChoice = "avloppssystemet"
		print(avloppssystemet + konsekvens)
	elif jordbrukettier7 == "ss":
		points += 3
		seventhChoice = "skriftspråket"
		print(skriftspråket + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			seventhChoice = "sophantering"
			print("Du tilldelades: " + str(seventhChoice) )
		elif randChoice == 2:
			points += 1
			seventhChoice = "avloppssystemet"
			print("Du tilldelades: " + str(seventhChoice) )
		else:
			points += 3
			seventhChoice = "skriftspråket"
			print("Du tilldelades: " + str(seventhChoice) )			

# Propellern			
elif sixthChoice == "propellern":
	propellerntier7 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är ångmaskinen: 'å', flygplan: 'f', eller vapen: 'v':\n")
	
	if propellerntier7 == "å":
		points += 5
		seventhChoice = "ångmaskinen"
		print(ångmaskinen + behov)
	elif propellerntier7 == "f":
		points += 1
		seventhChoice = "flygplan"
		print(flygplan + konsekvens)
	elif propellerntier7 == "v":
		points += 3
		seventhChoice = "vapen"
		print(vapen + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			seventhChoice = "ångmaskinen"
			print("Du tilldelades: " + str(seventhChoice) )
		elif randChoice == 2:
			points += 1
			seventhChoice = "flygplan"
			print("Du tilldelades: " + str(seventhChoice) )
		else:
			points += 3
			seventhChoice = "vapen"
			print("Du tilldelades: " + str(seventhChoice) )

# Vattenkraft
elif sixthChoice == "vattenkraft":
	vattenkrafttier7 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är ångmaskinen: 'å', jordbruket: 'j', eller byggnadskonsten: 'b':\n")
	
	if vattenkrafttier7 == "å":
		points += 5
		seventhChoice = "ångmaskinen"
		print(ångmaskinen + behov)
	elif vattenkrafttier7 == "j":
		points += 1
		seventhChoice = "jordbruket"
		print(jordbruket + konsekvens)
	elif vattenkrafttier7 == "b":
		points += 3
		seventhChoice = "byggnadskonsten"
		print(byggnadskonsten + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			seventhChoice = "ångmaskinen"
			print("Du tilldelades: " + str(seventhChoice) )
		elif randChoice == 2:
			points += 1
			seventhChoice = "jordbruket"
			print("Du tilldelades: " + str(seventhChoice) )
		else:
			points += 3
			seventhChoice = "byggnadskonsten"
			print("Du tilldelades: " + str(seventhChoice) )

# Skor
elif sixthChoice == "skor":
	skortier7 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är vävstolen: 'v', roboten: 'r', eller spiken & skruven: 'ss':\n")
	
	if skortier7 == "v":
		points += 5
		seventhChoice = "vävstolen"
		print(vävstolen + behov)
	elif skortier7 == "r":
		points += 1
		seventhChoice = "robot"
		print(robot + konsekvens)
	elif skortier7 == "ss":
		points += 3
		seventhChoice = "spiken & skruven"
		print(spikenochskruven + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			seventhChoice = "vävstolen"
			print("Du tilldelades: " + str(seventhChoice) )
		elif randChoice == 2:
			points += 1
			seventhChoice = "robot"
			print("Du tilldelades: " + str(seventhChoice) )
		else:
			points += 3
			seventhChoice = "spiken & skruven"
			print("Du tilldelades: " + str(seventhChoice) )
			
# Cykeln
elif sixthChoice == "cykeln":
	cykelntier7 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är låset: 'l', motorcykeln: 'm', eller förbränningsmotorn: 'f':\n")
	
	if cykelntier7 == "l":
		points += 5
		seventhChoice = "låset"
		print(låset + behov)
	elif cykelntier7 == "f":
		points += 1
		seventhChoice = "förbränningsmotorn"
		print(förbränningsmotorn + konsekvens)
	elif cykelntier7 == "m":
		points += 3
		seventhChoice = "motorcykeln"
		print(motorcykeln + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			seventhChoice = "låset"
			print("Du tilldelades: " + str(seventhChoice) )
		elif randChoice == 2:
			points += 1
			seventhChoice = "förbränningsmotorn"
			print("Du tilldelades: " + str(seventhChoice) )
		else:
			points += 3
			seventhChoice = "motorcykeln"
			print("Du tilldelades: " + str(seventhChoice) )
			
# Vävstolen
elif sixthChoice == "vävstolen":
	vävstolentier7 = input("Du kan nu gå vidare i ditt teknologiträd, de innovationer du kan välja att utveckla är ångmaskinen: 'å', roboten: 'r', eller spiken & skruven: 'ss':\n")
	
	if vävstolentier7 == "å":
		points += 5
		seventhChoice = "ångmaskinen"
		print(ångmaskinen + behov)
	elif vävstolentier7 == "r":
		points += 1
		seventhChoice = "robot"
		print(robot + konsekvens)
	elif vävstolentier7 == "ss":
		points += 3
		seventhChoice = "spiken & skruven"
		print(spikenochskruven + process)
	else:
		randChoice = random.randrange(1,3)
		print("Det var inte ett giltigt val, du kommer tilldelas en slumpmässig uppföljning.")
		if randChoice == 1:
			points += 5
			seventhChoice = "ångmaskinen"
			print("Du tilldelades: " + str(seventhChoice) )
		elif randChoice == 2:
			points += 1
			seventhChoice = "robot"
			print("Du tilldelades: " + str(seventhChoice) )
		else:
			points += 3
			seventhChoice = "spiken & skruven"
			print("Du tilldelades: " + str(seventhChoice) )

print("\n\n\n")

print("Du valde att börja bygga din civilisation runt " + firstChoice + ". Du lärde dig sedan hur du skulle använda " + secondChoice + " och det ledde dig i sin tur till att du började använda " + thirdChoice + " och " + fourthChoice + ". För att verkligen sätta din civilisation på kartan la du till " + fifthChoice + " och " + sixthChoice + " innan du avslutade ditt teknologiska träd med " + seventhChoice + ".")
print("\nDu fick ihop " + str(points) + " poäng.")
# Gruppindelning beroende på samlade poäng.
if points <= 23:
	print("Det innebär att du gärna valde innovationer som har uppfunnits lite som av en slump, vilket inte är så dumt, men det försök gärna lösa några av de problem som finns i världen också. Det blir roligare då!")
elif points <= 31:
	print("Det innebär att du gärna valde innovationer som har uppfunnits som en del av en större process. Du vill gärna vara med där det händer, men går inte utanför din 'comfort zone' för att uppfinna något revolutionerande. Våga vara annorlunda!")
else:
	print("Det innebär att du gärna valde innovationer som har uppfunnits som ett svar på ett direkt behov. Det är jättebra och det är sådana som du som verkligen för världen framåt. Underskatta dock inte nyttan av arbeta efter satta processer, också där kan du hitta nya innovationer!")
	
##choices.append(firstChoice)
##choices.append(secondChoice)
##choices.append(thirdChoice)
##choices.append(fourthChoice)
##choices.append(fifthChoice)
##choices.append(sixthChoice)
##choices.append(seventhChoice)
##for i in choices:
##	print(i)