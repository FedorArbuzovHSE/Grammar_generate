import pymorphy2
import random
from updateGenerate import Sphere, Theme_q


def main_met(i):
    # главное в вопросе
    k = random.randint(1, 3)
    sent[i] += Theme_q.main_t[k]
    sent[i] += Theme_q.main_t_i[k]

def sphere(i):
    # сфера
    k = random.randint(1, len(usl_new.values()) - 1)
    sent[i] += str(usl_new[k]) + '|O '
    k = random.randint(1, len(Sphere.sph.values()) - 1)
    sent[i] += ret_pad(Sphere.sph[k]) + '|' + Sphere.sph_i[k] + ' '


def year(i):
    # год
    sent[i] += str(random.randint(1800, 2045)) + '|B-T.time '
    sent[i] += 'год|I-T.time' + ' '

def region(i):
    # регион
    sent[i] += 'в|O' + ' '
    k = random.randint(1, len(places)-1)
    sent[i] += ret_pad(places[k]) + '|B-L.location'

def ret_pad(s):

    pad = {1: 'nomn', 2: 'gent', 3: 'datv', 4: 'accs', 5: 'ablt', 6: 'loct'}

    reg = morph.parse(s)[0]
    k = random.randint(1, 6)
    try:
        return reg.inflect({pad[k]})[0]
    except:
        return s


