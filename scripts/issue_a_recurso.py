import os
import re
import unicodedata
from pathlib import Path
import yaml

body = os.environ["ISSUE_BODY"].replace("\r\n", "\n")
numero = os.environ["ISSUE_NUMBER"]

# El formulario genera bloques "### Etiqueta" seguidos del valor
secciones = {}
for bloque in re.split(r"^### ", body, flags=re.MULTILINE)[1:]:
    nombre, _, valor = bloque.partition("\n")
    valor = valor.strip()
    secciones[nombre.strip()] = "" if valor == "_No response_" else valor


def slug(texto):
    texto = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode()
    texto = re.sub(r"[^a-z0-9]+", "-", texto.lower()).strip("-")
    return texto[:60] or "recurso"


recurso = {
    "titulo": secciones.get("Título", ""),
    "autor": secciones.get("Autor", ""),
    "idioma": secciones.get("Idioma", ""),
    "tipo": secciones.get("Tipo", ""),
    "licencia": secciones.get("Licencia", ""),
    "enlace": secciones.get("Enlace", ""),
    "etiquetas": [e.strip() for e in secciones.get("Etiquetas", "").split(",") if e.strip()],
}

ruta = Path("recursos") / f"{slug(recurso['titulo'])}.yml"
if ruta.exists():
    ruta = Path("recursos") / f"{slug(recurso['titulo'])}-{numero}.yml"

ruta.write_text(
    yaml.safe_dump(recurso, allow_unicode=True, sort_keys=False),
    encoding="utf-8",
)
print(f"Creado {ruta}")
