# Prepara los CSV para la story de Flourish "Nuevos argentinos"
# Fuente: RENAPER, datos abiertos. Correr desde la raíz del proyecto:
#   python flourish/preparar_datos_flourish.py
import pandas as pd
from pathlib import Path

DATA = Path("data")
OUT = Path("flourish")
OUT.mkdir(exist_ok=True)

# Nombre para mostrar e ISO3 de cada país (los duplicados de RENAPER se unifican)
PAISES = {
 "ALBANIA":("Albania","ALB"),"ALEMANIA":("Alemania","DEU"),"ANDORRA":("Andorra","AND"),"ANGOLA":("Angola","AGO"),
 "ARABIA SAUDITA":("Arabia Saudita","SAU"),"ARGELIA":("Argelia","DZA"),"ARMENIA":("Armenia","ARM"),"ARUBA":("Aruba","ABW"),
 "AUSTRALIA":("Australia","AUS"),"AUSTRIA":("Austria","AUT"),"AZERBAIJAN":("Azerbaiyán","AZE"),"BAHREIN":("Baréin","BHR"),
 "BANGLADESH":("Bangladés","BGD"),"BELGICA":("Bélgica","BEL"),"BIELORRUSIA":("Bielorrusia","BLR"),"BOLIVIA":("Bolivia","BOL"),
 "BRASIL":("Brasil","BRA"),"BULGARIA":("Bulgaria","BGR"),"BURKINA FASO":("Burkina Faso","BFA"),"CABO VERDE":("Cabo Verde","CPV"),
 "CAMBOYA":("Camboya","KHM"),"CAMERUN":("Camerún","CMR"),"CANADA":("Canadá","CAN"),"CHILE":("Chile","CHL"),"CHINA":("China","CHN"),
 "REPUBLICA POPULAR CHINA":("China","CHN"),"CHIPRE":("Chipre","CYP"),"COLOMBIA":("Colombia","COL"),"CONGO":("Congo","COG"),
 "COREA DEL SUR":("Corea del Sur","KOR"),"COSTA DE MARFIL":("Costa de Marfil","CIV"),"COSTA RICA":("Costa Rica","CRI"),
 "CROACIA":("Croacia","HRV"),"CUBA":("Cuba","CUB"),"DINAMARCA":("Dinamarca","DNK"),"DOMINICA":("Dominica","DMA"),
 "ECUADOR":("Ecuador","ECU"),"EGIPTO":("Egipto","EGY"),"EL SALVADOR":("El Salvador","SLV"),
 "EMIRATOS ARABES UNIDOS":("Emiratos Árabes Unidos","ARE"),"ESLOVENIA":("Eslovenia","SVN"),"ESPAÑA":("España","ESP"),
 "ESTADOS UNIDOS":("Estados Unidos","USA"),"ESTONIA":("Estonia","EST"),"FILIPINAS":("Filipinas","PHL"),"FINLANDIA":("Finlandia","FIN"),
 "FRANCIA":("Francia","FRA"),"GEORGIA":("Georgia","GEO"),"GHANA":("Ghana","GHA"),"GRECIA":("Grecia","GRC"),"GUATEMALA":("Guatemala","GTM"),
 "GUINEA":("Guinea","GIN"),"GUINEA-BISSAU":("Guinea-Bisáu","GNB"),"HAITI":("Haití","HTI"),"HOLANDA":("Países Bajos","NLD"),
 "PAISES BAJOS":("Países Bajos","NLD"),"HONDURAS":("Honduras","HND"),"HONG KONG":("Hong Kong","HKG"),"HUNGRIA":("Hungría","HUN"),
 "INDIA":("India","IND"),"INDONESIA":("Indonesia","IDN"),"IRAN":("Irán","IRN"),"IRAQ":("Irak","IRQ"),"IRLANDA":("Irlanda","IRL"),
 "ISLANDIA":("Islandia","ISL"),"ISRAEL":("Israel","ISR"),"ITALIA":("Italia","ITA"),"JAPON":("Japón","JPN"),"JORDANIA":("Jordania","JOR"),
 "KAZAKHSTAN":("Kazajistán","KAZ"),"KENIA":("Kenia","KEN"),"KIRGUISTAN":("Kirguistán","KGZ"),"KYRGYZSTAN":("Kirguistán","KGZ"),
 "KUWAIT":("Kuwait","KWT"),"LAOS":("Laos","LAO"),"LETONIA":("Letonia","LVA"),"LIBANO":("Líbano","LBN"),"LIBERIA":("Liberia","LBR"),
 "LIBIA":("Libia","LBY"),"LUXEMBURGO":("Luxemburgo","LUX"),"MALASIA":("Malasia","MYS"),"MALI":("Malí","MLI"),"MALTA":("Malta","MLT"),
 "MARRUECOS":("Marruecos","MAR"),"MEXICO":("México","MEX"),"MOLDAVIA":("Moldavia","MDA"),"MONACO":("Mónaco","MCO"),
 "MOZAMBIQUE":("Mozambique","MOZ"),"NICARAGUA":("Nicaragua","NIC"),"NIGERIA":("Nigeria","NGA"),"NORUEGA":("Noruega","NOR"),
 "NUEVA ZELANDA":("Nueva Zelanda","NZL"),"OTRO PAIS":("Otro país",""),"PAKISTAN":("Pakistán","PAK"),"PALESTINA":("Palestina","PSE"),
 "PANAMA":("Panamá","PAN"),"PARAGUAY":("Paraguay","PRY"),"PERU":("Perú","PER"),"POLONIA":("Polonia","POL"),"PORTUGAL":("Portugal","PRT"),
 "PUERTO RICO":("Puerto Rico","PRI"),"QATAR":("Catar","QAT"),"REINO UNIDO":("Reino Unido","GBR"),"REPUBLICA CHECA":("Chequia","CZE"),
 "REPUBLICA DEMOCRATICA DEL CONGO":("Rep. Dem. del Congo","COD"),"REPUBLICA DOMINICANA":("Rep. Dominicana","DOM"),
 "RUMANIA":("Rumania","ROU"),"RUSIA":("Rusia","RUS"),"SAN MARINO":("San Marino","SMR"),"SENEGAL":("Senegal","SEN"),"SERBIA":("Serbia","SRB"),
 "SIERRA LEONA":("Sierra Leona","SLE"),"SINGAPUR":("Singapur","SGP"),"SIRIA":("Siria","SYR"),"SUDAFRICA":("Sudáfrica","ZAF"),
 "SUDAN":("Sudán","SDN"),"SUECIA":("Suecia","SWE"),"SUIZA":("Suiza","CHE"),"TAILANDIA":("Tailandia","THA"),"TUNEZ":("Túnez","TUN"),
 "TURKMENISTAN":("Turkmenistán","TKM"),"TURQUIA":("Turquía","TUR"),"UCRANIA":("Ucrania","UKR"),"URUGUAY":("Uruguay","URY"),
 "UZBEKISTAN":("Uzbekistán","UZB"),"VENEZUELA":("Venezuela","VEN"),"VIETNAM":("Vietnam","VNM"),"YEMEN":("Yemen","YEM"),
 "YUGOSLAVIA":("Yugoslavia (ex)",""),"ZIMBABUE":("Zimbabue","ZWE"),
}
VIA = {"CARTA": "Carta de ciudadanía", "OPCION": "Opción"}

