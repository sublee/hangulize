# -*- coding: utf-8 -*-
from tests import HangulizeTestCase
from hangulize.langs.lat import Latin


class LatinTestCase(HangulizeTestCase):

    lang = Latin()

    def test_people_roman(self):
        self.assert_examples({
            u'Flavius Aëtius': u'플라비우스 아에티우스',
            u'FLAVIVS AËTIVS': u'플라비우스 아에티우스',
            u'Gnaeus Julius Agricola': u'그나이우스 율리우스 아그리콜라',
            u'GNAEUS IVLIVS AGRICOLA': u'그나이우스 율리우스 아그리콜라',
            u'Marcus Vipsanius Agrippa': u'마르쿠스 빕사니우스 아그리파',
            u'MARCVS VIPSANIVS AGRIPPA': u'마르쿠스 빕사니우스 아그리파',
            u'Julia Augusta Agrippina': u'율리아 아우구스타 아그리피나',
            u'IVLIA AVGVSTA AGRIPPINA': u'율리아 아우구스타 아그리피나',
            u'Marcus Antonius': u'마르쿠스 안토니우스',
            u'MARCVS ANTONIVS': u'마르쿠스 안토니우스',
            u'Apuleius': u'아풀레이우스',
            u'APVLEIVS': u'아풀레이우스',
            u'Gaius Julius Caesar Augustus': \
                u'가이우스 율리우스 카이사르 아우구스투스',
            u'GAIVS IVLIVS CAESAR AVGVSTVS': \
                u'가이우스 율리우스 카이사르 아우구스투스',
            u'Gaius Julius Caesar': u'가이우스 율리우스 카이사르',
            u'GAIVS IVLIVS CAESAR': u'가이우스 율리우스 카이사르',
            u'Gaius Valerius Catullus': u'가이우스 발레리우스 카툴루스',
            u'GAIVS VALERIVS CATVLLVS': u'가이우스 발레리우스 카툴루스',
            u'Marcus Tullius Cicero': u'마르쿠스 툴리우스 키케로',
            u'MARCVS TVLLIVS CICERO': u'마르쿠스 툴리우스 키케로',
            u'Tiberius Claudius Caesar Augustus Germanicus': \
                u'티베리우스 클라우디우스 카이사르 아우구스투스 게르마니쿠스',
            u'TIBERIVS CLAVDIVS CAESAR AVGVSTVS GERMANICVS': \
                u'티베리우스 클라우디우스 카이사르 아우구스투스 게르마니쿠스',
            u'Lucius Aurelius Commodus Antoninus': \
                u'루키우스 아우렐리우스 콤모두스 안토니누스',
            u'LVCIVS AVRELIVS COMMODVS ANTONINVS': \
                u'루키우스 아우렐리우스 콤모두스 안토니누스',
            u'Flavius Valerius Aurelius Constantinus': \
                u'플라비우스 발레리우스 아우렐리우스 콘스탄티누스',
            u'FLAVIVS VALERIVS AVRELIVS CONSTANTINVS': \
                u'플라비우스 발레리우스 아우렐리우스 콘스탄티누스',
            u'Cornelia Scipionis Africana': \
                u'코르넬리아 스키피오니스 아프리카나',
            u'CORNELIA SCIPIONIS AFRICANA': \
                u'코르넬리아 스키피오니스 아프리카나',
            u'Marcus Licinius Crassus': u'마르쿠스 리키니우스 크라수스',
            u'MARCVS LICINIVS CRASSVS': u'마르쿠스 리키니우스 크라수스',
            u'Gaius Aurelius Valerius Diocletianus': \
                u'가이우스 아우렐리우스 발레리우스 디오클레티아누스',
            u'GAIVS AVRELIVS VALERIVS DIOCLETIANVS': \
                u'가이우스 아우렐리우스 발레리우스 디오클레티아누스',
            u'Publius Aelius Hadrianus': u'푸블리우스 아일리우스 하드리아누스',
            u'PVBLIVS AELIVS HADRIANVS': u'푸블리우스 아일리우스 하드리아누스',
            u'Quintus Horatius Flaccus': u'퀸투스 호라티우스 플라쿠스',
            u'QVINTVS HORATIVS FLACCVS': u'퀸투스 호라티우스 플라쿠스',
            u'Flavius Petrus Sabbatius Justinianus': \
                u'플라비우스 페트루스 사바티우스 유스티니아누스',
            u'FLAVIVS PETRVS SABBATIVS IVSTINIANVS': \
                u'플라비우스 페트루스 사바티우스 유스티니아누스',
            u'Titus Livius': u'티투스 리비우스',
            u'TITVS LIVIVS': u'티투스 리비우스',
            u'Gaius Marius': u'가이우스 마리우스',
            u'GAIVS MARIVS': u'가이우스 마리우스',
            u'Nero Claudius Caesar Augustus Germanicus': \
                u'네로 클라우디우스 카이사르 아우구스투스 게르마니쿠스',
            u'NERO CLAVDIVS CAESAR AVGVSTVS GERMANICVS': \
                u'네로 클라우디우스 카이사르 아우구스투스 게르마니쿠스',
            u'Gaius Octavius': u'가이우스 옥타비우스',
            u'GAIVS OCTAVIVS': u'가이우스 옥타비우스',
            u'Titus Maccius Plautus': u'티투스 마키우스 플라우투스',
            u'TITVS MACCIVS PLAVTVS': u'티투스 마키우스 플라우투스',
            u'Gaius Plinius Secundus': u'가이우스 플리니우스 세쿤두스',
            u'GAIVS PLINIVS SECVNDVS': u'가이우스 플리니우스 세쿤두스',
            u'Gaius Plinius Caecilius Secundus': \
                u'가이우스 플리니우스 카이킬리우스 세쿤두스',
            u'GAIVS PLINIVS CAECILIVS SECVNDVS': \
                u'가이우스 플리니우스 카이킬리우스 세쿤두스',
            u'Gnaeus Pompeius Magnus': u'그나이우스 폼페이우스 마그누스',
            u'GNAEVS POMPEIVS MAGNVS': u'그나이우스 폼페이우스 마그누스',
            u'Sextus Aurelius Propertius': \
                u'섹스투스 아우렐리우스 프로페르티우스',
            u'SEXTVS AVRELIVS PROPERTIVS': \
                u'섹스투스 아우렐리우스 프로페르티우스',
            u'Gaius Sallustius Crispus': u'가이우스 살루스티우스 크리스푸스',
            u'GAIVS SALLVSTIVS CRISPVS': u'가이우스 살루스티우스 크리스푸스',
            u'Lucius Annaeus Seneca': u'루키우스 안나이우스 세네카',
            u'LVCIVS ANNAEUS SENECA': u'루키우스 안나이우스 세네카',
            u'Spartacus': u'스파르타쿠스',
            u'SPARTACVS': u'스파르타쿠스',
            u'Gaius Suetonius Tranquillus': u'가이우스 수에토니우스 트랑퀼루스',
            u'GAIVS SVETONIVS TRANQVILLVS': u'가이우스 수에토니우스 트랑퀼루스',
            u'Lucius Cornelius Sulla Felix': \
                u'루키우스 코르넬리우스 술라 펠릭스',
            u'LVCIVS CORNELIVS SVLLA FELIX': \
                u'루키우스 코르넬리우스 술라 펠릭스',
            u'Publius Cornelius Tacitus': u'푸블리우스 코르넬리우스 타키투스',
            u'PVBLIVS CORNELIVS TACITVS': u'푸블리우스 코르넬리우스 타키투스',
            u'Marcus Ulpius Nerva Trajanus': \
                u'마르쿠스 울피우스 네르바 트라야누스',
            u'MARCUS VLPIVS NERVA TRAIANVS': \
                u'마르쿠스 울피우스 네르바 트라야누스',
            u'Publius Vergilius Maro': u'푸블리우스 베르길리우스 마로',
            u'PVBLIVS VERGILIVS MARO': u'푸블리우스 베르길리우스 마로',
            u'Titus Flavius Vespasianus': u'티투스 플라비우스 베스파시아누스',
            u'TITVS FLAVIVS VESPASIANVS': u'티투스 플라비우스 베스파시아누스',
            u'Marcus Vitruvius Pollio': u'마르쿠스 비트루비우스 폴리오',
            u'MARCVS VITRVVIVS POLLIO': u'마르쿠스 비트루비우스 폴리오',
        })

    def test_people_nonroman(self):
        self.assert_examples({
            u'Georgius Agricola': u'게오르기우스 아그리콜라',
            u'Anselmus': u'안셀무스',
            u'Averroës': u'아베로에스',
            u'Aurelius Augustinus Hipponensis': \
                u'아우렐리우스 아우구스티누스 히포넨시스',
            u'Carolus Magnus': u'카롤루스 마그누스',
            u'Nicolaus Copernicus': u'니콜라우스 코페르니쿠스',
            u'Cyrus': u'키루스',
            u'Darius': u'다리우스',
            u'Gotarzes': u'고타르제스',
            u'Hannibal': u'한니발',
            u'Flavius Josephus': u'플라비우스 요세푸스',
            u'Mithridates': u'미트리다테스',
            u'Flavius Odoacer': u'플라비우스 오도아케르',
        })

    def test_places(self):
        self.assert_examples({
            u'Aegyptus': u'아이깁투스',
            u'Asia': u'아시아',
            u'Assyria': u'아시리아',
            u'Britannia': u'브리탄니아',
            u'Carthago': u'카르타고',
            u'Cannae': u'칸나이',
            u'Galatia': u'갈라티아',
            u'Gallia': u'갈리아',
            u'Germania': u'게르마니아',
            u'Hispania': u'히스파니아',
            u'Illyricum': u'일리리쿰',
            u'Iudaea': u'유다이아',
            u'Latium': u'라티움',
            u'Lusitania': u'루시타니아',
            u'Numidia': u'누미디아',
            u'Padus': u'파두스',
            u'Parthia': u'파르티아',
        #    u'Pompeii': u'폼페이',
            u'Roma': u'로마',
            u'Sicilia': u'시킬리아',
            u'Syracusae': u'시라쿠사이',
            u'Thracia': u'트라키아',
            u'Mons Vesuvius': u'몬스 베수비우스',
        })

    def test_texts(self):
        self.assert_examples({
            u'Aeneis': u'아이네이스',
            u'Naturalis Historia': u'나투랄리스 히스토리아',
            u'Commentarii de Bello Gallico': u'콤멘타리이 데 벨로 갈리코',
            u'Confessiones': u'콘페시오네스',
            u'Metamorphoseon': u'메타모르포세온',
            u'Philosophiæ Naturalis Principia Mathematica': \
                u'필로소피아이 나투랄리스 프링키피아 마테마티카',
        })

    def test_mythology(self):
        self.assert_examples({
            u'Apollo': u'아폴로',
            u'Bacchus': u'바쿠스',
            u'Ceres': u'케레스',
            u'Diana': u'디아나',
            u'Ianus': u'야누스',
            u'Iuno': u'유노',
            u'Iupitter': u'유피테르',
            u'Mars': u'마르스',
            u'Mercurius': u'메르쿠리우스',
            u'Minerva': u'미네르바',
            u'Neptunus': u'넵투누스',
            u'Pluto': u'플루토',
            u'Saturnus': u'사투르누스',
            u'Venus': u'베누스',
            u'Vesta': u'베스타',
            u'Vulcanus': u'불카누스',
        })

    def test_miscellaneous(self):
        self.assert_examples({
            u'consul': u'콘술',
            u'Pax Romana': u'팍스 로마나',
            u'res publica': u'레스 푸블리카',
            u'senatus': u'세나투스',
        })
