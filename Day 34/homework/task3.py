"""3) იმუშავეთ split-ის გამოყენებაზე: შექმენით 10 string და თითოეულზე გამოიყენეთ split ბრძანება, 
მოახდინეთ გახლეჩვა ნებისმიერი სიმბოლოთი"""


name ="giorgi wiklauri"
names = name.split()
print(names)

about ="im!15!years!old "
gio = about.split("!")
print(gio)

list1 = "phyton.html.css.java."
goa = list1.split(".")
print(goa)

sport = "football/basketball/voleyball/wrestling/boxing"
goal = sport.split("/")
print(goal)

cars = "bmw'mercedes'audi'pagani'porsche"
speed = cars.split("'")
print(speed)

contry = "georgia>usa>india>germany>italy"
word = contry.split(">")
print(word)

games = "fc25-spidermen-nba-fifa-fortnite"
game = games.split("-")
print(game)

consol = "playstationGxboxGnintendoGpc"
controler = consol.split("G")
print(controler)

phone = "iphone5xiaomi5samsung5realmi5"
brand = phone.split("5")
print(brand)

soc = "facebook?instagram?tiktok?snapchat"
socc = soc.split("?")
print(socc)