  [Català](CONTRIBUTING.ca.mc) | [Castellano](CONTRIBUTING.md)

# Contribuir al catàleg
Moltes gràcies per prendre't el temps de contribuir al projecte. Afegir un element al catàleg et portarà menys de dos minuts i ajudaràs a transmetre el lliure coneixement a través d'internet.

## Documents acceptats
- Llibres
- Contes ilustrats
- Noveles gràfiques
- Cursos online gratuits
- Manuals
- Pel·lícules de domini públic (enllaç directe)
- Vídeos a plataformes com Youtube que siguin d'interés acadèmic i tinguin una llicència lliure (com Creative Commons)
- Qualsevol arxiu PDF amb contingut interessant i que es pugui compartir lliurement

Recorda que la biblioteca és un catàleg d'enllaços: no es pujen arxius al repositori

### Llicències
Tots els recursos han de ser de domini públic o tenir una llicència lliure. Aquestes són les llicències que accepta el catàleg:

`Public-Domain`, `CC0-1.0`, `CC-BY-4.0`, `CC-BY-SA-4.0`, `MIT`, `Apache-2.0`, `GPL-3.0`, `Dominio Público` i `GFDL-1.3`.

Si el recurs té una altra llicència lliure, o l'autor t'ha donat un permís per a compartir-lo, obre un [issue](https://github.com/abelmarcofti/libre-internet/issues/new/choose) abans de proposar-lo i ho valorem.

## Documents no acceptats
- Enllaços a llocs que distribueixin continguts amb drets d'autor sense l'autorització dels seus titulars.
- Recursos sense llicència clara.
- Recursos que obliguin a pagar per accedir.
- Enllaços que no portin directament al recurs (pàgines intermèdies amb publicitat).
- Contingut ilegal o ofensiu.

## Com proposar un recurs

### Opció A: amb el formulari (sense tocar codi)
1. Entra al [formulari](https://github.com/abelmarcofti/libre-internet/issues/new?template=proponer-recurso.yml). Necessites un compte gratüit de GitHub.
2. Omple els camps i envia'l.
3. Reviso la proposta. Si encaixa, l'aprovo i es genera automàticament una solicitud de canvi amb el teu recurs.
4. Al fusionar-la, el recurs apareix al lloc web en uns minuts.

### Opció B: amb un pull request
Si saps utilitzar Git, també pots fer-ho directament:
1. Fes un *fork* del repositori.
2. Copia `plantilla.yml` dins de la carpeta `recursos/` amb un nom descriptiu, per exemple `recursos/linux-basico.yml`.
3. Omple els camps (veure a sota).
4. Comprova que es vàlid amb `python scripts/validar.py`.
5. Fes commit, puja-ho al teu fork i obre un *pull request*.

## Camps del recurs
| Camp | Que posar |
|---|---|
| `titulo` | Nom del recurs |
| `autor` | Persona o entitat autora |
| `idioma` | Codi de la llengua, per exemple `ca`, `es` o `en` |
| `tipo` | Una paraula, només lletres: `libro`, `manual`, `curso`... |
| `licencia` | Una de les llicències de la llista |
| `enlace` | Direcció que comenci per `https://` |
| `etiquetas` | Separades per comes |

Exemple:
```yaml
titulo: "Linux básico"
autor: "Nombre del autor"
idioma: es
tipo: manual
licencia: CC-BY-SA-4.0
enlace: https://ejemplo.org/linux-basico
etiquetas: [linux, basico]
```
Errades habituals: posar claudàtors seguits a les etiquetes (`[a] [b]` en llco de `[a, b]`), utilitzar `http://` en lloc de `https://` i escriure un tipus amb nombres o símbols.

## Com es revisa
Abans d'acceptar un recurs comprovo que l'enllaç funcioni, que la llicència es real i que no està duplicat. A més a més, un validador automàtic revisa el format de cada proposta: si veus una X roja al teu *pull request*, obre els detalls i et dirà quin camp corregir.

## Altres formes d'ajudar
- Avisar d'un enllaç trencat, amb la plantilla de [issues](https://github.com/abelmarcofti/libre-internet/issues/new/choose).
- Corregir errades al catàleg o a la documentació.
- Traduir els textos del projecte.

## Tracte respetuós
Aquest és un projecte comunitari: sigues amable amb la resta de persones que participin i pensa que quasi tothom està aqui per aprendre.

