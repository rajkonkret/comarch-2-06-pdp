wiek = 47
rok = 2023
temp = 36.6  # float

print(wiek)
print(type(wiek))

print(temp)
print(type(temp))  # <class 'float'>

print(wiek + rok)
print(wiek - rok)
print(wiek * rok)
print(wiek / rok)  # 0.023232822540781017 - wynik float
print(wiek // rok)  # 0 - czesc całkowita z dzielenia
print(wiek % rok)  # modulo, czyli reszta z dzielenia 47 (0 reszty 47)
print(5 % 2)  # 5 : 2 = 2 r 1
print(wiek ** rok)  # potęgowaie
# 45078203931754879833755371263184100554069693371970790166550086337166929282209631310820384917433394389818850084059682155738946923593519339971979987184878719143347822877080166016305633858980646982982035009169683929600866849370254284594410259081810914177936258354044844197957685991112972719936213350899025856675941841051542932699309570860500811860089660880894590720048830128020805934998022285279517404916699566535910334140980948627464893726683300308246256435922638780894767219469371567733648668536095220582084106058604576023853911329742621170597394044858954031904845204713320345898995536033430694777299073558461659990387482337510252059704429861973282695848464133756828002337849502205927608638026685335621581648588831440452901228066610064838511143722994680835572111905729526821003403999574052913058013780569284301447201199360862980125345185267458322244174754760235645685492606330652115206869099313959802457245401990040413683068161836804199589467286821543820708830799675526464077232536437272469674483842644916573967394952783615179074367201577861856098886185926849819419959301394174639112786434743515097974073038025983124023093249824747670597867804444795204518584499213273765002045747226159755508886128248794785774686807307831773937374117643191629720371814457473951753730504921867861109223743415365994646020128049058892170454783282077366522197531251839254246890919769662102146370872232817657253467073958257693272125447970629375795264183946841918141303914221458978000017230415479950239072477463966976071787992266303288650454465218458569924355985864631536903234309883129892060736262433196744704303250502412632973466768854052177805448941401050666946290231909444116150147483844446796347327747243052426364515747416871323515334730748403582809145391835272810484031079850218573060633682914087530820407495383437711846602496159014625053486468189491894555315124118273788837562217098940741007821082955984012535693481603867338662094863438358565016893065313864269812857421374700534759074168345195447148874028993380242219129043029606584072271104111234951374224200371331813017809039145682445339276347659456282869925148975207935531054581789121934239156632088333339333249805290742724702566333616109777903418918460999215339867622948293192281810875405315780167477214333924279573722692031442603630674205716724030206889414412720891645748569248133177403069148219335420214214642682225483345707366405930250019619710421753504878791328912926075949900464905837745495094954692637328243429893842624063547482126496861605663142123049949521674978969971820312692204650542893332751171994083744336728833310712591248556821428155891267382705463879972404942544986404586372649383332275282069968563292299653049327383801937808511262941533692735891000325633721673998706721808532823117603943759058083813072605254721799621972628638329854091343978787300984650013270263279630790696846902724657699981325921724643416838624350033281780450925937348241968601901508021853687897491611775047420759784229120349365961807631438609901844381849653020079498868126950887118012160522219113720179883099609422978767092259446730436000655651737064967890809868863017884718477737074924595396533930923439783108213537632322680816023909893007298911450557034767842493150642086876367257750264665859224024138024370588055954140761006530326933860591552092638968596147124041868253908587214992795590678005238962406463463464625777404041249253050594424105716702825619023
print(54 - 5 * 43 + 4 / 2 + 4 / 2)  # -157.0
print(54 - (5 * 43) + (4 / 2 + 4) / 2)  # -158.0
print(0.2 + 0.8)  # 1.0
print(0.2 + 0.7)  # 0.8999999999999999
wynik = 0.2 + 0.7
print(f"{wynik:.1f}")  # 0.9

print(f"\tSprawdzanie zmiennej temp {wiek} {temp}")
print(f"""
    {wiek}
    {temp}
""")

print(type(4 / 2))  # <class 'float'>
print(type(4 // 2))  # <class 'int'>

# typ logiczny
print("True/False")
czy_znasz_Pythona = True
print(czy_znasz_Pythona)
print(type(czy_znasz_Pythona))  # <class 'bool'>

print(int(czy_znasz_Pythona))  # int - rzutowanie na int, 1 - Prawda
print(int(False))  # int - rzutowanie na int, 0 - Fałsz

x = 1
print(bool(x))  # True
x = 100
print(bool(x))  # True
x = -10
print(bool(x))  # True

x = "radek"
print(bool(x))  # True
x = ''
print(bool(x))  # False

a = 14
b = 3
print(f"Wynik porównania {a} > {b}", a > b)  # Wynik porównania 14 > 3 True
print(f"Wynik porównania {a} < {b}", a < b)
print(f"Wynik porównania {a} == {b}", a == b)  # czy są równe
print(f"Wynik porównania {a} != {b}", a != b)  # czy są różne
# Wynik porównania 14 > 3 True
# Wynik porównania 14 < 3 False
# Wynik porównania 14 == 3 False
# Wynik porównania 14 != 3 True
# ctrl / - komentarz zaznaczonych linijek