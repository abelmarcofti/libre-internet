from pathlib import Path
import yaml

recursos = []
for f in sorted(Path("recursos").glob("*.yml")):
    recursos.append(yaml.safe_load(f.read_text(encoding="utf-8")))

lineas = [
    "# Catálogo", "",
    "| Título | Autor | Idioma | Tipo | Licencia |",
    "|---|---|---|---|---|",
]
for r in recursos:
    lineas.append(
        f"| [{r['titulo']}]({r['enlace']}) | {r['autor']} | "
        f"{r['idioma']} | {r['tipo']} | {r['licencia']} |"
    )

Path("docs/catalogo.md").write_text("\n".join(lineas) + "\n", encoding="utf-8")
print(f"{len(recursos)} recursos procesados")