base = pd.read_csv(DATA / "base_nacionalizaciones.csv")
faltan = set(base["pais_nac"]) - set(PAISES)
assert not faltan, f"Países sin mapear: {faltan}"
base["País"] = base["pais_nac"].map(lambda p: PAISES[p][0])
base["ISO3"] = base["pais_nac"].map(lambda p: PAISES[p][1])
base["Vía"] = base["Tipo_nacionalidad"].map(VIA)
base = base.groupby(["País", "ISO3", "Vía", "anio"], as_index=False)["cantidad"].sum()

# 1. Serie anual por vía
linea = base.pivot_table(index="anio", columns="Vía", values="cantidad", aggfunc="sum").reset_index()
linea = linea.rename(columns={"anio": "Año"})[["Año", "Carta de ciudadanía", "Opción"]]
linea.to_csv(OUT / "01_serie_anual_por_via.csv", index=False)

# 2. Bar chart race: carta de ciudadanía por país y año (anual y acumulado)
carta = base[base["Vía"] == "Carta de ciudadanía"]
race = carta.pivot_table(index="País", columns="anio", values="cantidad", aggfunc="sum", fill_value=0)
race.reset_index().to_csv(OUT / "02_bar_race_carta_anual.csv", index=False)
race.cumsum(axis=1).reset_index().to_csv(OUT / "02_bar_race_carta_acumulado.csv", index=False)

# 3. Mapa: total del período por país y vía
mapa = base.pivot_table(index=["País", "ISO3"], columns="Vía", values="cantidad", aggfunc="sum", fill_value=0).reset_index()
mapa["Total"] = mapa["Carta de ciudadanía"] + mapa["Opción"]
mapa["% por carta"] = (mapa["Carta de ciudadanía"] / mapa["Total"] * 100).round(1)
mapa = mapa[mapa["ISO3"] != ""].sort_values("Total", ascending=False)
mapa.to_csv(OUT / "03_mapa_por_pais.csv", index=False)