PLACES = {
    'адыгея': ('67646', 'республики Адыгеи'),
    'алания': ('67652', 'республики Алании'),
    'алтай': ('67684', 'республики Алтай'),
    'алтайский': ('67688', 'Алтайского края'),
    'амурская': ('67708', 'Амурской области'),
    'архангельская': ('67678', 'Архангельской области'),
    'астраханская': ('67645', 'Астраханской области'),
    'байконур': ('93015', 'Байконура'),
    'башкортостан': ('67655', 'республики Башкортостан'),
    'белгородская': ('67721', 'Белгородской области'),
    'брянская': ('67719', 'Брянской области'),
    'бурятия': ('67691', 'республики Бурятия'),
    'владимирская': ('67716', 'Владимирской области'),
    'волгоградская': ('67647', 'Волгоградской области'),
    'вологодская': ('67674', 'Вологодской области'),
    'воронежская': ('67723', 'Воронежской области'),
    'дагестан': ('67643', 'республики Дагестан'),
    'дальневосточный': ('17698', 'Дальневосточного федерального округа'),
    'еврейская': ('67705', 'Еврейской автономной области'),
    'забайкальский': ('67729', 'Забайкальского края'),
    'ивановская': ('67722', 'Ивановской области'),
    'ингушетия': ('67649', 'республики Ингушетия'),
    'иркутская': ('67682', 'Иркутской области'),
    'кабардино-балкарская': ('67651', 'Кабардино-Балкарской республики'),
    'калининградская': ('67670', 'Калининградской области'),
    'калмыкия': ('67648', 'Калмыкии'),
    'калужская': ('67712', 'Калужской области'),
    'камчатский': ('67728', 'Камчатского края'),
    'карачаево-черкесская': ('67638', 'Карачаево-Черкесской республики'),
    'карелия': ('67677', 'республики Карелия'),
    'кемеровская': ('67689', 'Кемеровской области'),
    'кировская': ('67663', 'Кировской области'),
    'коми': ('67673', 'республики Коми'),
    'костромская': ('67714', 'Костромской области'),
    'краснодарский': ('67644', 'Краснодарского края'),
    'красноярский': ('67694', 'Красноярского края'),
    'крым': ('93010', 'республики Крым'),
    'крымский': ('91128', 'Крымского федерального округа'),
    'курганская': ('67699', 'Курганской области'),
    'курская': ('67710', 'Курской области'),
    'ленинградская': ('67676', 'Ленинградской области'),
    'липецкая': ('67711', 'Липецкой области'),
    'магаданская': ('67703', 'Магаданской области'),
    'марий': ('67666', 'республики Марий Эл'),  # Meant 'Марий Эл'
    'мордовия': ('67662', 'республики Мордовия'),
    'москва': ('67724', 'Москвы'),
    'московская': ('67709', 'Московской области'),
    'мурманская': ('67669', 'Мурманской области'),
    'ненецкий': ('67672', 'Ненецкого автономного округа'),
    'нижегородская': ('67656', 'Нижегородской области'),
    'новгородская': ('67675', 'Новгородской области'),
    'новосибирская': ('67690', 'Новосибирской области'),
    'омская': ('67687', 'Омской области'),
    'оренбургская': ('67659', 'Оренбургской области'),
    'орловская': ('67726', 'Орловской области'),
    'осетия': ('67652', 'республики Северная Осетия'),
    'пензенская': ('67667', 'Пензенской области'),
    'пермский': ('67727', 'Пермского края'),
    'приволжский': ('3417', 'Приволожского федерального округа'),
    'приморский': ('67706', 'Приморского края'),
    'псковская': ('67671', 'Псковской области'),
    'россия': ('2', 'России'),
    'ростовская': ('67653', 'Ростовской области'),
    'рф': ('2', 'России'),
    'рязанская': ('67720', 'Рязанской области'),
    'самарская': ('67658', 'Самарской области'),
    'санкт-петербург': ('67639', 'Санкт-Петербурга'),
    'саратовская': ('67665', 'Саратовской области'),
    'саха': ('67642', 'республики Саха'),
    'сахалинская': ('67704', 'Сахалинской области'),
    'свердловская': ('67698', 'Свердловской области'),
    'севастополь': ('93011', 'Севастополя'),
    'северо-западный': ('10249', 'Северо-Западного федерального округа'),
    'северо-кавказский': ('24604', 'Северо-Кавказского федерального округа'),
    'сибирский': ('12097', 'Сибирского федерального округа'),
    'смоленская': ('67718', 'Смоленской области'),
    'ставропольский': ('67654', 'Ставропольского края'),
    'ставрополье': ('67654', 'Ставрополья'),  # Another version of 'ставропольский
    'тамбовская': ('67725', 'Тамбовской области'),
    'татарстан': ('67661', 'республики Татарстан'),
    'тверская': ('67717', 'Тверской области'),
    'томская': ('67692', 'Томской области'),
    'тульская': ('67715', 'Тульской области'),
    'тыва': ('67683', 'руспублики Тыва'),
    'тува': ('67683', 'Тувы'),  # Another version of 'тыва
    'тюменская': ('67697', 'Тюменской области'),
    'удмуртская': ('67668', 'республики Удмуртия'),
    'ульяновская': ('67660', 'Ульяновской области'),
    'уральский': ('16333', 'Уральского федерального округа'),
    'хабаровский': ('67707', 'Хабаровского края'),
    'хакасия': ('67681', 'республики Хакасия'),
    'ханты-мансийский': ('67695', 'Ханты-Мансийского автономного округа'),
    'центральный': ('19099', 'Центрального федерального округа'),
    'челябинская': ('67700', 'Челябинской области'),
    'чеченская': ('67650', 'Чеченской республики'),
    'чечня': ('67650', 'Чечни'),  # Another version of 'чеченская
    'чувашия': ('67664', 'Чувашии'),
    'чувашская': ('67664', 'Чувашской республики'),
    'чукотский': ('67640', 'Чукотского автономного округа'),
    'югра': ('67695', 'Югры'),
    'южный': ('3', 'Южного федерального округа'),
    'якутия': ('67642', 'Якутии'),
    'ямало-ненецкий': ('67696', 'Ямало-Ненецкого автономного округа'),
    'ярославская': ('67713', 'Ярославской области')
}
morph = pymorphy2.MorphAnalyzer()
places = list(PLACES.keys())
usl_new = {i: s for i, s in enumerate([
    'в', 'без', 'до', 'из', 'к', 'на', 'по', 'о', 'от', 'перед', 'при', 'через', 'с', 'у', 'за', 'над', 'об', 'под', 'про', 'для'])}

sent = ['' for i in range(1000)]

vector_of_methods = {1: main_met,
                      2: sphere,
                      3: year,
                      4: region}


sent1 = ['' for i in range(200)]
for i in range(200):
    mask_bool = [random.randint(1, 2) for i in range(4)]
    for num, i1 in enumerate(mask_bool):
        if i1 == 1:
            vector_of_methods[num + 1](i)


f = open('sent.txt', 'w')
for s in sent:
    f.write(s + '\n')