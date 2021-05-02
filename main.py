from ADP import ADP
from Colaborador import Colaborador
from Mapfre import Mapfre

ColaboradorA = Colaborador("Mapfre", "xxx", "111")
chamadoA = ADP(ColaboradorA)
ColaboradorB = Colaborador("BrasilSEG", "yyy", "222")
chamadoB = ADP(ColaboradorB)

print(type(chamadoA))

print(ColaboradorA.getEmpresa())
print(ColaboradorA.getUsuario())
print(ColaboradorA.getSenha())

print(ColaboradorA.getEmail())

print(chamadoA.getLink())

print(chamadoA.getUsuario())
print(chamadoA.getSenha())

