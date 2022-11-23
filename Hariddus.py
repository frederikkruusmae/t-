def loe_andmed():
    with open("haridus.txt", "r") as f:
        read = f.readlines()

    veerud = []
    for rida in read:
        veerg = []
        
        for i in rida.removesuffix("\n").split():
            try:
                veerg.append(int(i))
            except ValueError:
                veerg.append(i)
        veerud.append(veerg)

    return veerud


def suurim_korgharidus_meestest(andmed):
    suurim = 0
    suurim_koht = []

    for koht in andmed:
        protsent = koht[2]/koht[3]
        if protsent > suurim:
            suurim = protsent
            suurim_koht = koht

    return suurim_koht[0], suurim_koht[1], suurim


def loenda_korghariduseta_naisi_rohkem_kui_mehi(andmed):
    loendus = 0

    for koht in andmed:
        korghariduseta_naisi = koht[5] - koht[4]
        korghariduseta_mehi = koht[3] - koht[2]

        if korghariduseta_naisi > korghariduseta_mehi:
            loendus += 1

    return loendus


def tabel_andmetega(andmed, etteantud_suurus):
    tabel = ""

    for koht in andmed:
        korgharidusega_inimeste_arv = koht[4] + koht[2]

        if korgharidusega_inimeste_arv > etteantud_suurus:
            tabel += " ".join([koht[0], koht[1], str(korgharidusega_inimeste_arv) + "\n"])

    if tabel == "":
        return "Selliseid omavalitsusi ei ole"
    return tabel


andmed = loe_andmed()

skmk = suurim_korgharidus_meestest(andmed)
print("Suurim korgharidus meestest:", skmk[0], skmk[1], skmk[2]*100, "%")

knrkm = loenda_korghariduseta_naisi_rohkem_kui_mehi(andmed)
print(knrkm, "linnas on korghariduseta naisi rohkem kui mehi")

etteantud_suurus = int(input("Etteantud suurus: "))
tabel = tabel_andmetega(andmed, etteantud_suurus)
print(tabel)
