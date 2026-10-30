from pathlib import Path
import sys
import yaml
import re

OBLIGATORIOS = ["titulo", "autor", "idioma", "tipo", "licencia", "enlace", "etiquetas"]
IDIOMAS = {"ca", "es", "en", "de", "fr", "pt", "it", "gl", "eu", "nl", "pl", "ru", "zh", "ja", "ar"}
TIPOS = re.compile(r"^[^\W\d_]+( [^\W\d_]+)*$")
LICENCIAS = {
    "Public-Domain", "CC0-1.0", "CC-BY-4.0", "CC-BY-SA-4.0",
    "MIT", "Apache-2.0", "GPL-3.0", "GFDL-1.3", "Dominio Público", "CC BY-NC-ND 4.0",
}

errores = []
archivos = sorted(Path("recursos").glob("*.yml"))

for f in archivos:
    try:
        r = yaml.safe_load(f.read_text(encoding="utf-8"))
    except yaml.YAMLError as e:
        errores.append(f"{f}: YAML no válido ({e})")
        continue

    if not isinstance(r, dict):
        errores.append(f"{f}: el archivo está vacío o mal formado")
        continue

    for campo in OBLIGATORIOS:
        if not r.get(campo):
            errores.append(f"{f}: falta el campo '{campo}'")

    if r.get("idioma") and r["idioma"] not in IDIOMAS:
        errores.append(f"{f}: idioma '{r['idioma']}' no permitido ({sorted(IDIOMAS)})")
    if r.get("tipo") and not TIPOS.match(str(r["tipo"])):
        errores.append(f"{f}: tipo '{r['tipo']}' solo puede contener letras")
    if r.get("licencia") and r["licencia"] not in LICENCIAS:
        errores.append(f"{f}: licencia '{r['licencia']}' no está en la lista permitida")
    if r.get("enlace") and not str(r["enlace"]).startswith("https://"):
        errores.append(f"{f}: el enlace debe empezar por https://")
    if r.get("etiquetas") and not isinstance(r["etiquetas"], list):
        errores.append(f"{f}: 'etiquetas' debe ser una lista, p. ej. [linux, redes]")

if errores:
    print("\n".join(errores))
    sys.exit(1)

print(f"OK: {len(archivos)} recursos válidos")
