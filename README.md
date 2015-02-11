# FSFW-Dresden

Pelican baut aus den Markdown-Dateien im 'content'-Ordner statische
HTML-Seiten. Dazu braucht es noch ein Theme, das mit `pelican-themes`
installiert werden kann.

## Installation & Verwendung
Installieren lässt sich Pelican am einfachsten mit pip: `pip install pelican`
(bestenfalls in einem virtualenv). Ist die bin dann im PATH, kann man mit
`pelican-quickstart` das Projekt initialisieren und folgend mit dem erstellten
Makefile mit `make xx` weiterarbeiten.

Das Makefile in diesem Repository ist stark gekürzt, da wir außer dem
HTML-Output erstmal keine Funktionen verwenden.

Als Beispiel liegt in diesem Repo ein Protokoll als Eintrag und der About-Text als
Seite vor. 

## Theme
Das aktuelle Theme ist nur ein Test zu Demonstrationszwecken. Weitere sind z.B.
auf http://www.pelicanthemes.com zu finden. Ggf. lassen sich die Themes auch
weiter anpassen, es handelt sich lediglich um HTML mit Jinja2-Tags.

## Weiterführende Links
* Doku: http://docs.getpelican.com/en/3.5.0/
* Themes: http://www.pelicanthemes.com/
* Markdown: https://daringfireball.net/projects/markdown/ ,
  https://help.github.com/articles/markdown-basics/ ,
  https://pythonhosted.org//Markdown/extensions/index.html