# 4. Sankey país -> vía (top 10 de cada vía; el resto agrupado)
tot = base.groupby(["País", "Vía"], as_index=False)["cantidad"].sum()
top = set()
for v in VIA.values():
    top |= set(tot[tot["Vía"] == v].nlargest(10, "cantidad")["País"])
tot["Origen"] = tot["País"].where(tot["País"].isin(top), "Otros países")
sankey = tot.groupby(["Origen", "Vía"], as_index=False)["cantidad"].sum()
sankey = sankey.rename(columns={"Vía": "Destino", "cantidad": "Valor"}).sort_values("Valor", ascending=False)
sankey.to_csv(OUT / "04_sankey_pais_via.csv", index=False)

# 5 y 6. Perfil por sexo y edad al trámite (solo filas TOTAL, para no duplicar)
GRUPOS = {"0 a 4":"0 a 4","5 a 9":"5 a 9","10 a 14":"10 a 14","15 a 19":"15 a 24","18 a 24":"15 a 24","20 a 24":"15 a 24",
          "25 a 29":"25 a 29","30 a 34":"30 a 34","35 a 39":"35 a 39","40 a 44":"40 a 44","45 a 49":"45 a 49",
          "50 a 54":"50 a 54","55 a 59":"55 a 59","60 a 64":"60 a 64","65 a 69":"65 a 69","70 y mas":"70 y más"}
ORDEN = list(dict.fromkeys(GRUPOS.values()))
perfil = []
for archivo, via in [("desagregado_carta.csv", "Carta de ciudadanía"), ("desagregado_opcion.csv", "Opción")]:
    d = pd.read_csv(DATA / archivo)
    d = d[d["pais_nacimiento"] == "TOTAL"].copy()
    d["Vía"] = via
    perfil.append(d)
perfil = pd.concat(perfil)
perfil["Grupo etario"] = perfil["grupo_etario"].map(GRUPOS)
perfil["Sexo"] = perfil["sexo"].map({"VARON": "Varones", "MUJER": "Mujeres"})
p = perfil.groupby(["Vía", "Grupo etario", "Sexo"], as_index=False)["cantidad_edad_tramite"].sum()
p_todas = p.groupby(["Grupo etario", "Sexo"], as_index=False)["cantidad_edad_tramite"].sum().assign(Vía="Todas")
p = pd.concat([p_todas, p])

piramide = p.pivot_table(index=["Vía", "Grupo etario"], columns="Sexo", values="cantidad_edad_tramite", fill_value=0).reset_index()
piramide["Personas"] = piramide["Varones"] + piramide["Mujeres"]
total_via = piramide.groupby("Vía")["Personas"].transform("sum")
piramide["% mujeres en el grupo"] = (piramide["Mujeres"] / piramide["Personas"] * 100).round(1)
piramide["Varones"] = (piramide["Varones"] / total_via * 100).round(2)
piramide["Mujeres"] = (piramide["Mujeres"] / total_via * 100).round(2)
piramide["orden"] = piramide["Grupo etario"].map(ORDEN.index)
piramide["orden_via"] = piramide["Vía"].map({"Todas": 0, "Carta de ciudadanía": 1, "Opción": 2})
piramide = piramide.sort_values(["orden_via", "orden"], ascending=[True, False])
piramide[["Vía", "Grupo etario", "Varones", "Mujeres"]].to_csv(OUT / "05_piramide_por_via.csv", index=False)

pct = piramide.pivot_table(index=["orden", "Grupo etario"], columns="Vía", values="% mujeres en el grupo").reset_index()
pct = pct.sort_values("orden")[["Grupo etario", "Todas", "Carta de ciudadanía", "Opción"]]
pct.to_csv(OUT / "06_pct_mujeres_por_grupo.csv", index=False)

# 7. Cifras clave para tarjetas y textos
cifras = {
    "Total nacionalizaciones 2013-2025": int(base["cantidad"].sum()),
    "Carta de ciudadanía": int(base.loc[base["Vía"] == "Carta de ciudadanía", "cantidad"].sum()),
    "Opción": int(base.loc[base["Vía"] == "Opción", "cantidad"].sum()),
    "Total perfil (filas TOTAL)": int(perfil["cantidad_edad_tramite"].sum()),
    "% mujeres (perfil)": round(perfil.loc[perfil["Sexo"] == "Mujeres", "cantidad_edad_tramite"].sum() / perfil["cantidad_edad_tramite"].sum() * 100, 1),
}
pd.DataFrame(list(cifras.items()), columns=["Indicador", "Valor"], dtype=object).to_csv(OUT / "00_cifras_clave.csv", index=False)
print("Listo:", sorted(x.name for x in OUT.glob("*.csv")))
