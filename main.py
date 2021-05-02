from ADP import ADP
from Mapfre import Mapfre

chamado = ADP("Mapfre")
chamadoB = ADP("BrasilSEG")
chamadoC = Mapfre("MAPFRE SEGUROS GERAIS", 'xxx', 111)

print(type(chamado))

print(chamadoC.getEmpresa())
print(chamadoC.getUsuario())
print(chamadoC.getSenha())
