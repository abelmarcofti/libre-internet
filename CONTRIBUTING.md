  [Català](CONTRIBUTING.ca.mc) | [Castellano](CONTRIBUTING.md)

# Contribuir al catálogo
Muchas gracias por tomarte el tiempo de contribuir al proyecto. Añadir un elemento al catálogo te llevará menos de dos minutos y ayudarás a transmitir el libre conocimiento a través de internet.

## Documentos aceptados
- Libros
- Cuentos ilustrados
- Novelas gráficas
- Cursos online gratuitos
- Manuales
- Películas de dominio público (enlace directo)
- Vídeos en plataformas como YouTube que sean de interés académico y tengan una licencia libre (por ejemplo, Creative Commons)
- Cualquier archivo PDF con contenido interesante y que se pueda compartir libremente

Recuerda que la biblioteca es un catálogo de enlaces: no se suben archivos al repositorio.

### Licencias
Todo recurso debe ser de dominio público o tener una licencia libre. Estas son las licencias que acepta el catálogo:

`Public-Domain`, `CC0-1.0`, `CC-BY-4.0`, `CC-BY-SA-4.0`, `MIT`, `Apache-2.0`, `GPL-3.0`, `Dominio Público` y `GFDL-1.3`.

Si el recurso tiene otra licencia libre, o el autor te ha dado un permiso expreso para compartirlo, abre un [issue](https://github.com/abelmarcofti/libre-internet/issues/new/choose) antes de proponerlo y lo valoramos.

## Documentos no aceptados
- Enlaces a sitios que distribuyen contenidos con derechos de autor sin la autorización de sus titulares.
- Recursos sin licencia clara.
- Recursos de pago o que obliguen a pagar para acceder a ellos.
- Enlaces que no lleven directamente al recurso (acortadores, páginas intermedias llenas de publicidad).
- Contenido ilegal u ofensivo.

## Cómo proponer un recurso

### Opción A: con el formulario (sin tocar código)
1. Entra en el [formulario](https://github.com/abelmarcofti/libre-internet/issues/new?template=proponer-recurso.yml). Necesitas una cuenta gratuita de GitHub.
2. Rellena los campos y envíalo.
3. Reviso la propuesta. Si encaja, la apruebo y se genera automáticamente una solicitud de cambio (*pull request*) con tu recurso.
4. Al fusionarla, el recurso aparece en la web en unos minutos.

### Opción B: con un pull request
Si sabes usar Git, también puedes hacerlo directamente:
1. Haz un *fork* del repositorio.
2. Copia `plantilla.yml` dentro de la carpeta `recursos/` con un nombre descriptivo, por ejemplo `recursos/linux-basico.yml`.
3. Rellena los campos (ver más abajo).
4. Comprueba que es válido con `python scripts/validar.py`.
5. Haz commit, súbelo a tu fork y abre un *pull request*.

## Campos del recurso
| Campo | Qué poner |
|---|---|
| `titulo` | Nombre del recurso |
| `autor` | Persona o entidad autora |
| `idioma` | Código del idioma, por ejemplo `ca`, `es` o `en` |
| `tipo` | Una sola palabra, solo letras: `libro`, `manual`, `curso`... |
| `licencia` | Una de las licencias de la lista de arriba |
| `enlace` | Dirección que empiece por `https://` |
| `etiquetas` | Lista entre corchetes y separada por comas |

Ejemplo:
```yaml
titulo: "Linux básico"
autor: "Nombre del autor"
idioma: es
tipo: manual
licencia: CC-BY-SA-4.0
enlace: https://ejemplo.org/linux-basico
etiquetas: [linux, basico]
```
Errores habituales: poner varios corchetes seguidos en las etiquetas (`[a] [b]` en lugar de `[a, b]`), usar `http://` en lugar de `https://` y escribir un tipo con números o símbolos.

## Cómo se revisa
Antes de aceptar un recurso compruebo que el enlace funciona, que la licencia es real y que no está duplicado. Además, un validador automático revisa el formato de cada propuesta: si ves una X roja en tu *pull request*, abre los detalles y te dirá qué campo corregir.

## Otras formas de ayudar
- Avisar de un enlace roto, con la plantilla de [issues](https://github.com/abelmarcofti/libre-internet/issues/new/choose).
- Corregir errores en el catálogo o en la documentación.
- Traducir los textos del proyecto.

## Trato respetuoso
Este es un proyecto comunitario: sé amable con el resto de personas que participan y piensa que casi todo el mundo está aquí para aprender.
