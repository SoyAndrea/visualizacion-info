library(tidyverse)
library(janitor)
library(scales)
library(knitr)
library(tidytext)

renaper <- paste0(
  "https://datosabiertos.renaper.gob.ar/",
  "Cantidad_de_tramites_de_DNI_argentino_",
  "por_nacionalidad_pais_anio.csv"
)

pob_nacionalizada <- read_csv(renaper, show_col_types = FALSE)


desagregado_carta <- read_csv("https://datosabiertos.renaper.gob.ar/Cantidad_de_personas_nacionalizada_carta_de_ciudadania_sexo_edad_actual_y_edad_tramite.csv",
         show_col_types = FALSE)

desagregado_opcion <- read_csv("https://datosabiertos.renaper.gob.ar/Cantidad_de_personas_nacionalizadas_opcion_sexo_edad_actual_y_edad_tramite.csv",
                        show_col_types = FALSE)


write

## Lectura de composición del  dataset
glimpse(pob_nacionalizada)

write.csv(desagregado_carta, 
          "data/desagregado_carta.csv",
          row.names = FALSE,
          fileEncoding = "UTF-8")


write.csv(desagregado_opcion, 
          "data/desagregado_opcion.csv",
          row.names = FALSE,
          fileEncoding = "UTF-8")


write.csv(desagregado, 
          "data/base_desagregado.csv",
          row.names = FALSE,
          fileEncoding = "UTF-8")