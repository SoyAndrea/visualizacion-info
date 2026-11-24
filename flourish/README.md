# Datos para la story de Flourish "Nuevos argentinos"

Generados con `python flourish/preparar_datos_flourish.py` (desde la raíz del proyecto) a partir de `data/`.

| Archivo | Plantilla de Flourish | Cómo cargarlo |
|---|---|---|
| `00_cifras_clave.csv` | Number ticker / tarjetas | Valores para textos y contadores |
| `01_serie_anual_por_via.csv` | Line chart | Labels: Año · Values: Carta de ciudadanía, Opción |
| `02_bar_race_carta_anual.csv` | Bar chart race | Label: País · Values: 2013…2025 (trámites de cada año) |
| `02_bar_race_carta_acumulado.csv` | Bar chart race | Igual, pero acumulado (la carrera se ve más suave) |
| `03_mapa_por_pais.csv` | Projection map (regiones) | Geometría: ISO3 · Valor: Total o una vía |
| `04_sankey_pais_via.csv` | Sankey | Source: Origen · Target: Destino · Value: Valor |
| `05_piramide_por_via.csv` | Population pyramid | Category: Grupo etario · Values: Varones, Mujeres · Filtro: Vía |
| `06_pct_mujeres_por_grupo.csv` | Bar / column chart | Labels: Grupo etario · Values: una columna por vía |

## Decisiones

- País: nombres con tildes y duplicados unificados (China, Países Bajos, Kirguistán). "Otro país" y "Yugoslavia (ex)" no tienen ISO3 y quedan fuera del mapa.
- Perfil: solo filas `TOTAL` de RENAPER (las filas por país son los 10 principales y duplicaban personas). Edad al momento del trámite.
- Grupos etarios armonizados: carta usa "18 a 24" y opción "15 a 19" y "20 a 24"; se unificaron en **15 a 24**.
- Pirámide en % del total de cada vía (columna Vía: Todas, Carta de ciudadanía, Opción).
- 2025 es parcial (hasta el 20/8/2025).

Paleta: carta #6553C4 · opción #2A9D8F · varones #8D99AE · mujeres #FAD764 · estructura #3F3567
