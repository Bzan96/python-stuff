import urllib.request
import json
import turtle
import time

url = "http://api.open-notify.org/astros.json"
url2 = "http://api.open-notify.org/iss-now.json"
response = urllib.request.urlopen(url)
response2 = urllib.request.urlopen(url2)
result = json.loads(response.read() )
result2 = json.loads(response2.read() )
print("People in Space: ", result["number"])

people = result["people"]

for p in people:
	print(p["name"]+", "+p["craft"])
	
print("\n\n\n")
	
location = result2["iss_position"]
lat = location["latitude"]
lon = location["longitude"]
print("Latitude: ", lat)
print("Longitude: ", lon)

screen = turtle.Screen()
screen.setup(720, 360)
screen.setworldcoordinates(-180, -90, 180, 90)
screen.bgpic("C:/Users/bzan9/Desktop/Python/Minigames/map.gif")

screen.register_shape("C:/Users/bzan9/Desktop/Python/Minigames/iss2.gif")
iss = turtle.Turtle()
iss.shape("C:/Users/bzan9/Desktop/Python/Minigames/iss2.gif")
iss.setheading(90)

iss.penup()
iss.goto(float(lon), float(lat) )

# Space Center, Houston
lat = 29.5502
lon = -95.097

location = turtle.Turtle()
location.penup()
location.color("yellow")
location.goto(float(lon), float(lat) )
location.dot(5)
location.hideturtle()

url = "http://api.open-notify.org/iss-pass.json"
url = url + "?lat=" + str(lat) + "&lon=" + str(lon)
response = urllib.request.urlopen(url)
result = json.loads(response.read() )

over = result["response"][1]["risetime"]
style = ("Arial", 6, "bold")
location.write(time.ctime(over), font=style)

# Stockholm
lat = 59.329323
lon = 18.068581

location = turtle.Turtle()
location.penup()
location.color("yellow")
location.goto(float(lon), float(lat) )
location.dot(5)
location.hideturtle()
location.write("Stockholm", font=style)

print(over)