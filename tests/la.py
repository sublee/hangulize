# -*- coding: utf-8 -*-
from tests import HangulizeTestCase
from hangulize.langs.la import Latin


class LatinTestCase(HangulizeTestCase):

    lang = Latin()

    def test_people_roman(self):
        assert u'플라비우스 아에티우스' == self.hangulize(u'Flavius Aëtius')
        assert u'플라비우스 아에티우스' == self.hangulize(u'FLAVIVS AËTIVS')
        assert u'그나이우스 율리우스 아그리콜라' == \
               self.hangulize(u'Gnaeus Julius Agricola')
        assert u'그나이우스 율리우스 아그리콜라' == \
               self.hangulize(u'GNAEUS IVLIVS AGRICOLA')
        assert u'마르쿠스 빕사니우스 아그리파' == \
               self.hangulize(u'Marcus Vipsanius Agrippa')
        assert u'마르쿠스 빕사니우스 아그리파' == \
               self.hangulize(u'MARCVS VIPSANIVS AGRIPPA')
        assert u'율리아 아우구스타 아그리피나' == \
               self.hangulize(u'Julia Augusta Agrippina')
        assert u'율리아 아우구스타 아그리피나' == \
               self.hangulize(u'IVLIA AVGVSTA AGRIPPINA')
        assert u'마르쿠스 안토니우스' == self.hangulize(u'Marcus Antonius')
        assert u'마르쿠스 안토니우스' == self.hangulize(u'MARCVS ANTONIVS')
        assert u'아풀레이우스' == self.hangulize(u'Apuleius')
        assert u'아풀레이우스' == self.hangulize(u'APVLEIVS')
        assert u'가이우스 율리우스 카이사르 아우구스투스' == \
               self.hangulize(u'Gaius Julius Caesar Augustus')
        assert u'가이우스 율리우스 카이사르 아우구스투스' == \
               self.hangulize(u'GAIVS IVLIVS CAESAR AVGVSTVS')
        assert u'가이우스 율리우스 카이사르' == \
               self.hangulize(u'Gaius Julius Caesar')
        assert u'가이우스 율리우스 카이사르' == \
               self.hangulize(u'GAIVS IVLIVS CAESAR')
        assert u'가이우스 발레리우스 카툴루스' == \
               self.hangulize(u'Gaius Valerius Catullus')
        assert u'가이우스 발레리우스 카툴루스' == \
               self.hangulize(u'GAIVS VALERIVS CATVLLVS')
        assert u'마르쿠스 툴리우스 키케로' == \
               self.hangulize(u'Marcus Tullius Cicero')
        assert u'마르쿠스 툴리우스 키케로' == \
               self.hangulize(u'MARCVS TVLLIVS CICERO')
        assert u'티베리우스 클라우디우스 카이사르 아우구스투스 게르마니쿠스' ==\
               self.hangulize(u'Tiberius Claudius Caesar Augustus Germanicus')
        assert u'티베리우스 클라우디우스 카이사르 아우구스투스 게르마니쿠스' ==\
               self.hangulize(u'TIBERIVS CLAVDIVS CAESAR AVGVSTVS GERMANICVS')
        assert u'루키우스 아우렐리우스 콤모두스 안토니누스' == \
               self.hangulize(u'Lucius Aurelius Commodus Antoninus')
        assert u'루키우스 아우렐리우스 콤모두스 안토니누스' == \
               self.hangulize(u'LVCIVS AVRELIVS COMMODVS ANTONINVS')
        assert u'플라비우스 발레리우스 아우렐리우스 콘스탄티누스' == \
               self.hangulize(u'Flavius Valerius Aurelius Constantinus')
        assert u'플라비우스 발레리우스 아우렐리우스 콘스탄티누스' == \
               self.hangulize(u'FLAVIVS VALERIVS AVRELIVS CONSTANTINVS')
        assert u'코르넬리아 스키피오니스 아프리카나' == \
               self.hangulize(u'Cornelia Scipionis Africana')
        assert u'코르넬리아 스키피오니스 아프리카나' == \
               self.hangulize(u'CORNELIA SCIPIONIS AFRICANA')
        assert u'마르쿠스 리키니우스 크라수스' == \
               self.hangulize(u'Marcus Licinius Crassus')
        assert u'마르쿠스 리키니우스 크라수스' == \
               self.hangulize(u'MARCVS LICINIVS CRASSVS')
        assert u'가이우스 아우렐리우스 발레리우스 디오클레티아누스' == \
               self.hangulize(u'Gaius Aurelius Valerius Diocletianus')
        assert u'가이우스 아우렐리우스 발레리우스 디오클레티아누스' == \
               self.hangulize(u'GAIVS AVRELIVS VALERIVS DIOCLETIANVS')
        assert u'푸블리우스 아일리우스 하드리아누스' == \
               self.hangulize(u'Publius Aelius Hadrianus')
        assert u'푸블리우스 아일리우스 하드리아누스' == \
               self.hangulize(u'PVBLIVS AELIVS HADRIANVS')
        assert u'퀸투스 호라티우스 플라쿠스' == \
               self.hangulize(u'Quintus Horatius Flaccus')
        assert u'퀸투스 호라티우스 플라쿠스' == \
               self.hangulize(u'QVINTVS HORATIVS FLACCVS')
        assert u'플라비우스 페트루스 사바티우스 유스티니아누스' == \
               self.hangulize(u'Flavius Petrus Sabbatius Justinianus')
        assert u'플라비우스 페트루스 사바티우스 유스티니아누스' == \
               self.hangulize(u'FLAVIVS PETRVS SABBATIVS IVSTINIANVS')
        assert u'티투스 리비우스' == self.hangulize(u'Titus Livius')
        assert u'티투스 리비우스' == self.hangulize(u'TITVS LIVIVS')
        assert u'가이우스 마리우스' == self.hangulize(u'Gaius Marius')
        assert u'가이우스 마리우스' == self.hangulize(u'GAIVS MARIVS')
        assert u'네로 클라우디우스 카이사르 아우구스투스 게르마니쿠스' == \
               self.hangulize(u'Nero Claudius Caesar Augustus Germanicus')
        assert u'네로 클라우디우스 카이사르 아우구스투스 게르마니쿠스' == \
               self.hangulize(u'NERO CLAVDIVS CAESAR AVGVSTVS GERMANICVS')
        assert u'가이우스 옥타비우스' == self.hangulize(u'Gaius Octavius')
        assert u'가이우스 옥타비우스' == self.hangulize(u'GAIVS OCTAVIVS')
        assert u'티투스 마키우스 플라우투스' == \
               self.hangulize(u'Titus Maccius Plautus')
        assert u'티투스 마키우스 플라우투스' == \
               self.hangulize(u'TITVS MACCIVS PLAVTVS')
        assert u'가이우스 플리니우스 세쿤두스' == \
               self.hangulize(u'Gaius Plinius Secundus')
        assert u'가이우스 플리니우스 세쿤두스' == \
               self.hangulize(u'GAIVS PLINIVS SECVNDVS')
        assert u'가이우스 플리니우스 카이킬리우스 세쿤두스' == \
               self.hangulize(u'Gaius Plinius Caecilius Secundus')
        assert u'가이우스 플리니우스 카이킬리우스 세쿤두스' == \
               self.hangulize(u'GAIVS PLINIVS CAECILIVS SECVNDVS')
        assert u'그나이우스 폼페이우스 마그누스' == \
               self.hangulize(u'Gnaeus Pompeius Magnus')
        assert u'그나이우스 폼페이우스 마그누스' == \
               self.hangulize(u'GNAEVS POMPEIVS MAGNVS')
        assert u'섹스투스 아우렐리우스 프로페르티우스' == \
               self.hangulize(u'Sextus Aurelius Propertius')
        assert u'섹스투스 아우렐리우스 프로페르티우스' == \
               self.hangulize(u'SEXTVS AVRELIVS PROPERTIVS')
        assert u'가이우스 살루스티우스 크리스푸스' == \
               self.hangulize(u'Gaius Sallustius Crispus')
        assert u'가이우스 살루스티우스 크리스푸스' == \
               self.hangulize(u'GAIVS SALLVSTIVS CRISPVS')
        assert u'루키우스 안나이우스 세네카' == \
               self.hangulize(u'Lucius Annaeus Seneca')
        assert u'루키우스 안나이우스 세네카' == \
               self.hangulize(u'LVCIVS ANNAEUS SENECA')
        assert u'스파르타쿠스' == self.hangulize(u'Spartacus')
        assert u'스파르타쿠스' == self.hangulize(u'SPARTACVS')
        assert u'가이우스 수에토니우스 트랑퀼루스' == \
               self.hangulize(u'Gaius Suetonius Tranquillus')
        assert u'가이우스 수에토니우스 트랑퀼루스' == \
               self.hangulize(u'GAIVS SVETONIVS TRANQVILLVS')
        assert u'루키우스 코르넬리우스 술라 펠릭스' == \
               self.hangulize(u'Lucius Cornelius Sulla Felix')
        assert u'루키우스 코르넬리우스 술라 펠릭스' == \
               self.hangulize(u'LVCIVS CORNELIVS SVLLA FELIX')
        assert u'푸블리우스 코르넬리우스 타키투스' == \
               self.hangulize(u'Publius Cornelius Tacitus')
        assert u'푸블리우스 코르넬리우스 타키투스' == \
               self.hangulize(u'PVBLIVS CORNELIVS TACITVS')
        assert u'마르쿠스 울피우스 네르바 트라야누스' == \
               self.hangulize(u'Marcus Ulpius Nerva Trajanus')
        assert u'마르쿠스 울피우스 네르바 트라야누스' == \
               self.hangulize(u'MARCUS VLPIVS NERVA TRAIANVS')
        assert u'푸블리우스 베르길리우스 마로' == \
               self.hangulize(u'Publius Vergilius Maro')
        assert u'푸블리우스 베르길리우스 마로' == \
               self.hangulize(u'PVBLIVS VERGILIVS MARO')
        assert u'티투스 플라비우스 베스파시아누스' == \
               self.hangulize(u'Titus Flavius Vespasianus')
        assert u'티투스 플라비우스 베스파시아누스' == \
               self.hangulize(u'TITVS FLAVIVS VESPASIANVS')
        assert u'마르쿠스 비트루비우스 폴리오' == \
               self.hangulize(u'Marcus Vitruvius Pollio')
        assert u'마르쿠스 비트루비우스 폴리오' == \
               self.hangulize(u'MARCVS VITRVVIVS POLLIO')

    def test_people_nonroman(self):
        assert u'게오르기우스 아그리콜라' == \
               self.hangulize(u'Georgius Agricola')
        assert u'안셀무스' == self.hangulize(u'Anselmus')
        assert u'아베로에스' == self.hangulize(u'Averroës')
        assert u'아우렐리우스 아우구스티누스 히포넨시스' == \
               self.hangulize(u'Aurelius Augustinus Hipponensis')
        assert u'카롤루스 마그누스' == self.hangulize(u'Carolus Magnus')
        assert u'니콜라우스 코페르니쿠스' == \
               self.hangulize(u'Nicolaus Copernicus')
        assert u'키루스' == self.hangulize(u'Cyrus')
        assert u'다리우스' == self.hangulize(u'Darius')
        assert u'고타르제스' == self.hangulize(u'Gotarzes')
        assert u'한니발' == self.hangulize(u'Hannibal')
        assert u'플라비우스 요세푸스' == self.hangulize(u'Flavius Josephus')
        assert u'미트리다테스' == self.hangulize(u'Mithridates')
        assert u'플라비우스 오도아케르' == self.hangulize(u'Flavius Odoacer')

    def test_places(self):
        assert u'아이깁투스' == self.hangulize(u'Aegyptus')
        assert u'아시아' == self.hangulize(u'Asia')
        assert u'아시리아' == self.hangulize(u'Assyria')
        assert u'브리탄니아' == self.hangulize(u'Britannia')
        assert u'카르타고' == self.hangulize(u'Carthago')
        assert u'칸나이' == self.hangulize(u'Cannae')
        assert u'갈라티아' == self.hangulize(u'Galatia')
        assert u'갈리아' == self.hangulize(u'Gallia')
        assert u'게르마니아' == self.hangulize(u'Germania')
        assert u'히스파니아' == self.hangulize(u'Hispania')
        assert u'일리리쿰' == self.hangulize(u'Illyricum')
        assert u'유다이아' == self.hangulize(u'Iudaea')
        assert u'라티움' == self.hangulize(u'Latium')
        assert u'루시타니아' == self.hangulize(u'Lusitania')
        assert u'누미디아' == self.hangulize(u'Numidia')
        assert u'파두스' == self.hangulize(u'Padus')
        assert u'파르티아' == self.hangulize(u'Parthia')
        #assert u'폼페이' == self.hangulize(u'Pompeii')
        assert u'로마' == self.hangulize(u'Roma')
        assert u'시킬리아' == self.hangulize(u'Sicilia')
        assert u'시라쿠사이' == self.hangulize(u'Syracusae')
        assert u'트라키아' == self.hangulize(u'Thracia')
        assert u'몬스 베수비우스' == self.hangulize(u'Mons Vesuvius')

    def test_texts(self):
        assert u'아이네이스' == self.hangulize(u'Aeneis')
        assert u'나투랄리스 히스토리아' == \
               self.hangulize(u'Naturalis Historia')
        assert u'콤멘타리이 데 벨로 갈리코' == \
               self.hangulize(u'Commentarii de Bello Gallico')
        assert u'콘페시오네스' == self.hangulize(u'Confessiones')
        assert u'메타모르포세온' == self.hangulize(u'Metamorphoseon')
        assert u'필로소피아이 나투랄리스 프링키피아 마테마티카' == \
               self.hangulize(u'Philosophiæ Naturalis Principia Mathematica')

    def test_mythology(self):
        assert u'아폴로' == self.hangulize(u'Apollo')
        assert u'바쿠스' == self.hangulize(u'Bacchus')
        assert u'케레스' == self.hangulize(u'Ceres')
        assert u'디아나' == self.hangulize(u'Diana')
        assert u'야누스' == self.hangulize(u'Ianus')
        assert u'유노' == self.hangulize(u'Iuno')
        assert u'유피테르' == self.hangulize(u'Iupitter')
        assert u'마르스' == self.hangulize(u'Mars')
        assert u'메르쿠리우스' == self.hangulize(u'Mercurius')
        assert u'미네르바' == self.hangulize(u'Minerva')
        assert u'넵투누스' == self.hangulize(u'Neptunus')
        assert u'플루토' == self.hangulize(u'Pluto')
        assert u'사투르누스' == self.hangulize(u'Saturnus')
        assert u'베누스' == self.hangulize(u'Venus')
        assert u'베스타' == self.hangulize(u'Vesta')
        assert u'불카누스' == self.hangulize(u'Vulcanus')

    def test_miscellaneous(self):
        assert u'콘술' == self.hangulize(u'consul')
        assert u'팍스 로마나' == self.hangulize(u'Pax Romana')
        assert u'레스 푸블리카' == self.hangulize(u'res publica')
        assert u'세나투스' == self.hangulize(u'senatus')
