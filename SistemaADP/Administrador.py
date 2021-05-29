import xml.etree.ElementTree as ET


class Administrador:

    def __init__(self, empresa, arquivoXML="SistemaADP/admADP.xml"):

        empresa = empresa.strip().upper()

        self.__usuario, self.__senha = self.transcrever_xml_login(arquivoXML, empresa)
        
        self.__empresa = empresa


    def transcrever_xml_login(self, arquivoXML, empresa):
        with open(arquivoXML, 'r') as arquivo:
            xml = arquivo.read()
            xml = ET.fromstring(xml)

        empresas = xml.findall('adm/empresas')
        administrador = dict()
        administrador['empresa'] = [empresas[0][i].tag for i in range(len(empresas[0]))]

        for i in range(len(administrador['empresa'])):

            if administrador['empresa'][i] in empresa:
                usr = xml.findall('adm/empresas/' + administrador['empresa'][i])

                administrador['usuario'] = usr[0].find('usuario').text
                administrador['senha'] = usr[0].find('senha').text

        return administrador['usuario'], administrador['senha']


    def getUsuario(self):
        return self.__usuario


    def setUsuario(self, usuario):
        self.__usuario = usuario


    def getEmpresa(self):
        return self.__empresa


    def setEmpresa(self, empresa):
        self.__empresa = empresa


    def getSenha(self):
        return self.__senha


    def setSenha(self, senha):
        self.__senha = senha


    def getFormatoXML(self):
        '''
        :return: (string) retorna o formato do arquivo XML suportado pela classe.
        '''
        return "<adms>\n\
    <adm>\n\
        <empresas>\n\
            <MAPFRE>\n\
                <usuario></usuario>\n\
                <senha></senha>\n\
            </MAPFRE>\n\
            <BRASILSEG>\n\
                <usuario></usuario>\n\
                <senha></senha>\n\
            </BRASILSEG>\n\
        </empresas>\n\
    </adm>\n\
</adms>"
