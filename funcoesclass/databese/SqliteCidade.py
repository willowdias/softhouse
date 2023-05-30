import sqlite3
import time

def CreateCidade():
    db = sqlite3.connect('databese/database.db')
    cursor=db.cursor()        
    banco=cursor.executescript("""
    
    
            INSERT INTO Municipio (CODIBGE, CEP, Nome, Uf)VALUES ('1100015', '76954000', 'ALTA FLORESTA D OESTE', 'RO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)VALUES ('1100023', '76870000', 'ARIQUEMES', 'RO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)VALUES ('1100031', '76994000', 'CABIXI', 'RO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1100049', '76960000', 'CACOAL', 'RO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1100056', '76997000', 'CEREJEIRAS', 'RO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1100064', '76993000', 'COLORADO DO OESTE', 'RO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1100072', '76995000', 'CORUMBIARA', 'RO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1100080', '76937000', 'COSTA MARQUES', 'RO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1100098', '76974000', 'ESPIGAO D''OESTE', 'RO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1100106', '76850000', 'GUAJARA-MIRIM', 'RO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1100114', '76890000', 'JARU', 'RO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1100122', '76900000', 'JI-PARANA', 'RO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1100130', '76868000', 'MACHADINHO D''OESTE', 'RO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1100148', '76958000', 'NOVA BRASILANDIA D''OESTE', 'RO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1100155', '76920000', 'OURO PRETO DO OESTE', 'RO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1100189', '76970000', 'PIMENTA BUENO', 'RO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1100205', '76800000', 'PORTO VELHO', 'RO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1100254', '76916000', 'PRESIDENTE MEDICI', 'RO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1100262', '76863000', 'RIO CRESPO', 'RO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1100288', '76940000', 'ROLIM DE MOURA', 'RO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1100296', '76950000', 'SANTA LUZIA D''OESTE', 'RO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1100304', '76980000', 'VILHENA', 'RO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1100320', '76932000', 'SAO MIGUEL DO GUAPORE', 'RO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1100338', '76857000', 'NOVA MAMORE', 'RO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1100346', '76930000', 'ALVORADA D''OESTE', 'RO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1100379', '76952000', 'ALTO ALEGRE DO PARECIS', 'RO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1100403', '76862000', 'ALTO PARAISO', 'RO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1100452', '76880000', 'BURITIS', 'RO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1100502', '76956000', 'NOVO HORIZONTE DO OESTE', 'RO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1100601', '76889000', 'CACAULANDIA', 'RO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1100700', '76887000', 'CAMPO NOVO DE RONDONIA', 'RO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1100809', '76860000', 'CANDEIAS DO JAMARI', 'RO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1100908', '76948000', 'CASTANHEIRAS', 'RO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1100924', '76990000', 'CHUPINGUAIA', 'RO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1100940', '76864000', 'CUJUBIM', 'RO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1101005', '76898000', 'GOVERNADOR JORGE TEIXEIRA', 'RO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1101104', '76861000', 'ITAPUA DO OESTE', 'RO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1101203', '76919000', 'MINISTRO ANDREAZZA', 'RO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1101302', '76926000', 'MIRANTE DA SERRA', 'RO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1101401', '76888000', 'MONTE NEGRO', 'RO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1101435', '76924000', 'NOVA UNIAO', 'RO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1101450', '76979000', 'PARECIS', 'RO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1101468', '76999000', 'PIMENTEIRAS DO OESTE', 'RO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1101476', '76976000', 'PRIMAVERA DE RONDONIA', 'RO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1101484', '76977000', 'SAO FELIPE D''OESTE', 'RO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1101492', '76935000', 'SAO FRANCISCO DO GUAPORE', 'RO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1101500', '76934000', 'SERINGUEIRAS', 'RO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1101559', '76928000', 'TEIXEIROPOLIS', 'RO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1101609', '76866000', 'THEOBROMA', 'RO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1101708', '76929000', 'URUPA', 'RO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1101757', '76867000', 'VALE DO ANARI', 'RO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1101807', '76923000', 'VALE DO PARAISO', 'RO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1200013', '69945000', 'ACRELANDIA', 'AC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1200054', '69935000', 'ASSIS BRASIL', 'AC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1200104', '69932000', 'BRASILEIA', 'AC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1200138', '69923000', 'BUJARI', 'AC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1200179', '69922000', 'CAPIXABA', 'AC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1200203', '69980000', 'CRUZEIRO DO SUL', 'AC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1200252', '69934000', 'EPITACIOLANDIA', 'AC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1200302', '69960000', 'FEIJO', 'AC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1200328', '69975000', 'JORDAO', 'AC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1200336', '69990000', 'MANCIO LIMA', 'AC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1200344', '69950000', 'MANOEL URBANO', 'AC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1200351', '69983000', 'MARECHAL THAUMATURGO', 'AC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1200385', '69928000', 'PLACIDO DE CASTRO', 'AC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1200393', '69982000', 'PORTO WALTER', 'AC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1200401', '69900050', 'RIO BRANCO', 'AC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1200427', '69985000', 'RODRIGUES ALVES', 'AC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1200435', '69955000', 'SANTA ROSA DO PURUS', 'AC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1200450', '69925000', 'SENADOR GUIOMARD', 'AC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1200500', '69940000', 'SENA MADUREIRA', 'AC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1200609', '69970000', 'TARAUACA', 'AC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1200708', '69930000', 'XAPURI', 'AC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1200807', '69921000', 'PORTO ACRE', 'AC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1300029', '69475000', 'ALVARAES', 'AM');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1300060', '69620000', 'AMATURA', 'AM');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1300086', '69445000', 'ANAMA', 'AM');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1300102', '69440000', 'ANORI', 'AM');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1300144', '69265000', 'APUI', 'AM');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1300201', '69650000', 'ATALAIA DO NORTE', 'AM');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1300300', '69245000', 'AUTAZES', 'AM');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1300409', '69720000', 'BARCELOS', 'AM');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1300508', '69165000', 'BARREIRINHA', 'AM');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1300607', '69630000', 'BENJAMIN CONSTANT', 'AM');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1300631', '69430000', 'BERURI', 'AM');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1300680', '69197000', 'BOA VISTA DO RAMOS', 'AM');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1300706', '69855000', 'BOCA DO ACRE', 'AM');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1300805', '69212000', 'BORBA', 'AM');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1300839', '69410000', 'CAAPIRANGA', 'AM');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1300904', '69820000', 'CANUTAMA', 'AM');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1301001', '69500000', 'CARAUARI', 'AM');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1301100', '69250000', 'CAREIRO', 'AM');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1301159', '69255000', 'CAREIRO DA VARZEA', 'AM');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1301209', '69460000', 'COARI', 'AM');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1301308', '69452000', 'CODAJAS', 'AM');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1301407', '69880000', 'EIRUNEPE', 'AM');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1301506', '69870000', 'ENVIRA', 'AM');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1301605', '69670000', 'FONTE BOA', 'AM');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1301654', '69895000', 'GUAJARA', 'AM');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1301704', '69800000', 'HUMAITA', 'AM');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1301803', '69890000', 'IPIXUNA', 'AM');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1301852', '69405000', 'IRANDUBA', 'AM');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1301902', '69105000', 'ITACOATIARA', 'AM');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1301951', '69510000', 'ITAMARATI', 'AM');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1302009', '69120000', 'ITAPIRANGA', 'AM');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1302108', '69495000', 'JAPURA', 'AM');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1302207', '69520000', 'JURUA', 'AM');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1302306', '69660000', 'JUTAI', 'AM');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1302405', '69830000', 'LABREA', 'AM');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1302504', '69400000', 'MANACAPURU', 'AM');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1302553', '69435000', 'MANAQUIRI', 'AM');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1302603', '69005000', 'MANAUS', 'AM');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1302702', '69280000', 'MANICORE', 'AM');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1302801', '69490000', 'MARAA', 'AM');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1302900', '69193000', 'MAUES', 'AM');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1303007', '69140000', 'NHAMUNDA', 'AM');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1303106', '69230000', 'NOVA OLINDA DO NORTE', 'AM');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1303205', '69730000', 'NOVO AIRAO', 'AM');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1303304', '69260000', 'NOVO ARIPUANA', 'AM');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1303403', '69151000', 'PARINTINS', 'AM');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1303502', '69860000', 'PAUINI', 'AM');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1303536', '69736000', 'PRESIDENTE FIGUEIREDO', 'AM');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1303569', '69115000', 'RIO PRETO DA EVA', 'AM');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1303601', '69740000', 'SANTA ISABEL DO RIO NEGRO', 'AM');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1303700', '69680000', 'SANTO ANTONIO DO ICA', 'AM');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1303809', '69765000', 'SAO GABRIEL DA CACHOEIRA', 'AM');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1303908', '69610000', 'SAO PAULO DE OLIVENCA', 'AM');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1303957', '69135000', 'SAO SEBASTIAO DO UATUMA', 'AM');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1304005', '69110000', 'SILVES', 'AM');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1304062', '69640000', 'TABATINGA', 'AM');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1304104', '69480000', 'TAPAUA', 'AM');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1304203', '69470000', 'TEFE', 'AM');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1304237', '69685000', 'TONANTINS', 'AM');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1304260', '69485000', 'UARINI', 'AM');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1304302', '69130000', 'URUCARA', 'AM');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1304401', '69182000', 'URUCURITUBA', 'AM');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1400027', '69343000', 'AMAJARI', 'RR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1400050', '69350000', 'ALTO ALEGRE', 'RR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1400100', '69301000', 'BOA VISTA', 'RR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1400159', '69380000', 'BONFIM', 'RR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1400175', '69390000', 'CANTA', 'RR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1400209', '69360000', 'CARACARAI', 'RR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1400233', '69378000', 'CAROEBE', 'RR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1400282', '69348000', 'IRACEMA', 'RR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1400308', '69340000', 'MUCAJAI', 'RR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1400407', '69355000', 'NORMANDIA', 'RR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1400456', '69345000', 'PACARAIMA', 'RR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1400472', '69373000', 'RORAINOPOLIS', 'RR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1400506', '69375000', 'SAO JOAO DA BALIZA', 'RR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1400605', '69370000', 'SAO LUIZ', 'RR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1400704', '69358000', 'UIRAMUTA', 'RR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1500107', '68444000', 'ABAETETUBA', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1500131', '68527000', 'ABEL FIGUEIREDO', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1500206', '68692000', 'ACARA', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1500305', '68892000', 'AFUA', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1500347', '68533000', 'AGUA AZUL DO NORTE', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1500404', '68200000', 'ALENQUER', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1500503', '68240000', 'ALMEIRIM', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1500602', '68371000', 'ALTAMIRA', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1500701', '68810000', 'ANAJAS', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1500800', '67010000', 'ANANINDEUA', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1500859', '68365000', 'ANAPU', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1500909', '68612000', 'AUGUSTO CORREA', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1500958', '68658000', 'AURORA DO PARA', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1501006', '68160000', 'AVEIRO', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1501105', '68478000', 'BAGRE', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1501204', '68468000', 'BAIAO', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1501253', '68388000', 'BANNACH', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1501303', '68448000', 'BARCARENA', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1501402', '66010000', 'BELEM', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1501451', '68143000', 'BELTERRA', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1501501', '68797000', 'BENEVIDES', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1501576', '68525000', 'BOM JESUS DO TOCANTINS', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1501600', '68645000', 'BONITO', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1501709', '68608000', 'BRAGANCA', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1501725', '68148000', 'BRASIL NOVO', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1501758', '68522000', 'BREJO GRANDE DO ARAGUAIA', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1501782', '68488000', 'BREU BRANCO', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1501808', '68803000', 'BREVES', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1501907', '68672000', 'BUJARU', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1501956', '68617000', 'CACHOEIRA DO PIRIA', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1502004', '68848000', 'CACHOEIRA DO ARARI', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1502103', '68404000', 'CAMETA', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1502152', '68537000', 'CANAA DOS CARAJAS', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1502202', '68700005', 'CAPANEMA', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1502301', '68650000', 'CAPITAO POCO', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1502400', '68740005', 'CASTANHAL', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1502509', '68885000', 'CHAVES', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1502608', '68785000', 'COLARES', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1502707', '68540000', 'CONCEICAO DO ARAGUAIA', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1502756', '68685000', 'CONCORDIA DO PARA', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1502764', '68398000', 'CUMARU DO NORTE', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1502772', '68523000', 'CURIONOPOLIS', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1502806', '68818000', 'CURRALINHO', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1502855', '68210000', 'CURUA', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1502905', '68751000', 'CURUCA', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1502939', '68633000', 'DOM ELISEU', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1502954', '68524000', 'ELDORADO DOS CARAJAS', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1503002', '68280000', 'FARO', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1503044', '68543000', 'FLORESTA DO ARAGUAIA', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1503077', '68665000', 'GARRAFAO DO NORTE', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1503093', '68639000', 'GOIANESIA DO PARA', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1503101', '68310000', 'GURUPA', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1503200', '68726000', 'IGARAPE-ACU', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1503309', '68438000', 'IGARAPE-MIRI', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1503408', '68772000', 'INHANGAPI', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1503457', '68637000', 'IPIXUNA DO PARA', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1503507', '68655000', 'IRITUIA', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1503606', '68180005', 'ITAITUBA', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1503705', '68580000', 'ITUPIRANGA', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1503754', '68195000', 'JACAREACANGA', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1503804', '68590000', 'JACUNDA', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1503903', '68170000', 'JURUTI', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1504000', '68415000', 'LIMOEIRO DO AJURU', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1504059', '68675000', 'MAE DO RIO', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1504109', '68723000', 'MAGALHAES BARATA', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1504208', '68500005', 'MARABA', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1504307', '68712000', 'MARACANA', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1504406', '68764000', 'MARAPANIM', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1504422', '67200000', 'MARITUBA', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1504455', '68145000', 'MEDICILANDIA', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1504505', '68495000', 'MELGACO', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1504604', '68428000', 'MOCAJUBA', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1504703', '68453000', 'MOJU', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1504802', '68220000', 'MONTE ALEGRE', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1504901', '68828000', 'MUANA', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1504950', '68618000', 'NOVA ESPERANCA DO PIRIA', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1504976', '68585000', 'NOVA IPIXUNA', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1505007', '68732000', 'NOVA TIMBOTEUA', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1505031', '68193000', 'NOVO PROGRESSO', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1505064', '68473000', 'NOVO REPARTIMENTO', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1505106', '68260000', 'OBIDOS', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1505205', '68470000', 'OEIRAS DO PARA', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1505304', '68270000', 'ORIXIMINA', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1505403', '68642000', 'OUREM', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1505437', '68394000', 'OURILANDIA DO NORTE', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1505486', '68485000', 'PACAJA', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1505494', '68535000', 'PALESTINA DO PARA', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1505502', '68625005', 'PARAGOMINAS', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1505536', '68516000', 'PARAUAPEBAS', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1505551', '68545000', 'PAU D''ARCO', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1505601', '68735000', 'PEIXE-BOI', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1505635', '68575000', 'PICARRA', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1505650', '68138000', 'PLACAS', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1505700', '68835000', 'PONTA DE PEDRAS', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1505809', '68482000', 'PORTEL', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1505908', '68340000', 'PORTO DE MOZ', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1506005', '68135000', 'PRAINHA', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1506104', '68708000', 'PRIMAVERA', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1506112', '68709000', 'QUATIPURU', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1506138', '68550005', 'REDENCAO', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1506161', '68530000', 'RIO MARIA', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1506187', '68638000', 'RONDON DO PARA', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1506195', '68165000', 'RUROPOLIS', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1506203', '68721000', 'SALINOPOLIS', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1506302', '68862000', 'SALVATERRA', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1506351', '68798000', 'SANTA BARBARA DO PARA', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1506401', '68850000', 'SANTA CRUZ DO ARARI', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1506500', '68792000', 'SANTA ISABEL DO PARA', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1506559', '68644000', 'SANTA LUZIA DO PARA', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1506583', '68568000', 'SANTA MARIA DAS BARREIRAS', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1506609', '68738000', 'SANTA MARIA DO PARA', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1506708', '68560000', 'SANTANA DO ARAGUAIA', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1506807', '68005000', 'SANTAREM', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1506906', '68720000', 'SANTAREM NOVO', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1507003', '68787000', 'SANTO ANTONIO DO TAUA', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1507102', '68776000', 'SAO CAETANO DE ODIVELAS', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1507151', '68520000', 'SAO DOMINGOS DO ARAGUAIA', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1507201', '68636000', 'SAO DOMINGOS DO CAPIM', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1507300', '68380000', 'SAO FELIX DO XINGU', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1507409', '68749000', 'SAO FRANCISCO DO PARA', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1507458', '68570000', 'SAO GERALDO DO ARAGUAIA', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1507466', '68774000', 'SAO JOAO DA PONTA', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1507474', '68719000', 'SAO JOAO DE PIRABAS', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1507508', '68519000', 'SAO JOAO DO ARAGUAIA', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1507607', '68661000', 'SAO MIGUEL DO GUAMA', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1507706', '68820000', 'SAO SEBASTIAO DA BOA VISTA', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1507755', '68548000', 'SAPUCAIA', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1507805', '68360000', 'SENADOR JOSE PORFIRIO', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1507904', '68875000', 'SOURE', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1507953', '68695000', 'TAILANDIA', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1507961', '68773000', 'TERRA ALTA', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1507979', '68285000', 'TERRA SANTA', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1508001', '68680000', 'TOME-ACU', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1508035', '68647000', 'TRACUATEUA', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1508050', '68198000', 'TRAIRAO', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1508084', '68385000', 'TUCUMA', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1508100', '68455005', 'TUCURUI', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1508126', '68632000', 'ULIANOPOLIS', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1508159', '68140000', 'URUARA', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1508209', '68782000', 'VIGIA', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1508308', '68624000', 'VISEU', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1508357', '68383000', 'VITORIA DO XINGU', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1508407', '68555005', 'XINGUARA', 'PA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1600055', '68914000', 'SERRA DO NAVIO', 'AP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1600105', '68958000', 'AMAPA', 'AP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1600154', '68948000', 'PEDRA BRANCA DO AMAPARI', 'AP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1600204', '68965000', 'CALCOENE', 'AP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1600212', '68973000', 'CUTIAS', 'AP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1600238', '68917000', 'FERREIRA GOMES', 'AP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1600253', '68976000', 'ITAUBAL', 'AP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1600279', '68923000', 'LARANJAL DO JARI', 'AP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1600303', '68900010', 'MACAPA', 'AP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1600402', '68943000', 'MAZAGAO', 'AP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1600501', '68985000', 'OIAPOQUE', 'AP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1600535', '68997000', 'PORTO GRANDE', 'AP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1600550', '68918000', 'PRACUUBA', 'AP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1600600', '68939000', 'SANTANA', 'AP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1600709', '68994000', 'TARTARUGALZINHO', 'AP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1600808', '68924000', 'VITORIA DO JARI', 'AP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1700251', '77693000', 'ABREULANDIA', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1700301', '77908000', 'AGUIARNOPOLIS', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1700350', '77455000', 'ALIANCA DO TOCANTINS', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1700400', '77310000', 'ALMAS', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1700707', '77480000', 'ALVORADA', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1701002', '77890000', 'ANANAS', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1701051', '77905000', 'ANGICO', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1701101', '77620000', 'APARECIDA DO RIO NEGRO', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1701309', '77845000', 'ARAGOMINAS', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1701903', '77690000', 'ARAGUACEMA', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1702000', '77475000', 'ARAGUACU', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1702109', '77803010', 'ARAGUAINA', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1702158', '77855000', 'ARAGUANA', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1702208', '77953000', 'ARAGUATINS', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1702307', '77780000', 'ARAPOEMA', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1702406', '77333000', 'ARRAIAS', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1702554', '77960000', 'AUGUSTINOPOLIS', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1702703', '77325000', 'AURORA DO TOCANTINS', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1702901', '77930000', 'AXIXA DO TOCANTINS', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1703008', '77870000', 'BABACULANDIA', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1703057', '77783000', 'BANDEIRANTES DO TOCANTINS', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1703073', '77765000', 'BARRA DO OURO', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1703107', '77665000', 'BARROLANDIA', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1703206', '77755000', 'BERNARDO SAYAO', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1703305', '77714000', 'BOM JESUS DO TOCANTINS', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1703602', '77735000', 'BRASILANDIA DO TOCANTINS', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1703701', '77560000', 'BREJINHO DE NAZARE', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1703800', '77995000', 'BURITI DO TOCANTINS', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1703826', '77915000', 'CACHOEIRINHA', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1703842', '77777000', 'CAMPOS LINDOS', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1703867', '77453000', 'CARIRI DO TOCANTINS', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1703883', '77840000', 'CARMOLANDIA', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1703891', '77985000', 'CARRASCO BONITO', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1703909', '77683000', 'CASEARA', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1704105', '77723000', 'CENTENARIO', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1704600', '77575000', 'CHAPADA DE AREIA', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1705102', '77378000', 'CHAPADA DA NATIVIDADE', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1705508', '77760000', 'COLINAS DO TOCANTINS', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1705557', '77350000', 'COMBINADO', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1705607', '77305000', 'CONCEICAO DO TOCANTINS', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1706001', '77750000', 'COUTO DE MAGALHAES', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1706100', '77490000', 'CRISTALANDIA', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1706258', '77463000', 'CRIXAS DO TOCANTINS', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1706506', '77910000', 'DARCINOPOLIS', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1707009', '77300000', 'DIANOPOLIS', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1707108', '77670000', 'DIVINOPOLIS DO TOCANTINS', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1707207', '77685000', 'DOIS IRMAOS DO TOCANTINS', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1707306', '77485000', 'DUERE', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1707405', '77993000', 'ESPERANTINA', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1707553', '77555000', 'FATIMA', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1707652', '77465000', 'FIGUEIROPOLIS', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1707702', '77795000', 'FILADELFIA', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1708205', '77470000', 'FORMOSO DO ARAGUAIA', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1708254', '77708000', 'FORTALEZA DO TABOCAO', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1708304', '77695000', 'GOIANORTE', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1709005', '77774000', 'GOIATINS', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1709302', '77702000', 'GUARAI', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1709500', '77402010', 'GURUPI', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1709807', '77553000', 'IPUEIRAS', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1710508', '77720000', 'ITACAJA', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1710706', '77920000', 'ITAGUATINS', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1710904', '77718000', 'ITAPIRATINS', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1711100', '77740000', 'ITAPORA DO TOCANTINS', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1711506', '77450000', 'JAU DO TOCANTINS', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1711803', '77753000', 'JUARINA', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1711902', '77493000', 'LAGOA DA CONFUSAO', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1711951', '77613000', 'LAGOA DO TOCANTINS', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1712009', '77645000', 'LAJEADO', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1712157', '77328000', 'LAVANDEIRA', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1712405', '77630000', 'LIZARDA', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1712454', '77903000', 'LUZINOPOLIS', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1712504', '77675000', 'MARIANOPOLIS DO TOCANTINS', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1712702', '77593000', 'MATEIROS', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1712801', '77918000', 'MAURILANDIA DO TOCANTINS', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1713205', '77650000', 'MIRACEMA DO TOCANTINS', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1713304', '77660000', 'MIRANORTE', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1713601', '77585000', 'MONTE DO CARMO', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1713700', '77673000', 'MONTE SANTO DO TOCANTINS', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1713809', '77913000', 'PALMEIRAS DO TOCANTINS', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1713957', '77850000', 'MURICILANDIA', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1714203', '77373000', 'NATIVIDADE', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1714302', '77898000', 'NAZARE', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1714880', '77790000', 'NOVA OLINDA', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1715002', '77495000', 'NOVA ROSALANDIA', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1715101', '77610000', 'NOVO ACORDO', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1715150', '77353000', 'NOVO ALEGRE', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1715259', '77318000', 'NOVO JARDIM', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1715507', '77558000', 'OLIVEIRA DE FATIMA', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1715705', '77798000', 'PALMEIRANTE', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1715754', '77365000', 'PALMEIROPOLIS', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1716109', '77600000', 'PARAISO DO TOCANTINS', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1716208', '77360000', 'PARANA', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1716307', '77785000', 'PAU D''ARCO', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1716505', '77712000', 'PEDRO AFONSO', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1716604', '77460000', 'PEIXE', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1716653', '77730000', 'PEQUIZEIRO', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1716703', '77725000', 'COLMEIA', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1717008', '77380000', 'PINDORAMA DO TOCANTINS', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1717206', '77888000', 'PIRAQUE', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1717503', '77570000', 'PIUM', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1717800', '77315000', 'PONTE ALTA DO BOM JESUS', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1717909', '77590000', 'PONTE ALTA DO TOCANTINS', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1718006', '77395000', 'PORTO ALEGRE DO TOCANTINS', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1718204', '77500000', 'PORTO NACIONAL', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1718303', '77970000', 'PRAIA NORTE', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1718402', '77748000', 'PRESIDENTE KENNEDY', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1718451', '77603000', 'PUGMIL', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1718501', '77733000', 'RECURSOLANDIA', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1718550', '77893000', 'RIACHINHO', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1718659', '77303000', 'RIO DA CONCEICAO', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1718709', '77655000', 'RIO DOS BOIS', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1718758', '77635000', 'RIO SONO', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1718808', '77980000', 'SAMPAIO', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1718840', '77478000', 'SANDOLANDIA', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1718865', '77848000', 'SANTA FE DO ARAGUAIA', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1718881', '77716000', 'SANTA MARIA DO TOCANTINS', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1718899', '77565000', 'SANTA RITA DO TOCANTINS', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1718907', '77375000', 'SANTA ROSA DO TOCANTINS', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1719004', '77615000', 'SANTA TEREZA DO TOCANTINS', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1720002', '77885000', 'SANTA TEREZINHA DO TOCANTINS', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1720101', '77958000', 'SAO BENTO DO TOCANTINS', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1720150', '77605000', 'SAO FELIX DO TOCANTINS', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1720200', '77925000', 'SAO MIGUEL DO TOCANTINS', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1720259', '77368000', 'SAO SALVADOR DO TOCANTINS', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1720309', '77990000', 'SAO SEBASTIAO DO TOCANTINS', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1720499', '77393000', 'SAO VALERIO DA NATIVIDADE', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1720655', '77580000', 'SILVANOPOLIS', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1720804', '77940000', 'SITIO NOVO DO TOCANTINS', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1720853', '77458000', 'SUCUPIRA', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1720903', '77320000', 'TAGUATINGA', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1720937', '77308000', 'TAIPAS DO TOCANTINS', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1720978', '77483000', 'TALISMA', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1721000', '77001002', 'PALMAS', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1721109', '77640000', 'TOCANTINIA', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1721208', '77900000', 'TOCANTINOPOLIS', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1721257', '77704000', 'TUPIRAMA', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1721307', '77743000', 'TUPIRATINS', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1722081', '77860000', 'WANDERLANDIA', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('1722107', '77880000', 'XAMBIOA', 'TO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2100055', '65930000', 'ACAILANDIA', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2100105', '65505000', 'AFONSO CUNHA', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2100154', '65578000', 'AGUA DOCE DO MARANHAO', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2100204', '65253000', 'ALCANTARA', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2100303', '65610000', 'ALDEIAS ALTAS', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2100402', '65310000', 'ALTAMIRA DO MARANHAO', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2100436', '65413000', 'ALTO ALEGRE DO MARANHAO', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2100477', '65398000', 'ALTO ALEGRE DO PINDARE', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2100501', '65815000', 'ALTO PARNAIBA', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2100550', '65293000', 'AMAPA DO MARANHAO', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2100600', '65923000', 'AMARANTE DO MARANHAO', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2100709', '65493000', 'ANAJATUBA', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2100808', '65525000', 'ANAPURUS', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2100832', '65275000', 'APICUM-ACU', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2100873', '65368000', 'ARAGUANA', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2100907', '65575000', 'ARAIOSES', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2100956', '65945000', 'ARAME', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2101004', '65483000', 'ARARI', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2101103', '65108000', 'AXIXA', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2101202', '65700000', 'BACABAL', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2101251', '65103000', 'BACABEIRA', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2101301', '65270000', 'BACURI', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2101350', '65233000', 'BACURITUBA', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2101400', '65800000', 'BALSAS', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2101509', '65660000', 'BARAO DE GRAJAU', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2101608', '65955000', 'BARRA DO CORDA', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2101707', '65590000', 'BARREIRINHAS', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2101731', '65535000', 'BELAGUA', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2101772', '65335000', 'BELA VISTA DO MARANHAO', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2101806', '65885000', 'BENEDITO LEITE', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2101905', '65248000', 'BEQUIMAO', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2101939', '65723000', 'BERNARDO DO MEARIM', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2101970', '65292000', 'BOA VISTA DO GURUPI', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2102002', '65380000', 'BOM JARDIM', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2102036', '65395000', 'BOM JESUS DAS SELVAS', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2102077', '65704000', 'BOM LUGAR', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2102101', '65520000', 'BREJO', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2102150', '65315000', 'BREJO DE AREIA', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2102200', '65515000', 'BURITI', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2102309', '65688000', 'BURITI BRAVO', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2102325', '65393000', 'BURITICUPU', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2102358', '65935500', 'BURITIRANA', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2102374', '65165000', 'CACHOEIRA GRANDE', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2102408', '65230000', 'CAJAPIO', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2102507', '65211000', 'CAJARI', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2102556', '65968000', 'CAMPESTRE DO MARANHAO', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2102606', '65281000', 'CANDIDO MENDES', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2102705', '65465000', 'CANTANHEDE', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2102754', '65735000', 'CAPINZAL DO NORTE', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2102804', '65980000', 'CAROLINA', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2102903', '65298000', 'CARUTAPERA', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2103000', '65600010', 'CAXIAS', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2103109', '65260000', 'CEDRAL', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2103125', '65267000', 'CENTRAL DO MARANHAO', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2103158', '65288000', 'CENTRO DO GUILHERME', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2103174', '65299000', 'CENTRO NOVO DO MARANHAO', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2103208', '65500000', 'CHAPADINHA', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2103257', '65921000', 'CIDELANDIA', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2103307', '65405000', 'CODO', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2103406', '65620000', 'COELHO NETO', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2103505', '65690000', 'COLINAS', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2103554', '65340000', 'CONCEICAO DO LAGO-ACU', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2103604', '65415000', 'COROATA', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2103703', '65268000', 'CURURUPU', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2103752', '65927000', 'DAVINOPOLIS', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2103802', '65765000', 'DOM PEDRO', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2103901', '65625000', 'DUQUE BACELAR', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2104008', '65750000', 'ESPERANTINOPOLIS', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2104057', '65975000', 'ESTREITO', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2104073', '65995000', 'FEIRA NOVA DO MARANHAO', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2104081', '65964000', 'FERNANDO FALCAO', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2104099', '65943000', 'FORMOSA DA SERRA NEGRA', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2104107', '65805000', 'FORTALEZA DOS NOGUEIRAS', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2104206', '65695000', 'FORTUNA', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2104305', '65287000', 'GODOFREDO VIANA', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2104404', '65775000', 'GONCALVES DIAS', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2104503', '65770000', 'GOVERNADOR ARCHER', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2104552', '65928000', 'GOVERNADOR EDISON LOBAO', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2104602', '65780000', 'GOVERNADOR EUGENIO BARROS', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2104628', '65795000', 'GOVERNADOR LUIZ ROCHA', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2104651', '65363000', 'GOVERNADOR NEWTON BELLO', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2104677', '65284000', 'GOVERNADOR NUNES FREIRE', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2104701', '65785000', 'GRACA ARANHA', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2104800', '65940000', 'GRAJAU', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2104909', '65255000', 'GUIMARAES', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2105005', '65180000', 'HUMBERTO DE CAMPOS', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2105104', '65175000', 'ICATU', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2105153', '65345000', 'IGARAPE DO MEIO', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2105203', '65720000', 'IGARAPE GRANDE', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2105302', '65900010', 'IMPERATRIZ', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2105351', '65948000', 'ITAIPAVA DO GRAJAU', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2105401', '65485000', 'ITAPECURU MIRIM', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2105427', '65939000', 'ITINGA DO MARANHAO', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2105450', '65693000', 'JATOBA', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2105476', '65962000', 'JENIPAPO DOS VIEIRAS', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2105500', '65922000', 'JOAO LISBOA', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2105609', '65755000', 'JOSELANDIA', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2105658', '65294000', 'JUNCO DO MARANHAO', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2105708', '65715000', 'LAGO DA PEDRA', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2105807', '65710000', 'LAGO DO JUNCO', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2105906', '65705000', 'LAGO VERDE', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2105922', '65683000', 'LAGOA DO MATO', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2105948', '65712000', 'LAGO DOS RODRIGUES', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2105963', '65718000', 'LAGOA GRANDE DO MARANHAO', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2105989', '65937000', 'LAJEADO NOVO', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2106003', '65728000', 'LIMA CAMPOS', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2106102', '65895000', 'LORETO', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2106201', '65290000', 'LUIS DOMINGUES', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2106300', '65565000', 'MAGALHAES DE ALMEIDA', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2106326', '65289000', 'MARACACUME', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2106359', '65714000', 'MARAJA DO SENA', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2106375', '65283000', 'MARANHAOZINHO', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2106409', '65510000', 'MATA ROMA', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2106508', '65218000', 'MATINHA', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2106607', '65645000', 'MATOES', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2106631', '65468000', 'MATOES DO NORTE', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2106672', '65545000', 'MILAGRES DO MARANHAO', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2106706', '65855000', 'MIRADOR', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2106755', '65495000', 'MIRANDA DO NORTE', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2106805', '65265000', 'MIRINZAL', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2106904', '65360000', 'MONCAO', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2107001', '65936000', 'MONTES ALTOS', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2107100', '65160000', 'MORROS', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2107209', '65450000', 'NINA RODRIGUES', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2107258', '65808000', 'NOVA COLINAS', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2107308', '65880000', 'NOVA IORQUE', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2107357', '65274000', 'NOVA OLINDA DO MARANHAO', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2107407', '65706000', 'OLHO D''AGUA DAS CUNHAS', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2107456', '65223000', 'OLINDA NOVA DO MARANHAO', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2107506', '65130000', 'PACO DO LUMIAR', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2107605', '65238000', 'PALMEIRANDIA', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2107704', '65670000', 'PARAIBANO', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2107803', '65643000', 'PARNARAMA', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2107902', '65680000', 'PASSAGEM FRANCA', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2108009', '65875000', 'PASTOS BONS', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2108058', '65585000', 'PAULINO NEVES', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2108108', '65716000', 'PAULO RAMOS', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2108207', '65726000', 'PEDREIRAS', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2108256', '65206000', 'PEDRO DO ROSARIO', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2108306', '65213000', 'PENALVA', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2108405', '65245000', 'PERI MIRIM', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2108454', '65418000', 'PERITORO', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2108504', '65375000', 'PINDARE MIRIM', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2108603', '65202000', 'PINHEIRO', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2108702', '65707000', 'PIO XII', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2108801', '65460000', 'PIRAPEMAS', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2108900', '65740000', 'POCAO DE PEDRAS', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2109007', '65970000', 'PORTO FRANCO', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2109056', '65263000', 'PORTO RICO DO MARANHAO', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2109106', '65760000', 'PRESIDENTE DUTRA', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2109205', '65140000', 'PRESIDENTE JUSCELINO', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2109239', '65279000', 'PRESIDENTE MEDICI', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2109270', '65204000', 'PRESIDENTE SARNEY', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2109304', '65455000', 'PRESIDENTE VARGAS', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2109403', '65190000', 'PRIMEIRA CRUZ', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2109452', '65138000', 'RAPOSA', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2109502', '65990000', 'RIACHAO', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2109551', '65938000', 'RIBAMAR FIQUENE', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2109601', '65100000', 'ROSARIO', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2109700', '65830000', 'SAMBAIBA', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2109759', '65768000', 'SANTA FILOMENA DO MARANHAO', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2109809', '65209000', 'SANTA HELENA', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2109908', '65300000', 'SANTA INES', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2110005', '65390000', 'SANTA LUZIA', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2110039', '65272000', 'SANTA LUZIA DO PARUA', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2110104', '65540000', 'SANTA QUITERIA DO MARANHAO', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2110203', '65105000', 'SANTA RITA', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2110237', '65555000', 'SANTANA DO MARANHAO', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2110278', '65195000', 'SANTO AMARO DO MARANHAO', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2110302', '65730000', 'SANTO ANTONIO DOS LOPES', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2110401', '65440000', 'SAO BENEDITO DO RIO PRETO', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2110500', '65235000', 'SAO BENTO', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2110609', '65550000', 'SAO BERNARDO', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2110658', '65888000', 'SAO DOMINGOS DO AZEITAO', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2110708', '65790000', 'SAO DOMINGOS DO MARANHAO', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2110807', '65890000', 'SAO FELIX DE BALSAS', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2110856', '65929000', 'SAO FRANCISCO DO BREJAO', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2110906', '65658000', 'SAO FRANCISCO DO MARANHAO', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2111003', '65225000', 'SAO JOAO BATISTA', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2111029', '65385000', 'SAO JOAO DO CARU', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2111052', '65973000', 'SAO JOAO DO PARAISO', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2111078', '65615000', 'SAO JOAO DO SOTER', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2111102', '65665000', 'SAO JOAO DOS PATOS', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2111201', '65115000', 'SAO JOSE DE RIBAMAR', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2111250', '65762000', 'SAO JOSE DOS BASILIOS', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2111300', '65005402', 'SAO LUIS', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2111409', '65708000', 'SAO LUIS GONZAGA DO MARANHAO', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2111508', '65470000', 'SAO MATEUS DO MARANHAO', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2111532', '65920000', 'SAO PEDRO DA AGUA BRANCA', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2111573', '65978000', 'SAO PEDRO DOS CRENTES', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2111607', '65840000', 'SAO RAIMUNDO DAS MANGABEIRAS', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2111631', '65753000', 'SAO RAIMUNDO DO DOCA BEZERRA', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2111672', '65758000', 'SAO ROBERTO', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2111706', '65220000', 'SAO VICENTE FERRER', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2111722', '65709000', 'SATUBINHA', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2111748', '65783000', 'SENADOR ALEXANDRE COSTA', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2111763', '65935000', 'SENADOR LA ROCQUE', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2111789', '65269000', 'SERRANO DO MARANHAO', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2111805', '65925000', 'SITIO NOVO', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2111904', '65860000', 'SUCUPIRA DO NORTE', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2111953', '65668000', 'SUCUPIRA DO RIACHAO', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2112001', '65820000', 'TASSO FRAGOSO', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2112100', '65420000', 'TIMBIRAS', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2112209', '65630020', 'TIMON', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2112233', '65727000', 'TRIZIDELA DO VALE', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2112274', '65378000', 'TUFILANDIA', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2112308', '65764000', 'TUNTUM', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2112407', '65278000', 'TURIACU', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2112456', '65276000', 'TURILANDIA', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2112506', '65582000', 'TUTOIA', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2112605', '65530000', 'URBANO SANTOS', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2112704', '65430000', 'VARGEM GRANDE', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2112803', '65215000', 'VIANA', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2112852', '65924000', 'VILA NOVA DOS MARTIRIOS', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2112902', '65355000', 'VITORIA DO MEARIM', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2113009', '65320000', 'VITORINO FREIRE', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2114007', '65365000', 'ZE DOCA', 'MA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2200053', '64748000', 'ACAUA', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2200103', '64440000', 'AGRICOLANDIA', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2200202', '64460000', 'AGUA BRANCA', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2200251', '64655000', 'ALAGOINHA DO PIAUI', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2200277', '64675000', 'ALEGRETE DO PIAUI', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2200301', '64360000', 'ALTO LONGA', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2200400', '64290000', 'ALTOS', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2200459', '64923000', 'ALVORADA DO GURGUEIA', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2200509', '64400000', 'AMARANTE', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2200608', '64410000', 'ANGICAL DO PIAUI', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2200707', '64780000', 'ANISIO DE ABREU', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2200806', '64855000', 'ANTONIO ALMEIDA', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2200905', '64310000', 'AROAZES', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2201002', '64480000', 'ARRAIAL', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2201051', '64333000', 'ASSUNCAO DO PIAUI', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2201101', '64965000', 'AVELINO LOPES', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2201150', '64868000', 'BAIXA GRANDE DO RIBEIRO', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2201176', '64528000', 'BARRA D''ALCANTARA', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2201200', '64100000', 'BARRAS', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2201309', '64990000', 'BARREIRAS DO PIAUI', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2201408', '64455000', 'BARRO DURO', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2201507', '64190000', 'BATALHA', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2201556', '64705000', 'BELA VISTA DO PIAUI', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2201572', '64678000', 'BELEM DO PIAUI', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2201606', '64380000', 'BENEDITINOS', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2201705', '64870000', 'BERTOLINIA', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2201739', '64753000', 'BETANIA DO PIAUI', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2201770', '64108000', 'BOA HORA', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2201804', '64630000', 'BOCAINA', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2201903', '64900000', 'BOM JESUS', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2201919', '64225000', 'BOM PRINCIPIO DO PIAUI', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2201929', '64775000', 'BONFIM DO PIAUI', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2201945', '64283000', 'BOQUEIRAO DO PIAUI', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2201960', '64265000', 'BRASILEIRA', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2201988', '64895000', 'BREJO DO PIAUI', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2202000', '64230000', 'BURITI DOS LOPES', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2202026', '64345000', 'BURITI DOS MONTES', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2202059', '64105000', 'CABECEIRAS DO PIAUI', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2202075', '64514000', 'CAJAZEIRAS DO PIAUI', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2202083', '64222000', 'CAJUEIRO DA PRAIA', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2202091', '64695000', 'CALDEIRAO GRANDE DO PIAUI', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2202109', '64730000', 'CAMPINAS DO PIAUI', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2202117', '64767000', 'CAMPO ALEGRE DO FIDALGO', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2202133', '64578000', 'CAMPO GRANDE DO PIAUI', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2202174', '64148000', 'CAMPO LARGO DO PIAUI', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2202208', '64280000', 'CAMPO MAIOR', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2202251', '64833000', 'CANAVIEIRA', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2202307', '64890000', 'CANTO DO BURITI', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2202406', '64270000', 'CAPITAO DE CAMPOS', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2202455', '64763000', 'CAPITAO GERVASIO OLIVEIRA', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2202505', '64795000', 'CARACOL', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2202539', '64233000', 'CARAUBAS DO PIAUI', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2202554', '64590000', 'CARIDADE DO PIAUI', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2202604', '64340000', 'CASTELO DO PIAUI', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2202653', '64228000', 'CAXINGO', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2202703', '64235000', 'COCAL', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2202711', '64278000', 'COCAL DE TELHA', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2202729', '64238000', 'COCAL DOS ALVES', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2202737', '64335000', 'COIVARAS', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2202752', '64885000', 'COLONIA DO GURGUEIA', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2202778', '64516000', 'COLONIA DO PIAUI', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2202802', '64740000', 'CONCEICAO DO CANINDE', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2202851', '64793000', 'CORONEL JOSE DIAS', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2202901', '64980000', 'CORRENTE', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2203008', '64995000', 'CRISTALANDIA DO PIAUI', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2203107', '64920000', 'CRISTINO CASTRO', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2203206', '64960000', 'CURIMATA', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2203230', '64905000', 'CURRAIS', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2203255', '64453000', 'CURRALINHOS', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2203271', '64595000', 'CURRAL NOVO DO PIAUI', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2203305', '64390000', 'DEMERVAL LOBAO', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2203354', '64785000', 'DIRCEU ARCOVERDE', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2203404', '64620000', 'DOM EXPEDITO LOPES', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2203420', '64250000', 'DOMINGOS MOURAO', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2203453', '64790000', 'DOM INOCENCIO', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2203503', '64325000', 'ELESBAO VELOSO', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2203602', '64880000', 'ELISEU MARTINS', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2203701', '64180000', 'ESPERANTINA', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2203750', '64788000', 'FARTURA DO PIAUI', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2203800', '64815000', 'FLORES DO PIAUI', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2203859', '64563000', 'FLORESTA DO PIAUI', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2203909', '64800000', 'FLORIANO', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2204006', '64520000', 'FRANCINOPOLIS', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2204105', '64475000', 'FRANCISCO AYRES', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2204154', '64683000', 'FRANCISCO MACEDO', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2204204', '64645000', 'FRANCISCO SANTOS', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2204303', '64690000', 'FRONTEIRAS', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2204352', '64613000', 'GEMINIANO', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2204402', '64930000', 'GILBUES', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2204501', '64840000', 'GUADALUPE', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2204550', '64798000', 'GUARIBAS', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2204600', '64470000', 'HUGO NAPOLEAO', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2204659', '64224000', 'ILHA GRANDE', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2204709', '64535000', 'INHUMA', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2204808', '64540000', 'IPIRANGA DO PIAUI', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2204907', '64570000', 'ISAIAS COELHO', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2205003', '64565000', 'ITAINOPOLIS', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2205102', '64820000', 'ITAUEIRA', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2205151', '64755000', 'JACOBINA DO PIAUI', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2205201', '64575000', 'JAICOS', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2205250', '64495000', 'JARDIM DO MULATO', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2205276', '64275000', 'JATOBA DO PIAUI', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2205300', '64830000', 'JERUMENHA', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2205359', '64765000', 'JOAO COSTA', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2205409', '64170000', 'JOAQUIM PIRES', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2205458', '64165000', 'JOCA MARQUES', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2205508', '64110000', 'JOSE DE FREITAS', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2205516', '64343000', 'JUAZEIRO DO PIAUI', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2205524', '64963000', 'JULIO BORGES', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2205532', '64782000', 'JUREMA', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2205540', '64465000', 'LAGOINHA DO PIAUI', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2205557', '64138000', 'LAGOA ALEGRE', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2205565', '64768000', 'LAGOA DO BARRO DO PIAUI', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2205573', '64258000', 'LAGOA DE SAO FRANCISCO', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2205581', '64388000', 'LAGOA DO PIAUI', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2205599', '64308000', 'LAGOA DO SITIO', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2205607', '64850000', 'LANDRI SALES', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2205706', '64220000', 'LUIS CORREIA', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2205805', '64160000', 'LUZILANDIA', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2205854', '64168000', 'MADEIRO', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2205904', '64875000', 'MANOEL EMIDIO', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2205953', '64685000', 'MARCOLANDIA', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2206001', '64845000', 'MARCOS PARENTE', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2206050', '64573000', 'MASSAPE DO PIAUI', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2206100', '64150000', 'MATIAS OLIMPIO', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2206209', '64130000', 'MIGUEL ALVES', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2206308', '64445000', 'MIGUEL LEAO', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2206357', '64253000', 'MILTON BRANDAO', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2206407', '64450000', 'MONSENHOR GIL', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2206506', '64650000', 'MONSENHOR HIPOLITO', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2206605', '64940000', 'MONTE ALEGRE DO PIAUI', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2206654', '64968000', 'MORRO CABECA NO TEMPO', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2206670', '64178000', 'MORRO DO CHAPEU DO PIAUI', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2206696', '64175000', 'MURICI DOS PORTELAS', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2206704', '64825000', 'NAZARE DO PIAUI', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2206753', '64288000', 'NOSSA SENHORA DE NAZARE', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2206803', '64140000', 'NOSSA SENHORA DOS REMEDIOS', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2206902', '64530000', 'NOVO ORIENTE DO PIAUI', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2206951', '64365000', 'NOVO SANTO ANTONIO', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2207009', '64500000', 'OEIRAS', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2207108', '64468000', 'OLHO D''AGUA DO PIAUI', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2207207', '64680000', 'PADRE MARCOS', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2207306', '64710000', 'PAES LANDIM', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2207355', '64898000', 'PAJEU DO PIAUI', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2207405', '64925000', 'PALMEIRA DO PIAUI', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2207504', '64420000', 'PALMEIRAIS', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2207553', '64618000', 'PAQUETA', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2207603', '64970000', 'PARNAGUA', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2207702', '64200010', 'PARNAIBA', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2207751', '64395000', 'PASSAGEM FRANCA DO PIAUI', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2207777', '64580000', 'PATOS DO PIAUI', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2207801', '64750000', 'PAULISTANA', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2207850', '64838000', 'PAVUSSU', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2207900', '64255000', 'PEDRO II', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2207934', '64728000', 'PEDRO LAURENTINO', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2207959', '64764000', 'NOVA SANTA RITA', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2208007', '64600000', 'PICOS', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2208106', '64320000', 'PIMENTEIRAS', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2208205', '64660000', 'PIO IX', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2208304', '64240000', 'PIRACURUCA', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2208403', '64260000', 'PIRIPIRI', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2208502', '64145000', 'PORTO', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2208551', '64858000', 'PORTO ALEGRE DO PIAUI', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2208601', '64370000', 'PRATA DO PIAUI', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2208650', '64758000', 'QUEIMADA NOVA', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2208700', '64915000', 'REDENCAO DO GURGUEIA', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2208809', '64490000', 'REGENERACAO', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2208858', '64975000', 'RIACHO FRIO', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2208874', '64725000', 'RIBEIRA DO PIAUI', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2208908', '64865000', 'RIBEIRO GONCALVES', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2209005', '64835000', 'RIO GRANDE DO PIAUI', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2209104', '64545000', 'SANTA CRUZ DO PIAUI', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2209153', '64315000', 'SANTA CRUZ DOS MILAGRES', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2209203', '64945000', 'SANTA FILOMENA', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2209302', '64910000', 'SANTA LUZ', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2209351', '64615000', 'SANTANA DO PIAUI', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2209377', '64518000', 'SANTA ROSA DO PIAUI', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2209401', '64640000', 'SANTO ANTONIO DE LISBOA', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2209450', '64438000', 'SANTO ANTONIO DOS MILAGRES', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2209500', '64560000', 'SANTO INACIO DO PIAUI', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2209559', '64783000', 'SAO BRAZ DO PIAUI', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2209609', '64375000', 'SAO FELIX DO PIAUI', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2209658', '64745000', 'SAO FRANCISCO DE ASSIS DO PIAUI', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2209708', '64550000', 'SAO FRANCISCO DO PIAUI', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2209757', '64993000', 'SAO GONCALO DO GURGUEIA', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2209807', '64435000', 'SAO GONCALO DO PIAUI', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2209856', '64635000', 'SAO JOAO DA CANABRAVA', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2209872', '64243000', 'SAO JOAO DA FRONTEIRA', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2209906', '64350000', 'SAO JOAO DA SERRA', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2209955', '64510000', 'SAO JOAO DA VARJOTA', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2209971', '64155000', 'SAO JOAO DO ARRAIAL', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2210003', '64760000', 'SAO JOAO DO PIAUI', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2210052', '64245000', 'SAO JOSE DO DIVINO', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2210102', '64555000', 'SAO JOSE DO PEIXE', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2210201', '64625000', 'SAO JOSE DO PIAUI', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2210300', '64670000', 'SAO JULIAO', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2210359', '64778000', 'SAO LOURENCO DO PIAUI', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2210375', '64638000', 'SAO LUIS DO PIAUI', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2210383', '64378000', 'SAO MIGUEL DA BAIXA GRANDE', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2210391', '64558000', 'SAO MIGUEL DO FIDALGO', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2210409', '64330000', 'SAO MIGUEL DO TAPUIO', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2210508', '64430000', 'SAO PEDRO DO PIAUI', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2210607', '64770000', 'SAO RAIMUNDO NONATO', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2210623', '64985000', 'SEBASTIAO BARROS', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2210631', '64873000', 'SEBASTIAO LEAL', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2210656', '64285000', 'SIGEFREDO PACHECO', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2210706', '64585000', 'SIMOES', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2210805', '64700000', 'SIMPLICIO MENDES', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2210904', '64720000', 'SOCORRO DO PIAUI', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2210938', '64610000', 'SUSSUAPARA', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2210953', '64893000', 'TAMBORIL DO PIAUI', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2210979', '64512000', 'TANQUE DO PIAUI', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2211001', '64000010', 'TERESINA', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2211100', '64120000', 'UNIAO', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2211209', '64860000', 'URUCUI', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2211308', '64300000', 'VALENCA DO PIAUI', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2211357', '64773000', 'VARZEA BRANCA', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2211407', '64525000', 'VARZEA GRANDE', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2211506', '64568000', 'VERA MENDES', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2211605', '64688000', 'VILA NOVA DO PIAUI', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2211704', '64548000', 'WALL FERRAZ', 'PI');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2300101', '63245000', 'ABAIARA', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2300150', '62785000', 'ACARAPE', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2300200', '62585000', 'ACARAU', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2300309', '63567000', 'ACOPIARA', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2300408', '63578000', 'AIUABA', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2300507', '62125000', 'ALCANTARAS', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2300606', '63198000', 'ALTANEIRA', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2300705', '62975000', 'ALTO SANTO', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2300754', '62548000', 'AMONTADA', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2300804', '63573000', 'ANTONINA DO NORTE', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2300903', '62638000', 'APUIARES', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2301000', '61753000', 'AQUIRAZ', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2301109', '62807500', 'ARACATI', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2301208', '62754100', 'ARACOIABA', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2301257', '62213000', 'ARARENDA', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2301307', '63176000', 'ARARIPE', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2301406', '62762000', 'ARATUBA', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2301505', '63670000', 'ARNEIROZ', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2301604', '63143000', 'ASSARE', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2301703', '63370000', 'AURORA', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2301802', '63320000', 'BAIXIO', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2301851', '63962000', 'BANABUIU', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2301901', '63183000', 'BARBALHA', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2301950', '62795000', 'BARREIRA', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2302008', '63383000', 'BARRO', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2302057', '62414000', 'BARROQUINHA', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2302107', '62760000', 'BATURITE', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2302206', '62843000', 'BEBERIBE', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2302305', '62575000', 'BELA CRUZ', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2302404', '63880000', 'BOA VIAGEM', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2302503', '63268000', 'BREJO SANTO', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2302602', '62405000', 'CAMOCIM', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2302701', '63151000', 'CAMPOS SALES', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2302800', '62705000', 'CANINDE', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2302909', '62748000', 'CAPISTRANO', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2303006', '62734000', 'CARIDADE', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2303105', '62186000', 'CARIRE', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2303204', '63225000', 'CARIRIACU', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2303303', '63538000', 'CARIUS', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2303402', '62375000', 'CARNAUBAL', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2303501', '62852000', 'CASCAVEL', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2303600', '63595000', 'CATARINA', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2303659', '62297000', 'CATUNDA', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2303709', '61600004', 'CAUCAIA', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2303808', '62878500', 'CEDRO', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2303907', '62425000', 'CHAVAL', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2303931', '63957000', 'CHORO', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2303956', '62878000', 'CHOROZINHO', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2304004', '62165000', 'COREAU', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2304103', '63715000', 'CRATEUS', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2304202', '63100005', 'CRATO', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2304236', '62269000', 'CROATA', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2304251', '62603000', 'CRUZ', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2304269', '63645000', 'DEPUTADO IRAPUAN PINHEIRO', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2304277', '63470000', 'ERERE', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2304285', '61760000', 'EUSEBIO', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2304301', '63189000', 'FARIAS BRITO', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2304350', '62115000', 'FORQUILHA', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2304400', '60010000', 'FORTALEZA', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2304459', '62817000', 'FORTIM', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2304509', '62340000', 'FRECHEIRINHA', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2304608', '62738000', 'GENERAL SAMPAIO', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2304657', '62365000', 'GRACA', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2304707', '62435000', 'GRANJA', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2304806', '63230000', 'GRANJEIRO', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2304905', '62190000', 'GROAIRAS', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2304954', '61895000', 'GUAIUBA', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2305001', '62382000', 'GUARACIABA DO NORTE', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2305100', '62768000', 'GUARAMIRANGA', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2305209', '62273000', 'HIDROLANDIA', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2305233', '62882000', 'HORIZONTE', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2305266', '63984000', 'IBARETAMA', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2305308', '62363000', 'IBIAPINA', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2305332', '62955000', 'IBICUITINGA', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2305357', '62814000', 'ICAPUI', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2305407', '63440000', 'ICO', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2305506', '63512000', 'IGUATU', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2305605', '63641000', 'INDEPENDENCIA', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2305654', '62218000', 'IPAPORANGA', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2305704', '63345000', 'IPAUMIRIM', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2305803', '62253000', 'IPU', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2305902', '62240000', 'IPUEIRAS', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2306009', '62988000', 'IRACEMA', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2306108', '62623000', 'IRAUCUBA', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2306207', '62820000', 'ITAICABA', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2306256', '61887000', 'ITAITINGA', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2306306', '62602000', 'ITAPAGE', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2306405', '62508000', 'ITAPIPOCA', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2306504', '62742000', 'ITAPIUNA', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2306553', '62592000', 'ITAREMA', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2306603', '62723000', 'ITATIRA', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2306702', '63480000', 'JAGUARETAMA', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2306801', '63495000', 'JAGUARIBARA', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2306900', '63479000', 'JAGUARIBE', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2307007', '62835000', 'JAGUARUANA', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2307106', '63295000', 'JARDIM', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2307205', '63275000', 'JATI', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2307254', '62598000', 'JIJOCA DE JERICOACOARA', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2307304', '63010000', 'JUAZEIRO DO NORTE', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2307403', '63582000', 'JUCAS', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2307502', '63305000', 'LAVRAS DA MANGABEIRA', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2307601', '62935000', 'LIMOEIRO DO NORTE', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2307635', '63865000', 'MADALENA', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2307650', '61900005', 'MARACANAU', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2307700', '61965000', 'MARANGUAPE', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2307809', '62565000', 'MARCO', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2307908', '62450000', 'MARTINOPOLE', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2308005', '62142000', 'MASSAPE', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2308104', '63212000', 'MAURITI', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2308203', '62132000', 'MERUOCA', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2308302', '63255000', 'MILAGRES', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2308351', '63637000', 'MILHA', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2308377', '62533000', 'MIRAIMA', 'CE');

            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2308401', '63208000', 'MISSAO VELHA', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2308500', '63615000', 'MOMBACA', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2308609', '63785000', 'MONSENHOR TABOSA', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2308708', '62951000', 'MORADA NOVA', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2308807', '62485000', 'MORAUJO', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2308906', '62550000', 'MORRINHOS', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2309003', '62175000', 'MUCAMBO', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2309102', '63606000', 'MULUNGU', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2309201', '63165000', 'NOVA OLINDA', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2309300', '62203000', 'NOVA RUSSAS', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2309409', '62759100', 'NOVO ORIENTE', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2309458', '62759000', 'OCARA', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2309508', '63528000', 'OROS', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2309607', '62872000', 'PACAJUS', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2309706', '61860000', 'PACATUBA', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2309805', '62772000', 'PACOTI', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2309904', '62180000', 'PACUJA', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2310001', '62913000', 'PALHANO', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2310100', '62784000', 'PALMACIA', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2310209', '62682000', 'PARACURU', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2310258', '62686000', 'PARAIPABA', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2310308', '63685000', 'PARAMBU', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2310407', '62736000', 'PARAMOTI', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2310506', '63632000', 'PEDRA BRANCA', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2310605', '63280000', 'PENAFORTE', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2310704', '62645000', 'PENTECOSTE', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2310803', '63465000', 'PEREIRO', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2310852', '62860000', 'PINDORETAMA', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2310902', '63608000', 'PIQUET CARNEIRO', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2310951', '62259000', 'PIRES FERREIRA', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2311009', '62225000', 'PORANGA', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2311108', '63270000', 'PORTEIRAS', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2311207', '63163000', 'POTENGI', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2311231', '62995000', 'POTIRETAMA', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2311264', '63655000', 'QUITERIANOPOLIS', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2311306', '63920000', 'QUIXADA', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2311355', '63515000', 'QUIXELO', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2311405', '63810000', 'QUIXERAMOBIM', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2311504', '62922000', 'QUIXERE', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2311603', '62791000', 'REDENCAO', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2311702', '62263000', 'RERIUTABA', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2311801', '62905000', 'RUSSAS', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2311900', '63592000', 'SABOEIRO', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2311959', '63157000', 'SALITRE', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2312007', '62154000', 'SANTANA DO ACARAU', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2312106', '63193000', 'SANTANA DO CARIRI', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2312205', '62290000', 'SANTA QUITERIA', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2312304', '62374000', 'SAO BENEDITO', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2312403', '62674000', 'SAO GONCALO DO AMARANTE', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2312502', '62965000', 'SAO JOAO DO JAGUARIBE', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2312601', '62665000', 'SAO LUIS DO CURU', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2312700', '63601000', 'SENADOR POMPEU', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2312809', '62475000', 'SENADOR SA', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2312908', '62010000', 'SOBRAL', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2313005', '63625000', 'SOLONOPOLE', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2313104', '62964000', 'TABULEIRO DO NORTE', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2313203', '63770000', 'TAMBORIL', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2313252', '63145000', 'TARRAFAS', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2313302', '63662000', 'TAUA', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2313351', '62614000', 'TEJUCUOCA', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2313401', '62328000', 'TIANGUA', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2313500', '62692000', 'TRAIRI', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2313559', '62657000', 'TURURU', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2313609', '62352000', 'UBAJARA', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2313708', '63315000', 'UMARI', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2313757', '62664000', 'UMIRIM', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2313807', '62652000', 'URUBURETAMA', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2313906', '62468000', 'URUOCA', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2313955', '62265000', 'VARJOTA', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2314003', '63545000', 'VARZEA ALEGRE', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2314102', '62305000', 'VICOSA DO CEARA', 'CE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2400109', '59370000', 'ACARI', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2400208', '59650000', 'ACU', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2400307', '59510000', 'AFONSO BEZERRA', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2400406', '59995000', 'AGUA NOVA', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2400505', '59965000', 'ALEXANDRIA', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2400604', '59760000', 'ALMINO AFONSO', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2400703', '59507000', 'ALTO DO RODRIGUES', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2400802', '59515000', 'ANGICOS', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2400901', '59870000', 'ANTONIO MARTINS', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2401008', '59700000', 'APODI', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2401107', '59655000', 'AREIA BRANCA', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2401206', '59170000', 'ARES', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2401305', '59680000', 'AUGUSTO SEVERO', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2401404', '59194000', 'BAIA FORMOSA', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2401453', '59695000', 'BARAUNA', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2401503', '59410000', 'BARCELONA', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2401602', '59558000', 'BENTO FERNANDES', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2401651', '59528000', 'BODO', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2401701', '59270000', 'BOM JESUS', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2401800', '59219000', 'BREJINHO', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2401859', '59592000', 'CAICARA DO NORTE', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2401909', '59540000', 'CAICARA DO RIO DO VENTO', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2402006', '59300000', 'CAICO', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2402105', '59230000', 'CAMPO REDONDO', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2402204', '59190000', 'CANGUARETAMA', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2402303', '59785000', 'CARAUBAS', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2402402', '59374000', 'CARNAUBA DOS DANTAS', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2402501', '59665000', 'CARNAUBAIS', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2402600', '59570000', 'CEARA-MIRIM', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2402709', '59395000', 'CERRO CORA', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2402808', '59220000', 'CORONEL EZEQUIEL', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2402907', '59930000', 'CORONEL JOAO PESSOA', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2403004', '59375000', 'CRUZETA', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2403103', '59380000', 'CURRAIS NOVOS', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2403202', '59910000', 'DOUTOR SEVERIANO', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2403251', '59150000', 'PARNAMIRIM', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2403301', '59905000', 'ENCANTO', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2403400', '59355000', 'EQUADOR', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2403509', '59660000', 'ESPIRITO SANTO', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2403608', '59575000', 'EXTREMOZ', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2403707', '59795000', 'FELIPE GUERRA', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2403756', '59517000', 'FERNANDO PEDROZA', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2403806', '59335000', 'FLORANIA', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2403905', '59902000', 'FRANCISCO DANTAS', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2404002', '59890000', 'FRUTUOSO GOMES', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2404101', '59596000', 'GALINHOS', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2404200', '59173000', 'GOIANINHA', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2404309', '59790000', 'GOVERNADOR DIX-SEPT ROSADO', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2404408', '59675000', 'GROSSOS', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2404507', '59598000', 'GUAMARE', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2404606', '59490000', 'IELMO MARINHO', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2404705', '59508000', 'IPANGUACU', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2404804', '59315000', 'IPUEIRA', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2404853', '59513000', 'ITAJA', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2404903', '59855000', 'ITAU', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2405009', '59225000', 'JACANA', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2405108', '59594000', 'JANDAIRA', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2405207', '59690000', 'JANDUIS', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2405306', '59265000', 'JANUARIO CICCO', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2405405', '59213000', 'JAPI', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2405504', '59544000', 'JARDIM DE ANGICOS', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2405603', '59324000', 'JARDIM DE PIRANHAS', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2405702', '59343000', 'JARDIM DO SERIDO', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2405801', '59550000', 'JOAO CAMARA', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2405900', '59885000', 'JOAO DIAS', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2406007', '59985000', 'JOSE DA PENHA', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2406106', '59330000', 'JUCURUTU', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2406205', '59227000', 'LAGOA D''ANTA', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2406304', '59244000', 'LAGOA DE PEDRAS', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2406403', '59430000', 'LAGOA DE VELHOS', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2406502', '59390000', 'LAGOA NOVA', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2406601', '59247000', 'LAGOA SALGADA', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2406700', '59538000', 'LAJES', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2406809', '59235000', 'LAJES PINTADAS', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2406908', '59805000', 'LUCRECIA', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2407005', '59943000', 'LUIS GOMES', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2407104', '59280000', 'MACAIBA', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2407203', '59500000', 'MACAU', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2407252', '59945000', 'MAJOR SALES', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2407302', '59970000', 'MARCELINO VIEIRA', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2407401', '59803000', 'MARTINS', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2407500', '59580000', 'MAXARANGUAPE', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2407609', '59775000', 'MESSIAS TARGINO', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2407708', '59198000', 'MONTANHAS', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2407807', '59182000', 'MONTE ALEGRE', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2407906', '59217000', 'MONTE DAS GAMELEIRAS', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2408003', '59600005', 'MOSSORO', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2408102', '59010000', 'NATAL', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2408201', '59164000', 'NISIA FLORESTA', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2408300', '59215000', 'NOVA CRUZ', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2408409', '59730000', 'OLHO-D''AGUA DO BORGES', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2408508', '59347000', 'OURO BRANCO', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2408607', '59950000', 'PARANA', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2408805', '59586000', 'PARAZINHO', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2408904', '59360000', 'PARELHAS', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2408953', '59578000', 'RIO DO FOGO', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2409100', '59218000', 'PASSA E FICA', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2409209', '59259000', 'PASSAGEM', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2409308', '59770000', 'PATU', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2409332', '59464000', 'SANTA MARIA', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2409407', '59900000', 'PAU DOS FERROS', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2409506', '59588000', 'PEDRA GRANDE', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2409605', '59547000', 'PEDRA PRETA', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2409704', '59530000', 'PEDRO AVELINO', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2409803', '59196000', 'PEDRO VELHO', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2409902', '59504000', 'PENDENCIAS', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2410009', '59960000', 'PILOES', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2410108', '59560000', 'POCO BRANCO', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2410207', '59810000', 'PORTALEGRE', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2410256', '59668000', 'PORTO DO MANGUE', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2410306', '59245000', 'PRESIDENTE JUSCELINO', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2410405', '59582000', 'PUREZA', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2410504', '59990000', 'RAFAEL FERNANDES', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2410603', '59740000', 'RAFAEL GODEIRO', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2410702', '59820000', 'RIACHO DA CRUZ', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2410801', '59987000', 'RIACHO DE SANTANA', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2410900', '59470000', 'RIACHUELO', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2411007', '59830000', 'RODOLFO FERNANDES', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2411056', '59678000', 'TIBAU', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2411106', '59420000', 'RUY BARBOSA', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2411205', '59200000', 'SANTA CRUZ', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2411403', '59522000', 'SANTANA DO MATOS', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2411429', '59350000', 'SANTANA DO SERIDO', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2411502', '59255000', 'SANTO ANTONIO', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2411601', '59590000', 'SAO BENTO DO NORTE', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2411700', '59210000', 'SAO BENTO DO TRAIRI', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2411809', '59327000', 'SAO FERNANDO', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2411908', '59908000', 'SAO FRANCISCO DO OESTE', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2412005', '59299000', 'SAO GONCALO DO AMARANTE', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2412104', '59310000', 'SAO JOAO DO SABUGI', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2412203', '59162000', 'SAO JOSE DE MIPIBU', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2412302', '59275500', 'SAO JOSE DO CAMPESTRE', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2412401', '59378000', 'SAO JOSE DO SERIDO', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2412500', '59920000', 'SAO MIGUEL', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2412559', '59585000', 'SAO MIGUEL DE TOUROS', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2412609', '59460000', 'SAO PAULO DO POTENGI', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2412708', '59480000', 'SAO PEDRO', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2412807', '59518000', 'SAO RAFAEL', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2412906', '59400000', 'SAO TOME', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2413003', '59340000', 'SAO VICENTE', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2413102', '59250000', 'SENADOR ELOI DE SOUZA', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2413201', '59168000', 'SENADOR GEORGINO AVELINO', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2413300', '59214000', 'SERRA DE SAO BENTO', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2413359', '59663000', 'SERRA DO MEL', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2413409', '59318000', 'SERRA NEGRA DO NORTE', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2413508', '59258000', 'SERRINHA', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2413557', '59808000', 'SERRINHA DOS PINTOS', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2413607', '59856000', 'SEVERIANO MELO', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2413706', '59445000', 'SITIO NOVO', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2413805', '59840000', 'TABOLEIRO GRANDE', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2413904', '59568000', 'TAIPU', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2414001', '59242000', 'TANGARA', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2414100', '59958000', 'TENENTE ANANIAS', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2414159', '59338000', 'TENENTE LAURENTINO CRUZ', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2414209', '59178000', 'TIBAU DO SUL', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2414308', '59320000', 'TIMBAUBA DOS BATISTAS', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2414407', '59584000', 'TOUROS', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2414456', '59685000', 'TRIUNFO POTIGUAR', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2414506', '59865000', 'UMARIZAL', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2414605', '59670000', 'UPANEMA', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2414704', '59187000', 'VARZEA', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2414753', '59925000', 'VENHA-VER', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2414803', '59184000', 'VERA CRUZ', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2414902', '59815000', 'VICOSA', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2415008', '59192000', 'VILA FLOR', 'RN');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2500106', '58748000', 'AGUA BRANCA', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2500205', '58778000', 'AGUIAR', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2500304', '58388000', 'ALAGOA GRANDE', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2500403', '58125000', 'ALAGOA NOVA', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2500502', '58390000', 'ALAGOINHA', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2500536', '58460000', 'ALCANTIL', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2500577', '58399000', 'ALGODAO DE JANDAIRA', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2500601', '58320000', 'ALHANDRA', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2500700', '58913000', 'SAO JOAO DO RIO DO PEIXE', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2500734', '58548000', 'AMPARO', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2500775', '58823000', 'APARECIDA', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2500809', '58270000', 'ARACAGI', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2500908', '58396000', 'ARARA', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2501005', '58233000', 'ARARUNA', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2501104', '58397500', 'AREIA', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2501153', '58732000', 'AREIA DE BARAUNAS', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2501203', '58140000', 'AREIAL', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2501302', '58489000', 'AROEIRAS', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2501351', '58685000', 'ASSUNCAO', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2501401', '58295000', 'BAIA DA TRAICAO', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2501500', '58222000', 'BANANEIRAS', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2501534', '58188000', 'BARAUNA', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2501575', '58458000', 'BARRA DE SANTANA', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2501609', '58170000', 'BARRA DE SANTA ROSA', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2501708', '58483000', 'BARRA DE SAO MIGUEL', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2501807', '58305003', 'BAYEUX', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2501906', '58257000', 'BELEM', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2502003', '58895000', 'BELEM DO BREJO DO CRUZ', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2502052', '58922000', 'BERNARDINO BATISTA', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2502102', '58993000', 'BOA VENTURA', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2502151', '58123000', 'BOA VISTA', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2502201', '58930000', 'BOM JESUS', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2502300', '58156000', 'BOM SUCESSO', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2502409', '58960000', 'BONITO DE SANTA FE', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2502508', '58450000', 'BOQUEIRAO', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2502607', '58775000', 'IGARACY', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2502706', '58394000', 'BORBOREMA', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2502805', '58890000', 'BREJO DO CRUZ', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2502904', '58880000', 'BREJO DOS SANTOS', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2503001', '58327000', 'CAAPORA', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2503100', '58480000', 'CABACEIRAS', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2503209', '58310000', 'CABEDELO', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2503308', '58937000', 'CACHOEIRA DOS INDIOS', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2503407', '58730000', 'CACIMBA DE AREIA', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2503506', '58230000', 'CACIMBA DE DENTRO', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2503555', '58698000', 'CACIMBAS', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2503605', '58253000', 'CAICARA', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2503704', '58905000', 'CAJAZEIRAS', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2503753', '58855000', 'CAJAZEIRINHAS', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2503803', '58350000', 'CALDAS BRANDAO', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2503902', '58533000', 'CAMALAU', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2504009', '58400000', 'CAMPINA GRANDE', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2504033', '58287000', 'CAPIM', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2504074', '58595000', 'CARAUBAS', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2504108', '58945000', 'CARRAPATEIRA', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2504157', '58238000', 'CASSERENGUE', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2504207', '58718000', 'CATINGUEIRA', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2504306', '58885000', 'CATOLE DO ROCHA', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2504355', '58455000', 'CATURITE', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2504405', '58975000', 'CONCEICAO', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2504504', '58714000', 'CONDADO', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2504603', '58322000', 'CONDE', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2504702', '58535000', 'CONGO', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2504801', '58770000', 'COREMAS', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2504850', '58588000', 'COXIXOLA', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2504900', '58337000', 'CRUZ DO ESPIRITO SANTO', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2505006', '58167000', 'CUBATI', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2505105', '58176000', 'CUITE', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2505204', '58208000', 'CUITEGI', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2505238', '58289000', 'CUITE DE MAMANGUAPE', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2505279', '58291000', 'CURRAL DE CIMA', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2505303', '58990000', 'CURRAL VELHO', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2505352', '58173000', 'DAMIAO', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2505402', '58695000', 'DESTERRO', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2505501', '58710000', 'VISTA SERRANA', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2505600', '58997000', 'DIAMANTE', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2505709', '58228000', 'DONA INES', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2505808', '58265000', 'DUAS ESTRADAS', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2505907', '58763000', 'EMAS', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2506004', '58135000', 'ESPERANCA', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2506103', '58487000', 'FAGUNDES', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2506202', '58195000', 'FREI MARTINHO', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2506251', '58492000', 'GADO BRAVO', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2506301', '58205000', 'GUARABIRA', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2506400', '58356000', 'GURINHEM', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2506509', '58670000', 'GURJAO', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2506608', '58983000', 'IBIARA', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2506707', '58745000', 'IMACULADA', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2506806', '58380000', 'INGA', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2506905', '58364000', 'ITABAIANA', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2507002', '58780000', 'ITAPORANGA', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2507101', '58275000', 'ITAPOROROCA', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2507200', '58378000', 'ITATUBA', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2507309', '58278000', 'JACARAU', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2507408', '58830000', 'JERICO', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2507507', '58010000', 'JOAO PESSOA', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2507606', '58387000', 'JUAREZ TAVORA', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2507705', '58660000', 'JUAZEIRINHO', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2507804', '58640000', 'JUNCO DO SERIDO', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2507903', '58330000', 'JURIPIRANGA', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2508000', '58750000', 'JURU', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2508109', '58835000', 'LAGOA', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2508208', '58250000', 'LAGOA DE DENTRO', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2508307', '58117000', 'LAGOA SECA', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2508406', '58820000', 'LASTRO', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2508505', '58690000', 'LIVRAMENTO', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2508554', '58254000', 'LOGRADOURO', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2508604', '58315000', 'LUCENA', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2508703', '58740000', 'MAE D''AGUA', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2508802', '58713000', 'MALTA', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2508901', '58286000', 'MAMANGUAPE', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2509008', '58996000', 'MANAIRA', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2509057', '58294000', 'MARCACAO', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2509107', '58345000', 'MARI', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2509156', '58819000', 'MARIZOPOLIS', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2509206', '58120000', 'MASSARANDUBA', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2509305', '58293000', 'MATARACA', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2509339', '58128000', 'MATINHAS', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2509370', '58832000', 'MATO GROSSO', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2509396', '58737000', 'MATUREIA', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2509404', '58375000', 'MOGEIRO', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2509503', '58145000', 'MONTADAS', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2509602', '58950000', 'MONTE HOREBE', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2509701', '58500000', 'MONTEIRO', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2509800', '58354000', 'MULUNGU', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2509909', '58494000', 'NATUBA', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2510006', '58817000', 'NAZAREZINHO', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2510105', '58178000', 'NOVA FLORESTA', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2510204', '58798000', 'NOVA OLINDA', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2510303', '58184000', 'NOVA PALMEIRA', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2510402', '58760000', 'OLHO D''AGUA', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2510501', '58160000', 'OLIVEDOS', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2510600', '58560000', 'OURO VELHO', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2510659', '58575000', 'PARARI', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2510709', '58734000', 'PASSAGEM', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2510808', '58700002', 'PATOS', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2510907', '58860000', 'PAULISTA', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2511004', '58790000', 'PEDRA BRANCA', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2511103', '58180000', 'PEDRA LAVRADA', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2511202', '58328000', 'PEDRAS DE FOGO', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2511301', '58765000', 'PIANCO', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2511400', '58187000', 'PICUI', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2511509', '58338000', 'PILAR', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2511608', '58393000', 'PILOES', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2511707', '58210000', 'PILOEZINHOS', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2511806', '58213000', 'PIRPIRITUBA', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2511905', '58324000', 'PITIMBU', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2512002', '58152000', 'POCINHOS', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2512036', '58933000', 'POCO DANTAS', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2512077', '58908000', 'POCO DE JOSE DE MOURA', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2512101', '58850000', 'POMBAL', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2512200', '58550000', 'PRATA', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2512309', '58755000', 'PRINCESA ISABEL', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2512408', '58115000', 'PUXINANA', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2512507', '58475000', 'QUEIMADAS', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2512606', '58733000', 'QUIXABA', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2512705', '58398000', 'REMIGIO', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2512721', '58273000', 'PEDRO REGIS', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2512747', '58235000', 'RIACHAO', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2512754', '58382000', 'RIACHAO DO BACAMARTE', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2512762', '58348000', 'RIACHAO DO POCO', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2512788', '58465000', 'RIACHO DE SANTO ANTONIO', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2512804', '58870000', 'RIACHO DOS CAVALOS', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2512903', '58299000', 'RIO TINTO', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2513000', '58650000', 'SALGADINHO', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2513109', '58370000', 'SALGADO DE SAO FELIX', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2513158', '58463000', 'SANTA CECILIA', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2513208', '58826000', 'SANTA CRUZ', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2513307', '58925000', 'SANTA HELENA', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2513356', '58978000', 'SANTA INES', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2513406', '58600000', 'SANTA LUZIA', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2513505', '58985000', 'SANTANA DE MANGUEIRA', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2513604', '58795000', 'SANTANA DOS GARROTES', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2513653', '58928000', 'SANTAREM', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2513703', '58300010', 'SANTA RITA', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2513802', '58720000', 'SANTA TERESINHA', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2513851', '58675000', 'SANTO ANDRE', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2513901', '58857000', 'SAO BENTO', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2513943', '58485000', 'SAO DOMINGOS DO CARIRI', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2513968', '58853000', 'SAO DOMINGOS DE POMBAL', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2513984', '58818000', 'SAO FRANCISCO', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2514008', '58590000', 'SAO JOAO DO CARIRI', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2514107', '58525000', 'SAO JOAO DO TIGRE', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2514206', '58815000', 'SAO JOSE DA LAGOA TAPADA', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2514305', '58784000', 'SAO JOSE DE CAIANA', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2514404', '58723000', 'SAO JOSE DE ESPINHARAS', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2514453', '58339000', 'SAO JOSE DOS RAMOS', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2514503', '58940000', 'SAO JOSE DE PIRANHAS', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2514552', '58758000', 'SAO JOSE DE PRINCESA', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2514602', '58725000', 'SAO JOSE DO BONFIM', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2514651', '58893000', 'SAO JOSE DO BREJO DO CRUZ', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2514701', '58610000', 'SAO JOSE DO SABUGI', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2514800', '58570000', 'SAO JOSE DOS CORDEIROS', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2514909', '58625000', 'SAO MAMEDE', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2515005', '58334000', 'SAO MIGUEL DE TAIPU', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2515104', '58119000', 'SAO SEBASTIAO DE LAGOA DE ROCA', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2515203', '58510000', 'SAO SEBASTIAO DO UMBUZEIRO', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2515302', '58340000', 'SAPE', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2515401', '58159000', 'SERIDO', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2515500', '58586000', 'SERRA BRANCA', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2515609', '58260000', 'SERRA DA RAIZ', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2515708', '58955000', 'SERRA GRANDE', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2515807', '58385000', 'SERRA REDONDA', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2515906', '58395000', 'SERRARIA', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2515930', '58268000', 'SERTAOZINHO', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2515971', '58342000', 'SOBRADO', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2516003', '58225000', 'SOLANEA', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2516102', '58155000', 'SOLEDADE', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2516151', '58177000', 'SOSSEGO', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2516201', '58800005', 'SOUSA', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2516300', '58545000', 'SUME', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2516409', '58240000', 'CAMPO DE SANTANA', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2516508', '58680000', 'TAPEROA', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2516607', '58753000', 'TAVARES', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2516706', '58735000', 'TEIXEIRA', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2516755', '58665000', 'TENORIO', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2516805', '58920000', 'TRIUNFO', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2516904', '58916000', 'UIRAUNA', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2517001', '58497000', 'UMBUZEIRO', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2517100', '58620000', 'VARZEA', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2517209', '58822000', 'VIEIROPOLIS', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2517407', '58515000', 'ZABELE', 'PB');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2600054', '53510000', 'ABREU E LIMA', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2600104', '56800000', 'AFOGADOS DA INGAZEIRA', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2600203', '56365000', 'AFRANIO', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2600302', '55498000', 'AGRESTINA', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2600401', '55550000', 'AGUA PRETA', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2600500', '55340000', 'AGUAS BELAS', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2600609', '55265000', 'ALAGOINHA', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2600708', '55896000', 'ALIANCA', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2600807', '55493000', 'ALTINHO', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2600906', '55515000', 'AMARAJI', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2601003', '55430000', 'ANGELIM', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2601052', '53690000', 'ARACOIABA', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2601102', '56284000', 'ARARIPINA', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2601201', '56503000', 'ARCOVERDE', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2601300', '55690000', 'BARRA DE GUABIRABA', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2601409', '55564000', 'BARREIROS', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2601508', '55445000', 'BELEM DE MARIA', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2601607', '56450000', 'BELEM DE SAO FRANCISCO', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2601706', '55155000', 'BELO JARDIM', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2601805', '56680000', 'BETANIA', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2601904', '55662000', 'BEZERROS', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2602001', '56228000', 'BODOCO', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2602100', '55336000', 'BOM CONSELHO', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2602209', '55735000', 'BOM JARDIM', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2602308', '55685000', 'BONITO', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2602407', '55325000', 'BREJAO', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2602506', '56740000', 'BREJINHO', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2602605', '55175000', 'BREJO DA MADRE DE DEUS', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2602704', '55845000', 'BUENOS AIRES', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2602803', '56537000', 'BUIQUE', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2602902', '54505000', 'CABO DE SANTO AGOSTINHO', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2603009', '56180000', 'CABROBO', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2603108', '55383000', 'CACHOEIRINHA', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2603207', '55360000', 'CAETES', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2603306', '55375000', 'CALCADO', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2603405', '56930000', 'CALUMBI', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2603454', '54753000', 'CAMARAGIBE', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2603504', '55665000', 'CAMOCIM DE SAO FELIX', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2603603', '55930000', 'CAMUTANGA', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2603702', '55425000', 'CANHOTINHO', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2603801', '55365000', 'CAPOEIRAS', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2603900', '56825000', 'CARNAIBA', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2603926', '56420000', 'CARNAUBEIRA DA PENHA', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2604007', '55813010', 'CARPINA', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2604106', '55002000', 'CARUARU', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2604155', '55759000', 'CASINHAS', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2604205', '55402000', 'CATENDE', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2604304', '56130000', 'CEDRO', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2604403', '55835000', 'CHA DE ALEGRIA', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2604502', '55636000', 'CHA GRANDE', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2604601', '55940000', 'CONDADO', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2604700', '55317000', 'CORRENTES', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2604809', '55525000', 'CORTES', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2604908', '55658000', 'CUMARU', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2605004', '55465000', 'CUPIRA', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2605103', '56660000', 'CUSTODIA', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2605152', '56355000', 'DORMENTES', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2605202', '55505000', 'ESCADA', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2605301', '56245000', 'EXU', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2605400', '55715000', 'FEIRA NOVA', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2605459', '53990000', 'FERNANDO DE NORONHA', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2605509', '55880000', 'FERREIROS', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2605608', '56860000', 'FLORES', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2605707', '56410000', 'FLORESTA', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2605806', '55780000', 'FREI MIGUELINHO', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2605905', '55533000', 'GAMELEIRA', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2606002', '55291000', 'GARANHUNS', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2606101', '55625000', 'GLORIA DO GOITA', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2606200', '55905000', 'GOIANA', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2606309', '56160000', 'GRANITO', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2606408', '55641000', 'GRAVATA', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2606507', '55345000', 'IATI', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2606606', '56585000', 'IBIMIRIM', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2606705', '55390000', 'IBIRAJUBA', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2606804', '53610000', 'IGARASSU', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2606903', '56845000', 'IGUARACI', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2607000', '56560000', 'INAJA', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2607109', '56830000', 'INGAZEIRA', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2607208', '55592000', 'IPOJUCA', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2607307', '56270000', 'IPUBI', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2607406', '56430000', 'ITACURUBA', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2607505', '56555000', 'ITAIBA', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2607604', '53900000', 'ITAMARACA', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2607653', '55928000', 'ITAMBE', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2607703', '56730000', 'ITAPETIM', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2607752', '53700000', 'ITAPISSUMA', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2607802', '55950000', 'ITAQUITINGA', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2607901', '54070000', 'JABOATAO DOS GUARARAPES', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2607950', '55409000', 'JAQUEIRA', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2608008', '55185000', 'JATAUBA', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2608057', '56475000', 'JATOBA', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2608107', '55720000', 'JOAO ALFREDO', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2608206', '55535000', 'JOAQUIM NABUCO', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2608255', '55398000', 'JUCATI', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2608305', '55395000', 'JUPI', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2608404', '55485000', 'JUREMA', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2608453', '55820000', 'LAGOA DO CARRO', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2608503', '55840000', 'LAGOA DO ITAENGA', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2608602', '55322000', 'LAGOA DO OURO', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2608701', '55453000', 'LAGOA DOS GATOS', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2608750', '56395000', 'LAGOA GRANDE', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2608800', '55385000', 'LAJEDO', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2608909', '55705000', 'LIMOEIRO', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2609006', '55865000', 'MACAPARANA', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2609105', '55740000', 'MACHADOS', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2609154', '56565000', 'MANARI', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2609204', '55408000', 'MARAIAL', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2609303', '56990000', 'MIRANDIBA', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2609402', '54800000', 'MORENO', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2609501', '55800000', 'NAZARE DA MATA', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2609600', '53010000', 'OLINDA', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2609709', '55748000', 'OROBO', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2609808', '56170000', 'OROCO', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2609907', '56205000', 'OURICURI', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2610004', '55548000', 'PALMARES', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2610103', '55310000', 'PALMEIRINA', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2610202', '55473000', 'PANELAS', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2610301', '55355000', 'PARANATAMA', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2610400', '56165000', 'PARNAMIRIM', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2610509', '55652000', 'PASSIRA', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2610608', '55825000', 'PAUDALHO', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2610707', '53401000', 'PAULISTA', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2610806', '55285000', 'PEDRA', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2610905', '55210000', 'PESQUEIRA', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2611002', '56460000', 'PETROLANDIA', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2611101', '56302000', 'PETROLINA', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2611200', '55245000', 'POCAO', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2611309', '55633000', 'POMBOS', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2611408', '55510000', 'PRIMAVERA', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2611507', '55418000', 'QUIPAPA', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2611533', '56828000', 'QUIXABA', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2611606', '50010000', 'RECIFE', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2611705', '55122000', 'RIACHO DAS ALMAS', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2611804', '55522000', 'RIBEIRAO', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2611903', '55572000', 'RIO FORMOSO', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2612000', '55695000', 'SAIRE', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2612109', '55675000', 'SALGADINHO', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2612208', '56110000', 'SALGUEIRO', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2612307', '55353000', 'SALOA', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2612406', '55255000', 'SANHARO', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2612455', '56215000', 'SANTA CRUZ', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2612471', '56895000', 'SANTA CRUZ DA BAIXA VERDE', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2612505', '55198000', 'SANTA CRUZ DO CAPIBARIBE', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2612554', '56210000', 'SANTA FILOMENA', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2612604', '56390000', 'SANTA MARIA DA BOA VISTA', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2612703', '55765000', 'SANTA MARIA DO CAMBUCA', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2612802', '55552000', 'SANTA TEREZINHA', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2612901', '55412000', 'SAO BENEDITO DO SUL', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2613008', '55374000', 'SAO BENTO DO UNA', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2613107', '55138000', 'SAO CAITANO', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2613206', '55435000', 'SAO JOAO', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2613305', '55672000', 'SAO JOAQUIM DO MONTE', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2613404', '55565000', 'SAO JOSE DA COROA GRANDE', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2613503', '56970000', 'SAO JOSE DO BELMONTE', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2613602', '56710000', 'SAO JOSE DO EGITO', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2613701', '54705000', 'SAO LOURENCO DA MATA', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2613800', '55863000', 'SAO VICENTE FERRER', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2613909', '56903000', 'SERRA TALHADA', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2614006', '56145000', 'SERRITA', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2614105', '56610000', 'SERTANIA', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2614204', '55585000', 'SIRINHAEM', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2614303', '56155000', 'MOREILANDIA', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2614402', '56795000', 'SOLIDAO', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2614501', '55750000', 'SURUBIM', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2614600', '56780000', 'TABIRA', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2614709', '55145000', 'TACAIMBO', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2614808', '56485000', 'TACARATU', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2614857', '55578000', 'TAMANDARE', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2615003', '55798000', 'TAQUARITINGA DO NORTE', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2615102', '55305000', 'TEREZINHA', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2615201', '56190000', 'TERRA NOVA', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2615300', '55878000', 'TIMBAUBA', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2615409', '55125000', 'TORITAMA', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2615508', '55805000', 'TRACUNHAEM', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2615607', '56250000', 'TRINDADE', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2615706', '56890000', 'TRIUNFO', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2615805', '56540000', 'TUPANATINGA', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2615904', '56770000', 'TUPARETAMA', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2616001', '55275000', 'VENTUROSA', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2616100', '56120000', 'VERDEJANTE', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2616183', '55760000', 'VERTENTE DO LERIO', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2616209', '55770000', 'VERTENTES', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2616308', '55855000', 'VICENCIA', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2616407', '55602000', 'VITORIA DE SANTO ANTAO', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2616506', '55555000', 'XEXEU', 'PE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2700102', '57490000', 'AGUA BRANCA', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2700201', '57660000', 'ANADIA', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2700300', '57300005', 'ARAPIRACA', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2700409', '57693000', 'ATALAIA', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2700508', '57925000', 'BARRA DE SANTO ANTONIO', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2700607', '57180000', 'BARRA DE SAO MIGUEL', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2700706', '57420000', 'BATALHA', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2700805', '57630000', 'BELEM', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2700904', '57435000', 'BELO MONTE', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2701001', '57680000', 'BOCA DA MATA', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2701100', '57830000', 'BRANQUINHA', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2701209', '57570000', 'CACIMBINHAS', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2701308', '57770000', 'CAJUEIRO', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2701357', '57968000', 'CAMPESTRE', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2701407', '57250000', 'CAMPO ALEGRE', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2701506', '57350000', 'CAMPO GRANDE', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2701605', '57530000', 'CANAPI', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2701704', '57790000', 'CAPELA', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2701803', '57535000', 'CARNEIROS', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2701902', '57760000', 'CHA PRETA', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2702009', '57325000', 'COITE DO NOIA', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2702108', '57975000', 'COLONIA LEOPOLDINA', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2702207', '57140000', 'COQUEIRO SECO', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2702306', '57235000', 'CORURIPE', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2702355', '57320000', 'CRAIBAS', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2702405', '57480000', 'DELMIRO GOUVEIA', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2702504', '57560000', 'DOIS RIACHOS', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2702553', '57625000', 'ESTRELA DE ALAGOAS', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2702603', '57340000', 'FEIRA GRANDE', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2702702', '57220000', 'FELIZ DESERTO', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2702801', '57995000', 'FLEXEIRAS', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2702900', '57360000', 'GIRAU DO PONCIANO', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2703007', '57895000', 'IBATEGUARA', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2703106', '57620000', 'IGACI', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2703205', '57280000', 'IGREJA NOVA', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2703304', '57545000', 'INHAPI', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2703403', '57430000', 'JACARE DOS HOMENS', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2703502', '57960000', 'JACUIPE', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2703601', '57950000', 'JAPARATINGA', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2703700', '57425000', 'JARAMATAIA', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2703809', '57980000', 'JOAQUIM GOMES', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2703908', '57965000', 'JUNDIA', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2704005', '57270000', 'JUNQUEIRO', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2704104', '57330000', 'LAGOA DA CANOA', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2704203', '57260000', 'LIMOEIRO DE ANADIA', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2704302', '57010000', 'MACEIO', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2704401', '57585000', 'MAJOR ISIDORO', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2704500', '57958000', 'MARAGOGI', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2704609', '57520000', 'MARAVILHA', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2704708', '57160000', 'MARECHAL DEODORO', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2704807', '57670000', 'MARIBONDO', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2704906', '57730000', 'MAR VERMELHO', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2705002', '57540000', 'MATA GRANDE', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2705101', '57910000', 'MATRIZ DE CAMARAGIBE', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2705200', '57990000', 'MESSIAS', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2705309', '57615000', 'MINADOR DO NEGRAO', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2705408', '57440000', 'MONTEIROPOLIS', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2705507', '57820000', 'MURICI', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2705606', '57970000', 'NOVO LINO', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2705705', '57442000', 'OLHO D''AGUA DAS FLORES', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2705804', '57470000', 'OLHO D''AGUA DO CASADO', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2705903', '57390000', 'OLHO D''AGUA GRANDE', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2706000', '57550000', 'OLIVENCA', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2706109', '57525000', 'OURO BRANCO', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2706208', '57410000', 'PALESTINA', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2706307', '57600005', 'PALMEIRA DOS INDIOS', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2706406', '57405000', 'PAO DE ACUCAR', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2706422', '57475000', 'PARICONHA', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2706448', '57935000', 'PARIPUEIRA', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2706505', '57930000', 'PASSO DE CAMARAGIBE', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2706604', '57740000', 'PAULO JACINTO', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2706703', '57200000', 'PENEDO', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2706802', '57210000', 'PIACABUCU', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2706901', '57150000', 'PILAR', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2707008', '57720000', 'PINDOBA', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2707107', '57465000', 'PIRANHAS', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2707206', '57510000', 'POCO DAS TRINCHEIRAS', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2707305', '57900000', 'PORTO CALVO', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2707404', '57948000', 'PORTO DE PEDRAS', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2707503', '57290000', 'PORTO REAL DO COLEGIO', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2707602', '57750000', 'QUEBRANGULO', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2707701', '57100000', 'RIO LARGO', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2707800', '57246000', 'ROTEIRO', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2707909', '57130000', 'SANTA LUZIA DO NORTE', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2708006', '57500000', 'SANTANA DO IPANEMA', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2708105', '57850000', 'SANTANA DO MUNDAU', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2708204', '57380000', 'SAO BRAS', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2708303', '57860000', 'SAO JOSE DA LAJE', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2708402', '57445000', 'SAO JOSE DA TAPERA', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2708501', '57920000', 'SAO LUIS DO QUITUNDE', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2708600', '57240000', 'SAO MIGUEL DOS CAMPOS', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2708709', '57940000', 'SAO MIGUEL DOS MILAGRES', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2708808', '57275000', 'SAO SEBASTIAO', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2708907', '57120000', 'SATUBA', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2708956', '57515000', 'SENADOR RUI PALMEIRA', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2709004', '57635000', 'TANQUE D''ARCA', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2709103', '57640000', 'TAQUARANA', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2709152', '57265000', 'TEOTONIO VILELA', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2709202', '57370000', 'TRAIPU', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2709301', '57810000', 'UNIAO DOS PALMARES', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2709400', '57710000', 'VICOSA', 'AL');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2800100', '49920000', 'AMPARO DE SAO FRANCISCO', 'SE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2800209', '49790000', 'AQUIDABA', 'SE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2800308', '49085350', 'ARACAJU', 'SE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2800407', '49220000', 'ARAUA', 'SE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2800506', '49580000', 'AREIA BRANCA', 'SE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2800605', '49140000', 'BARRA DOS COQUEIROS', 'SE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2800670', '49360000', 'BOQUIM', 'SE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2800704', '49995000', 'BREJO GRANDE', 'SE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2801009', '49520000', 'CAMPO DO BRITO', 'SE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2801108', '49880000', 'CANHOBA', 'SE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2801207', '49820000', 'CANINDE DE SAO FRANCISCO', 'SE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2801306', '49710000', 'CAPELA', 'SE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2801405', '49550000', 'CARIRA', 'SE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2801504', '49740000', 'CARMOPOLIS', 'SE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2801603', '49930000', 'CEDRO DE SAO JOAO', 'SE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2801702', '49270000', 'CRISTINAPOLIS', 'SE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2801900', '49660000', 'CUMBE', 'SE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2802007', '49650000', 'DIVINA PASTORA', 'SE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2802106', '49200000', 'ESTANCIA', 'SE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2802205', '49670000', 'FEIRA NOVA', 'SE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2802304', '49514000', 'FREI PAULO', 'SE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2802403', '49835000', 'GARARU', 'SE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2802502', '49750000', 'GENERAL MAYNARD', 'SE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2802601', '49860000', 'GRACHO CARDOSO', 'SE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2802700', '49990000', 'ILHA DAS FLORES', 'SE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2802809', '49250000', 'INDIAROBA', 'SE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2802908', '49500990', 'ITABAIANA', 'SE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2803005', '49290000', 'ITABAIANINHA', 'SE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2803104', '49870000', 'ITABI', 'SE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2803203', '49120000', 'ITAPORANGA D''AJUDA', 'SE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2803302', '49960000', 'JAPARATUBA', 'SE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2803401', '49950000', 'JAPOATA', 'SE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2803500', '49400990', 'LAGARTO', 'SE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2803609', '49170990', 'LARANJEIRAS', 'SE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2803708', '49565000', 'MACAMBIRA', 'SE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2803807', '49940000', 'MALHADA DOS BOIS', 'SE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2803906', '49570000', 'MALHADOR', 'SE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2804003', '49770000', 'MARUIM', 'SE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2804102', '49560000', 'MOITA BONITA', 'SE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2804201', '49690000', 'MONTE ALEGRE DE SERGIPE', 'SE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2804300', '49780000', 'MURIBECA', 'SE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2804409', '49980000', 'NEOPOLIS', 'SE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2804458', '49540000', 'NOSSA SENHORA APARECIDA', 'SE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2804508', '49680000', 'NOSSA SENHORA DA GLORIA', 'SE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2804607', '49600000', 'NOSSA SENHORA DAS DORES', 'SE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2804706', '49890000', 'NOSSA SENHORA DE LOURDES', 'SE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2804805', '49160990', 'NOSSA SENHORA DO SOCORRO', 'SE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2804904', '49970000', 'PACATUBA', 'SE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2805000', '49512000', 'PEDRA MOLE', 'SE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2805109', '49350000', 'PEDRINHAS', 'SE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2805208', '49517000', 'PINHAO', 'SE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2805307', '49190000', 'PIRAMBU', 'SE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2805406', '49810000', 'POCO REDONDO', 'SE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2805505', '49490000', 'POCO VERDE', 'SE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2805604', '49800000', 'PORTO DA FOLHA', 'SE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2805703', '49900000', 'PROPRIA', 'SE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2805802', '49320000', 'RIACHAO DO DANTAS', 'SE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2805901', '49130000', 'RIACHUELO', 'SE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2806008', '49530000', 'RIBEIROPOLIS', 'SE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2806107', '49760000', 'ROSARIO DO CATETE', 'SE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2806206', '49390000', 'SALGADO', 'SE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2806305', '49230000', 'SANTA LUZIA DO ITANHY', 'SE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2806404', '49985000', 'SANTANA DO SAO FRANCISCO', 'SE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2806503', '49640000', 'SANTA ROSA DE LIMA', 'SE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2806602', '49180000', 'SANTO AMARO DAS BROTAS', 'SE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2806701', '49100000', 'SAO CRISTOVAO', 'SE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2806800', '49525000', 'SAO DOMINGOS', 'SE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2806909', '49945000', 'SAO FRANCISCO', 'SE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2807006', '49535000', 'SAO MIGUEL DO ALEIXO', 'SE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2807105', '49480000', 'SIMAO DIAS', 'SE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2807204', '49630000', 'SIRIRI', 'SE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2807303', '49910000', 'TELHA', 'SE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2807402', '49300000', 'TOBIAS BARRETO', 'SE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2807501', '49280000', 'TOMAR DO GERU', 'SE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2807600', '49260000', 'UMBAUBA', 'SE');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2900108', '46695000', 'ABAIRA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2900207', '48685000', 'ABARE', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2900306', '48360000', 'ACAJUTIBA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2900355', '48435000', 'ADUSTINA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2900405', '48175000', 'AGUA FRIA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2900504', '46180000', 'ERICO CARDOSO', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2900603', '45220000', 'AIQUARA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2900702', '48005010', 'ALAGOINHAS', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2900801', '45990000', 'ALCOBACA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2900900', '45640000', 'ALMADINA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2901007', '45303000', 'AMARGOSA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2901106', '44235000', 'AMELIA RODRIGUES', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2901155', '44912000', 'AMERICA DOURADA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2901205', '45185000', 'ANAGE', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2901304', '46834000', 'ANDARAI', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2901353', '48994000', 'ANDORINHA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2901403', '47960000', 'ANGICAL', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2901502', '44670000', 'ANGUERA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2901601', '48420000', 'ANTAS', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2901700', '44180000', 'ANTONIO CARDOSO', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2901809', '44780000', 'ANTONIO GONCALVES', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2901908', '48355000', 'APORA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2901957', '45358000', 'APUAREMA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2902005', '46130000', 'ARACATU', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2902054', '48108000', 'ARACAS', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2902104', '48760000', 'ARACI', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2902203', '48130000', 'ARAMARI', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2902252', '45698000', 'ARATACA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2902302', '44495000', 'ARATUIPE', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2902401', '45678000', 'AURELINO LEAL', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2902500', '47840000', 'BAIANOPOLIS', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2902609', '44620000', 'BAIXA GRANDE', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2902658', '48409000', 'BANZAE', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2902708', '47105000', 'BARRA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2902807', '46660000', 'BARRA DA ESTIVA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2902906', '45120000', 'BARRA DO CHOCA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2903003', '44995000', 'BARRA DO MENDES', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2903102', '45560000', 'BARRA DO ROCHA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2903201', '47800000', 'BARREIRAS', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2903235', '44898000', 'BARRO ALTO', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2903300', '45625000', 'BARRO PRETO', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2903409', '45805000', 'BELMONTE', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2903508', '44911000', 'BELO CAMPO', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2903607', '48780000', 'BIRITINGA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2903706', '45250000', 'BOA NOVA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2903805', '46855000', 'BOA VISTA DO TUPIM', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2903904', '47600000', 'BOM JESUS DA LAPA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2903953', '45263000', 'BOM JESUS DA SERRA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2904001', '46745000', 'BONINAL', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2904050', '46820000', 'BONITO', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2904100', '46535000', 'BOQUIRA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2904209', '46570000', 'BOTUPORA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2904308', '45325000', 'BREJOES', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2904407', '47750000', 'BREJOLANDIA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2904506', '47565000', 'BROTAS DE MACAUBAS', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2904605', '46108000', 'BRUMADO', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2904704', '45615000', 'BUERAREMA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2904753', '47120000', 'BURITIRAMA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2904803', '45130000', 'CAATIBA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2904852', '44349000', 'CABACEIRAS DO PARAGUACU', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2904902', '44315000', 'CACHOEIRA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2905008', '46300000', 'CACULE', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2905107', '44730000', 'CAEM', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2905156', '45265000', 'CAETANOS', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2905206', '46405000', 'CAETITE', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2905305', '44880000', 'CAFARNAUM', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2905404', '45424000', 'CAIRU', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2905503', '44750000', 'CALDEIRAO GRANDE', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2905602', '45880000', 'CAMACAN', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2905701', '42800005', 'CAMACARI', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2905800', '45448000', 'CAMAMU', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2905909', '47230000', 'CAMPO ALEGRE DE LOURDES', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2906006', '44935000', 'CAMPO FORMOSO', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2906105', '47730000', 'CANAPOLIS', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2906204', '44892000', 'CANARANA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2906303', '45863000', 'CANAVIEIRAS', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2906402', '48710000', 'CANDEAL', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2906501', '43805000', 'CANDEIAS', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2906600', '46380000', 'CANDIBA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2906709', '45158000', 'CANDIDO SALES', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2906808', '48840000', 'CANSANCAO', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2906824', '44889000', 'CANUDOS', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2906857', '44645000', 'CAPELA DO ALTO ALEGRE', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2906873', '44697000', 'CAPIM GROSSO', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2906899', '45177000', 'CARAIBAS', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2906907', '45910000', 'CARAVELAS', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2907004', '48390000', 'CARDEAL DA SILVA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2907103', '46445000', 'CARINHANHA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2907202', '47330000', 'CASA NOVA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2907301', '44505000', 'CASTRO ALVES', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2907400', '47815000', 'CATOLANDIA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2907509', '48113000', 'CATU', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2907558', '46575000', 'CATURAMA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2907608', '44940000', 'CENTRAL', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2907707', '48668000', 'CHORROCHO', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2907806', '48413000', 'CICERO DANTAS', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2907905', '48450000', 'CIPO', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2908002', '45638000', 'COARACI', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2908101', '47680000', 'COCOS', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2908200', '44320000', 'CONCEICAO DA FEIRA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2908309', '44545000', 'CONCEICAO DO ALMEIDA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2908408', '48745000', 'CONCEICAO DO COITE', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2908507', '44245000', 'CONCEICAO DO JACUIPE', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2908606', '48300000', 'CONDE', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2908705', '46203000', 'CONDEUBA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2908804', '46630000', 'CONTENDAS DO SINCORA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2908903', '44253000', 'CORACAO DE MARIA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2909000', '46280000', 'CORDEIROS', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2909109', '47695000', 'CORIBE', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2909208', '48590000', 'CORONEL JOAO SA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2909307', '47650000', 'CORRENTINA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2909406', '47920000', 'COTEGIPE', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2909505', '45330000', 'CRAVOLANDIA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2909604', '48483000', 'CRISOPOLIS', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2909703', '47950000', 'CRISTOPOLIS', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2909802', '44380000', 'CRUZ DAS ALMAS', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2909901', '48935000', 'CURACA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2910008', '45590000', 'DARIO MEIRA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2910057', '42850000', 'DIAS D''AVILA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2910107', '46165000', 'DOM BASILIO', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2910206', '44560000', 'DOM MACEDO COSTA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2910305', '45306000', 'ELISIO MEDRADO', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2910404', '45153000', 'ENCRUZILHADA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2910503', '48185000', 'ENTRE RIOS', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2910602', '48380000', 'ESPLANADA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2910701', '48504000', 'EUCLIDES DA CUNHA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2910727', '45820002', 'EUNAPOLIS', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2910750', '48415000', 'FATIMA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2910776', '46446000', 'FEIRA DA MATA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2910800', '44010000', 'FEIRA DE SANTANA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2910859', '44775000', 'FILADELFIA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2910909', '45723000', 'FIRMINO ALVES', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2911006', '45740000', 'FLORESTA AZUL', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2911105', '47990000', 'FORMOSA DO RIO PRETO', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2911204', '45450000', 'GANDU', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2911253', '44650000', 'GAVIAO', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2911303', '47470000', 'GENTIO DO OURO', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2911402', '48610000', 'GLORIA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2911501', '45543000', 'GONGOGI', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2911600', '44350000', 'GOVERNADOR MANGABEIRA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2911659', '46205000', 'GUAJERU', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2911709', '46433000', 'GUANAMBI', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2911808', '45845000', 'GUARATINGA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2911857', '48445000', 'HELIOPOLIS', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2911907', '46865000', 'IACU', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2912004', '46390000', 'IBIASSUCE', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2912103', '45745000', 'IBICARAI', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2912202', '46760000', 'IBICOARA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2912301', '45295000', 'IBICUI', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2912400', '44975000', 'IBIPEBA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2912509', '46540000', 'IBIPITANGA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2912608', '46840000', 'IBIQUERA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2912707', '45500000', 'IBIRAPITANGA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2912806', '45940000', 'IBIRAPUA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2912905', '45582000', 'IBIRATAIA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2913002', '46720000', 'IBITIARA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2913101', '44965000', 'IBITITA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2913200', '47525000', 'IBOTIRAMA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2913309', '48725000', 'ICHU', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2913408', '46490000', 'IGAPORA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2913457', '45443000', 'IGRAPIUNA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2913507', '45285000', 'IGUAI', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2913606', '45650015', 'ILHEUS', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2913705', '48490000', 'INHAMBUPE', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2913804', '44685000', 'IPECAETA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2913903', '45570000', 'IPIAU', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2914000', '44600000', 'IPIRA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2914109', '47595000', 'IPUPIARA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2914208', '45370000', 'IRAJUBA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2914307', '46775000', 'IRAMAIA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2914406', '46985000', 'IRAQUARA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2914505', '44258000', 'IRARA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2914604', '44900000', 'IRECE', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2914653', '45848000', 'ITABELA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2914703', '46880000', 'ITABERABA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2914802', '45600002', 'ITABUNA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2914901', '45534000', 'ITACARE', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2915007', '46790000', 'ITAETE', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2915106', '45230000', 'ITAGI', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2915205', '45588000', 'ITAGIBA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2915304', '45850000', 'ITAGIMIRIM', 'BA');
            
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2915353', '47440000', 'ITAGUACU DA BAHIA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2915403', '45730000', 'ITAJU DO COLONIA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2915502', '45635000', 'ITAJUIPE', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2915601', '45838000', 'ITAMARAJU', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2915700', '45455000', 'ITAMARI', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2915809', '45145000', 'ITAMBE', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2915908', '48290000', 'ITANAGRA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2916005', '45975000', 'ITANHEM', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2916104', '44460000', 'ITAPARICA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2916203', '45750000', 'ITAPE', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2916302', '45858000', 'ITAPEBI', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2916401', '45705000', 'ITAPETINGA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2916500', '48476000', 'ITAPICURU', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2916609', '45645000', 'ITAPITANGA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2916708', '45340000', 'ITAQUARA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2916807', '45785000', 'ITARANTIM', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2916856', '46875000', 'ITATIM', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2916906', '45350000', 'ITIRUCU', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2917003', '48850000', 'ITIUBA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2917102', '45714000', 'ITORORO', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2917201', '46640000', 'ITUACU', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2917300', '45435000', 'ITUBERA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2917334', '46438000', 'IUIU', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2917359', '47655000', 'JABORANDI', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2917409', '46315000', 'JACARACI', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2917508', '44704000', 'JACOBINA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2917607', '45347000', 'JAGUAQUARA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2917706', '48965000', 'JAGUARARI', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2917805', '44482000', 'JAGUARIPE', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2917904', '48320000', 'JANDAIRA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2918001', '45200005', 'JEQUIE', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2918100', '48560000', 'JEREMOABO', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2918209', '45470000', 'JIQUIRICA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2918308', '45225000', 'JITAUNA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2918357', '44920000', 'JOAO DOURADO', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2918407', '48900010', 'JUAZEIRO', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2918456', '45834000', 'JUCURUCU', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2918506', '44927000', 'JUSSARA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2918555', '45610000', 'JUSSARI', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2918605', '46680000', 'JUSSIAPE', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2918704', '45215000', 'LAFAIETE COUTINHO', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2918753', '46425000', 'LAGOA REAL', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2918803', '45498000', 'LAJE', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2918902', '45950000', 'LAJEDAO', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2919009', '46825000', 'LAJEDINHO', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2919058', '45365000', 'LAJEDO DO TABOCAL', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2919108', '48720000', 'LAMARAO', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2919157', '44905000', 'LAPAO', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2919207', '42700000', 'LAURO DE FREITAS', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2919306', '46965000', 'LENCOIS', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2919405', '46335000', 'LICINIO DE ALMEIDA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2919504', '46143000', 'LIVRAMENTO DO BRUMADO', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2919603', '46805000', 'MACAJUBA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2919702', '45760000', 'MACARANI', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2919801', '46510000', 'MACAUBAS', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2919900', '48650000', 'MACURURE', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2919926', '42600000', 'MADRE DE DEUS', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2919959', '46255000', 'MAETINGA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2920007', '45770000', 'MAIQUINIQUE', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2920106', '44633000', 'MAIRI', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2920205', '46443000', 'MALHADA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2920304', '46110000', 'MALHADA DE PEDRAS', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2920403', '45245000', 'MANOEL VITORINO', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2920452', '47160000', 'MANSIDAO', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2920502', '45360000', 'MARACAS', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2920601', '44425000', 'MARAGOGIPE', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2920700', '45523000', 'MARAU', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2920809', '46785000', 'MARCIONILIO SOUZA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2920908', '45870000', 'MASCOTE', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2921005', '48288000', 'MATA DE SAO JOAO', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2921054', '46480000', 'MATINA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2921104', '45968000', 'MEDEIROS NETO', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2921203', '44727000', 'MIGUEL CALMON', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2921302', '45318000', 'MILAGRES', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2921401', '44747000', 'MIRANGABA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2921450', '45255000', 'MIRANTE', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2921500', '48800000', 'MONTE SANTO', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2921609', '47585000', 'MORPARA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2921708', '44860000', 'MORRO DO CHAPEU', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2921807', '46290000', 'MORTUGABA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2921906', '46755000', 'MUCUGE', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2922003', '45938000', 'MUCURI', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2922052', '44888000', 'MULUNGU DO MORRO', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2922102', '44810000', 'MUNDO NOVO', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2922201', '44578000', 'MUNIZ FERREIRA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2922250', '47115000', 'MUQUEM DE SAO FRANCISCO', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2922300', '44343000', 'MURITIBA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2922409', '45480000', 'MUTUIPE', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2922508', '44400000', 'NAZARE', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2922607', '45440000', 'NILO PECANHA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2922656', '48870000', 'NORDESTINA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2922706', '45275000', 'NOVA CANAA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2922730', '44642000', 'NOVA FATIMA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2922755', '45452000', 'NOVA IBIA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2922805', '45390000', 'NOVA ITARANA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2922854', '46835000', 'NOVA REDENCAO', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2922904', '48460000', 'NOVA SOURE', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2923001', '45925000', 'NOVA VICOSA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2923035', '46733000', 'NOVO HORIZONTE', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2923050', '48455000', 'NOVO TRIUNFO', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2923100', '48473000', 'OLINDINA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2923209', '47550000', 'OLIVEIRA DOS BREJINHOS', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2923308', '48150000', 'OURICANGAS', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2923357', '44718000', 'OUROLANDIA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2923407', '46460000', 'PALMAS DE MONTE ALTO', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2923506', '46940000', 'PALMEIRAS', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2923605', '46195000', 'PARAMIRIM', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2923704', '47505000', 'PARATINGA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2923803', '48430000', 'PARIPIRANGA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2923902', '45890000', 'PAU BRASIL', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2924009', '48601000', 'PAULO AFONSO', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2924058', '44655000', 'PE DE SERRA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2924108', '48140000', 'PEDRAO', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2924207', '48580000', 'PEDRO ALEXANDRE', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2924306', '46766000', 'PIATA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2924405', '47260000', 'PILAO ARCADO', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2924504', '46370000', 'PINDAI', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2924603', '44770000', 'PINDOBACU', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2924652', '44610000', 'PINTADAS', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2924678', '45436000', 'PIRAI DO NORTE', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2924702', '46270000', 'PIRIPA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2924801', '44837000', 'PIRITIBA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2924900', '45378000', 'PLANALTINO', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2925006', '45195000', 'PLANALTO', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2925105', '45260000', 'POCOES', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2925204', '48126000', 'POJUCA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2925253', '44757000', 'PONTO NOVO', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2925303', '45819000', 'PORTO SEGURO', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2925402', '45795000', 'POTIRAGUA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2925501', '45983000', 'PRADO', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2925600', '44930000', 'PRESIDENTE DUTRA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2925709', '46250000', 'PRESIDENTE JANIO QUADROS', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2925758', '45416000', 'PRESIDENTE TANCREDO NEVES', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2925808', '48860000', 'QUEIMADAS', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2925907', '48832000', 'QUIJINGUE', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2925931', '44713000', 'QUIXABEIRA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2925956', '44525000', 'RAFAEL JAMBEIRO', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2926004', '47210000', 'REMANSO', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2926103', '48750000', 'RETIROLANDIA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2926202', '47980000', 'RIACHAO DAS NEVES', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2926301', '44640000', 'RIACHAO DO JACUIPE', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2926400', '46475000', 'RIACHO DE SANTANA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2926509', '48440000', 'RIBEIRA DO AMPARO', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2926608', '48403000', 'RIBEIRA DO POMBAL', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2926657', '45156000', 'RIBEIRAO DO LARGO', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2926707', '46177000', 'RIO DE CONTAS', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2926806', '46225000', 'RIO DO ANTONIO', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2926905', '46560000', 'RIO DO PIRES', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2927002', '48330000', 'RIO REAL', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2927101', '48630000', 'RODELAS', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2927200', '46802000', 'RUY BARBOSA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2927309', '44450000', 'SALINAS DA MARGARIDA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2927408', '40010000', 'SALVADOR', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2927507', '44150000', 'SANTA BARBARA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2927606', '48570000', 'SANTA BRIGIDA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2927705', '45807000', 'SANTA CRUZ CABRALIA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2927804', '45725000', 'SANTA CRUZ DA VITORIA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2927903', '45320000', 'SANTA INES', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2928000', '48880000', 'SANTALUZ', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2928059', '45865000', 'SANTA LUZIA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2928109', '47645000', 'SANTA MARIA DA VITORIA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2928208', '47710000', 'SANTANA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2928307', '44265000', 'SANTANOPOLIS', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2928406', '47150000', 'SANTA RITA DE CASSIA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2928505', '44590000', 'SANTA TERESINHA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2928604', '44218000', 'SANTO AMARO', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2928703', '44570330', 'SANTO ANTONIO DE JESUS', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2928802', '44190000', 'SANTO ESTEVAO', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2928901', '47825000', 'SAO DESIDERIO', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2928950', '48895000', 'SAO DOMINGOS', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2929008', '44365000', 'SAO FELIX', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2929057', '47665000', 'SAO FELIX DO CORIBE', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2929107', '44555000', 'SAO FELIPE', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2929206', '43980000', 'SAO FRANCISCO DO CONDE', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2929255', '44915000', 'SAO GABRIEL', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2929305', '44338000', 'SAO GONCALO DOS CAMPOS', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2929354', '45620000', 'SAO JOSE DA VITORIA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2929370', '44698000', 'SAO JOSE DO JACUIPE', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2929404', '44580000', 'SAO MIGUEL DAS MATAS', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2929503', '43870000', 'SAO SEBASTIAO DO PASSE', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2929602', '44535000', 'SAPEACU', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2929701', '48485000', 'SATIRO DIAS', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2929750', '44220000', 'SAUBARA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2929800', '44740000', 'SAUDE', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2929909', '46920000', 'SEABRA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2930006', '46455000', 'SEBASTIAO LARANJEIRAS', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2930105', '48985000', 'SENHOR DO BONFIM', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2930154', '47630000', 'SERRA DO RAMALHO', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2930204', '47370000', 'SENTO SE', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2930303', '47740000', 'SERRA DOURADA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2930402', '44660000', 'SERRA PRETA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2930501', '48700000', 'SERRINHA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2930600', '44710000', 'SERROLANDIA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2930709', '43700000', 'SIMOES FILHO', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2930758', '47620000', 'SITIO DO MATO', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2930766', '48565000', 'SITIO DO QUINTO', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2930774', '48925000', 'SOBRADINHO', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2930808', '46990000', 'SOUTO SOARES', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2930907', '47770000', 'TABOCAS DO BREJO VELHO', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2931004', '46605000', 'TANHACU', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2931053', '46580000', 'TANQUE NOVO', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2931103', '44160000', 'TANQUINHO', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2931202', '45434000', 'TAPEROA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2931301', '44845000', 'TAPIRAMUTA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2931350', '45995001', 'TEIXEIRA DE FREITAS', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2931400', '44285000', 'TEODORO SAMPAIO', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2931509', '48770000', 'TEOFILANDIA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2931608', '45465000', 'TEOLANDIA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2931707', '44273000', 'TERRA NOVA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2931806', '45175000', 'TREMEDAL', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2931905', '48790000', 'TUCANO', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2932002', '48955000', 'UAUA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2932101', '45312000', 'UBAIRA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2932200', '45545000', 'UBAITABA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2932309', '45550000', 'UBATA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2932408', '44955000', 'UIBAI', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2932457', '44798000', 'UMBURANAS', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2932507', '45690000', 'UNA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2932606', '46350000', 'URANDI', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2932705', '45680000', 'URUCUCA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2932804', '46815000', 'UTINGA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2932903', '45413000', 'VALENCA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2933000', '48890000', 'VALENTE', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2933059', '44635000', 'VARZEA DA ROCA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2933109', '44715000', 'VARZEA DO POCO', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2933158', '44690000', 'VARZEA NOVA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2933174', '44568000', 'VARZEDO', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2933208', '44475000', 'VERA CRUZ', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2933257', '45958000', 'VEREDA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2933307', '45010000', 'VITORIA DA CONQUISTA', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2933406', '46970000', 'WAGNER', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2933455', '47940000', 'WANDERLEY', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2933505', '45460000', 'WENCESLAU GUIMARAES', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('2933604', '47410000', 'XIQUE-XIQUE', 'BA');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3100104', '38540000', 'ABADIA DOS DOURADOS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3100203', '35620000', 'ABAETE', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3100302', '35365700', 'ABRE CAMPO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3100401', '35438000', 'ACAIACA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3100500', '35155000', 'ACUCENA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3100609', '39790000', 'AGUA BOA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3100708', '38110000', 'AGUA COMPRIDA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3100807', '37273000', 'AGUANIL', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3100906', '39880000', 'AGUAS FORMOSAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3101003', '39993000', 'AGUAS VERMELHAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3101102', '35215000', 'AIMORES', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3101201', '37450000', 'AIURUOCA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3101300', '37458000', 'ALAGOA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3101409', '37596000', 'ALBERTINA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3101508', '36664000', 'ALEM PARAIBA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3101607', '37131000', 'ALFENAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3101631', '36272000', 'ALFREDO VASCONCELOS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3101706', '39910000', 'ALMENARA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3101805', '35138000', 'ALPERCATA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3101904', '37940000', 'ALPINOPOLIS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3102001', '37147000', 'ALTEROSA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3102050', '36836000', 'ALTO CAPARAO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3102100', '36264000', 'ALTO RIO DOCE', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3102209', '35249000', 'ALVARENGA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3102308', '35952000', 'ALVINOPOLIS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3102407', '39145000', 'ALVORADA DE MINAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3102506', '35445000', 'AMPARO DO SERRA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3102605', '37797000', 'ANDRADAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3102704', '39980000', 'CACHOEIRA DE PAJEU', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3102803', '37300000', 'ANDRELANDIA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3102852', '39685000', 'ANGELANDIA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3102902', '36220000', 'ANTONIO CARLOS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3103009', '35178000', 'ANTONIO DIAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3103108', '36850000', 'ANTONIO PRADO DE MINAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3103207', '35777000', 'ARACAI', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3103306', '36255000', 'ARACITABA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3103405', '39602000', 'ARACUAI', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3103504', '38440001', 'ARAGUARI', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3103603', '37360000', 'ARANTINA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3103702', '36596000', 'ARAPONGA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3103751', '38435000', 'ARAPORA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3103801', '38860000', 'ARAPUA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3103900', '35603000', 'ARAUJOS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3104007', '38180001', 'ARAXA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3104106', '37820000', 'ARCEBURGO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3104205', '35588000', 'ARCOS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3104304', '37140000', 'AREADO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3104403', '36710000', 'ARGIRITA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3104452', '39678000', 'ARICANDUVA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3104502', '38686000', 'ARINOS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3104601', '36783000', 'ASTOLFO DUTRA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3104700', '39851000', 'ATALEIA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3104809', '39220000', 'AUGUSTO DE LIMA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3104908', '37443000', 'BAEPENDI', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3105004', '35707000', 'BALDIM', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3105103', '38900000', 'BAMBUI', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3105202', '39917000', 'BANDEIRA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3105301', '37740000', 'BANDEIRA DO SUL', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3105400', '35975000', 'BARAO DE COCAIS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3105509', '36873000', 'BARAO DE MONTE ALTO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3105608', '36200001', 'BARBACENA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3105707', '35447000', 'BARRA LONGA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3105905', '36212000', 'BARROSO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3106002', '35938000', 'BELA VISTA DE MINAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3106101', '36128000', 'BELMIRO BRAGA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3106200', '30110000', 'BELO HORIZONTE', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3106309', '35196000', 'BELO ORIENTE', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3106408', '35475000', 'BELO VALE', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3106507', '39640000', 'BERILO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3106606', '39877000', 'BERTOPOLIS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3106655', '39555000', 'BERIZAL', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3106705', '32510000', 'BETIM', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3106804', '36230000', 'BIAS FORTES', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3106903', '36600000', 'BICAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3107000', '35621000', 'BIQUINHAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3107109', '37170000', 'BOA ESPERANCA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3107208', '37345000', 'BOCAINA DE MINAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3107307', '39394000', 'BOCAIUVA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3107406', '35602000', 'BOM DESPACHO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3107505', '37315000', 'BOM JARDIM DE MINAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3107604', '37948000', 'BOM JESUS DA PENHA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3107703', '35908000', 'BOM JESUS DO AMPARO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3107802', '35343000', 'BOM JESUS DO GALHO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3107901', '37610000', 'BOM REPOUSO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3108008', '37221000', 'BOM SUCESSO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3108107', '35522000', 'BONFIM', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3108206', '38650000', 'BONFINOPOLIS DE MINAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3108255', '39490000', 'BONITO DE MINAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3108305', '37565500', 'BORDA DA MATA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3108404', '37725000', 'BOTELHOS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3108503', '39595000', 'BOTUMIRIM', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3108552', '38779000', 'BRASILANDIA DE MINAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3108602', '39332000', 'BRASILIA DE MINAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3108701', '36542000', 'BRAS PIRES', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3108800', '35169000', 'BRAUNAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3108909', '37532000', 'BRASOPOLIS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3109006', '35464000', 'BRUMADINHO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3109105', '37578000', 'BUENO BRANDAO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3109204', '39235000', 'BUENOPOLIS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3109253', '35193000', 'BUGRE', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3109303', '38665000', 'BURITIS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3109402', '39285000', 'BURITIZEIRO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3109451', '38625000', 'CABECEIRA GRANDE', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3109501', '37885000', 'CABO VERDE', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3109600', '35765000', 'CACHOEIRA DA PRATA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3109709', '37546000', 'CACHOEIRA DE MINAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3109808', '38370000', 'CACHOEIRA DOURADA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3109907', '35770000', 'CAETANOPOLIS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3110004', '34950000', 'CAETE', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3110103', '36832000', 'CAIANA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3110202', '36565000', 'CAJURI', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3110301', '37787000', 'CALDAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3110400', '35555000', 'CAMACHO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3110509', '37652000', 'CAMANDUCAIA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3110608', '37600000', 'CAMBUI', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3110707', '37420000', 'CAMBUQUIRA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3110806', '39835000', 'CAMPANARIO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3110905', '37400000', 'CAMPANHA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3111002', '37730000', 'CAMPESTRE', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3111101', '38272000', 'CAMPINA VERDE', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3111150', '39338000', 'CAMPO AZUL', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3111200', '37271000', 'CAMPO BELO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3111309', '37165000', 'CAMPO DO MEIO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3111408', '38130000', 'CAMPO FLORIDO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3111507', '38975000', 'CAMPOS ALTOS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3111606', '37163000', 'CAMPOS GERAIS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3111705', '36592000', 'CANAA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3111804', '38380000', 'CANAPOLIS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3111903', '37267000', 'CANA VERDE', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3112000', '37280000', 'CANDEIAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3112059', '39703000', 'CANTAGALO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3112109', '36834000', 'CAPARAO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3112208', '36290000', 'CAPELA NOVA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3112307', '39680000', 'CAPELINHA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3112406', '37994000', 'CAPETINGA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3112505', '35730000', 'CAPIM BRANCO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3112604', '38360000', 'CAPINOPOLIS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3112653', '35123000', 'CAPITAO ANDRADE', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3112703', '39448000', 'CAPITAO ENEAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3112802', '37930000', 'CAPITOLIO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3112901', '36925000', 'CAPUTIRA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3113008', '39812000', 'CARAI', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3113107', '36428000', 'CARANAIBA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3113206', '36282000', 'CARANDAI', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3113305', '36805000', 'CARANGOLA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3113404', '35300000', 'CARATINGA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3113503', '39665000', 'CARBONITA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3113602', '37556000', 'CAREACU', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3113701', '39865000', 'CARLOS CHAGAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3113800', '35878000', 'CARMESIA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3113909', '37225000', 'CARMO DA CACHOEIRA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3114006', '35547000', 'CARMO DA MATA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3114105', '37472000', 'CARMO DE MINAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3114204', '35512000', 'CARMO DO CAJURU', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3114303', '38845000', 'CARMO DO PARANAIBA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3114402', '37155000', 'CARMO DO RIO CLARO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3114501', '35534000', 'CARMOPOLIS DE MINAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3114550', '38292000', 'CARNEIRINHO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3114600', '37245000', 'CARRANCAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3114709', '37760000', 'CARVALHOPOLIS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3114808', '37456000', 'CARVALHOS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3114907', '36422000', 'CASA GRANDE', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3115003', '38460000', 'CASCALHO RICO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3115102', '37980000', 'CASSIA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3115201', '36360000', 'CONCEICAO DA BARRA DE MINAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3115300', '36770001', 'CATAGUASES', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3115359', '35969000', 'CATAS ALTAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3115409', '36450000', 'CATAS ALTAS DA NORUEGA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3115458', '39816000', 'CATUJI', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3115474', '39526700', 'CATUTI', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3115508', '37440000', 'CAXAMBU', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3115607', '35624000', 'CEDRO DO ABAETE', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3115706', '35263000', 'CENTRAL DE MINAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3115805', '38390000', 'CENTRALINA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3115904', '36110000', 'CHACARA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3116001', '36988000', 'CHALE', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3116100', '39648000', 'CHAPADA DO NORTE', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3116159', '39314000', 'CHAPADA GAUCHA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3116209', '36635000', 'CHIADOR', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3116308', '36265000', 'CIPOTANEA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3116407', '37997000', 'CLARAVAL', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3116506', '39385000', 'CLARO DOS POCOES', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3116605', '35532000', 'CLAUDIO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3116704', '36550000', 'COIMBRA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3116803', '39770000', 'COLUNA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3116902', '38250000', 'COMENDADOR GOMES', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3117009', '39629000', 'COMERCINHO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3117108', '37148000', 'CONCEICAO DA APARECIDA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3117207', '37527000', 'CONCEICAO DAS PEDRAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3117306', '38126000', 'CONCEICAO DAS ALAGOAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3117405', '36947000', 'CONCEICAO DE IPANEMA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3117504', '35862000', 'CONCEICAO DO MATO DENTRO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3117603', '35668000', 'CONCEICAO DO PARA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3117702', '37435000', 'CONCEICAO DO RIO VERDE', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3117801', '37548000', 'CONCEICAO DOS OUROS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3117836', '39489000', 'CONEGO MARINHO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3117876', '33500000', 'CONFINS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3117900', '37557000', 'CONGONHAL', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3118007', '36417000', 'CONGONHAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3118106', '35850000', 'CONGONHAS DO NORTE', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3118205', '38196000', 'CONQUISTA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3118304', '36413000', 'CONSELHEIRO LAFAIETE', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3118403', '35241000', 'CONSELHEIRO PENA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3118502', '37670000', 'CONSOLACAO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3118601', '32010000', 'CONTAGEM', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3118700', '37237000', 'COQUEIRAL', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3118809', '39348000', 'CORACAO DE JESUS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3118908', '35782000', 'CORDISBURGO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3119005', '37498000', 'CORDISLANDIA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3119104', '39202000', 'CORINTO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3119203', '39712000', 'COROACI', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3119302', '38555000', 'COROMANDEL', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3119401', '35170001', 'CORONEL FABRICIANO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3119500', '39637000', 'CORONEL MURTA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3119609', '36155000', 'CORONEL PACHECO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3119708', '36330000', 'CORONEL XAVIER CHAVES', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3119807', '38995000', 'CORREGO DANTA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3119906', '37605000', 'CORREGO DO BOM JESUS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3119955', '35578000', 'CORREGO FUNDO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3120003', '35345000', 'CORREGO NOVO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3120102', '39188000', 'COUTO DE MAGALHAES DE MINAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3120151', '39885000', 'CRISOLITA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3120201', '37275000', 'CRISTAIS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3120300', '39598000', 'CRISTALIA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3120409', '36426000', 'CRISTIANO OTONI', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3120508', '37476000', 'CRISTINA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3120607', '35520000', 'CRUCILANDIA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3120706', '38738000', 'CRUZEIRO DA FORTALEZA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3120805', '37445000', 'CRUZILIA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3120839', '35246000', 'CUPARAQUE', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3120870', '39998000', 'CURRAL DE DENTRO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3120904', '35791000', 'CURVELO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3121001', '39130000', 'DATAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3121100', '37514000', 'DELFIM MOREIRA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3121209', '37915000', 'DELFINOPOLIS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3121258', '38108000', 'DELTA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3121308', '36690000', 'DESCOBERTO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3121407', '35492000', 'DESTERRO DE ENTRE RIOS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3121506', '36210000', 'DESTERRO DO MELO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3121605', '39110000', 'DIAMANTINA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3121704', '35437000', 'DIOGO DE VASCONCELOS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3121803', '35985000', 'DIONISIO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3121902', '36546000', 'DIVINESIA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3122009', '36825000', 'DIVINO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3122108', '35267000', 'DIVINO DAS LARANJEIRAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3122207', '39735000', 'DIVINOLANDIA DE MINAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3122306', '35500000', 'DIVINOPOLIS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3122355', '39995000', 'DIVISA ALEGRE', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3122405', '37134000', 'DIVISA NOVA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3122454', '39912000', 'DIVISOPOLIS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3122470', '38654000', 'DOM BOSCO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3122504', '35148000', 'DOM CAVATI', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3122603', '35868000', 'DOM JOAQUIM', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3122702', '35440000', 'DOM SILVERIO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3122801', '37474000', 'DOM VICOSO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3122900', '36787000', 'DONA EUZEBIA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3123007', '36213000', 'DORES DE CAMPOS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3123106', '35894000', 'DORES DE GUANHAES', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3123205', '35610000', 'DORES DO INDAIA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3123304', '36513000', 'DORES DO TURVO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3123403', '37926000', 'DORESOPOLIS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3123502', '38530000', 'DOURADOQUARA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3123528', '36974000', 'DURANDE', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3123601', '37110000', 'ELOI MENDES', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3123700', '35133000', 'ENGENHEIRO CALDAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3123809', '39417000', 'ENGENHEIRO NAVARRO', 'MG');
            
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3123858', '35324000', 'ENTRE FOLHAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3123908', '35491000', 'ENTRE RIOS DE MINAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3124005', '36555000', 'ERVALIA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3124104', '35745000', 'ESMERALDAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3124203', '36831000', 'ESPERA FELIZ', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3124302', '39515000', 'ESPINOSA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3124401', '37566000', 'ESPIRITO SANTO DO DOURADO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3124500', '37543000', 'ESTIVA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3124609', '36728000', 'ESTRELA DALVA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3124708', '35615000', 'ESTRELA DO INDAIA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3124807', '38526000', 'ESTRELA DO SUL', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3124906', '36857000', 'EUGENOPOLIS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3125002', '36108000', 'EWBANK DA CAMARA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3125101', '37640000', 'EXTREMA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3125200', '37138000', 'FAMA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3125309', '36840000', 'FARIA LEMOS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3125408', '39180000', 'FELICIO DOS SANTOS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3125507', '39185000', 'SAO GONCALO DO RIO PRETO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3125606', '39895000', 'FELISBURGO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3125705', '35795000', 'FELIXLANDIA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3125804', '35136000', 'FERNANDES TOURINHO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3125903', '35807000', 'FERROS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3125952', '36819000', 'FERVEDOURO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3126000', '35690000', 'FLORESTAL', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3126109', '35577000', 'FORMIGA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3126208', '38690000', 'FORMOSO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3126307', '37905000', 'FORTALEZA DE MINAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3126406', '35760000', 'FORTUNA DE MINAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3126505', '39644000', 'FRANCISCO BADARO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3126604', '39387000', 'FRANCISCO DUMONT', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3126703', '39581000', 'FRANCISCO SA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3126752', '39697000', 'FRANCISCOPOLIS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3126802', '39840000', 'FREI GASPAR', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3126901', '35112000', 'FREI INOCENCIO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3126950', '39708000', 'FREI LAGONEGRO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3127008', '38230000', 'FRONTEIRA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3127057', '39870000', 'FRONTEIRA DOS VALES', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3127073', '39558000', 'FRUTA DE LEITE', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3127107', '38205000', 'FRUTAL', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3127206', '35709000', 'FUNILANDIA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3127305', '35255000', 'GALILEIA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3127339', '39505000', 'GAMELEIRAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3127354', '39592000', 'GLAUCILANDIA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3127370', '35248000', 'GOIABEIRA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3127388', '36152000', 'GOIANA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3127404', '37680000', 'GONCALVES', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3127503', '39721000', 'GONZAGA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3127602', '39120000', 'GOUVEA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3127701', '35010000', 'GOVERNADOR VALADARES', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3127800', '39572000', 'GRAO MOGOL', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3127909', '38470000', 'GRUPIARA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3128006', '39742000', 'GUANHAES', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3128105', '37180000', 'GUAPE', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3128204', '35436000', 'GUARACIABA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3128253', '39397000', 'GUARACIAMA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3128303', '37815000', 'GUARANESIA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3128402', '36160000', 'GUARANI', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3128501', '36606000', 'GUARARA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3128600', '38570000', 'GUARDA-MOR', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3128709', '37800000', 'GUAXUPE', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3128808', '36515000', 'GUIDOVAL', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3128907', '38730000', 'GUIMARANIA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3129004', '36528000', 'GUIRICEMA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3129103', '38315000', 'GURINHATA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3129202', '37484000', 'HELIODORA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3129301', '35192000', 'IAPU', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3129400', '36225000', 'IBERTIOGA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3129509', '38953000', 'IBIA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3129608', '39350000', 'IBIAI', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3129657', '39457000', 'IBIRACATU', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3129707', '37990000', 'IBIRACI', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3129806', '32440000', 'IBIRITE', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3129905', '37790000', 'IBITIURA DE MINAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3130002', '37223000', 'IBITURUNA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3130051', '39318000', 'ICARAI DE MINAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3130101', '32900000', 'IGARAPE', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3130200', '35698000', 'IGARATINGA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3130309', '38910000', 'IGUATAMA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3130408', '37205000', 'IJACI', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3130507', '37175000', 'ILICINEA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3130556', '35323000', 'IMBE DE MINAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3130606', '37576000', 'INCONFIDENTES', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3130655', '39536000', 'INDAIABIRA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3130705', '38490000', 'INDIANOPOLIS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3130804', '37215000', 'INGAI', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3130903', '35333000', 'INHAPIM', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3131000', '35710000', 'INHAUMA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3131109', '35796000', 'INIMUTABA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3131158', '35198500', 'IPABA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3131208', '36950000', 'IPANEMA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3131307', '35160000', 'IPATINGA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3131406', '38350000', 'IPIACU', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3131505', '37559000', 'IPUIUNA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3131604', '38510000', 'IRAI DE MINAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3131703', '35900000', 'ITABIRA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3131802', '35285000', 'ITABIRINHA DE MANTENA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3131901', '35455000', 'ITABIRITO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3132008', '39594000', 'ITACAMBIRA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3132107', '39470000', 'ITACARAMBI', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3132206', '35514000', 'ITAGUARA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3132305', '39815000', 'ITAIPE', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3132404', '37500001', 'ITAJUBA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3132503', '39675000', 'ITAMARANDIBA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3132602', '36788000', 'ITAMARATI DE MINAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3132701', '39833000', 'ITAMBACURI', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3132800', '35820000', 'ITAMBE DO MATO DENTRO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3132909', '37955000', 'ITAMOGI', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3133006', '37466000', 'ITAMONTE', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3133105', '37464000', 'ITANHANDU', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3133204', '35122000', 'ITANHOMI', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3133303', '39625000', 'ITAOBIM', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3133402', '38240000', 'ITAPAGIPE', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3133501', '35551000', 'ITAPECERICA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3133600', '37655000', 'ITAPEVA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3133709', '35688000', 'ITATIAIUCU', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3133758', '37975000', 'ITAU DE MINAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3133808', '35680000', 'ITAUNA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3133907', '36445000', 'ITAVERAVA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3134004', '39613000', 'ITINGA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3134103', '35222000', 'ITUETA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3134202', '38300001', 'ITUIUTABA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3134301', '37212000', 'ITUMIRIM', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3134400', '38282000', 'ITURAMA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3134509', '36390000', 'ITUTINGA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3134608', '35835000', 'JABOTICATUBAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3134707', '39931000', 'JACINTO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3134806', '37965000', 'JACUI', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3134905', '37592000', 'JACUTINGA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3135001', '35188000', 'JAGUARACU', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3135050', '39508000', 'JAIBA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3135076', '39839000', 'JAMPRUCA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3135100', '39443000', 'JANAUBA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3135209', '39488000', 'JANUARIA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3135308', '35580000', 'JAPARAIBA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3135357', '39335700', 'JAPONVAR', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3135407', '35497000', 'JECEABA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3135456', '39645000', 'JENIPAPO DE MINAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3135506', '35393000', 'JEQUERI', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3135605', '39370000', 'JEQUITAI', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3135704', '35768000', 'JEQUITIBA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3135803', '39961000', 'JEQUITINHONHA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3135902', '37485000', 'JESUANIA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3136009', '39890000', 'JOAIMA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3136108', '35168000', 'JOANESIA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3136207', '35930000', 'JOAO MONLEVADE', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3136306', '38772000', 'JOAO PINHEIRO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3136405', '39240000', 'JOAQUIM FELICIO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3136504', '39923000', 'JORDANIA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3136520', '39642000', 'JOSE GONCALVES DE MINAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3136553', '39775000', 'JOSE RAYDAN', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3136579', '39575000', 'JOSENOPOLIS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3136603', '34990000', 'NOVA UNIAO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3136652', '35675000', 'JUATUBA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3136702', '36010000', 'JUIZ DE FORA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3136801', '39590000', 'JURAMENTO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3136900', '37805000', 'JURUAIA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3136959', '39469000', 'JUVENILIA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3137007', '39826000', 'LADAINHA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3137106', '38788000', 'LAGAMAR', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3137205', '35593000', 'LAGOA DA PRATA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3137304', '39360000', 'LAGOA DOS PATOS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3137403', '36345000', 'LAGOA DOURADA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3137502', '38722000', 'LAGOA FORMOSA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3137536', '38755000', 'LAGOA GRANDE', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3137601', '33450000', 'LAGOA SANTA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3137700', '36980000', 'LAJINHA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3137809', '37480000', 'LAMBARI', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3137908', '36455000', 'LAMIM', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3138005', '36765000', 'LARANJAL', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3138104', '39250000', 'LASSANCE', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3138203', '37200000', 'LAVRAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3138302', '35657000', 'LEANDRO FERREIRA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3138351', '39655000', 'LEME DO PRADO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3138401', '36708000', 'LEOPOLDINA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3138500', '37350000', 'LIBERDADE', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3138609', '36141000', 'LIMA DUARTE', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3138625', '38295000', 'LIMEIRA DO OESTE', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3138658', '39439000', 'LONTRA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3138674', '36923000', 'LUISBURGO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3138682', '39336000', 'LUISLANDIA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3138708', '37240000', 'LUMINARIAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3138807', '35596000', 'LUZ', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3138906', '39873000', 'MACHACALIS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3139003', '37755000', 'MACHADO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3139102', '37305000', 'MADRE DE DEUS DE MINAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3139201', '39691000', 'MALACACHETA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3139250', '39516000', 'MAMONAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3139300', '39463000', 'MANGA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3139409', '36906000', 'MANHUACU', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3139508', '36970000', 'MANHUMIRIM', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3139607', '35295000', 'MANTENA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3139706', '35666000', 'MARAVILHAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3139805', '36645000', 'MAR DE ESPANHA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3139904', '37518000', 'MARIA DA FE', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3140001', '35422000', 'MARIANA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3140100', '35115000', 'MARILAC', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3140159', '32470000', 'MARIO CAMPOS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3140209', '36608000', 'MARIPA DE MINAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3140308', '35185000', 'MARLIERIA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3140407', '37516000', 'MARMELOPOLIS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3140506', '35608000', 'MARTINHO CAMPOS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3140530', '36972000', 'MARTINS SOARES', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3140555', '39915000', 'MATA VERDE', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3140605', '39755000', 'MATERLANDIA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3140704', '35674000', 'MATEUS LEME', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3140803', '36120000', 'MATIAS BARBOSA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3140852', '39478000', 'MATIAS CARDOSO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3140902', '35367700', 'MATIPO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3141009', '39528000', 'MATO VERDE', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3141108', '35725000', 'MATOZINHOS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3141207', '38870000', 'MATUTINA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3141306', '38930000', 'MEDEIROS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3141405', '39623000', 'MEDINA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3141504', '35270000', 'MENDES PIMENTEL', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3141603', '36190000', 'MERCES', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3141702', '35166000', 'MESQUITA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3141801', '39650000', 'MINAS NOVAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3141900', '37447000', 'MINDURI', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3142007', '39423000', 'MIRABELA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3142106', '36893000', 'MIRADOURO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3142205', '36792000', 'MIRAI', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3142254', '39465000', 'MIRAVANIA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3142304', '35472000', 'MOEDA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3142403', '35604000', 'MOEMA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3142502', '39218000', 'MONJOLOS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3142601', '37405000', 'MONSENHOR PAULO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3142700', '39498000', 'MONTALVANIA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3142809', '38420000', 'MONTE ALEGRE DE MINAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3142908', '39500000', 'MONTE AZUL', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3143005', '37119000', 'MONTE BELO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3143104', '38500000', 'MONTE CARMELO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3143153', '39893000', 'MONTE FORMOSO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3143203', '37959000', 'MONTE SANTO DE MINAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3143302', '39400000', 'MONTES CLAROS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3143401', '37580000', 'MONTE SIAO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3143450', '39547000', 'MONTEZUMA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3143500', '35629000', 'MORADA NOVA DE MINAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3143609', '35798000', 'MORRO DA GARCA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3143708', '35875000', 'MORRO DO PILAR', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3143807', '37620000', 'MUNHOZ', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3143906', '36889000', 'MURIAE', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3144003', '36959000', 'MUTUM', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3144102', '37890000', 'MUZAMBINHO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3144201', '39718000', 'NACIP RAYDAN', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3144300', '39862000', 'NANUQUE', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3144359', '35157000', 'NAQUE', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3144375', '38658000', 'NATALANDIA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3144409', '37524000', 'NATERCIA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3144508', '36370000', 'NAZARENO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3144607', '37255000', 'NEPOMUCENO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3144656', '39553000', 'NINHEIRA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3144672', '35298000', 'NOVA BELEM', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3144706', '35920000', 'NOVA ERA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3144805', '34000000', 'NOVA LIMA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3144904', '35113000', 'NOVA MODICA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3145000', '38160000', 'NOVA PONTE', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3145059', '39525000', 'NOVA PORTEIRINHA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3145109', '37865000', 'NOVA RESENDE', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3145208', '35517000', 'NOVA SERRANA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3145307', '39823000', 'NOVO CRUZEIRO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3145356', '39817000', 'NOVO ORIENTE DE MINAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3145372', '39568000', 'NOVORIZONTE', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3145406', '36145000', 'OLARIA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3145455', '39398000', 'OLHOS-D''AGUA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3145505', '37488000', 'OLIMPIO NORONHA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3145604', '35541000', 'OLIVEIRA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3145703', '36250000', 'OLIVEIRA FORTES', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3145802', '35655000', 'ONCA DE PITANGUI', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3145851', '35439000', 'ORATORIOS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3145877', '36828000', 'ORIZANIA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3145901', '36420000', 'OURO BRANCO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3146008', '37574000', 'OURO FINO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3146107', '35407000', 'OURO PRETO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3146206', '39855000', 'OURO VERDE DE MINAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3146255', '39573000', 'PADRE CARVALHO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3146305', '39818000', 'PADRE PARAISO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3146404', '35623000', 'PAINEIRAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3146503', '35583000', 'PAINS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3146552', '39517000', 'PAI PEDRO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3146602', '36195000', 'PAIVA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3146701', '36753000', 'PALMA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3146750', '39948000', 'PALMOPOLIS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3146909', '35669000', 'PAPAGAIOS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3147006', '38600000', 'PARACATU', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3147105', '35660000', 'PARA DE MINAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3147204', '37125000', 'PARAGUACU', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3147303', '37665000', 'PARAISOPOLIS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3147402', '35774000', 'PARAOPEBA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3147501', '35810000', 'PASSABEM', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3147600', '37462000', 'PASSA QUATRO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3147709', '35537000', 'PASSA TEMPO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3147808', '37330000', 'PASSA VINTE', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3147907', '37900001', 'PASSOS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3147956', '39425000', 'PATIS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3148004', '38700001', 'PATOS DE MINAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3148103', '38748000', 'PATROCINIO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3148202', '36860000', 'PATROCINIO DO MURIAE', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3148301', '36544000', 'PAULA CANDIDO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3148400', '39765000', 'PAULISTAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3148509', '39814000', 'PAVAO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3148608', '39702000', 'PECANHA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3148707', '39970000', 'PEDRA AZUL', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3148756', '35364000', 'PEDRA BONITA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3148806', '36585000', 'PEDRA DO ANTA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3148905', '35565000', 'PEDRA DO INDAIA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3149002', '36847000', 'PEDRA DOURADA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3149101', '37520000', 'PEDRALVA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3149150', '39494000', 'PEDRAS DE MARIA DA CRUZ', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3149200', '38178000', 'PEDRINOPOLIS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3149309', '33680000', 'PEDRO LEOPOLDO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3149408', '36148000', 'PEDRO TEIXEIRA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3149507', '36610000', 'PEQUERI', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3149606', '35667000', 'PEQUI', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3149705', '35515000', 'PERDIGAO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3149804', '38170000', 'PERDIZES', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3149903', '37260000', 'PERDOES', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3149952', '35156000', 'PERIQUITO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3150000', '35114000', 'PESCADOR', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3150109', '36157000', 'PIAU', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3150158', '35325000', 'PIEDADE DE CARATINGA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3150208', '35382000', 'PIEDADE DE PONTE NOVA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3150307', '36227000', 'PIEDADE DO RIO GRANDE', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3150406', '35526000', 'PIEDADE DOS GERAIS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3150505', '35586000', 'PIMENTA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3150539', '35348000', 'PINGO D''AGUA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3150570', '39317000', 'PINTOPOLIS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3150604', '35536000', 'PIRACEMA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3150703', '38210000', 'PIRAJUBA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3150802', '36490000', 'PIRANGA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3150901', '37511000', 'PIRANGUCU', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3151008', '37509000', 'PIRANGUINHO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3151107', '36735000', 'PIRAPETINGA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3151206', '39270000', 'PIRAPORA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3151305', '36170000', 'PIRAUBA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3151404', '35650000', 'PITANGUI', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3151503', '37925000', 'PIUMHI', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3151602', '38220000', 'PLANURA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3151701', '37758000', 'POCO FUNDO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3151800', '37701000', 'POCOS DE CALDAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3151909', '36963000', 'POCRANE', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3152006', '35645000', 'POMPEU', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3152105', '35430001', 'PONTE NOVA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3152131', '39328000', 'PONTO CHIQUE', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3152170', '39618000', 'PONTO DOS VOLANTES', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3152204', '39524500', 'PORTEIRINHA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3152303', '36576000', 'PORTO FIRME', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3152402', '39828000', 'POTE', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3152501', '37549000', 'POUSO ALEGRE', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3152600', '37469000', 'POUSO ALTO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3152709', '36320000', 'PRADOS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3152808', '38145000', 'PRATA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3152907', '37970000', 'PRATAPOLIS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3153004', '38960000', 'PRATINHA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3153103', '36475000', 'PRESIDENTE BERNARDES', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3153202', '35797000', 'PRESIDENTE JUSCELINO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3153301', '39135000', 'PRESIDENTE KUBITSCHEK', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3153400', '38754000', 'PRESIDENTE OLEGARIO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3153509', '36978000', 'ALTO JEQUITIBA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3153608', '35715000', 'PRUDENTE DE MORAIS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3153707', '35626000', 'QUARTEL GERAL', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3153806', '36424000', 'QUELUZITA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3153905', '34400000', 'RAPOSOS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3154002', '35358000', 'RAUL SOARES', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3154101', '36743000', 'RECREIO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3154150', '36920000', 'REDUTO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3154200', '36342000', 'RESENDE COSTA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3154309', '35238000', 'RESPLENDOR', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3154408', '36270000', 'RESSAQUINHA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3154457', '38640000', 'RIACHINHO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3154507', '39529000', 'RIACHO DOS MACHADOS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3154606', '33805000', 'RIBEIRAO DAS NEVES', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3154705', '37264000', 'RIBEIRAO VERMELHO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3154804', '34300000', 'RIO ACIMA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3154903', '35375000', 'RIO CASCA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3155009', '35442000', 'RIO DOCE', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3155108', '39940000', 'RIO DO PRADO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3155207', '36462000', 'RIO ESPERA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3155306', '35523000', 'RIO MANSO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3155405', '36150000', 'RIO NOVO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3155504', '38812000', 'RIO PARANAIBA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3155603', '39532000', 'RIO PARDO DE MINAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3155702', '35945000', 'RIO PIRACICABA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3155801', '36180000', 'RIO POMBA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3155900', '36131000', 'RIO PRETO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3156007', '39175000', 'RIO VERMELHO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3156106', '36335000', 'RITAPOLIS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3156205', '36604000', 'ROCHEDO DE MINAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3156304', '36510000', 'RODEIRO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3156403', '38520000', 'ROMARIA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3156452', '36878000', 'ROSARIO DA LIMEIRA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3156502', '39565000', 'RUBELITA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3156601', '39955000', 'RUBIM', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3156700', '34505000', 'SABARA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3156809', '39753000', 'SABINOPOLIS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3156908', '38193000', 'SACRAMENTO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3157005', '39562000', 'SALINAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3157104', '39925000', 'SALTO DA DIVISA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3157203', '35963000', 'SANTA BARBARA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3157252', '35328000', 'SANTA BARBARA DO LESTE', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3157278', '36132000', 'SANTA BARBARA DO MONTE VERDE', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3157302', '36218000', 'SANTA BARBARA DO TUGURIO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3157336', '36328000', 'SANTA CRUZ DE MINAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3157377', '39563000', 'SANTA CRUZ DE SALINAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3157401', '35387000', 'SANTA CRUZ DO ESCALVADO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3157500', '39725000', 'SANTA EFIGENIA DE MINAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3157609', '39295000', 'SANTA FE DE MINAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3157658', '39874000', 'SANTA HELENA DE MINAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3157708', '38176000', 'SANTA JULIANA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3157807', '33010000', 'SANTA LUZIA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3157906', '36915000', 'SANTA MARGARIDA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3158003', '35915000', 'SANTA MARIA DE ITABIRA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3158102', '39928000', 'SANTA MARIA DO SALTO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3158201', '39783000', 'SANTA MARIA DO SUACUI', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3158300', '37195000', 'SANTANA DA VARGEM', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3158409', '36795000', 'SANTANA DE CATAGUASES', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3158508', '35788000', 'SANTANA DE PIRAPAMA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3158607', '36620000', 'SANTANA DO DESERTO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3158706', '36146000', 'SANTANA DO GARAMBEU', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3158805', '37278000', 'SANTANA DO JACARE', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3158904', '36945000', 'SANTANA DO MANHUACU', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3158953', '35167000', 'SANTANA DO PARAISO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3159001', '35847000', 'SANTANA DO RIACHO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3159100', '36435000', 'SANTANA DOS MONTES', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3159209', '37776000', 'SANTA RITA DE CALDAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3159308', '36138000', 'SANTA RITA DE JACUTINGA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3159357', '35326000', 'SANTA RITA DE MINAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3159407', '36236000', 'SANTA RITA DE IBITIPOCA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3159506', '35228000', 'SANTA RITA DO ITUETO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3159605', '37540000', 'SANTA RITA DO SAPUCAI', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3159704', '38805000', 'SANTA ROSA DA SERRA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3159803', '38328000', 'SANTA VITORIA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3159902', '37262000', 'SANTO ANTONIO DO AMPARO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3160009', '36675000', 'SANTO ANTONIO DO AVENTUREIRO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3160108', '35388000', 'SANTO ANTONIO DO GRAMA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3160207', '39160000', 'SANTO ANTONIO DO ITAMBE', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3160306', '39937000', 'SANTO ANTONIO DO JACINTO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3160405', '35560000', 'SANTO ANTONIO DO MONTE', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3160454', '39538000', 'SANTO ANTONIO DO RETIRO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3160504', '35880000', 'SANTO ANTONIO DO RIO ABAIXO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3160603', '39213000', 'SANTO HIPOLITO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3160702', '36245000', 'SANTOS DUMONT', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3160801', '37414000', 'SAO BENTO ABADE', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3160900', '35495000', 'SAO BRAS DO SUACUI', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3160959', '35335000', 'SAO DOMINGOS DAS DORES', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3161007', '35997000', 'SAO DOMINGOS DO PRATA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3161056', '35275000', 'SAO FELIX DE MINAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3161106', '39310000', 'SAO FRANCISCO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3161205', '35543000', 'SAO FRANCISCO DE PAULA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3161304', '38260000', 'SAO FRANCISCO DE SALES', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3161403', '36810000', 'SAO FRANCISCO DO GLORIA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3161502', '39342000', 'SAO GERALDO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3161601', '39723000', 'SAO GERALDO DA PIEDADE', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3161650', '35258000', 'SAO GERALDO DO BAIXIO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3161700', '38792000', 'SAO GONCALO DO ABAETE', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3161809', '35516000', 'SAO GONCALO DO PARA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3161908', '35935000', 'SAO GONCALO DO RIO ABAIXO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3162005', '37492000', 'SAO GONCALO DO SAPUCAI', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3162104', '38804000', 'SAO GOTARDO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3162203', '37920000', 'SAO JOAO BATISTA DO GLORIA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3162252', '39358000', 'SAO JOAO DA LAGOA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3162302', '37568000', 'SAO JOAO DA MATA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3162401', '39433000', 'SAO JOAO DA PONTE', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3162450', '39475000', 'SAO JOAO DAS MISSOES', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3162500', '36300001', 'SAO JOAO DEL REI', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3162559', '36918000', 'SAO JOAO DO MANHUACU', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3162575', '35277000', 'SAO JOAO DO MANTENINHA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3162609', '35146000', 'SAO JOAO DO ORIENTE', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3162658', '39368000', 'SAO JOAO DO PACUI', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3162708', '39545000', 'SAO JOAO DO PARAISO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3162807', '39704000', 'SAO JOAO EVANGELISTA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3162906', '36682000', 'SAO JOAO NEPOMUCENO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3162922', '32920000', 'SAO JOAQUIM DE BICAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3162948', '37945000', 'SAO JOSE DA BARRA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3162955', '33350000', 'SAO JOSE DA LAPA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3163003', '39785000', 'SAO JOSE DA SAFIRA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3163102', '35694000', 'SAO JOSE DA VARGINHA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3163201', '37510000', 'SAO JOSE DO ALEGRE', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3163300', '39848000', 'SAO JOSE DO DIVINO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3163409', '35986000', 'SAO JOSE DO GOIABAL', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3163508', '39707000', 'SAO JOSE DO JACURI', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3163607', '36990000', 'SAO JOSE DO MANTIMENTO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3163706', '37470000', 'SAO LOURENCO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3163805', '36590000', 'SAO MIGUEL DO ANTA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3163904', '37855000', 'SAO PEDRO DA UNIAO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3164001', '35362000', 'SAO PEDRO DOS FERROS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3164100', '39784000', 'SAO PEDRO DO SUACUI', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3164209', '39290000', 'SAO ROMAO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3164308', '37927000', 'SAO ROQUE DE MINAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3164407', '37567000', 'SAO SEBASTIAO DA BELA VISTA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3164431', '36793000', 'SAO SEBASTIAO DA VARGEM ALEGRE', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3164472', '35334000', 'SAO SEBASTIAO DO ANTA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3164506', '39796000', 'SAO SEBASTIAO DO MARANHAO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3164605', '35506000', 'SAO SEBASTIAO DO OESTE', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3164704', '37952000', 'SAO SEBASTIAO DO PARAISO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3164803', '35815000', 'SAO SEBASTIAO DO RIO PRETO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3164902', '37467000', 'SAO SEBASTIAO DO RIO VERDE', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3165008', '36352000', 'SAO TIAGO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3165107', '37960000', 'SAO TOMAS DE AQUINO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3165206', '37418000', 'SAO THOME DAS LETRAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3165305', '37370000', 'SAO VICENTE DE MINAS', 'MG');
            
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3165404', '37690000', 'SAPUCAI-MIRIM', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3165503', '39728000', 'SARDOA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3165537', '32450000', 'SARZEDO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3165552', '39688000', 'SETUBINHA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3165560', '35441000', 'SEM-PEIXE', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3165578', '37618000', 'SENADOR AMARAL', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3165602', '36650000', 'SENADOR CORTES', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3165701', '36540000', 'SENADOR FIRMINO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3165800', '37558000', 'SENADOR JOSE BENTO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3165909', '39190000', 'SENADOR MODESTINO GONCALVES', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3166006', '36470000', 'SENHORA DE OLIVEIRA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3166105', '39745000', 'SENHORA DO PORTO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3166204', '36278000', 'SENHORA DOS REMEDIOS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3166303', '35368000', 'SERICITA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3166402', '37454000', 'SERITINGA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3166501', '39165000', 'SERRA AZUL DE MINAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3166600', '35617000', 'SERRA DA SAUDADE', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3166709', '39868000', 'SERRA DOS AIMORES', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3166808', '38762000', 'SERRA DO SALITRE', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3166907', '37136000', 'SERRANIA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3166956', '39518000', 'SERRANOPOLIS DE MINAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3167004', '37452000', 'SERRANOS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3167103', '39158000', 'SERRO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3167202', '35700000', 'SETE LAGOAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3167301', '36185000', 'SILVEIRANIA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3167400', '37560000', 'SILVIANOPOLIS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3167509', '36123000', 'SIMAO PEREIRA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3167608', '36935000', 'SIMONESIA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3167707', '35144000', 'SOBRALIA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3167806', '37478000', 'SOLEDADE DE MINAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3167905', '36165000', 'TABULEIRO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3168002', '39550000', 'TAIOBEIRAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3168051', '36953000', 'TAPARUBA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3168101', '38185000', 'TAPIRA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3168200', '38985000', 'TAPIRAI', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3168309', '33980000', 'TAQUARACU DE MINAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3168408', '35143000', 'TARUMIRIM', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3168507', '36580000', 'TEIXEIRAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3168606', '39800001', 'TEOFILO OTONI', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3168705', '35180001', 'TIMOTEO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3168804', '36325000', 'TIRADENTES', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3168903', '38890000', 'TIROS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3169000', '36512000', 'TOCANTINS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3169059', '37563000', 'TOCOS DO MOJI', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3169109', '37630000', 'TOLEDO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3169208', '36846000', 'TOMBOS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3169307', '37410000', 'TRES CORACOES', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3169356', '39207000', 'TRES MARIAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3169406', '37192000', 'TRES PONTAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3169505', '35126000', 'TUMIRITINGA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3169604', '38430000', 'TUPACIGUARA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3169703', '39662000', 'TURMALINA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3169802', '37496000', 'TURVOLANDIA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3169901', '36508000', 'UBA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3170008', '39325000', 'UBAI', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3170057', '35339000', 'UBAPORANGA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3170107', '38010000', 'UBERABA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3170206', '38400010', 'UBERLANDIA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3170305', '39878000', 'UMBURATIBA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3170404', '38613000', 'UNAI', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3170438', '38288000', 'UNIAO DE MINAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3170479', '38630000', 'URUANA DE MINAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3170503', '35381000', 'URUCANIA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3170529', '39315000', 'URUCUIA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3170578', '35199000', 'VARGEM ALEGRE', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3170602', '37922000', 'VARGEM BONITA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3170651', '39535000', 'VARGEM GRANDE DO RIO PARDO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3170701', '37002000', 'VARGINHA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3170750', '38794000', 'VARJAO DE MINAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3170800', '39265000', 'VARZEA DA PALMA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3170909', '39452000', 'VARZELANDIA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3171006', '38782000', 'VAZANTE', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3171030', '39458000', 'VERDELANDIA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3171071', '39664000', 'VEREDINHA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3171105', '38150000', 'VERISSIMO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3171154', '35359000', 'VERMELHO NOVO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3171204', '33200000', 'VESPASIANO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3171303', '36572000', 'VICOSA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3171402', '36897000', 'VIEIRAS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3171501', '35110000', 'MATHIAS LOBATO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3171600', '39630000', 'VIRGEM DA LAPA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3171709', '37465000', 'VIRGINIA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3171808', '39730000', 'VIRGINOPOLIS', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3171907', '39716000', 'VIRGOLANDIA', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3172004', '36520000', 'VISCONDE DO RIO BRANCO', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3172103', '36723000', 'VOLTA GRANDE', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3172202', '37513000', 'WENCESLAU BRAZ', 'MG');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3200102', '29609000', 'AFONSO CLAUDIO', 'ES');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3200136', '29795000', 'AGUIA BRANCA', 'ES');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3200169', '29826000', 'AGUA DOCE DO NORTE', 'ES');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3200201', '29530000', 'ALEGRE', 'ES');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3200300', '29242000', 'ALFREDO CHAVES', 'ES');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3200359', '29767000', 'ALTO RIO NOVO', 'ES');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3200409', '29238000', 'ANCHIETA', 'ES');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3200508', '29458000', 'APIACA', 'ES');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3200607', '29199000', 'ARACRUZ', 'ES');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3200706', '29490000', 'ATILIO VIVACQUA', 'ES');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3200805', '29737000', 'BAIXO GUANDU', 'ES');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3200904', '29805000', 'BARRA DE SAO FRANCISCO', 'ES');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3201001', '29847000', 'BOA ESPERANCA', 'ES');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3201100', '29460000', 'BOM JESUS DO NORTE', 'ES');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3201159', '29635000', 'BREJETUBA', 'ES');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3201209', '29300002', 'CACHOEIRO DE ITAPEMIRIM', 'ES');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3201308', '29140010', 'CARIACICA', 'ES');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3201407', '29367000', 'CASTELO', 'ES');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3201506', '29700005', 'COLATINA', 'ES');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3201605', '29967000', 'CONCEICAO DA BARRA', 'ES');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3201704', '29370000', 'CONCEICAO DO CASTELO', 'ES');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3201803', '29590000', 'DIVINO DE SAO LOURENCO', 'ES');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3201902', '29263000', 'DOMINGOS MARTINS', 'ES');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3202009', '29585000', 'DORES DO RIO PRETO', 'ES');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3202108', '29855000', 'ECOPORANGA', 'ES');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3202207', '29189000', 'FUNDAO', 'ES');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3202306', '29562000', 'GUACUI', 'ES');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3202405', '29200010', 'GUARAPARI', 'ES');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3202454', '29395000', 'IBATIBA', 'ES');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3202504', '29675000', 'IBIRACU', 'ES');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3202553', '29545000', 'IBITIRAMA', 'ES');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3202603', '29283000', 'ICONHA', 'ES');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3202652', '29399000', 'IRUPI', 'ES');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3202702', '29695000', 'ITAGUACU', 'ES');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3202801', '29335000', 'ITAPEMIRIM', 'ES');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3202900', '29620000', 'ITARANA', 'ES');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3203007', '29393000', 'IUNA', 'ES');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3203056', '29954000', 'JAGUARE', 'ES');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3203106', '29550000', 'JERONIMO MONTEIRO', 'ES');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3203130', '29687000', 'JOAO NEIVA', 'ES');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3203163', '29617000', 'LARANJA DA TERRA', 'ES');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3203205', '29900010', 'LINHARES', 'ES');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3203304', '29778000', 'MANTENOPOLIS', 'ES');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3203320', '29345000', 'MARATAIZES', 'ES');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3203346', '29259000', 'MARECHAL FLORIANO', 'ES');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3203353', '29728000', 'MARILANDIA', 'ES');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3203403', '29445000', 'MIMOSO DO SUL', 'ES');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3203502', '29894000', 'MONTANHA', 'ES');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3203601', '29884000', 'MUCURICI', 'ES');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3203700', '29388000', 'MUNIZ FREIRE', 'ES');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3203809', '29485000', 'MUQUI', 'ES');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3203908', '29842000', 'NOVA VENECIA', 'ES');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3204005', '29755000', 'PANCAS', 'ES');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3204054', '29978000', 'PEDRO CANARIO', 'ES');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3204104', '29985000', 'PINHEIROS', 'ES');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3204203', '29287000', 'PIUMA', 'ES');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3204252', '29889000', 'PONTO BELO', 'ES');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3204302', '29350000', 'PRESIDENTE KENNEDY', 'ES');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3204351', '29925000', 'RIO BANANAL', 'ES');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3204401', '29293000', 'RIO NOVO DO SUL', 'ES');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3204500', '29642000', 'SANTA LEOPOLDINA', 'ES');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3204559', '29649000', 'SANTA MARIA DE JETIBA', 'ES');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3204609', '29662000', 'SANTA TERESA', 'ES');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3204658', '29745000', 'SAO DOMINGOS DO NORTE', 'ES');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3204708', '29783000', 'SAO GABRIEL DA PALHA', 'ES');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3204807', '29477000', 'SAO JOSE DO CALCADO', 'ES');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3204906', '29932000', 'SAO MATEUS', 'ES');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3204955', '29667000', 'SAO ROQUE DO CANAA', 'ES');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3205002', '29160003', 'SERRA', 'ES');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3205010', '29927000', 'SOORETAMA', 'ES');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3205036', '29297000', 'VARGEM ALTA', 'ES');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3205069', '29378000', 'VENDA NOVA DO IMIGRANTE', 'ES');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3205101', '29138000', 'VIANA', 'ES');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3205150', '29843000', 'VILA PAVAO', 'ES');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3205176', '29793000', 'VILA VALERIO', 'ES');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3205200', '29100010', 'VILA VELHA', 'ES');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3205309', '29010001', 'VITORIA', 'ES');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3300100', '23960000', 'ANGRA DOS REIS', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3300159', '28495000', 'APERIBE', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3300209', '28975000', 'ARARUAMA', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3300225', '25845000', 'AREAL', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3300233', '28950000', 'ARMACAO DOS BUZIOS', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3300258', '28930000', 'ARRAIAL DO CABO', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3300308', '27110000', 'BARRA DO PIRAI', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3300407', '27310000', 'BARRA MANSA', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3300456', '26110000', 'BELFORD ROXO', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3300506', '28662000', 'BOM JARDIM', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3300605', '28372000', 'BOM JESUS DO ITABAPOANA', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3300704', '28905000', 'CABO FRIO', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3300803', '28685000', 'CACHOEIRAS DE MACACU', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3300902', '28435000', 'CAMBUCI', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3300936', '27998000', 'CARAPEBUS', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3300951', '25875000', 'COMENDADOR LEVY GASPARIAN', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3301009', '28010000', 'CAMPOS DOS GOYTACAZES', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3301108', '28525000', 'CANTAGALO', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3301157', '28195000', 'CARDOSO MOREIRA', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3301207', '28642000', 'CARMO', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3301306', '28880000', 'CASIMIRO DE ABREU', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3301405', '28745000', 'CONCEICAO DE MACABU', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3301504', '28540000', 'CORDEIRO', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3301603', '28655000', 'DUAS BARRAS', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3301702', '25010000', 'DUQUE DE CAXIAS', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3301801', '26660000', 'ENGENHEIRO PAULO DE FRONTIN', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3301850', '25940000', 'GUAPIMIRIM', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3301876', '28960000', 'IGUABA GRANDE', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3301900', '24850000', 'ITABORAI', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3302007', '23810000', 'ITAGUAI', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3302056', '28250000', 'ITALVA', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3302106', '28590000', 'ITAOCARA', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3302205', '28340000', 'ITAPERUNA', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3302254', '27580000', 'ITATIAIA', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3302270', '26410000', 'JAPERI', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3302304', '28350000', 'LAJE DO MURIAE', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3302403', '27910000', 'MACAE', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3302452', '28545000', 'MACUCO', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3302502', '25935000', 'MAGE', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3302601', '23885000', 'MANGARATIBA', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3302700', '24910000', 'MARICA', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3302809', '26700000', 'MENDES', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3302908', '26920000', 'MIGUEL PEREIRA', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3303005', '28463000', 'MIRACEMA', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3303104', '28383000', 'NATIVIDADE', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3303203', '26510000', 'NILOPOLIS', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3303302', '24006049', 'NITEROI', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3303401', '28605000', 'NOVA FRIBURGO', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3303500', '26010003', 'NOVA IGUACU', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3303609', '26600000', 'PARACAMBI', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3303708', '25865000', 'PARAIBA DO SUL', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3303807', '23972000', 'PARATI', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3303856', '26980000', 'PATY DO ALFERES', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3303906', '25610000', 'PETROPOLIS', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3303955', '27197000', 'PINHEIRAL', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3304003', '27185000', 'PIRAI', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3304102', '28398000', 'PORCIUNCULA', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3304110', '27570000', 'PORTO REAL', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3304128', '27410000', 'QUATIS', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3304144', '26310000', 'QUEIMADOS', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3304151', '28735000', 'QUISSAMA', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3304201', '27510000', 'RESENDE', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3304300', '28810000', 'RIO BONITO', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3304409', '27475000', 'RIO CLARO', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3304508', '27670000', 'RIO DAS FLORES', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3304524', '28890000', 'RIO DAS OSTRAS', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3304557', '20010000', 'RIO DE JANEIRO', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3304607', '28772000', 'SANTA MARIA MADALENA', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3304706', '28483000', 'SANTO ANTONIO DE PADUA', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3304755', '28240000', 'SAO FRANCISCO DE ITABAPOANA', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3304805', '28420000', 'SAO FIDELIS', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3304904', '24410000', 'SAO GONCALO', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3305000', '28220000', 'SAO JOAO DA BARRA', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3305109', '25510000', 'SAO JOAO DE MERITI', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3305133', '28455000', 'SAO JOSE DE UBA', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3305158', '25780000', 'SAO JOSE DO VALE DO RIO PRETO', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3305208', '28940000', 'SAO PEDRO DA ALDEIA', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3305307', '28555000', 'SAO SEBASTIAO DO ALTO', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3305406', '25882000', 'SAPUCAIA', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3305505', '28993000', 'SAQUAREMA', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3305554', '23890000', 'SEROPEDICA', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3305604', '28830000', 'SILVA JARDIM', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3305703', '28637000', 'SUMIDOURO', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3305752', '24890000', 'TANGUA', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3305802', '25953000', 'TERESOPOLIS', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3305901', '28757000', 'TRAJANO DE MORAIS', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3306008', '25802000', 'TRES RIOS', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3306107', '27640000', 'VALENCA', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3306156', '28375000', 'VARRE-SAI', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3306206', '27770000', 'VASSOURAS', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3306305', '27210000', 'VOLTA REDONDA', 'RJ');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3500105', '17800000', 'ADAMANTINA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3500204', '15230000', 'ADOLFO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3500303', '13860000', 'AGUAI', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3500402', '13895000', 'AGUAS DA PRATA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3500501', '13940000', 'AGUAS DE LINDOIA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3500550', '18770000', 'AGUAS DE SANTA BARBARA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3500600', '13525000', 'AGUAS DE SAO PEDRO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3500709', '17123000', 'AGUDOS', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3500758', '18220000', 'ALAMBARI', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3500808', '19180000', 'ALFREDO MARCONDES', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3500907', '15437000', 'ALTAIR', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3501004', '14350000', 'ALTINOPOLIS', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3501103', '16320000', 'ALTO ALEGRE', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3501152', '18125000', 'ALUMINIO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3501202', '15545000', 'ALVARES FLORENCE', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3501301', '19165000', 'ALVARES MACHADO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3501400', '17410000', 'ALVARO DE CARVALHO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3501509', '17430000', 'ALVINLANDIA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3501608', '13465005', 'AMERICANA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3501707', '14820000', 'AMERICO BRASILIENSE', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3501806', '15550000', 'AMERICO DE CAMPOS', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3501905', '13900005', 'AMPARO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3502002', '13550000', 'ANALANDIA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3502101', '16900000', 'ANDRADINA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3502200', '18243000', 'ANGATUBA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3502309', '18630000', 'ANHEMBI', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3502408', '13435000', 'ANHUMAS', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3502507', '12570000', 'APARECIDA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3502606', '15735000', 'APARECIDA D''OESTE', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3502705', '18323000', 'APIAI', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3502754', '18147000', 'ARACARIGUAMA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3502804', '16010000', 'ARACATUBA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3502903', '18190000', 'ARACOIABA DA SERRA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3503000', '14550000', 'ARAMINA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3503109', '18710000', 'ARANDU', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3503158', '12870000', 'ARAPEI', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3503208', '14800005', 'ARARAQUARA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3503307', '13600001', 'ARARAS', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3503356', '17630000', 'ARCO-IRIS', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3503406', '17170000', 'AREALVA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3503505', '12820000', 'AREIAS', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3503604', '18670000', 'AREIOPOLIS', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3503703', '15960000', 'ARIRANHA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3503802', '13160000', 'ARTUR NOGUEIRA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3503901', '07400000', 'ARUJA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3503950', '15763000', 'ASPASIA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3504008', '19800001', 'ASSIS', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3504107', '12940020', 'ATIBAIA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3504206', '15350000', 'AURIFLAMA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3504305', '16690000', 'AVAI', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3504404', '16360000', 'AVANHANDAVA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3504503', '18700005', 'AVARE', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3504602', '15115000', 'BADY BASSITT', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3504701', '16640000', 'BALBINOS', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3504800', '15140000', 'BALSAMO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3504909', '12850000', 'BANANAL', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3505005', '18490000', 'BARAO DE ANTONINA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3505104', '16350000', 'BARBOSA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3505203', '17250000', 'BARIRI', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3505302', '17340000', 'BARRA BONITA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3505351', '18325000', 'BARRA DO CHAPEU', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3505401', '11955000', 'BARRA DO TURVO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3505500', '14780005', 'BARRETOS', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3505609', '14860000', 'BARRINHA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3505708', '06401000', 'BARUERI', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3505807', '17690000', 'BASTOS', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3505906', '14300000', 'BATATAIS', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3506003', '17010000', 'BAURU', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3506102', '14700005', 'BEBEDOURO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3506201', '16790000', 'BENTO DE ABREU', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3506300', '18960000', 'BERNARDINO DE CAMPOS', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3506359', '11250000', 'BERTIOGA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3506409', '16210000', 'BILAC', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3506508', '16200001', 'BIRIGUI', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3506607', '08940000', 'BIRITIBA-MIRIM', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3506706', '14930000', 'BOA ESPERANCA DO SUL', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3506805', '17240000', 'BOCAINA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3506904', '18590000', 'BOFETE', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3507001', '18550000', 'BOITUVA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3507100', '12955000', 'BOM JESUS DOS PERDOES', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3507159', '18475000', 'BOM SUCESSO DE ITARARE', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3507209', '19740000', 'BORA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3507308', '17270000', 'BORACEIA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3507407', '14955000', 'BORBOREMA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3507456', '18675000', 'BOREBI', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3507506', '18600001', 'BOTUCATU', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3507605', '12900002', 'BRAGANCA PAULISTA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3507704', '16290000', 'BRAUNA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3507753', '16265000', 'BREJO ALEGRE', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3507803', '14340000', 'BRODOSQUI', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3507902', '17390000', 'BROTAS', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3508009', '18295000', 'BURI', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3508108', '15290000', 'BURITAMA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3508207', '14570000', 'BURITIZAL', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3508306', '17480000', 'CABRALIA PAULISTA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3508405', '13319000', 'CABREUVA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3508504', '12280005', 'CACAPAVA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3508603', '12630000', 'CACHOEIRA PAULISTA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3508702', '13775000', 'CACONDE', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3508801', '16510000', 'CAFELANDIA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3508900', '19540000', 'CAIABU', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3509007', '07700000', 'CAIEIRAS', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3509106', '19450000', 'CAIUA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3509205', '07770000', 'CAJAMAR', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3509254', '11950000', 'CAJATI', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3509304', '15417000', 'CAJOBI', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3509403', '14240000', 'CAJURU', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3509452', '18245000', 'CAMPINA DO MONTE ALEGRE', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3509502', '13010000', 'CAMPINAS', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3509601', '13230000', 'CAMPO LIMPO PAULISTA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3509700', '12460000', 'CAMPOS DO JORDAO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3509809', '19960000', 'CAMPOS NOVOS PAULISTA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3509908', '11995000', 'CANANEIA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3509957', '12615000', 'CANAS', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3510005', '19882000', 'CANDIDO MOTA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3510104', '15930000', 'CANDIDO RODRIGUES', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3510153', '18990000', 'CANITAR', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3510203', '18300005', 'CAPAO BONITO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3510302', '18195000', 'CAPELA DO ALTO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3510401', '13360000', 'CAPIVARI', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3510500', '11660005', 'CARAGUATATUBA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3510609', '06310010', 'CARAPICUIBA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3510708', '15575000', 'CARDOSO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3510807', '13707000', 'CASA BRANCA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3510906', '14260000', 'CASSIA DOS COQUEIROS', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3511003', '16920000', 'CASTILHO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3511102', '15800003', 'CATANDUVA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3511201', '15870000', 'CATIGUA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3511300', '15895000', 'CEDRAL', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3511409', '18760000', 'CERQUEIRA CESAR', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3511508', '18520000', 'CERQUILHO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3511607', '18288000', 'CESARIO LANGE', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3511706', '13517000', 'CHARQUEADA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3511904', '16255000', 'CLEMENTINA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3512001', '14770000', 'COLINA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3512100', '14795000', 'COLOMBIA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3512209', '13839000', 'CONCHAL', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3512308', '18575000', 'CONCHAS', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3512407', '13490000', 'CORDEIROPOLIS', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3512506', '16260000', 'COROADOS', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3512605', '18745000', 'CORONEL MACEDO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3512704', '13540000', 'CORUMBATAI', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3512803', '13150000', 'COSMOPOLIS', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3512902', '15530000', 'COSMORAMA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3513009', '06700020', 'COTIA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3513108', '14140000', 'CRAVINHOS', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3513207', '14460000', 'CRISTAIS PAULISTA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3513306', '19860000', 'CRUZALIA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3513405', '12701000', 'CRUZEIRO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3513504', '11500005', 'CUBATAO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3513603', '12540000', 'CUNHA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3513702', '13690000', 'DESCALVADO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3513801', '09910000', 'DIADEMA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3513850', '15715000', 'DIRCE REIS', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3513900', '13785000', 'DIVINOLANDIA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3514007', '15980000', 'DOBRADA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3514106', '17310000', 'DOIS CORREGOS', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3514205', '15740000', 'DOLCINOPOLIS', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3514304', '13590000', 'DOURADO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3514403', '17905000', 'DRACENA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3514502', '17470000', 'DUARTINA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3514601', '14120000', 'DUMONT', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3514700', '19830000', 'ECHAPORA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3514809', '11980000', 'ELDORADO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3514908', '13355000', 'ELIAS FAUSTO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3514924', '15823000', 'ELISIARIO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3514957', '15425000', 'EMBAUBA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3515004', '06803000', 'EMBU', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3515103', '06930000', 'EMBU-GUACU', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3515129', '19350000', 'EMILIANOPOLIS', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3515152', '13165000', 'ENGENHEIRO COELHO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3515186', '13990000', 'ESPIRITO SANTO DO PINHAL', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3515194', '18935000', 'ESPIRITO SANTO DO TURVO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3515202', '15650000', 'ESTRELA D''OESTE', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3515301', '19230000', 'ESTRELA DO NORTE', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3515350', '19275000', 'EUCLIDES DA CUNHA PAULISTA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3515400', '18870000', 'FARTURA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3515509', '15617000', 'FERNANDOPOLIS', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3515608', '15945000', 'FERNANDO PRESTES', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3515657', '17455000', 'FERNAO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3515707', '08500010', 'FERRAZ DE VASCONCELOS', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3515806', '17870000', 'FLORA RICA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3515905', '15320000', 'FLOREAL', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3516002', '17840000', 'FLORIDA PAULISTA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3516101', '19870000', 'FLORINIA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3516200', '14400005', 'FRANCA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3516309', '07901000', 'FRANCISCO MORATO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3516408', '07801000', 'FRANCO DA ROCHA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3516507', '16220000', 'GABRIEL MONTEIRO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3516606', '17450000', 'GALIA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3516705', '17405000', 'GARCA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3516804', '15330000', 'GASTAO VIDIGAL', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3516853', '14813000', 'GAVIAO PEIXOTO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3516903', '15307000', 'GENERAL SALGADO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3517000', '16455000', 'GETULINA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3517109', '16280000', 'GLICERIO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3517208', '16430000', 'GUAICARA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3517307', '16490000', 'GUAIMBE', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3517406', '14790000', 'GUAIRA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3517505', '15110000', 'GUAPIACU', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3517604', '18310000', 'GUAPIARA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3517703', '14590000', 'GUARA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3517802', '16980000', 'GUARACAI', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3517901', '15420000', 'GUARACI', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3518008', '15680000', 'GUARANI D''OESTE', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3518107', '16570000', 'GUARANTA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3518206', '16710000', 'GUARARAPES', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3518305', '08900000', 'GUARAREMA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3518404', '12500010', 'GUARATINGUETA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3518503', '18250000', 'GUAREI', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3518602', '14840000', 'GUARIBA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3518701', '11410000', 'GUARUJA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3518800', '07010000', 'GUARULHOS', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3518859', '14115000', 'GUATAPARA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3518909', '15355000', 'GUZOLANDIA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3519006', '17660000', 'HERCULANDIA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3519055', '13825000', 'HOLAMBRA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3519071', '13183005', 'HORTOLANDIA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3519105', '17180000', 'IACANGA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3519204', '17685000', 'IACRI', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3519253', '18775000', 'IARAS', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3519303', '14815000', 'IBATE', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3519402', '15868000', 'IBIRA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3519501', '19940000', 'IBIRAREMA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3519600', '14945000', 'IBITINGA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3519709', '18155000', 'IBIUNA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3519808', '15460000', 'ICEM', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3519907', '19640000', 'IEPE', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3520004', '17350000', 'IGARACU DO TIETE', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3520103', '14540000', 'IGARAPAVA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3520202', '12350000', 'IGARATA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3520301', '11920000', 'IGUAPE', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3520400', '11650000', 'ILHABELA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3520426', '11925000', 'ILHA COMPRIDA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3520442', '15385000', 'ILHA SOLTEIRA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3520509', '13330005', 'INDAIATUBA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3520608', '19560000', 'INDIANA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3520707', '15690000', 'INDIAPORA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3520806', '17760000', 'INUBIA PAULISTA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3520905', '18950000', 'IPAUCU', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3521002', '18565000', 'IPERO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3521101', '13537000', 'IPEUNA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3521150', '15108000', 'IPIGUA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3521200', '18330000', 'IPORANGA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3521309', '14610000', 'IPUA', 'SP');
            
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3521408', '13495000', 'IRACEMAPOLIS', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3521507', '14990000', 'IRAPUA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3521606', '17880000', 'IRAPURU', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3521705', '18450000', 'ITABERA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3521804', '18730000', 'ITAI', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3521903', '15840000', 'ITAJOBI', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3522000', '17260000', 'ITAJU', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3522109', '11740000', 'ITANHAEM', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3522158', '18360000', 'ITAOCA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3522208', '06850001', 'ITAPECERICA DA SERRA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3522307', '18200001', 'ITAPETININGA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3522406', '18400002', 'ITAPEVA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3522505', '06653000', 'ITAPEVI', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3522604', '13970005', 'ITAPIRA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3522653', '18385000', 'ITAPIRAPUA PAULISTA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3522703', '14904000', 'ITAPOLIS', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3522802', '18480000', 'ITAPORANGA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3522901', '17230000', 'ITAPUI', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3523008', '15390000', 'ITAPURA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3523107', '08570002', 'ITAQUAQUECETUBA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3523206', '18465000', 'ITARARE', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3523305', '11770000', 'ITARIRI', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3523404', '13250005', 'ITATIBA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3523503', '18695000', 'ITATINGA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3523602', '13535000', 'ITIRAPINA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3523701', '14420000', 'ITIRAPUA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3523800', '13715000', 'ITOBI', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3523909', '13300003', 'ITU', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3524006', '13295000', 'ITUPEVA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3524105', '14505000', 'ITUVERAVA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3524204', '14775000', 'JABORANDI', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3524303', '14870010', 'JABOTICABAL', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3524402', '12301000', 'JACAREI', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3524501', '15155000', 'JACI', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3524600', '11940000', 'JACUPIRANGA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3524709', '13820000', 'JAGUARIUNA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3524808', '15700000', 'JALES', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3524907', '12270000', 'JAMBEIRO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3525003', '06600005', 'JANDIRA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3525102', '14690000', 'JARDINOPOLIS', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3525201', '13240000', 'JARINU', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3525300', '17201000', 'JAU', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3525409', '14450000', 'JERIQUARA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3525508', '12980000', 'JOANOPOLIS', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3525607', '19680000', 'JOAO RAMALHO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3525706', '15208000', 'JOSE BONIFACIO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3525805', '17550000', 'JULIO MESQUITA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3525854', '18535000', 'JUMIRIM', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3525904', '13201000', 'JUNDIAI', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3526001', '17890000', 'JUNQUEIROPOLIS', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3526100', '11800000', 'JUQUIA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3526209', '06950000', 'JUQUITIBA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3526308', '12130000', 'LAGOINHA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3526407', '18510000', 'LARANJAL PAULISTA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3526506', '16855000', 'LAVINIA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3526605', '12770000', 'LAVRINHAS', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3526704', '13610005', 'LEME', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3526803', '18680005', 'LENCOIS PAULISTA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3526902', '13480001', 'LIMEIRA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3527009', '13950000', 'LINDOIA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3527108', '16400010', 'LINS', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3527207', '12600005', 'LORENA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3527256', '15285000', 'LOURDES', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3527306', '13290000', 'LOUVEIRA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3527405', '17780000', 'LUCELIA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3527504', '17475000', 'LUCIANOPOLIS', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3527603', '14210000', 'LUIS ANTONIO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3527702', '16340000', 'LUIZIANIA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3527801', '17420000', 'LUPERCIO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3527900', '19750000', 'LUTECIA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3528007', '17290000', 'MACATUBA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3528106', '15270000', 'MACAUBAL', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3528205', '15620000', 'MACEDONIA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3528304', '15310000', 'MAGDA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3528403', '18120000', 'MAIRINQUE', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3528502', '07600000', 'MAIRIPORA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3528601', '18785000', 'MANDURI', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3528700', '19430000', 'MARABA PAULISTA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3528809', '19845000', 'MARACAI', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3528858', '15845000', 'MARAPOAMA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3528908', '17815000', 'MARIAPOLIS', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3529005', '17500001', 'MARILIA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3529104', '15730000', 'MARINOPOLIS', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3529203', '19505000', 'MARTINOPOLIS', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3529302', '15990005', 'MATAO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3529401', '09310000', 'MAUA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3529500', '15220000', 'MENDONCA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3529609', '15625000', 'MERIDIANO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3529658', '15748000', 'MESOPOLIS', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3529708', '14530000', 'MIGUELOPOLIS', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3529807', '17320000', 'MINEIROS DO TIETE', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3529906', '11860000', 'MIRACATU', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3530003', '15580000', 'MIRA ESTRELA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3530102', '16830000', 'MIRANDOPOLIS', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3530201', '19270000', 'MIRANTE DO PARANAPANEMA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3530300', '15135000', 'MIRASSOL', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3530409', '15145000', 'MIRASSOLANDIA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3530508', '13730005', 'MOCOCA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3530607', '08710000', 'MOJI DAS CRUZES', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3530706', '13840001', 'MOGI GUACU', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3530805', '13800001', 'MOJI-MIRIM', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3530904', '13380000', 'MOMBUCA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3531001', '15275000', 'MONCOES', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3531100', '11730000', 'MONGAGUA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3531209', '13915000', 'MONTE ALEGRE DO SUL', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3531308', '15915000', 'MONTE ALTO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3531407', '15154000', 'MONTE APRAZIVEL', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3531506', '14733000', 'MONTE AZUL PAULISTA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3531605', '17960000', 'MONTE CASTELO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3531704', '12250000', 'MONTEIRO LOBATO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3531803', '13190000', 'MONTE MOR', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3531902', '14640000', 'MORRO AGUDO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3532009', '13260000', 'MORUNGABA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3532058', '14835000', 'MOTUCA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3532108', '16950000', 'MURUTINGA DO SUL', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3532157', '19645000', 'NANTES', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3532207', '19220000', 'NARANDIBA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3532306', '12190000', 'NATIVIDADE DA SERRA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3532405', '12960000', 'NAZARE PAULISTA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3532504', '15128000', 'NEVES PAULISTA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3532603', '15195000', 'NHANDEARA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3532702', '15240000', 'NIPOA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3532801', '15215000', 'NOVA ALIANCA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3532827', '18435000', 'NOVA CAMPINA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3532843', '15773000', 'NOVA CANAA PAULISTA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3532868', '15313000', 'NOVA CASTILHO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3532900', '14920000', 'NOVA EUROPA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3533007', '15445000', 'NOVA GRANADA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3533106', '17950000', 'NOVA GUATAPORANGA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3533205', '16940000', 'NOVA INDEPENDENCIA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3533254', '15885000', 'NOVAIS', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3533304', '15340000', 'NOVA LUZITANIA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3533403', '13460000', 'NOVA ODESSA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3533502', '14970000', 'NOVO HORIZONTE', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3533601', '14670000', 'NUPORANGA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3533700', '17540000', 'OCAUCU', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3533809', '18794000', 'OLEO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3533908', '15408000', 'OLIMPIA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3534005', '15450000', 'ONDA VERDE', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3534104', '17570000', 'ORIENTE', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3534203', '15480000', 'ORINDIUVA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3534302', '14620000', 'ORLANDIA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3534401', '06010000', 'OSASCO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3534500', '19770000', 'OSCAR BRESSANE', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3534609', '17705000', 'OSVALDO CRUZ', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3534708', '19900001', 'OURINHOS', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3534757', '15685000', 'OUROESTE', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3534807', '17925000', 'OURO VERDE', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3534906', '17860000', 'PACAEMBU', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3535002', '15472000', 'PALESTINA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3535101', '15828000', 'PALMARES PAULISTA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3535200', '15725000', 'PALMEIRA D''OESTE', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3535309', '19975000', 'PALMITAL', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3535408', '17980000', 'PANORAMA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3535507', '19720000', 'PARAGUACU PAULISTA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3535606', '12260000', 'PARAIBUNA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3535705', '15825000', 'PARAISO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3535804', '18720000', 'PARANAPANEMA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3535903', '15745000', 'PARANAPUA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3536000', '17730000', 'PARAPUA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3536109', '18640000', 'PARDINHO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3536208', '11930000', 'PARIQUERA-ACU', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3536257', '15525000', 'PARISI', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3536307', '14415000', 'PATROCINIO PAULISTA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3536406', '17990000', 'PAULICEIA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3536505', '13140000', 'PAULINIA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3536570', '17150000', 'PAULISTANIA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3536604', '15490000', 'PAULO DE FARIA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3536703', '17288000', 'PEDERNEIRAS', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3536802', '12990000', 'PEDRA BELA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3536901', '15635000', 'PEDRANOPOLIS', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3537008', '14475000', 'PEDREGULHO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3537107', '13920000', 'PEDREIRA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3537156', '19865000', 'PEDRINHAS PAULISTA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3537206', '11790000', 'PEDRO DE TOLEDO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3537305', '16300000', 'PENAPOLIS', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3537404', '15374000', 'PEREIRA BARRETO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3537503', '18580000', 'PEREIRAS', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3537602', '11750000', 'PERUIBE', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3537701', '16230000', 'PIACATU', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3537800', '18170000', 'PIEDADE', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3537909', '18185000', 'PILAR DO SUL', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3538006', '12400010', 'PINDAMONHANGABA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3538105', '15835000', 'PINDORAMA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3538204', '12995000', 'PINHALZINHO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3538303', '19410000', 'PIQUEROBI', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3538501', '12620000', 'PIQUETE', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3538600', '12975000', 'PIRACAIA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3538709', '13400005', 'PIRACICABA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3538808', '18810000', 'PIRAJU', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3538907', '16606000', 'PIRAJUI', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3539004', '15820000', 'PIRANGI', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3539103', '06550000', 'PIRAPORA DO BOM JESUS', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3539202', '19208000', 'PIRAPOZINHO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3539301', '13630005', 'PIRASSUNUNGA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3539400', '17490000', 'PIRATININGA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3539509', '14760000', 'PITANGUEIRAS', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3539608', '16915000', 'PLANALTO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3539707', '19990000', 'PLATINA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3539806', '08550010', 'POA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3539905', '15160000', 'POLONI', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3540002', '17585000', 'POMPEIA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3540101', '16660000', 'PONGAI', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3540200', '14185000', 'PONTAL', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3540259', '15718000', 'PONTALINDA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3540309', '15560000', 'PONTES GESTAL', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3540408', '15670000', 'POPULINA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3540507', '18260000', 'PORANGABA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3540606', '18540000', 'PORTO FELIZ', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3540705', '13660000', 'PORTO FERREIRA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3540754', '12525000', 'POTIM', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3540804', '15105000', 'POTIRENDABA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3540853', '17790000', 'PRACINHA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3540903', '14850000', 'PRADOPOLIS', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3541000', '11700005', 'PRAIA GRANDE', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3541059', '18660000', 'PRATANIA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3541109', '16675000', 'PRESIDENTE ALVES', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3541208', '19330000', 'PRESIDENTE BERNARDES', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3541307', '19490000', 'PRESIDENTE EPITACIO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3541406', '19010000', 'PRESIDENTE PRUDENTE', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3541505', '19400000', 'PRESIDENTE VENCESLAU', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3541604', '16380000', 'PROMISSAO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3541653', '18255000', 'QUADRA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3541703', '19780000', 'QUATA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3541802', '17590000', 'QUEIROZ', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3541901', '12800000', 'QUELUZ', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3542008', '17670000', 'QUINTANA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3542107', '13370000', 'RAFARD', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3542206', '19610000', 'RANCHARIA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3542305', '12170000', 'REDENCAO DA SERRA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3542404', '19575000', 'REGENTE FEIJO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3542503', '17190000', 'REGINOPOLIS', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3542602', '11900000', 'REGISTRO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3542701', '14430000', 'RESTINGA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3542800', '18380000', 'RIBEIRA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3542909', '13585000', 'RIBEIRAO BONITO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3543006', '18433000', 'RIBEIRAO BRANCO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3543105', '14445000', 'RIBEIRAO CORRENTE', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3543204', '19930000', 'RIBEIRAO DO SUL', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3543238', '19380000', 'RIBEIRAO DOS INDIOS', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3543253', '18315000', 'RIBEIRAO GRANDE', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3543303', '09400005', 'RIBEIRAO PIRES', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3543402', '14010000', 'RIBEIRAO PRETO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3543501', '18470000', 'RIVERSUL', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3543600', '14490000', 'RIFAINA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3543709', '14830000', 'RINCAO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3543808', '17740000', 'RINOPOLIS', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3543907', '13500030', 'RIO CLARO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3544004', '13390000', 'RIO DAS PEDRAS', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3544103', '09450000', 'RIO GRANDE DA SERRA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3544202', '15495000', 'RIOLANDIA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3544251', '19274000', 'ROSANA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3544301', '12580000', 'ROSEIRA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3544400', '16750000', 'RUBIACEA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3544509', '15795000', 'RUBINEIA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3544608', '16440000', 'SABINO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3544707', '17710000', 'SAGRES', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3544806', '14980000', 'SALES', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3544905', '14660000', 'SALES OLIVEIRA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3545001', '08980000', 'SALESOPOLIS', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3545100', '17720000', 'SALMOURAO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3545159', '13440000', 'SALTINHO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3545209', '13320005', 'SALTO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3545308', '18160000', 'SALTO DE PIRAPORA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3545407', '19920000', 'SALTO GRANDE', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3545506', '19250000', 'SANDOVALINA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3545605', '15955000', 'SANTA ADELIA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3545704', '15750000', 'SANTA ALBERTINA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3545803', '13450001', 'SANTA BARBARA D''OESTE', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3546009', '12380000', 'SANTA BRANCA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3546108', '15785000', 'SANTA CLARA D''OESTE', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3546207', '13625000', 'SANTA CRUZ DA CONCEICAO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3546256', '14250000', 'SANTA CRUZ DA ESPERANCA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3546306', '13650000', 'SANTA CRUZ DAS PALMEIRAS', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3546405', '18910000', 'SANTA CRUZ DO RIO PARDO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3546504', '15970000', 'SANTA ERNESTINA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3546603', '15775000', 'SANTA FE DO SUL', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3546702', '13510000', 'SANTA GERTRUDES', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3546801', '07500000', 'SANTA ISABEL', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3546900', '14825000', 'SANTA LUCIA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3547007', '17370000', 'SANTA MARIA DA SERRA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3547106', '17945000', 'SANTA MERCEDES', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3547205', '15765000', 'SANTANA DA PONTE PENSA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3547304', '06501001', 'SANTANA DE PARNAIBA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3547403', '15783000', 'SANTA RITA D''OESTE', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3547502', '13675000', 'SANTA RITA DO PASSA QUATRO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3547601', '14270000', 'SANTA ROSA DE VITERBO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3547650', '15768000', 'SANTA SALETE', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3547700', '19360000', 'SANTO ANASTACIO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3547809', '09010000', 'SANTO ANDRE', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3547908', '14390000', 'SANTO ANTONIO DA ALEGRIA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3548005', '13830000', 'SANTO ANTONIO DE POSSE', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3548054', '16140000', 'SANTO ANTONIO DO ARACANGUA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3548104', '13995000', 'SANTO ANTONIO DO JARDIM', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3548203', '12450000', 'SANTO ANTONIO DO PINHAL', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3548302', '19190000', 'SANTO EXPEDITO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3548401', '16240000', 'SANTOPOLIS DO AGUAPEI', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3548500', '11010000', 'SANTOS', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3548609', '12490000', 'SAO BENTO DO SAPUCAI', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3548708', '09600000', 'SAO BERNARDO DO CAMPO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3548807', '09510000', 'SAO CAETANO DO SUL', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3548906', '13560001', 'SAO CARLOS', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3549003', '15710000', 'SAO FRANCISCO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3549102', '13870005', 'SAO JOAO DA BOA VISTA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3549201', '15640000', 'SAO JOAO DAS DUAS PONTES', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3549250', '15315000', 'SAO JOAO DE IRACEMA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3549300', '17970000', 'SAO JOAO DO PAU D''ALHO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3549409', '14600000', 'SAO JOAQUIM DA BARRA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3549508', '14440000', 'SAO JOSE DA BELA VISTA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3549607', '12830000', 'SAO JOSE DO BARREIRO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3549706', '13720000', 'SAO JOSE DO RIO PARDO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3549805', '15010010', 'SAO JOSE DO RIO PRETO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3549904', '12209000', 'SAO JOSE DOS CAMPOS', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3549953', '06890000', 'SAO LOURENCO DA SERRA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3550001', '12150000', 'SAO LUIS DO PARAITINGA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3550100', '18655000', 'SAO MANUEL', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3550209', '18230000', 'SAO MIGUEL ARCANJO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3550308', '01001000', 'SAO PAULO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3550407', '13520000', 'SAO PEDRO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3550506', '18940000', 'SAO PEDRO DO TURVO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3550605', '18130005', 'SAO ROQUE', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3550704', '11610000', 'SAO SEBASTIAO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3550803', '13790000', 'SAO SEBASTIAO DA GRAMA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3550902', '14200000', 'SAO SIMAO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3551009', '11310000', 'SAO VICENTE', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3551108', '18227000', 'SARAPUI', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3551207', '18840000', 'SARUTAIA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3551306', '15180000', 'SEBASTIANOPOLIS DO SUL', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3551405', '14230000', 'SERRA AZUL', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3551504', '14150000', 'SERRANA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3551603', '13930000', 'SERRA NEGRA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3551702', '14160005', 'SERTAOZINHO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3551801', '11910000', 'SETE BARRAS', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3551900', '14735000', 'SEVERINIA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3552007', '12690000', 'SILVEIRAS', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3552106', '13960000', 'SOCORRO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3552205', '18010000', 'SOROCABA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3552304', '15367000', 'SUD MENNUCCI', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3552403', '13170000', 'SUMARE', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3552502', '08610000', 'SUZANO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3552551', '15380000', 'SUZANAPOLIS', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3552601', '15880000', 'TABAPUA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3552700', '14915000', 'TABATINGA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3552809', '06753000', 'TABOAO DA SERRA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3552908', '19590000', 'TACIBA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3553005', '18890000', 'TAGUAI', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3553104', '14725000', 'TAIACU', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3553203', '14720000', 'TAIUVA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3553302', '13710000', 'TAMBAU', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3553401', '15175000', 'TANABI', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3553500', '18180000', 'TAPIRAI', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3553609', '13760000', 'TAPIRATIBA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3553658', '14765000', 'TAQUARAL', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3553708', '15905000', 'TAQUARITINGA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3553807', '18740000', 'TAQUARITUBA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3553856', '18425000', 'TAQUARIVAI', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3553906', '19210000', 'TARABAI', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3553955', '19820000', 'TARUMA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3554003', '18270000', 'TATUI', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3554102', '12010000', 'TAUBATE', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3554201', '18830000', 'TEJUPA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3554300', '19295000', 'TEODORO SAMPAIO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3554409', '14745000', 'TERRA ROXA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3554508', '18530000', 'TIETE', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3554607', '18860000', 'TIMBURI', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3554656', '18265000', 'TORRE DE PEDRA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3554706', '17360000', 'TORRINHA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3554755', '14935000', 'TRABIJU', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3554805', '12120000', 'TREMEMBE', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3554904', '15770000', 'TRES FRONTEIRAS', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3554953', '12930000', 'TUIUTI', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3555000', '17600005', 'TUPA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3555109', '17932000', 'TUPI PAULISTA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3555208', '15280000', 'TURIUBA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3555307', '15757000', 'TURMALINA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3555356', '15225000', 'UBARANA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3555406', '11690000', 'UBATUBA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3555505', '17440000', 'UBIRAJARA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3555604', '15890000', 'UCHOA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3555703', '15250000', 'UNIAO PAULISTA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3555802', '15760000', 'URANIA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3555901', '16650000', 'URU', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3556008', '15855000', 'URUPES', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3556107', '15520000', 'VALENTIM GENTIL', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3556206', '13270005', 'VALINHOS', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3556305', '16880000', 'VALPARAISO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3556354', '12935000', 'VARGEM', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3556404', '13880000', 'VARGEM GRANDE DO SUL', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3556453', '06730000', 'VARGEM GRANDE PAULISTA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3556503', '13220001', 'VARZEA PAULISTA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3556602', '17560000', 'VERA CRUZ', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3556701', '13280000', 'VINHEDO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3556800', '14740000', 'VIRADOURO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3556909', '15920000', 'VISTA ALEGRE DO ALTO', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3556958', '15705000', 'VITORIA BRASIL', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3557006', '18110005', 'VOTORANTIM', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3557105', '15500001', 'VOTUPORANGA', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3557154', '15265000', 'ZACARIAS', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3557204', '18980000', 'CHAVANTES', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('3557303', '13857000', 'ESTIVA GERBI', 'SP');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4100103', '86460000', 'ABATIA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4100202', '83490000', 'ADRIANOPOLIS', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4100301', '83855000', 'AGUDOS DO SUL', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4100400', '83501000', 'ALMIRANTE TAMANDARE', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4100459', '85280000', 'ALTAMIRA DO PARANA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4100509', '87552000', 'ALTONIA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4100608', '87755000', 'ALTO PARANA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4100707', '87588000', 'ALTO PIQUIRI', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4100806', '86155000', 'ALVORADA DO SUL', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4100905', '87855000', 'AMAPORA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4101002', '85643000', 'AMPERE', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4101051', '85425000', 'ANAHY', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4101101', '86383000', 'ANDIRA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4101150', '86755000', 'ANGULO', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4101200', '83380000', 'ANTONINA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4101309', '83980000', 'ANTONIO OLINTO', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4101408', '86800005', 'APUCARANA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4101507', '86701000', 'ARAPONGAS', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4101606', '84998000', 'ARAPOTI', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4101655', '86887000', 'ARAPUA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4101705', '87262000', 'ARARUNA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4101804', '83701000', 'ARAUCARIA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4101853', '86880000', 'ARIRANHA DO IVAI', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4101903', '86224000', 'ASSAI', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4102000', '85937000', 'ASSIS CHATEAUBRIAND', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4102109', '86742000', 'ASTORGA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4102208', '87630000', 'ATALAIA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4102307', '83670000', 'BALSA NOVA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4102406', '86365000', 'BANDEIRANTES', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4102505', '86968000', 'BARBOSA FERRAZ', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4102604', '85705000', 'BARRACAO', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4102703', '86385000', 'BARRA DO JACARE', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4102752', '85745000', 'BELA VISTA DA CAROBA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4102802', '86135000', 'BELA VISTA DO PARAISO', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4102901', '84650000', 'BITURUNA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4103008', '87390000', 'BOA ESPERANCA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4103024', '85680000', 'BOA ESPERANCA DO IGUACU', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4103040', '85225000', 'BOA VENTURA DE SAO ROQUE', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4103057', '85780000', 'BOA VISTA DA APARECIDA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4103107', '83450000', 'BOCAIUVA DO SUL', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4103156', '85708000', 'BOM JESUS DO SUL', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4103206', '86940000', 'BOM SUCESSO', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4103222', '85515000', 'BOM SUCESSO DO SUL', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4103305', '86925000', 'BORRAZOPOLIS', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4103354', '85430000', 'BRAGANEY', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4103370', '87595000', 'BRASILANDIA DO SUL', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4103404', '86640000', 'CAFEARA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4103453', '85415000', 'CAFELANDIA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4103479', '87569000', 'CAFEZAL DO SUL', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4103503', '86820000', 'CALIFORNIA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4103602', '86390000', 'CAMBARA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4103701', '86181000', 'CAMBE', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4103800', '86890000', 'CAMBIRA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4103909', '87349000', 'CAMPINA DA LAGOA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4103958', '85148000', 'CAMPINA DO SIMAO', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4104006', '83440000', 'CAMPINA GRANDE DO SUL', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4104055', '85450000', 'CAMPO BONITO', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4104105', '83870000', 'CAMPO DO TENENTE', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4104204', '83601000', 'CAMPO LARGO', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4104253', '83535000', 'CAMPO MAGRO', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4104303', '87300005', 'CAMPO MOURAO', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4104402', '84480000', 'CANDIDO DE ABREU', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4104428', '85140000', 'CANDOI', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4104451', '85160000', 'CANTAGALO', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4104501', '85767000', 'CAPANEMA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4104600', '85794000', 'CAPITAO LEONIDAS MARQUES', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4104659', '84145000', 'CARAMBEI', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4104709', '86425000', 'CARLOPOLIS', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4104808', '85801000', 'CASCAVEL', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4104907', '84165000', 'CASTRO', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4105003', '85470000', 'CATANDUVAS', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4105102', '86630000', 'CENTENARIO DO SUL', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4105201', '83580000', 'CERRO AZUL', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4105300', '85840000', 'CEU AZUL', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4105409', '85562000', 'CHOPINZINHO', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4105508', '87205000', 'CIANORTE', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4105607', '87820000', 'Nome GAUCHA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4105706', '85534000', 'CLEVELANDIA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4105805', '83401000', 'COLOMBO', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4105904', '86695000', 'COLORADO', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4106001', '86323000', 'CONGONHINHAS', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4106100', '86480000', 'CONSELHEIRO MAIRINCK', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4106209', '83740000', 'CONTENDA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4106308', '85422000', 'CORBELIA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4106407', '86305000', 'CORNELIO PROCOPIO', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4106456', '85559000', 'CORONEL DOMINGOS SOARES', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4106506', '85554000', 'CORONEL VIVIDA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4106555', '86970000', 'CORUMBATAI DO SUL', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4106571', '85598000', 'CRUZEIRO DO IGUACU', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4106605', '87408000', 'CRUZEIRO DO OESTE', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4106704', '87650000', 'CRUZEIRO DO SUL', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4106803', '84625000', 'CRUZ MACHADO', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4106852', '86857000', 'CRUZMALTINA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4106902', '80010000', 'CURITIBA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4107009', '84284000', 'CURIUVA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4107108', '87990000', 'DIAMANTE DO NORTE', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4107124', '85408000', 'DIAMANTE DO SUL', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4107157', '85896000', 'DIAMANTE D''OESTE', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4107207', '85668000', 'DOIS VIZINHOS', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4107256', '87485000', 'DOURADINA', 'PR');
            
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4107306', '87155000', 'DOUTOR CAMARGO', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4107405', '85634000', 'ENEAS MARQUES', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4107504', '87275000', 'ENGENHEIRO BELTRAO', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4107520', '87545000', 'ESPERANCA NOVA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4107538', '85988000', 'ENTRE RIOS DO OESTE', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4107546', '85465000', 'ESPIGAO ALTO DO IGUACU', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4107553', '87325000', 'FAROL', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4107603', '86842000', 'FAXINAL', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4107652', '83820000', 'FAZENDA RIO GRANDE', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4107702', '86955000', 'FENIX', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4107736', '84538000', 'FERNANDES PINHEIRO', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4107751', '84285000', 'FIGUEIRA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4107801', '87188000', 'FLORAI', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4107850', '85618000', 'FLOR DA SERRA DO SUL', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4107900', '87120000', 'FLORESTA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4108007', '86165000', 'FLORESTOPOLIS', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4108106', '86780000', 'FLORIDA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4108205', '85830000', 'FORMOSA DO OESTE', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4108304', '85851000', 'FOZ DO IGUACU', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4108320', '87575000', 'FRANCISCO ALVES', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4108403', '85601000', 'FRANCISCO BELTRAO', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4108452', '85145000', 'FOZ DO JORDAO', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4108502', '84664000', 'GENERAL CARNEIRO', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4108551', '86938000', 'GODOY MOREIRA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4108601', '87364000', 'GOIOERE', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4108650', '85167000', 'GOIOXIM', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4108700', '86847000', 'GRANDES RIOS', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4108809', '85985000', 'GUAIRA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4108908', '85113000', 'GUAIRACA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4108957', '84435000', 'GUAMIRANGA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4109005', '86465000', 'GUAPIRAMA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4109104', '87810000', 'GUAPOREMA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4109203', '86625000', 'GUARACI', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4109302', '85405000', 'GUARANIACU', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4109401', '85010000', 'GUARAPUAVA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4109500', '83395000', 'GUARAQUECABA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4109609', '83290000', 'GUARATUBA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4109658', '85548000', 'HONORIO SERPA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4109708', '84916000', 'IBAITI', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4109757', '85478000', 'IBEMA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4109807', '86200000', 'IBIPORA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4109906', '87532000', 'ICARAIMA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4110003', '86750000', 'IGUARACU', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4110052', '85423000', 'IGUATU', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4110078', '84250000', 'IMBAU', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4110102', '84433000', 'IMBITUVA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4110201', '85155000', 'INACIO MARTINS', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4110300', '87670000', 'INAJA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4110409', '87210000', 'INDIANOPOLIS', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4110508', '84450000', 'IPIRANGA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4110607', '87562000', 'IPORA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4110656', '85833000', 'IRACEMA DO OESTE', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4110706', '84515000', 'IRATI', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4110805', '87282000', 'IRETAMA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4110904', '86670000', 'ITAGUAJE', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4110953', '85883000', 'ITAIPULANDIA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4111001', '86378000', 'ITAMBARACA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4111100', '87175000', 'ITAMBE', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4111209', '85584000', 'ITAPEJARA D''OESTE', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4111258', '83560000', 'ITAPERUCU', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4111308', '87980000', 'ITAUNA DO SUL', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4111407', '84465000', 'IVAI', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4111506', '86878000', 'IVAIPORA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4111555', '87527000', 'IVATE', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4111605', '87130000', 'IVATUBA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4111704', '84930000', 'JABOTI', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4111803', '86400000', 'JACAREZINHO', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4111902', '86610000', 'JAGUAPITA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4112009', '84210000', 'JAGUARIAIVA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4112108', '86905000', 'JANDAIA DO SUL', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4112207', '87385000', 'JANIOPOLIS', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4112306', '84923000', 'JAPIRA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4112405', '87225000', 'JAPURA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4112504', '86860000', 'JARDIM ALEGRE', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4112603', '87690000', 'JARDIM OLINDA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4112702', '86213000', 'JATAIZINHO', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4112751', '85837000', 'JESUITAS', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4112801', '86457000', 'JOAQUIM TAVORA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4112900', '86470000', 'JUNDIAI DO SUL', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4112959', '87357000', 'JURANDA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4113007', '87230000', 'JUSSARA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4113106', '86923000', 'KALORE', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4113205', '83760000', 'LAPA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4113254', '85275000', 'LARANJAL', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4113304', '85301000', 'LARANJEIRAS DO SUL', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4113403', '86335000', 'LEOPOLIS', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4113429', '86865000', 'LIDIANOPOLIS', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4113452', '85826000', 'LINDOESTE', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4113502', '87900000', 'LOANDA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4113601', '86790000', 'LOBATO', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4113700', '86010000', 'LONDRINA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4113734', '87290000', 'LUIZIANA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4113759', '86935000', 'LUNARDELLI', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4113809', '86638000', 'LUPIONOPOLIS', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4113908', '84577000', 'MALLET', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4114005', '87340000', 'MAMBORE', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4114104', '87165000', 'MANDAGUACU', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4114203', '86975000', 'MANDAGUARI', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4114302', '83810000', 'MANDIRITUBA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4114351', '85628000', 'MANFRINOPOLIS', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4114401', '85545000', 'MANGUEIRINHA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4114500', '85265000', 'MANOEL RIBAS', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4114609', '85974000', 'MARECHAL CANDIDO RONDON', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4114708', '87483000', 'MARIA HELENA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4114807', '86994000', 'MARIALVA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4114906', '86826000', 'MARILANDIA DO SUL', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4115002', '87960000', 'MARILENA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4115101', '87475000', 'MARILUZ', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4115200', '87005000', 'MARINGA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4115309', '85526000', 'MARIOPOLIS', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4115358', '85958000', 'MARIPA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4115408', '85615000', 'MARMELEIRO', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4115457', '85168000', 'MARQUINHO', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4115507', '86910000', 'MARUMBI', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4115606', '85887000', 'MATELANDIA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4115705', '83260000', 'MATINHOS', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4115739', '85245000', 'MATO RICO', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4115754', '86828000', 'MAUA DA SERRA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4115804', '85884000', 'MEDIANEIRA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4115853', '85998000', 'MERCEDES', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4115903', '87840000', 'MIRADOR', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4116000', '86615000', 'MIRASELVA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4116059', '85890000', 'MISSAL', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4116109', '87375000', 'MOREIRA SALES', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4116208', '83360000', 'MORRETES', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4116307', '86765000', 'MUNHOZ DE MELO', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4116406', '86685000', 'NOSSA SENHORA DAS GRACAS', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4116505', '87790000', 'NOVA ALIANCA DO IVAI', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4116604', '86230000', 'NOVA AMERICA DA COLINA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4116703', '85412000', 'NOVA AURORA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4116802', '87335000', 'NOVA CANTU', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4116901', '87620000', 'NOVA ESPERANCA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4116950', '85635000', 'NOVA ESPERANCA DO SUDOESTE', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4117008', '86310000', 'NOVA FATIMA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4117057', '85370000', 'NOVA LARANJEIRAS', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4117107', '87975000', 'NOVA LONDRINA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4117206', '87490000', 'NOVA OLIMPIA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4117214', '86250000', 'NOVA SANTA BARBARA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4117222', '85931000', 'NOVA SANTA ROSA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4117255', '85685000', 'NOVA PRATA DO IGUACU', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4117271', '85255000', 'NOVA TEBAS', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4117297', '86895000', 'NOVO ITACOLOMI', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4117305', '84360000', 'ORTIGUEIRA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4117404', '87170000', 'OURIZONA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4117453', '85933000', 'OURO VERDE DO OESTE', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4117503', '87145000', 'PAICANDU', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4117602', '85556000', 'PALMAS', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4117701', '84135000', 'PALMEIRA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4117800', '85270000', 'PALMITAL', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4117909', '85952000', 'PALOTINA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4118006', '87780000', 'PARAISO DO NORTE', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4118105', '87665000', 'PARANACITY', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4118204', '83203000', 'PARANAGUA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4118303', '87680000', 'PARANAPOEMA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4118402', '87701000', 'PARANAVAI', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4118451', '85948000', 'PATO BRAGADO', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4118501', '85501000', 'PATO BRANCO', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4118600', '84630000', 'PAULA FREITAS', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4118709', '84638000', 'PAULO FRONTIN', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4118808', '87250000', 'PEABIRU', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4118857', '87538000', 'PEROBAL', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4118907', '87540000', 'PEROLA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4119004', '85743000', 'PEROLA D''OESTE', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4119103', '83860000', 'PIEN', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4119152', '83320005', 'PINHAIS', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4119202', '84928000', 'PINHALAO', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4119251', '85727000', 'PINHAL DE SAO BENTO', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4119301', '85190000', 'PINHAO', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4119400', '84240000', 'PIRAI DO SUL', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4119509', '83301000', 'PIRAQUARA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4119608', '85218000', 'PITANGA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4119657', '86613000', 'PITANGUEIRAS', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4119707', '87870000', 'PLANALTINA DO PARANA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4119806', '85756000', 'PLANALTO', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4119905', '84010000', 'PONTA GROSSA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4119954', '83255000', 'PONTAL DO PARANA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4120002', '86160000', 'PORECATU', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4120101', '84140000', 'PORTO AMAZONAS', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4120150', '85348000', 'PORTO BARREIRO', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4120200', '87950000', 'PORTO RICO', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4120309', '84610000', 'PORTO VITORIA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4120333', '86618000', 'PRADO FERREIRA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4120358', '85735000', 'PRANCHITA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4120408', '87180000', 'PRESIDENTE CASTELO BRANCO', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4120507', '86142000', 'PRIMEIRO DE MAIO', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4120606', '84410000', 'PRUDENTOPOLIS', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4120655', '87368000', 'QUARTO CENTENARIO', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4120705', '86450000', 'QUATIGUA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4120804', '83425000', 'QUATRO BARRAS', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4120853', '85940000', 'QUATRO PONTES', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4120903', '85460000', 'QUEDAS DO IGUACU', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4121000', '87940000', 'QUERENCIA DO NORTE', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4121109', '87267000', 'QUINTA DO SOL', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4121208', '83848000', 'QUITANDINHA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4121257', '85888000', 'RAMILANDIA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4121307', '86290000', 'RANCHO ALEGRE', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4121356', '87395000', 'RANCHO ALEGRE D''OESTE', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4121406', '85775000', 'REALEZA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4121505', '84550000', 'REBOUCAS', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4121604', '85613000', 'RENASCENCA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4121703', '84330000', 'RESERVA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4121752', '85198000', 'RESERVA DO IGUACU', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4121802', '86415000', 'RIBEIRAO CLARO', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4121901', '86495000', 'RIBEIRAO DO PINHAL', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4122008', '84560000', 'RIO AZUL', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4122107', '86835000', 'RIO BOM', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4122156', '85340000', 'RIO BONITO DO IGUACU', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4122172', '86848000', 'RIO BRANCO DO IVAI', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4122206', '83550000', 'RIO BRANCO DO SUL', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4122305', '83880000', 'RIO NEGRO', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4122404', '86607000', 'ROLANDIA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4122503', '87323000', 'RONCADOR', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4122602', '87805000', 'RONDON', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4122651', '86850000', 'ROSARIO DO IVAI', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4122701', '86728000', 'SABAUDIA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4122800', '85625000', 'SALGADO FILHO', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4122909', '84945000', 'SALTO DO ITARARE', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4123006', '85678000', 'SALTO DO LONTRA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4123105', '86370000', 'SANTA AMELIA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4123204', '86225000', 'SANTA CECILIA DO PAVAO', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4123303', '87925000', 'SANTA CRUZ DE MONTE CASTELO', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4123402', '86770000', 'SANTA FE', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4123501', '85894000', 'SANTA HELENA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4123600', '86660000', 'SANTA INES', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4123709', '87913000', 'SANTA ISABEL DO IVAI', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4123808', '85655000', 'SANTA IZABEL DO OESTE', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4123824', '85795000', 'SANTA LUCIA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4123857', '85235000', 'SANTA MARIA DO OESTE', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4123907', '86355000', 'SANTA MARIANA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4123956', '87915000', 'SANTA MONICA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4124004', '84970000', 'SANTANA DO ITARARE', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4124020', '85825000', 'SANTA TEREZA DO OESTE', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4124053', '85875000', 'SANTA TEREZINHA DE ITAIPU', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4124103', '86435000', 'SANTO ANTONIO DA PLATINA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4124202', '87730000', 'SANTO ANTONIO DO CAIUA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4124301', '86318000', 'SANTO ANTONIO DO PARAISO', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4124400', '85720000', 'SANTO ANTONIO DO SUDOESTE', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4124509', '86650000', 'SANTO INACIO', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4124608', '87775000', 'SAO CARLOS DO IVAI', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4124707', '86278000', 'SAO JERONIMO DA SERRA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4124806', '85572000', 'SAO JOAO', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4124905', '87740000', 'SAO JOAO DO CAIUA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4125001', '86931000', 'SAO JOAO DO IVAI', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4125100', '84155000', 'SAO JOAO DO TRIUNFO', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4125209', '85577000', 'SAO JORGE D''OESTE', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4125308', '87195000', 'SAO JORGE DO IVAI', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4125357', '87555000', 'SAO JORGE DO PATROCINIO', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4125407', '84980000', 'SAO JOSE DA BOA VISTA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4125456', '85898000', 'SAO JOSE DAS PALMEIRAS', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4125506', '83005000', 'SAO JOSE DOS PINHAIS', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4125555', '87215000', 'SAO MANOEL DO PARANA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4125605', '83910000', 'SAO MATEUS DO SUL', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4125704', '85879000', 'SAO MIGUEL DO IGUACU', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4125753', '85929000', 'SAO PEDRO DO IGUACU', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4125803', '86947000', 'SAO PEDRO DO IVAI', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4125902', '87957000', 'SAO PEDRO DO PARANA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4126009', '86240000', 'SAO SEBASTIAO DA AMOREIRA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4126108', '87220000', 'SAO TOME', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4126207', '84295000', 'SAPOPEMA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4126256', '87111000', 'SARANDI', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4126272', '85568000', 'SAUDADE DO IGUACU', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4126306', '84230000', 'SENGES', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4126355', '85886000', 'SERRANOPOLIS DO IGUACU', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4126405', '86345000', 'SERTANEJA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4126504', '86170000', 'SERTANOPOLIS', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4126603', '84943000', 'SIQUEIRA CAMPOS', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4126652', '85565000', 'SULINA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4126678', '86125000', 'TAMARANA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4126702', '87760000', 'TAMBOARA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4126801', '87440000', 'TAPEJARA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4126900', '87830000', 'TAPIRA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4127007', '84534000', 'TEIXEIRA SOARES', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4127106', '84261000', 'TELEMACO BORBA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4127205', '87245000', 'TERRA BOA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4127304', '87895000', 'TERRA RICA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4127403', '85995000', 'TERRA ROXA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4127502', '84315000', 'TIBAGI', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4127601', '83190000', 'TIJUCAS DO SUL', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4127700', '85900005', 'TOLEDO', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4127809', '84938000', 'TOMAZINA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4127858', '85485000', 'TRES BARRAS DO PARANA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4127882', '83485000', 'TUNAS DO PARANA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4127908', '87458000', 'TUNEIRAS DO OESTE', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4127957', '85945000', 'TUPASSI', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4127965', '85150000', 'TURVO', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4128005', '85445000', 'UBIRATA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4128104', '87501000', 'UMUARAMA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4128203', '84609000', 'UNIAO DA VITORIA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4128302', '87640000', 'UNIFLOR', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4128401', '86285000', 'URAI', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4128500', '84950000', 'WENCESLAU BRAZ', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4128534', '84345000', 'VENTANIA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4128559', '85845000', 'VERA CRUZ DO OESTE', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4128609', '85587000', 'VERE', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4128625', '87528000', 'VILA ALTA', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4128633', '83590000', 'DOUTOR ULYSSES', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4128658', '85390000', 'VIRMOND', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4128708', '85520000', 'VITORINO', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4128807', '87535000', 'XAMBRE', 'PR');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4200051', '89636000', 'ABDON BATISTA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4200101', '89830000', 'ABELARDO LUZ', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4200200', '88420000', 'AGROLANDIA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4200309', '89188000', 'AGRONOMICA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4200408', '89657000', 'AGUA DOCE', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4200507', '89883000', 'AGUAS DE CHAPECO', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4200556', '89843000', 'AGUAS FRIAS', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4200606', '88150000', 'AGUAS MORNAS', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4200705', '88452000', 'ALFREDO WAGNER', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4200754', '89730000', 'ALTO BELA VISTA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4200804', '89970000', 'ANCHIETA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4200903', '88463000', 'ANGELINA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4201000', '88595000', 'ANITA GARIBALDI', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4201109', '88475000', 'ANITAPOLIS', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4201208', '88180000', 'ANTONIO CARLOS', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4201257', '89135000', 'APIUNA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4201273', '89740000', 'ARABUTA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4201307', '89246000', 'ARAQUARI', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4201406', '88911000', 'ARARANGUA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4201505', '88740000', 'ARMAZEM', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4201604', '89590000', 'ARROIO TRINTA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4201653', '89778000', 'ARVOREDO', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4201703', '89138000', 'ASCURRA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4201802', '88410000', 'ATALANTA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4201901', '89186000', 'AURORA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4201950', '88914000', 'BALNEARIO ARROIO DO SILVA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4202008', '88330000', 'BALNEARIO CAMBORIU', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4202057', '89247000', 'BALNEARIO BARRA DO SUL', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4202073', '88955000', 'BALNEARIO GAIVOTA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4202081', '89905000', 'BANDEIRANTE', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4202099', '89909000', 'BARRA BONITA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4202107', '88390000', 'BARRA VELHA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4202131', '89478000', 'BELA VISTA DO TOLDO', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4202156', '89925000', 'BELMONTE', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4202206', '89125000', 'BENEDITO NOVO', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4202305', '88165000', 'BIGUACU', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4202404', '89010000', 'BLUMENAU', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4202438', '88538000', 'BOCAINA DO SUL', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4202453', '88215000', 'BOMBINHAS', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4202503', '88640000', 'BOM JARDIM DA SERRA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4202537', '89824000', 'BOM JESUS', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4202578', '89873000', 'BOM JESUS DO OESTE', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4202602', '88688000', 'BOM RETIRO', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4202701', '88370000', 'BOTUVERA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4202800', '88750000', 'BRACO DO NORTE', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4202859', '89178000', 'BRACO DO TROMBUDO', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4202875', '89635000', 'BRUNOPOLIS', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4202909', '88350001', 'BRUSQUE', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4203006', '89513000', 'CACADOR', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4203105', '89888000', 'CAIBI', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4203154', '89430000', 'CALMON', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4203204', '88348000', 'CAMBORIU', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4203253', '88548000', 'CAPAO ALTO', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4203303', '89294600', 'CAMPO ALEGRE', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4203402', '88580000', 'CAMPO BELO DO SUL', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4203501', '89980000', 'CAMPO ERE', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4203600', '89628000', 'CAMPOS NOVOS', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4203709', '88230000', 'CANELINHA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4203808', '89473000', 'CANOINHAS', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4203907', '89666000', 'CAPINZAL', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4203956', '88745000', 'CAPIVARI DE BAIXO', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4204004', '89670000', 'CATANDUVAS', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4204103', '89880000', 'CAXAMBU DO SUL', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4204152', '88598000', 'CELSO RAMOS', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4204178', '88585000', 'CERRO NEGRO', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4204194', '88407000', 'CHAPADAO DO LAGEADO', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4204202', '89801000', 'CHAPECO', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4204251', '88845000', 'COCAL DO SUL', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4204301', '89720000', 'CONCORDIA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4204350', '89819000', 'CORDILHEIRA ALTA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4204400', '89840000', 'CORONEL FREITAS', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4204459', '89837000', 'CORONEL MARTINS', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4204509', '89280000', 'CORUPA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4204558', '88535000', 'CORREIA PINTO', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4204608', '88801000', 'CRICIUMA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4204707', '89890000', 'CUNHA PORA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4204756', '89886000', 'CUNHATAI', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4204806', '89528000', 'CURITIBANOS', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4204905', '89913000', 'DESCANSO', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4205001', '89960000', 'DIONISIO CERQUEIRA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4205100', '89155000', 'DONA EMMA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4205159', '89126000', 'DOUTOR PEDRINHO', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4205175', '89862000', 'ENTRE RIOS', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4205191', '88935000', 'ERMO', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4205209', '89615000', 'ERVAL VELHO', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4205308', '89696000', 'FAXINAL DOS GUEDES', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4205357', '89878000', 'FLOR DO SERTAO', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4205407', '88010000', 'FLORIANOPOLIS', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4205431', '89859000', 'FORMOSA DO SUL', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4205456', '88850000', 'FORQUILHINHA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4205506', '89580000', 'FRAIBURGO', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4205555', '89530000', 'FREI ROGERIO', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4205605', '89838000', 'GALVAO', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4205704', '88495000', 'GAROPABA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4205803', '89248000', 'GARUVA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4205902', '89110000', 'GASPAR', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4206009', '88190000', 'GOVERNADOR CELSO RAMOS', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4206108', '88892000', 'GRAO PARA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4206207', '88735000', 'GRAVATAL', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4206306', '88360000', 'GUABIRUBA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4206405', '89920000', 'GUARACIABA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4206504', '89270000', 'GUARAMIRIM', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4206603', '89940000', 'GUARUJA DO SUL', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4206652', '89817500', 'GUATAMBU', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4206702', '89610000', 'HERVAL D''OESTE', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4206751', '89652000', 'IBIAM', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4206801', '89640000', 'IBICARE', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4206900', '89143000', 'IBIRAMA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4207007', '88820000', 'ICARA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4207106', '88320000', 'ILHOTA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4207205', '88775000', 'IMARUI', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4207304', '88782000', 'IMBITUBA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4207403', '88440000', 'IMBUIA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4207502', '89130000', 'INDAIAL', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4207577', '89558000', 'IOMERE', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4207601', '89669000', 'IPIRA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4207650', '89899000', 'IPORA DO OESTE', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4207684', '89832000', 'IPUACU', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4207700', '89790000', 'IPUMIRIM', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4207759', '89892000', 'IRACEMINHA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4207809', '89680000', 'IRANI', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4207858', '89856000', 'IRATI', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4207908', '89450000', 'IRINEOPOLIS', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4208005', '89760000', 'ITA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4208104', '89346000', 'ITAIOPOLIS', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4208203', '88301000', 'ITAJAI', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4208302', '88220000', 'ITAPEMA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4208401', '89896000', 'ITAPIRANGA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4208450', '89249000', 'ITAPOA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4208500', '88403000', 'ITUPORANGA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4208609', '89677000', 'JABORA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4208708', '88950000', 'JACINTO MACHADO', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4208807', '88715000', 'JAGUARUNA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4208906', '89251000', 'JARAGUA DO SUL', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4208955', '89848000', 'JARDINOPOLIS', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4209003', '89607000', 'JOACABA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4209102', '89201000', 'JOINVILLE', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4209151', '89145000', 'JOSE BOITEUX', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4209177', '89839000', 'JUPIA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4209201', '89660000', 'LACERDOPOLIS', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4209300', '88501000', 'LAGES', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4209409', '88798000', 'LAGUNA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4209458', '89828000', 'LAJEADO GRANDE', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4209508', '89170000', 'LAURENTINO', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4209607', '88882000', 'LAURO MULLER', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4209706', '89517000', 'LEBON REGIS', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4209805', '88445000', 'LEOBERTO LEAL', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4209854', '89735000', 'LINDOIA DO SUL', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4209904', '89182000', 'LONTRAS', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4210001', '89115000', 'LUIZ ALVES', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4210035', '89609000', 'LUZERNA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4210050', '89518000', 'MACIEIRA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4210100', '89320000', 'MAFRA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4210209', '88265000', 'MAJOR GERCINO', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4210308', '89480000', 'MAJOR VIEIRA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4210407', '88915000', 'MARACAJA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4210506', '89874000', 'MARAVILHA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4210555', '89860000', 'MAREMA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4210605', '89108000', 'MASSARANDUBA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4210704', '89420000', 'MATOS COSTA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4210803', '88923000', 'MELEIRO', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4210852', '89194000', 'MIRIM DOCE', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4210902', '89872000', 'MODELO', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4211009', '89893000', 'MONDAI', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4211058', '89618000', 'MONTE CARLO', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4211108', '89384000', 'MONTE CASTELO', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4211207', '88835000', 'MORRO DA FUMACA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4211256', '88925000', 'MORRO GRANDE', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4211306', '88378000', 'NAVEGANTES', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4211405', '89865000', 'NOVA ERECHIM', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4211454', '89818000', 'NOVA ITABERABA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4211504', '88280000', 'NOVA TRENTO', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4211603', '88867000', 'NOVA VENEZA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4211652', '89998000', 'NOVO HORIZONTE', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4211702', '88873000', 'ORLEANS', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4211751', '88540000', 'OTACILIO COSTA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4211801', '89664000', 'OURO', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4211850', '89923000', 'OURO VERDE', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4211876', '89765000', 'PAIAL', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4211892', '88543000', 'PAINEL', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4211900', '88130005', 'PALHOCA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4212007', '89985000', 'PALMA SOLA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4212056', '88545000', 'PALMEIRA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4212106', '89887700', 'PALMITOS', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4212205', '89375000', 'PAPANDUVA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4212239', '89907000', 'PARAISO', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4212254', '88980000', 'PASSO DE TORRES', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4212270', '89687000', 'PASSOS MAIA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4212304', '88490000', 'PAULO LOPES', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4212403', '88725000', 'PEDRAS GRANDES', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4212502', '88385000', 'PENHA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4212601', '89750000', 'PERITIBA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4212700', '88435000', 'PETROLANDIA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4212809', '88380000', 'PICARRAS', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4212908', '89870000', 'PINHALZINHO', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4213005', '89570000', 'PINHEIRO PRETO', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4213104', '89668000', 'PIRATUBA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4213153', '89882000', 'PLANALTO ALEGRE', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4213203', '89107000', 'POMERODE', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4213302', '88550000', 'PONTE ALTA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4213351', '89535000', 'PONTE ALTA DO NORTE', 'SC');
            
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4213401', '89685000', 'PONTE SERRADA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4213500', '88210000', 'PORTO BELO', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4213609', '89415000', 'PORTO UNIAO', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4213708', '89173000', 'POUSO REDONDO', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4213807', '88993000', 'PRAIA GRANDE', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4213906', '89745000', 'PRESIDENTE CASTELO BRANCO', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4214003', '89153000', 'PRESIDENTE GETULIO', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4214102', '89184000', 'PRESIDENTE NEREU', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4214151', '89935000', 'PRINCESA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4214201', '89850000', 'QUILOMBO', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4214300', '88474000', 'RANCHO QUEIMADO', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4214409', '89555000', 'RIO DAS ANTAS', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4214508', '89198000', 'RIO DO CAMPO', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4214607', '89180000', 'RIO DO OESTE', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4214706', '89122000', 'RIO DOS CEDROS', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4214805', '89160000', 'RIO DO SUL', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4214904', '88760000', 'RIO FORTUNA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4215000', '89298000', 'RIO NEGRINHO', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4215059', '88658000', 'RIO RUFINO', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4215075', '89895000', 'RIQUEZA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4215109', '89136000', 'RODEIO', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4215208', '89908000', 'ROMELANDIA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4215307', '89196000', 'SALETE', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4215356', '89981000', 'SALTINHO', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4215406', '89595000', 'SALTO VELOSO', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4215455', '88717000', 'SANGAO', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4215505', '89540000', 'SANTA CECILIA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4215554', '89608000', 'SANTA HELENA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4215604', '88763000', 'SANTA ROSA DE LIMA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4215653', '88965000', 'SANTA ROSA DO SUL', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4215679', '89199000', 'SANTA TEREZINHA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4215687', '89983000', 'SANTA TEREZINHA DO PROGRESSO', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4215695', '89854000', 'SANTIAGO DO SUL', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4215703', '88140000', 'SANTO AMARO DA IMPERATRIZ', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4215752', '89982000', 'SAO BERNARDINO', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4215802', '89290000', 'SAO BENTO DO SUL', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4215901', '88485000', 'SAO BONIFACIO', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4216008', '89885000', 'SAO CARLOS', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4216057', '89533000', 'SAO CRISTOVAO DO SUL', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4216107', '89836000', 'SAO DOMINGOS', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4216206', '89243000', 'SAO FRANCISCO DO SUL', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4216255', '89897000', 'SAO JOAO DO OESTE', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4216305', '88245000', 'SAO JOAO BATISTA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4216354', '88395000', 'SAO JOAO DO ITAPERIU', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4216404', '88975000', 'SAO JOAO DO SUL', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4216503', '88615000', 'SAO JOAQUIM', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4216602', '88101000', 'SAO JOSE', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4216701', '89933000', 'SAO JOSE DO CEDRO', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4216800', '88570000', 'SAO JOSE DO CERRITO', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4216909', '89994000', 'SAO LOURENCO DO OESTE', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4217006', '88730000', 'SAO LUDGERO', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4217105', '88766000', 'SAO MARTINHO', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4217154', '89879000', 'SAO MIGUEL DA BOA VISTA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4217204', '89904000', 'SAO MIGUEL DO OESTE', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4217253', '88125000', 'SAO PEDRO DE ALCANTARA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4217303', '89868000', 'SAUDADES', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4217402', '89275000', 'SCHROEDER', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4217501', '89772000', 'SEARA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4217550', '89871000', 'SERRA ALTA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4217600', '88860000', 'SIDEROPOLIS', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4217709', '88964000', 'SOMBRIO', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4217758', '89855000', 'SUL BRASIL', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4217808', '89192000', 'TAIO', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4217907', '89648000', 'TANGARA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4217956', '89875000', 'TIGRINHOS', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4218004', '88200000', 'TIJUCAS', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4218103', '88940000', 'TIMBE DO SUL', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4218202', '89120000', 'TIMBO', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4218251', '89545000', 'TIMBO GRANDE', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4218301', '89495000', 'TRES BARRAS', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4218350', '88862000', 'TREVISO', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4218400', '88712000', 'TREZE DE MAIO', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4218509', '89650000', 'TREZE TILIAS', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4218608', '89176000', 'TROMBUDO CENTRAL', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4218707', '88701000', 'TUBARAO', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4218756', '89898000', 'TUNAPOLIS', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4218806', '88934000', 'TURVO', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4218855', '89845000', 'UNIAO DO OESTE', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4218905', '88655000', 'URUBICI', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4218954', '88625000', 'URUPEMA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4219002', '88840000', 'URUSSANGA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4219101', '89690000', 'VARGEAO', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4219150', '89638000', 'VARGEM', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4219176', '89675000', 'VARGEM BONITA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4219200', '88443000', 'VIDAL RAMOS', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4219309', '89566000', 'VIDEIRA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4219358', '89149000', 'VITOR MEIRELES', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4219408', '89157000', 'WITMARSUM', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4219507', '89822000', 'XANXERE', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4219606', '89785000', 'XAVANTINA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4219705', '89825000', 'XAXIM', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4219853', '89633000', 'ZORTEA', 'SC');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4300059', '99965000', 'AGUA SANTA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4300109', '96540000', 'AGUDO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4300208', '98753000', 'AJURICABA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4300307', '98950000', 'ALECRIM', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4300406', '97541000', 'ALEGRETE', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4300455', '98907000', 'ALEGRIA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4300505', '98490000', 'ALPESTRE', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4300554', '96380000', 'ALTO ALEGRE', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4300570', '95773000', 'ALTO FELIZ', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4300604', '94810000', 'ALVORADA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4300638', '96635000', 'AMARAL FERRADOR', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4300646', '98465000', 'AMETISTA DO SUL', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4300661', '95312000', 'ANDRE DA ROCHA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4300703', '95980000', 'ANTA GORDA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4300802', '95250000', 'ANTONIO PRADO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4300851', '96178000', 'ARAMBARE', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4300877', '93880000', 'ARARICA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4300901', '99775000', 'ARATIBA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4301008', '95940000', 'ARROIO DO MEIO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4301057', '95585000', 'ARROIO DO SAL', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4301107', '96740000', 'ARROIO DOS RATOS', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4301206', '96980000', 'ARROIO DO TIGRE', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4301305', '99455000', 'ARROIO GRANDE', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4301404', '95995000', 'ARVOREZINHA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4301503', '98745000', 'AUGUSTO PESTANA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4301552', '99835000', 'AUREA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4301602', '96400003', 'BAGE', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4301636', '95599000', 'BALNEARIO PINHAL', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4301651', '95733000', 'BARAO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4301701', '99740000', 'BARAO DE COTEGIPE', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4301750', '96735000', 'BARAO DO TRIUNFO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4301800', '95375000', 'BARRACAO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4301859', '98530000', 'BARRA DO GUARITA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4301875', '97538000', 'BARRA DO QUARAI', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4301909', '96790000', 'BARRA DO RIBEIRO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4301925', '99795000', 'BARRA DO RIO AZUL', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4301958', '99585000', 'BARRA FUNDA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4302006', '99360000', 'BARROS CASSAL', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4302055', '99650000', 'BENJAMIN CONSTANT DO SUL', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4302105', '95713000', 'BENTO GONCALVES', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4302154', '98335000', 'BOA VISTA DAS MISSOES', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4302204', '98918000', 'BOA VISTA DO BURICA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4302253', '95727000', 'BOA VISTA DO SUL', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4302303', '95296000', 'BOM JESUS', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4302352', '95765000', 'BOM PRINCIPIO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4302378', '98575000', 'BOM PROGRESSO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4302402', '95870000', 'BOM RETIRO DO SUL', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4302451', '95920000', 'BOQUEIRAO DO LEAO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4302501', '97855000', 'BOSSOROCA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4302600', '98565000', 'BRAGA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4302659', '95790000', 'BROCHIER', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4302709', '96753000', 'BUTIA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4302808', '96578000', 'CACAPAVA DO SUL', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4302907', '97460000', 'CACEQUI', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4303004', '96500000', 'CACHOEIRA DO SUL', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4303103', '94910000', 'CACHOEIRINHA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4303202', '99865000', 'CACIQUE DOBLE', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4303301', '97930000', 'CAIBATE', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4303400', '98445000', 'CAICARA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4303509', '96188000', 'CAMAQUA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4303558', '99165000', 'CAMARGO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4303608', '95495000', 'CAMBARA DO SUL', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4303673', '95255000', 'CAMPESTRE DA SERRA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4303707', '98975000', 'CAMPINA DAS MISSOES', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4303806', '99660000', 'CAMPINAS DO SUL', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4303905', '93700000', 'CAMPO BOM', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4304002', '99372000', 'CAMPO NOVO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4304101', '99435000', 'CAMPOS BORGES', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4304200', '96935000', 'CANDELARIA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4304309', '98970000', 'CANDIDO GODOI', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4304358', '96495000', 'CANDIOTA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4304408', '95680000', 'CANELA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4304507', '96600000', 'CANGUCU', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4304606', '92010000', 'CANOAS', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4304630', '95558000', 'CAPAO DA CANOA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4304663', '96163000', 'CAPAO DO LEAO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4304671', '95552000', 'CAPIVARI DO SUL', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4304689', '95745000', 'CAPELA DE SANTANA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4304697', '95935000', 'CAPITAO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4304705', '99522000', 'CARAZINHO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4304713', '95515000', 'CARAA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4304804', '95186000', 'CARLOS BARBOSA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4304853', '99825000', 'CARLOS GOMES', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4304903', '99262000', 'CASCA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4304952', '95315000', 'CASEIROS', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4305009', '98777000', 'CATUIPE', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4305108', '95010000', 'CAXIAS DO SUL', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4305116', '98313000', 'CENTENARIO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4305124', '96395000', 'CERRITO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4305132', '96535000', 'CERRO BRANCO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4305157', '98340000', 'CERRO GRANDE', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4305173', '96770000', 'CERRO GRANDE DO SUL', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4305207', '97913000', 'CERRO LARGO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4305306', '99555000', 'CHAPADA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4305355', '96745000', 'CHARQUEADAS', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4305371', '99960000', 'CHARRUA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4305405', '98760000', 'CHIAPETA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4305439', '96255000', 'CHUI', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4305447', '96193000', 'CHUVISCA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4305454', '95598000', 'CIDREIRA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4305504', '99975000', 'CIRIACO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4305587', '95895000', 'COLINAS', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4305603', '99460000', 'COLORADO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4305702', '98290000', 'CONDOR', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4305801', '99686000', 'CONSTANTINA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4305850', '99528000', 'COQUEIROS DO SUL', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4305871', '98735000', 'CORONEL BARROS', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4305900', '98583000', 'CORONEL BICACO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4305959', '95338000', 'COTIPORA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4305975', '99145000', 'COXILHA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4306007', '98655000', 'CRISSIUMAL', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4306056', '96195000', 'CRISTAL', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4306072', '98368000', 'CRISTAL DO SUL', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4306106', '98005000', 'CRUZ ALTA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4306205', '95930000', 'CRUZEIRO DO SUL', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4306304', '99980000', 'DAVID CANABARRO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4306320', '98528000', 'DERRUBADAS', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4306353', '97845000', 'DEZESSEIS DE NOVEMBRO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4306379', '97180000', 'DILERMANDO DE AGUIAR', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4306403', '93950000', 'DOIS IRMAOS', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4306429', '98385000', 'DOIS IRMAOS DAS MISSOES', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4306452', '99220000', 'DOIS LAJEADOS', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4306502', '94350000', 'DOM FELICIANO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4306551', '95568000', 'DOM PEDRO DE ALCANTARA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4306601', '96455000', 'DOM PEDRITO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4306700', '97280000', 'DONA FRANCISCA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4306734', '98926000', 'DOUTOR MAURICIO CARDOSO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4306759', '95967000', 'DOUTOR RICARDO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4306767', '92990000', 'ELDORADO DO SUL', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4306809', '95964000', 'ENCANTADO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4306908', '96610000', 'ENCRUZILHADA DO SUL', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4306924', '99698000', 'ENGENHO VELHO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4306932', '98857000', 'ENTRE-IJUIS', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4306957', '99645000', 'ENTRE RIOS DO SUL', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4306973', '99920000', 'EREBANGO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4307005', '99717000', 'ERECHIM', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4307054', '99140000', 'ERNESTINA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4307104', '96320000', 'HERVAL', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4307203', '99752000', 'ERVAL GRANDE', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4307302', '98393000', 'ERVAL SECO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4307401', '95388000', 'ESMERALDA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4307450', '98635000', 'ESPERANCA DO SUL', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4307500', '99425000', 'ESPUMOSO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4307559', '99930000', 'ESTACAO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4307609', '93600000', 'ESTANCIA VELHA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4307708', '93260000', 'ESTEIO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4307807', '95884000', 'ESTRELA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4307815', '96990000', 'ESTRELA VELHA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4307831', '98860000', 'EUGENIO DE CASTRO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4307864', '95333000', 'FAGUNDES VARELA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4307906', '95181000', 'FARROUPILHA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4308003', '97220000', 'FAXINAL DO SOTURNO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4308052', '99655000', 'FAXINALZINHO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4308078', '95875000', 'FAZENDA VILANOVA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4308102', '95770000', 'FELIZ', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4308201', '95272000', 'FLORES DA CUNHA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4308250', '99910000', 'FLORIANO PEIXOTO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4308300', '99375000', 'FONTOURA XAVIER', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4308409', '97210000', 'FORMIGUEIRO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4308458', '98125000', 'FORTALEZA DOS VALOS', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4308508', '98405000', 'FREDERICO WESTPHALEN', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4308607', '95724000', 'GARIBALDI', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4308656', '97690000', 'GARRUCHOS', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4308706', '99833000', 'GAURAMA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4308805', '95830000', 'GENERAL CAMARA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4308854', '99160000', 'GENTIL', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4308904', '99904000', 'GETULIO VARGAS', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4309001', '98885000', 'GIRUA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4309050', '94380000', 'GLORINHA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4309100', '95670000', 'GRAMADO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4309126', '99605000', 'GRAMADO DOS LOUREIROS', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4309159', '96875000', 'GRAMADO XAVIER', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4309209', '94010000', 'GRAVATAI', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4309258', '95355000', 'GUABIJU', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4309308', '92800000', 'GUAIBA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4309407', '99200000', 'GUAPORE', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4309506', '97950000', 'GUARANI DAS MISSOES', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4309555', '95785000', 'HARMONIA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4309571', '96888000', 'HERVEIRAS', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4309605', '98922000', 'HORIZONTINA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4309654', '96465000', 'HULHA NEGRA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4309704', '98670000', 'HUMAITA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4309753', '96925000', 'IBARAMA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4309803', '99945000', 'IBIACA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4309902', '95307000', 'IBIRAIARAS', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4309951', '99320000', 'IBIRAPUITA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4310009', '98210000', 'IBIRUBA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4310108', '99515000', 'IGREJINHA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4310207', '98713000', 'IJUI', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4310306', '95990000', 'ILOPOLIS', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4310330', '95625000', 'IMBE', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4310363', '95888000', 'IMIGRANTE', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4310405', '98917000', 'INDEPENDENCIA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4310413', '98765000', 'INHACORA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4310439', '95244000', 'IPE', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4310462', '99925000', 'IPIRANGA DO SUL', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4310504', '98460000', 'IRAI', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4310538', '97185000', 'ITAARA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4310553', '97720000', 'ITACURUBI', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4310579', '95983000', 'ITAPUCA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4310603', '97653000', 'ITAQUI', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4310702', '99768000', 'ITATIBA DO SUL', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4310751', '98160000', 'IVORA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4310801', '93900000', 'IVOTI', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4310850', '98355000', 'JABOTICABA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4310900', '99730000', 'JACUTINGA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4311007', '96300000', 'JAGUARAO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4311106', '97763000', 'JAGUARI', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4311122', '95430000', 'JAQUIRANA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4311130', '98175000', 'JARI', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4311155', '98180000', 'JOIA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4311205', '98130000', 'JULIO DE CASTILHOS', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4311254', '99340000', 'LAGOAO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4311270', '99495000', 'LAGOA DOS TRES CANTOS', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4311304', '95302000', 'LAGOA VERMELHA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4311403', '95914000', 'LAJEADO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4311429', '98320000', 'LAJEADO DO BUGRE', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4311502', '97395000', 'LAVRAS DO SUL', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4311601', '99695000', 'LIBERATO SALZANO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4311627', '93940000', 'LINDOLFO COLLOR', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4311643', '95768000', 'LINHA NOVA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4311700', '99885000', 'MACHADINHO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4311718', '97645000', 'MACAMBARA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4311734', '95572000', 'MAMPITUBA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4311759', '97640000', 'MANOEL VIANA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4311775', '95532000', 'MAQUINE', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4311791', '95793000', 'MARATA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4311809', '99150000', 'MARAU', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4311908', '99805000', 'MARCELINO RAMOS', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4311981', '92900000', 'MARIANA PIMENTEL', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4312005', '99790000', 'MARIANO MORO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4312054', '95923000', 'MARQUES DE SOUZA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4312104', '97415000', 'MATA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4312138', '99185000', 'MATO CASTELHANO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4312153', '95835000', 'MATO LEITAO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4312203', '99890000', 'MAXIMILIANO DE ALMEIDA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4312252', '96755000', 'MINAS DO LEAO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4312302', '98545000', 'MIRAGUAI', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4312351', '99255000', 'MONTAURI', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4312377', '95236000', 'MONTE ALEGRE DOS CAMPOS', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4312385', '95718000', 'MONTE BELO DO SUL', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4312401', '95780000', 'MONTENEGRO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4312427', '99315000', 'MORMACO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4312443', '95577000', 'MORRINHOS DO SUL', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4312450', '96150000', 'MORRO REDONDO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4312476', '93990000', 'MORRO REUTER', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4312500', '96280000', 'MOSTARDAS', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4312609', '95970000', 'MUCUM', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4312617', '95230000', 'MUITOS CAPOES', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4312625', '99990000', 'MULITERNO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4312658', '99480000', 'NAO-ME-TOQUE', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4312674', '99175000', 'NICOLAU VERGUEIRO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4312708', '99600000', 'NONOAI', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4312757', '95987000', 'NOVA ALVORADA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4312807', '95350000', 'NOVA ARACA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4312906', '95340000', 'NOVA BASSANO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4312955', '99580000', 'NOVA BOA VISTA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4313003', '95950000', 'NOVA BRESCIA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4313011', '98919000', 'NOVA CANDELARIA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4313037', '97770000', 'NOVA ESPERANCA DO SUL', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4313060', '93893000', 'NOVA HARTZ', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4313086', '95275000', 'NOVA PADUA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4313102', '97270000', 'NOVA PALMA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4313201', '95170000', 'NOVA PETROPOLIS', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4313300', '95322000', 'NOVA PRATA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4313334', '98758000', 'NOVA RAMADA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4313359', '95260000', 'NOVA ROMA DO SUL', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4313375', '92480000', 'NOVA SANTA RITA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4313391', '96550000', 'NOVO CABRAIS', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4313409', '93310001', 'NOVO HAMBURGO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4313425', '98955000', 'NOVO MACHADO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4313441', '98370000', 'NOVO TIRADENTES', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4313490', '98338000', 'NOVO BARREIRO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4313508', '95527000', 'OSORIO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4313607', '99850000', 'PAIM FILHO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4313656', '95549000', 'PALMARES DO SUL', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4313706', '98319000', 'PALMEIRA DAS MISSOES', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4313805', '98430000', 'PALMITINHO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4313904', '98280000', 'PANAMBI', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4313953', '96695000', 'PANTANO GRANDE', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4314001', '95360000', 'PARAI', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4314027', '96530000', 'PARAISO DO SUL', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4314035', '95783000', 'PARECI NOVO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4314050', '95640000', 'PAROBE', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4314068', '96908000', 'PASSA SETE', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4314076', '96685000', 'PASSO DO SOBRADO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4314100', '99010000', 'PASSO FUNDO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4314159', '95865000', 'PAVERAMA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4314209', '96390000', 'PEDRO OSORIO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4314308', '98270000', 'PEJUCARA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4314407', '96010000', 'PELOTAS', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4314423', '95175000', 'PICADA CAFE', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4314456', '99307000', 'PINHAL', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4314472', '98150000', 'PINHAL GRANDE', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4314498', '98435000', 'PINHEIRINHO DO VALE', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4314506', '97990000', 'PINHEIRO MACHADO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4314555', '97885000', 'PIRAPO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4314605', '96490000', 'PIRATINI', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4314704', '98474000', 'PLANALTO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4314753', '95740000', 'POCO DAS ANTAS', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4314779', '99190000', 'PONTAO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4314787', '99735000', 'PONTE PRETA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4314803', '93180000', 'PORTAO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4314902', '90010000', 'PORTO ALEGRE', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4315008', '98980000', 'PORTO LUCENA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4315057', '98947000', 'PORTO MAUA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4315073', '98985000', 'PORTO VERA CRUZ', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4315107', '98995000', 'PORTO XAVIER', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4315131', '95945000', 'POUSO NOVO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4315149', '93945000', 'PRESIDENTE LUCENA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4315156', '95926000', 'PROGRESSO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4315172', '95345000', 'PROTASIO ALVES', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4315206', '95975000', 'PUTINGA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4315305', '97560000', 'QUARAI', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4315321', '98140000', 'QUEVEDOS', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4315354', '98234000', 'QUINZE DE NOVEMBRO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4315404', '98555000', 'REDENTORA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4315453', '95965000', 'RELVADO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4315503', '98829000', 'RESTINGA SECA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4315552', '99610000', 'RIO DOS INDIOS', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4315602', '96200003', 'RIO GRANDE', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4315701', '96670000', 'RIO PARDO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4315750', '95695000', 'RIOZINHO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4315800', '95735000', 'ROCA SALES', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4315909', '98365000', 'RODEIO BONITO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4316006', '95693000', 'ROLANTE', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4316105', '99673000', 'RONDA ALTA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4316204', '99590000', 'RONDINHA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4316303', '97973000', 'ROQUE GONZALES', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4316402', '97594000', 'ROSARIO DO SUL', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4316428', '98333000', 'SAGRADA FAMILIA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4316436', '98255000', 'SALDANHA MARINHO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4316451', '99447000', 'SALTO DO JACUI', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4316477', '97945000', 'SALVADOR DAS MISSOES', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4316501', '95751000', 'SALVADOR DO SUL', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4316600', '99845000', 'SANANDUVA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4316709', '98240000', 'SANTA BARBARA DO SUL', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4316758', '95915000', 'SANTA CLARA DO SUL', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4316808', '96810000', 'SANTA CRUZ DO SUL', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4316907', '97010000', 'SANTA MARIA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4316956', '93995000', 'SANTA MARIA DO HERVAL', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4317004', '96590000', 'SANTANA DA BOA VISTA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4317103', '97571000', 'SANTANA DO LIVRAMENTO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4317202', '95544000', 'SANTA ROSA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4317251', '98778000', 'SANTA TEREZA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4317301', '96240000', 'SANTA VITORIA DO PALMAR', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4317400', '97733000', 'SANTIAGO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4317509', '98800000', 'SANTO ANGELO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4317558', '99265000', 'SANTO ANTONIO DO PALMA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4317608', '95508000', 'SANTO ANTONIO DA PATRULHA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4317707', '97875000', 'SANTO ANTONIO DAS MISSOES', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4317756', '99525000', 'SANTO ANTONIO DO PLANALTO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4317806', '98594000', 'SANTO AUGUSTO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4317905', '98968000', 'SANTO CRISTO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4317954', '99895000', 'SANTO EXPEDITO DO SUL', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4318002', '97680000', 'SAO BORJA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4318051', '99270000', 'SAO DOMINGOS DO SUL', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4318101', '97620000', 'SAO FRANCISCO DE ASSIS', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4318200', '95405000', 'SAO FRANCISCO DE PAULA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4318309', '97330000', 'SAO GABRIEL', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4318408', '96720000', 'SAO JERONIMO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4318424', '99855000', 'SAO JOAO DA URTIGA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4318432', '97235000', 'SAO JOAO DO POLESINE', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4318440', '95365000', 'SAO JORGE', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4318457', '98325000', 'SAO JOSE DAS MISSOES', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4318465', '99380000', 'SAO JOSE DO HERVAL', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4318481', '95755000', 'SAO JOSE DO HORTENCIO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4318499', '98958000', 'SAO JOSE DO INHACORA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4318507', '96228000', 'SAO JOSE DO NORTE', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4318606', '99872000', 'SAO JOSE DO OURO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4318622', '95285000', 'SAO JOSE DOS AUSENTES', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4318705', '93010001', 'SAO LEOPOLDO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4318804', '96175000', 'SAO LOURENCO DO SUL', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4318903', '97825000', 'SAO LUIZ GONZAGA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4319000', '97535000', 'SAO MARCOS', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4319109', '98690000', 'SAO MARTINHO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4319125', '97190000', 'SAO MARTINHO DA SERRA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4319158', '98868000', 'SAO MIGUEL DAS MISSOES', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4319208', '97880000', 'SAO NICOLAU', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4319307', '97980000', 'SAO PAULO DAS MISSOES', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4319356', '95758000', 'SAO PEDRO DA SERRA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4319372', '97920000', 'SAO PEDRO DO BUTIA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4319406', '97403000', 'SAO PEDRO DO SUL', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4319505', '95763000', 'SAO SEBASTIAO DO CAI', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4319604', '97380000', 'SAO SEPE', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4319703', '98917500', 'SAO VALENTIM', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4319711', '99245000', 'SAO VALENTIM DO SUL', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4319737', '98598000', 'SAO VALERIO DO SUL', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4319752', '95795000', 'SAO VENDELINO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4319802', '97440000', 'SAO VICENTE DO SUL', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4319901', '93800000', 'SAPIRANGA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4320008', '93210000', 'SAPUCAIA DO SUL', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4320107', '99565000', 'SARANDI', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4320206', '98380000', 'SEBERI', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4320230', '98675000', 'SEDE NOVA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4320263', '96912000', 'SEGREDO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4320305', '99450000', 'SELBACH', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4320321', '98895000', 'SENADOR SALGADO FILHO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4320354', '96765000', 'SENTINELA DO SUL', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4320404', '99253000', 'SERAFINA CORREA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4320453', '95918000', 'SERIO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4320503', '99170000', 'SERTAO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4320552', '92850000', 'SERTAO SANTANA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4320578', '98903000', 'SETE DE SETEMBRO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4320602', '99815000', 'SEVERIANO DE ALMEIDA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4320651', '97195000', 'SILVEIRA MARTINS', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4320677', '96894000', 'SINIMBU', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4320701', '96900000', 'SOBRADINHO', 'RS');
            
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4320800', '99300000', 'SOLEDADE', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4320859', '95863000', 'TABAI', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4320909', '99950000', 'TAPEJARA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4321006', '96297000', 'TAPERA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4321105', '96760000', 'TAPES', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4321204', '95608000', 'TAQUARA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4321303', '95860000', 'TAQUARI', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4321329', '98410000', 'TAQUARUCU DO SUL', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4321352', '96293000', 'TAVARES', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4321402', '98525000', 'TENENTE PORTELA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4321436', '95535000', 'TERRA DE AREIA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4321451', '95890000', 'TEUTONIA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4321477', '98685000', 'TIRADENTES DO SUL', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4321493', '97418000', 'TOROPI', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4321501', '95565000', 'TORRES', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4321600', '95590000', 'TRAMANDAI', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4321626', '95948000', 'TRAVESSEIRO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4321634', '99725000', 'TRES ARROIOS', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4321667', '95583000', 'TRES CACHOEIRAS', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4321709', '95660000', 'TRES COROAS', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4321808', '98914000', 'TRES DE MAIO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4321832', '95575000', 'TRES FORQUILHAS', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4321857', '99675000', 'TRES PALMEIRAS', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4321907', '98605000', 'TRES PASSOS', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4321956', '99615000', 'TRINDADE DO SUL', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4322004', '95855000', 'TRIUNFO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4322103', '98936000', 'TUCUNDUVA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4322152', '99330000', 'TUNAS', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4322186', '99878000', 'TUPANCI DO SUL', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4322202', '98173000', 'TUPANCIRETA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4322251', '95775000', 'TUPANDI', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4322301', '98946000', 'TUPARENDI', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4322327', '96148000', 'TURUCU', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4322343', '98898000', 'UBIRETAMA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4322350', '99215000', 'UNIAO DA SERRA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4322376', '97755000', 'UNISTALDA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4322400', '97500002', 'URUGUAIANA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4322509', '95225000', 'VACARIA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4322525', '95833000', 'VALE VERDE', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4322533', '96878000', 'VALE DO SOL', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4322541', '95778000', 'VALE REAL', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4322558', '99290000', 'VANINI', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4322608', '95810000', 'VENANCIO AIRES', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4322707', '96880000', 'VERA CRUZ', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4322806', '95330000', 'VERANOPOLIS', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4322855', '95972000', 'VESPASIANO CORREA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4322905', '99820000', 'VIADUTOS', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4323002', '94410000', 'VIAMAO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4323101', '98455000', 'VICENTE DUTRA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4323200', '99357000', 'VICTOR GRAEFF', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4323309', '95334000', 'VILA FLORES', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4323358', '99955000', 'VILA LANGARO', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4323408', '99155000', 'VILA MARIA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4323457', '97385000', 'VILA NOVA DO SUL', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4323507', '99465000', 'VISTA ALEGRE', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4323606', '95325000', 'VISTA ALEGRE DO PRATA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4323705', '98535000', 'VISTA GAUCHA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4323754', '98853000', 'VITORIA DAS MISSOES', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('4323804', '95588000', 'XANGRI-LA', 'RS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5000203', '79682000', 'AGUA CLARA', 'MS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5000252', '79530000', 'ALCINOPOLIS', 'MS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5000609', '79990000', 'AMAMBAI', 'MS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5000708', '79210000', 'ANASTACIO', 'MS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5000807', '79774000', 'ANAURILANDIA', 'MS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5000856', '79787000', 'ANGELICA', 'MS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5000906', '79912000', 'ANTONIO JOAO', 'MS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5001003', '79578000', 'APARECIDA DO TABOADO', 'MS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5001102', '79208000', 'AQUIDAUANA', 'MS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5001243', '79932000', 'ARAL MOREIRA', 'MS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5001508', '79432000', 'BANDEIRANTES', 'MS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5001904', '79782000', 'BATAGUASSU', 'MS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5002001', '79760000', 'BATAIPORA', 'MS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5002100', '79262000', 'BELA VISTA', 'MS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5002159', '79392000', 'BODOQUENA', 'MS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5002209', '79292000', 'BONITO', 'MS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5002308', '79677000', 'BRASILANDIA', 'MS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5002407', '79942000', 'CAARAPO', 'MS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5002605', '79424000', 'CAMAPUA', 'MS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5002704', '79002000', 'CAMPO GRANDE', 'MS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5002803', '79270000', 'CARACOL', 'MS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5002902', '79542000', 'CASSILANDIA', 'MS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5002951', '79560000', 'CHAPADAO DO SUL', 'MS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5003108', '79462000', 'CORGUINHO', 'MS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5003157', '79995000', 'CORONEL SAPUCAIA', 'MS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5003207', '79300002', 'CORUMBA', 'MS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5003256', '79554000', 'COSTA RICA', 'MS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5003306', '79406000', 'COXIM', 'MS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5003454', '79798000', 'DEODAPOLIS', 'MS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5003488', '79217000', 'DOIS IRMAOS DO BURITI', 'MS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5003504', '79883000', 'DOURADINA', 'MS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5003702', '79800002', 'DOURADOS', 'MS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5003751', '79972000', 'ELDORADO', 'MS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5003801', '79702000', 'FATIMA DO SUL', 'MS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5004007', '79734000', 'GLORIA DE DOURADOS', 'MS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5004106', '79230000', 'GUIA LOPES DA LAGUNA', 'MS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5004304', '79960000', 'IGUATEMI', 'MS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5004403', '79584000', 'INOCENCIA', 'MS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5004502', '79892000', 'ITAPORA', 'MS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5004601', '79965000', 'ITAQUIRAI', 'MS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5004700', '79742000', 'IVINHEMA', 'MS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5004809', '79988000', 'JAPORA', 'MS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5004908', '79442000', 'JARAGUARI', 'MS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5005004', '79242000', 'JARDIM', 'MS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5005103', '79722000', 'JATEI', 'MS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5005152', '79955000', 'JUTI', 'MS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5005202', '79370000', 'LADARIO', 'MS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5005251', '79923000', 'LAGUNA CARAPA', 'MS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5005400', '79152000', 'MARACAJU', 'MS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5005608', '79380000', 'MIRANDA', 'MS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5005681', '79980000', 'MUNDO NOVO', 'MS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5005707', '79950000', 'NAVIRAI', 'MS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5005806', '79220000', 'NIOAQUE', 'MS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5006002', '79140000', 'NOVA ALVORADA DO SUL', 'MS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5006200', '79750000', 'NOVA ANDRADINA', 'MS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5006259', '79745000', 'NOVO HORIZONTE DO SUL', 'MS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5006309', '79504000', 'PARANAIBA', 'MS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5006358', '79925000', 'PARANHOS', 'MS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5006408', '79410000', 'PEDRO GOMES', 'MS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5006606', '79908000', 'PONTA PORA', 'MS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5006903', '79280000', 'PORTO MURTINHO', 'MS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5007109', '79182000', 'RIBAS DO RIO PARDO', 'MS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5007208', '79134000', 'RIO BRILHANTE', 'MS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5007307', '79472000', 'RIO NEGRO', 'MS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5007406', '79482000', 'RIO VERDE DE MATO GROSSO', 'MS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5007505', '79452000', 'ROCHEDO', 'MS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5007554', '79690000', 'SANTA RITA DO PARDO', 'MS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5007695', '79492000', 'SAO GABRIEL DO OESTE', 'MS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5007703', '79935000', 'SETE QUEDAS', 'MS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5007802', '79590000', 'SELVIRIA', 'MS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5007901', '79174000', 'SIDROLANDIA', 'MS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5007935', '79415000', 'SONORA', 'MS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5007950', '79975000', 'TACURU', 'MS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5007976', '79765000', 'TAQUARUSSU', 'MS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5008008', '79190000', 'TERENOS', 'MS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5008305', '79600001', 'TRES LAGOAS', 'MS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5008404', '79714000', 'VICENTINA', 'MS');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5100102', '78483000', 'ACORIZAL', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5100201', '78635000', 'AGUA BOA', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5100250', '78584000', 'ALTA FLORESTA', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5100300', '78782000', 'ALTO ARAGUAIA', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5100359', '78665000', 'ALTO BOA VISTA', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5100409', '78770000', 'ALTO GARCAS', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5100508', '78411000', 'ALTO PARAGUAI', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5100607', '78785000', 'ALTO TAQUARI', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5100805', '78595000', 'APIACAS', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5101001', '78685000', 'ARAGUAIANA', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5101209', '78615000', 'ARAGUAINHA', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5101258', '78260000', 'ARAPUTANGA', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5101308', '78420000', 'ARENAPOLIS', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5101407', '78326000', 'ARIPUANA', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5101605', '78192000', 'BARAO DE MELGACO', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5101704', '78396000', 'BARRA DO BUGRES', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5101803', '78603000', 'BARRA DO GARCAS', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5101902', '78350000', 'BRASNORTE', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5102504', '78234000', 'CACERES', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5102603', '78630000', 'CAMPINAPOLIS', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5102637', '78360000', 'CAMPO NOVO DO PARECIS', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5102678', '78843000', 'CAMPO VERDE', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5102686', '78307000', 'CAMPOS DE JULIO', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5102694', '78658000', 'CANABRAVA DO NORTE', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5102702', '78640000', 'CANARANA', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5102793', '78587000', 'CARLINDA', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5102850', '78348000', 'CASTANHEIRA', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5103007', '78197000', 'CHAPADA DOS GUIMARAES', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5103056', '78540000', 'CLAUDIA', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5103106', '78680000', 'COCALINHO', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5103205', '78502000', 'COLIDER', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5103304', '78316000', 'COMODORO', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5103353', '78652000', 'CONFRESA', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5103379', '78330000', 'COTRIGUACU', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5103403', '78005000', 'CUIABA', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5103452', '78380000', 'DENISE', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5103502', '78405000', 'DIAMANTINO', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5103601', '78833000', 'DOM AQUINO', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5103700', '78885000', 'FELIZ NATAL', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5103809', '78290000', 'FIGUEIROPOLIS D''OESTE', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5103858', '78875000', 'GAUCHA DO NORTE', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5103908', '78620000', 'GENERAL CARNEIRO', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5103957', '78293000', 'GLORIA D''OESTE', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5104104', '78522000', 'GUARANTA DO NORTE', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5104203', '78764000', 'GUIRATINGA', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5104500', '78295000', 'INDIAVAI', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5104559', '78510000', 'ITAUBA', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5104609', '78790000', 'ITIQUIRA', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5104807', '78823000', 'JACIARA', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5104906', '78490000', 'JANGADA', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5105002', '78258000', 'JAURU', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5105101', '78575000', 'JUARA', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5105150', '78321000', 'JUINA', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5105176', '78340000', 'JURUENA', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5105200', '78813000', 'JUSCIMEIRA', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5105234', '78278000', 'LAMBARI D''OESTE', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5105259', '78455000', 'LUCAS DO RIO VERDE', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5105309', '78660000', 'LUCIARA', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5105507', '78248000', 'VILA BELA DA SANTISSIMA TRINDADE', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5105580', '78536000', 'MARCELANDIA', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5105606', '78525000', 'MATUPA', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5105622', '78284000', 'MIRASSOL D''OESTE', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5105903', '78463000', 'NOBRES', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5106000', '78430000', 'NORTELANDIA', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5106109', '78171000', 'NOSSA SENHORA DO LIVRAMENTO', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5106158', '78565000', 'NOVA BANDEIRANTES', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5106182', '78243000', 'NOVA LACERDA', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5106208', '78866000', 'NOVA BRASILANDIA', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5106216', '78518000', 'NOVA CANAA DO NORTE', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5106224', '78450000', 'NOVA MUTUM', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5106232', '78370000', 'NOVA OLIMPIA', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5106240', '78888000', 'NOVA UBIRATA', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5106257', '78691000', 'NOVA XAVANTINA', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5106265', '78528000', 'NOVO MUNDO', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5106273', '78572000', 'NOVO HORIZONTE DO NORTE', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5106281', '78625000', 'NOVO SAO JOAQUIM', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5106299', '78590000', 'PARANAITA', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5106307', '78870000', 'PARANATINGA', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5106372', '78798000', 'PEDRA PRETA', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5106422', '78534000', 'PEIXOTO DE AZEVEDO', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5106455', '78855000', 'PLANALTO DA SERRA', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5106505', '78178000', 'POCONE', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5106653', '78698000', 'PONTAL DO ARAGUAIA', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5106703', '78610000', 'PONTE BRANCA', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5106752', '78250000', 'PONTES E LACERDA', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5106778', '78655000', 'PORTO ALEGRE DO NORTE', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5106802', '78562000', 'PORTO DOS GAUCHOS', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5106828', '78240000', 'PORTO ESPERIDIAO', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5106851', '78398000', 'PORTO ESTRELA', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5107008', '78803000', 'POXOREO', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5107040', '78850000', 'PRIMAVERA DO LESTE', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5107065', '78643000', 'QUERENCIA', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5107107', '78288000', 'SAO JOSE DOS QUATRO MARCOS', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5107156', '78265000', 'RESERVA DO CABACAL', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5107180', '78675000', 'RIBEIRAO CASCALHEIRA', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5107198', '78613000', 'RIBEIRAOZINHO', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5107206', '78277000', 'RIO BRANCO', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5107248', '78545000', 'SANTA CARMEM', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5107263', '78425000', 'SANTO AFONSO', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5107297', '78773000', 'SAO JOSE DO POVO', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5107305', '78437000', 'SAO JOSE DO RIO CLARO', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5107354', '78663000', 'SAO JOSE DO XINGU', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5107404', '78835000', 'SAO PEDRO DA CIPA', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5107602', '78700002', 'RONDONOPOLIS', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5107701', '78473000', 'ROSARIO OESTE', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5107750', '78272000', 'SALTO DO CEU', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5107776', '78650000', 'SANTA TEREZINHA', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5107800', '78186000', 'SANTO ANTONIO DO LEVERGER', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5107859', '78672000', 'SAO FELIX DO ARAGUAIA', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5107875', '78365000', 'SAPEZAL', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5107909', '78551000', 'SINOP', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5107925', '78896000', 'SORRISO', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5107941', '78563000', 'TABAPORA', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5107958', '78361000', 'TANGARA DA SERRA', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5108006', '78558000', 'TAPURAH', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5108055', '78505000', 'TERRA NOVA DO NORTE', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5108105', '78776000', 'TESOURO', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5108204', '78695000', 'TORIXOREU', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5108303', '78543000', 'UNIAO DO SUL', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5108402', '78110000', 'VARZEA GRANDE', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5108501', '78880000', 'VERA', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5108600', '78648000', 'VILA RICA', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5108808', '78508000', 'NOVA GUARITA', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5108857', '78415000', 'NOVA MARILANDIA', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5108907', '78445000', 'NOVA MARINGA', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5108956', '78593000', 'NOVA MONTE VERDE', 'MT');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5200050', '75345000', 'ABADIA DE GOIAS', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5200100', '72944000', 'ABADIANIA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5200134', '75960000', 'ACREUNA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5200159', '76155000', 'ADELANDIA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5200175', '73780000', 'AGUA FRIA DE GOIAS', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5200209', '75665000', 'AGUA LIMPA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5200258', '72910000', 'AGUAS LINDAS DE GOIAS', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5200308', '72920000', 'ALEXANIA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5200506', '75615000', 'ALOANDIA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5200555', '76560000', 'ALTO HORIZONTE', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5200605', '3770000', 'ALTO PARAISO DE GOIAS', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5200803', '73950000', 'ALVORADA DO NORTE', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5200829', '76493000', 'AMARALINA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5200852', '76165000', 'AMERICANO DO BRASIL', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5200902', '76140000', 'AMORINOPOLIS', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5201108', '75020010', 'ANAPOLIS', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5201207', '75770000', 'ANHANGUERA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5201306', '76174000', 'ANICUNS', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5201405', '74905010', 'APARECIDA DE GOIANIA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5201454', '75827000', 'APARECIDA DO RIO DOCE', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5201504', '75825000', 'APORE', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5201603', '75410000', 'ARACU', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5201702', '76240000', 'ARAGARCAS', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5201801', '75360000', 'ARAGOIANIA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5202155', '76720000', 'ARAGUAPAZ', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5202353', '76235000', 'ARENOPOLIS', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5202502', '76710000', 'ARUANA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5202601', '76120000', 'AURILANDIA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5202809', '75395000', 'AVELINOPOLIS', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5203104', '76250000', 'BALIZA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5203203', '76390000', 'BARRO ALTO', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5203302', '75240000', 'BELA VISTA DE GOIAS', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5203401', '76245000', 'BOM JARDIM DE GOIAS', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5203500', '75574000', 'BOM JESUS DE GOIAS', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5203559', '75195000', 'BONFINOPOLIS', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5203575', '76555000', 'BONOPOLIS', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5203609', '75440000', 'BRAZABRANTES', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5203807', '76280000', 'BRITANIA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5203906', '75660000', 'BURITI ALEGRE', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5203939', '76152000', 'BURITI DE GOIAS', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5203962', '73975000', 'BURITINOPOLIS', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5204003', '73870000', 'CABECEIRAS', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5204102', '75870000', 'CACHOEIRA ALTA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5204201', '76125000', 'CACHOEIRA DE GOIAS', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5204250', '75560000', 'CACHOEIRA DOURADA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5204300', '75813000', 'CACU', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5204409', '75850000', 'CAIAPONIA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5204508', '75690000', 'CALDAS NOVAS', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5204557', '75245000', 'CALDAZINHA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5204607', '75385000', 'CAMPESTRE DE GOIAS', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5204656', '76440000', 'CAMPINACU', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5204706', '76412000', 'CAMPINORTE', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5204805', '75795000', 'CAMPO ALEGRE DE GOIAS', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5204904', '73840000', 'CAMPOS BELOS', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5204953', '76515000', 'CAMPOS VERDES', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5205000', '76340000', 'CARMO DO RIO VERDE', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5205059', '75925000', 'CASTELANDIA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5205109', '75701010', 'CATALAO', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5205208', '75430000', 'CATURAI', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5205307', '73790000', 'CAVALCANTE', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5205406', '76300000', 'CERES', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5205455', '76195000', 'CEZARINA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5205471', '75828000', 'CHAPADAO DO CEU', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5205497', '72880000', 'Nome OCIDENTAL', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5205513', '72975000', 'COCALZINHO DE GOIAS', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5205521', '73740000', 'COLINAS DO SUL', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5205703', '76145000', 'CORREGO DO OURO', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5205802', '72960000', 'CORUMBA DE GOIAS', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5205901', '75680000', 'CORUMBAIBA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5206206', '73850000', 'CRISTALINA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5206305', '75230000', 'CRISTIANOPOLIS', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5206404', '76513000', 'CRIXAS', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5206503', '75635000', 'CROMINIA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5206602', '75760000', 'CUMARI', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5206701', '73980000', 'DAMIANOPOLIS', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5206800', '75420000', 'DAMOLANDIA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5206909', '75730000', 'DAVINOPOLIS', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5207105', '76260000', 'DIORAMA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5207253', '75855000', 'DOVERLANDIA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5207352', '75945000', 'EDEALINA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5207402', '75940000', 'EDEIA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5207501', '76485000', 'ESTRELA DO NORTE', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5207535', '76742000', 'FAINA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5207600', '76222000', 'FAZENDA NOVA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5207808', '76105000', 'FIRMINOPOLIS', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5207907', '73890000', 'FLORES DE GOIAS', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5208004', '73801010', 'FORMOSA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5208103', '76478000', 'FORMOSO', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5208301', '73865000', 'DIVINOPOLIS DE GOIAS', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5208400', '75170000', 'GOIANAPOLIS', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5208509', '75740000', 'GOIANDIRA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5208608', '76383000', 'GOIANESIA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5208707', '74003010', 'GOIANIA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5208806', '75370000', 'GOIANIRA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5208905', '76606000', 'GOIAS', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5209101', '75600000', 'GOIATUBA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5209150', '75865000', 'GOUVELANDIA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5209200', '75350000', 'GUAPO', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5209291', '76690000', 'GUARAITA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5209408', '73910000', 'GUARANI DE GOIAS', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5209457', '76385000', 'GUARINOS', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5209606', '76670000', 'HEITORAI', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5209705', '75340000', 'HIDROLANDIA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5209804', '76375000', 'HIDROLINA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5209903', '73920000', 'IACIARA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5209937', '75550000', 'INACIOLANDIA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5209952', '75955000', 'INDIARA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5210000', '75400000', 'INHUMAS', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5210109', '75783000', 'IPAMERI', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5210208', '76200000', 'IPORA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5210307', '76208000', 'ISRAELANDIA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5210406', '76630000', 'ITABERAI', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5210562', '76650000', 'ITAGUARI', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5210604', '76660000', 'ITAGUARU', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5210802', '75815000', 'ITAJA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5210901', '76363000', 'ITAPACI', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5211008', '76293000', 'ITAPIRAPUA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5211206', '76683000', 'ITAPURANGA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5211305', '75812000', 'ITARUMA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5211404', '75450000', 'ITAUCU', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5211503', '75503010', 'ITUMBIARA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5211602', '76133000', 'IVOLANDIA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5211701', '75950000', 'JANDAIA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5211800', '76330000', 'JARAGUA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5211909', '75800001', 'JATAI', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5212006', '76210000', 'JAUPACI', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5212055', '75495000', 'JESUPOLIS', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5212105', '75610000', 'JOVIANIA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5212204', '76274000', 'JUSSARA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5212303', '75190000', 'LEOPOLDO DE BULHOES', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5212501', '72800010', 'LUZIANIA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5212600', '75630000', 'MAIRIPOTABA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5212709', '73970000', 'MAMBAI', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5212808', '76490000', 'MARA ROSA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5212907', '75670000', 'MARZAGAO', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5212956', '76730000', 'MATRINCHA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5213004', '75930000', 'MAURILANDIA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5213053', '73730000', 'MIMOSO DE GOIAS', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5213087', '76458000', 'MINACU', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5213103', '75830000', 'MINEIROS', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5213400', '76138000', 'MOIPORA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5213509', '73830000', 'MONTE ALEGRE DE GOIAS', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5213707', '76256000', 'MONTES CLAROS DE GOIAS', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5213756', '75915000', 'MONTIVIDIU', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5213772', '76465000', 'MONTIVIDIU DO NORTE', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5213806', '75650000', 'MORRINHOS', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5213855', '76355000', 'MORRO AGUDO DE GOIAS', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5213905', '76150000', 'MOSSAMEDES', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5214002', '76700000', 'MOZARLANDIA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5214051', '76530000', 'MUNDO NOVO', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5214101', '76540000', 'MUTUNOPOLIS', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5214408', '76180000', 'NAZARIO', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5214507', '75460000', 'NEROPOLIS', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5214606', '76424000', 'NIQUELANDIA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5214705', '76345000', 'NOVA AMERICA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5214804', '75750000', 'NOVA AURORA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5214838', '76523000', 'NOVA CRIXAS', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5214861', '76305000', 'NOVA GLORIA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5214879', '76495000', 'NOVA IGUACU DE GOIAS', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5214903', '73820000', 'NOVA ROMA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5215009', '75470000', 'NOVA VENEZA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5215207', '76285000', 'NOVO BRASIL', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5215231', '72860001', 'NOVO GAMA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5215256', '76580000', 'NOVO PLANALTO', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5215306', '75283000', 'ORIZONA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5215405', '75165000', 'OURO VERDE DE GOIAS', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5215504', '75715000', 'OUVIDOR', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5215603', '73700000', 'PADRE BERNARDO', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5215652', '75845000', 'PALESTINA DE GOIAS', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5215702', '76190000', 'PALMEIRAS DE GOIAS', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5215801', '75210000', 'PALMELO', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5215900', '75990000', 'PALMINOPOLIS', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5216007', '75580000', 'PANAMA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5216304', '75880000', 'PARANAIGUARA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5216403', '75980000', 'PARAUNA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5216452', '75823000', 'PEROLANDIA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5216809', '75480000', 'PETROLINA DE GOIAS', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5216908', '76370000', 'PILAR DE GOIAS', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5217104', '75640000', 'PIRACANJUBA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5217203', '76230000', 'PIRANHAS', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5217302', '72984000', 'PIRENOPOLIS', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5217401', '75200000', 'PIRES DO RIO', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5217609', '73750005', 'PLANALTINA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5217708', '75620000', 'PONTALINA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5218003', '76554000', 'PORANGATU', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5218052', '75603000', 'PORTEIRAO', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5218102', '75835000', 'PORTELANDIA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5218300', '73907000', 'POSSE', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5218391', '75645000', 'PROFESSOR JAMIL', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5218508', '75860000', 'QUIRINOPOLIS', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5218607', '76310000', 'RIALMA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5218706', '76313000', 'RIANAPOLIS', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5218789', '75695000', 'RIO QUENTE', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5218805', '75900002', 'RIO VERDE', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5218904', '76352000', 'RUBIATABA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5219001', '76163000', 'SANCLERLANDIA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5219100', '75390000', 'SANTA BARBARA DE GOIAS', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5219209', '75220000', 'SANTA CRUZ DE GOIAS', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5219258', '76265000', 'SANTA FE DE GOIAS', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5219308', '75920000', 'SANTA HELENA DE GOIAS', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5219357', '76323000', 'SANTA ISABEL', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5219407', '75840000', 'SANTA RITA DO ARAGUAIA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5219456', '76395000', 'SANTA RITA DO NOVO DESTINO', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5219506', '75455000', 'SANTA ROSA DE GOIAS', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5219605', '76480000', 'SANTA TEREZA DE GOIAS', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5219704', '76500000', 'SANTA TEREZINHA DE GOIAS', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5219712', '75935000', 'SANTO ANTONIO DA BARRA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5219738', '75375000', 'SANTO ANTONIO DE GOIAS', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5219753', '72900000', 'SANTO ANTONIO DO DESCOBERTO', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5219803', '73860000', 'SAO DOMINGOS', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5219902', '75490000', 'SAO FRANCISCO DE GOIAS', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5220009', '73764000', 'SAO JOAO D''ALIANCA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5220058', '75985000', 'SAO JOAO DA PARAUNA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5220108', '76103000', 'SAO LUIS DE MONTES BELOS', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5220157', '76365000', 'SAO LUIZ DO NORTE', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5220207', '76590000', 'SAO MIGUEL DO ARAGUAIA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5220264', '75185000', 'SAO MIGUEL DO PASSA QUATRO', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5220280', '76343000', 'SAO PATRICIO', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5220405', '75893000', 'SAO SIMAO', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5220454', '75250000', 'SENADOR CANEDO', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5220504', '75820000', 'SERRANOPOLIS', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5220603', '75180000', 'SILVANIA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5220686', '73930000', 'SIMOLANDIA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5220702', '73990000', 'SITIO D''ABADIA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5221007', '76640000', 'TAQUARAL DE GOIAS', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5221080', '73795000', 'TERESINA DE GOIAS', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5221197', '75175000', 'TEREZOPOLIS DE GOIAS', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5221304', '75720000', 'TRES RANCHOS', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5221403', '75380000', 'TRINDADE', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5221452', '76460000', 'TROMBAS', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5221502', '76110000', 'TURVANIA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5221551', '75970000', 'TURVELANDIA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5221577', '76528000', 'UIRAPURU', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5221601', '76402000', 'URUACU', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5221700', '76338000', 'URUANA', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5221809', '75790000', 'URUTAI', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5221858', '72870001', 'VALPARAISO DE GOIAS', 'GO');
            INSERT INTO Municipio (CODIBGE, CEP, Nome, UF)
            VALUES ('5221908', '75355000', 'VARJAO', 'GO');
        """)
    
    print('Tabela criada com sucesso.')
        # desconectando...
    
