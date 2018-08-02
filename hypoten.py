#lasketaan hypotenuusa
#oletetaan, että käyttäjä osaa syöttää vain oikeita lukuja
print('Anna hypotenuusat \nensimmäinen')
a=float(input())
print('toinen')
b=float(input())
#neliöjuuri on potensiin 0.5
c=(a*a + b*b) ** 0.5
print('kantojen ', a, ' ja ', b, 'hypotenuusa on ', c)
print("The hypotenuse of a right triangle with sides", a, "and", b, "has length", round(c,3))
