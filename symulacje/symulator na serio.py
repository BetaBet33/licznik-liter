import dataclasses

from matplotlib import pyplot as plt
#zasymulować ruch piłki
#narysować wykresy ruchu piłki
prędkość_początkowa = v0 = 20 #m/s
waga = m = 100 #kg
położenie_początkowe = x0 = 0 #m
przyśpieszenie_ziemskie = g = 9.81 #m/s/s
przyśpieszenie_piłki = a = -g

@dataclasses.dataclass
class Body:
    x: float
    v: float
    m: float

def położenie_od_czasu(czas: float) -> float:
    t = czas  # s
    return v0 * t + x0 + a * 0.5 * t ** 2  # m

def prędkość_od_czasu(czas: float) -> float:
    return v0 + a * czas

t_all = lista_czasów = [i * 2 for i in range(21)]
lista_położeń = x_all = [położenie_od_czasu(t) for t in t_all]
print("nr", "czas", "położenie")
for frame in range(21):
    t_frame = t_all[frame]
    snapshot = Body(x = położenie_od_czasu(t_frame),v = prędkość_od_czasu(t_frame),m = m)
    print(frame, t_frame, snapshot)

plt.plot(t_all, x_all)
plt.xlabel("czas t [s]")
plt.ylabel("położenie x [m]")
plt.grid()
plt.savefig("wykres.png")
plt.show()