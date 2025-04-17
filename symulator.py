from matplotlib import pyplot as plt
#zasymulować ruch piłki
#narysować wykresy ruchu piłki
prędkość = v = 20 #m/s
waga = m = 100 #kg
położenie_początkowe = x0 = 0 #m
przyśpieszenie_ziemskie = g = -9.81 #m/s/s

def położenie_od_czasu(czas:float)->float:
    t = czas #s
    return v * t + x0 + g * 0.5 * t ** 2 #m

t_all = lista_czasów = [i*2 for i in range(21)]
lista_położeń = x_all = [położenie_od_czasu(t) for t in t_all]
print("nr","czas","położenie")
for frame in range(21):
    t_frame = t_all[frame]
    x_frame = x_all[frame]
    print(frame,t_frame,x_frame)

plt.plot(t_all, x_all)
plt.xlabel("czas t [s]")
plt.ylabel("położenie x [m]")
plt.grid()
plt.show()