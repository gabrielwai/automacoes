from ADP import ADP
from Mapfre import Mapfre

chamado = ADP("Mapfre", "xxx", "111")
chamadoB = ADP("BrasilSEG", "yyy", "222")

print(type(chamado))

print(chamadoB.getEmpresa())
print(chamadoB.getUsuario())
print(chamadoB.getSenha())
print(chamadoB.getLink())
