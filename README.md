=======
pyDojos
=======

Éstos son los dojos realizados con la comunidad [pybcn] en Barcelona. Cada dojo realizado se almacena separadamente en su directorio.

Participantes
=============

Cada uno de los grupos participantes bifurcará éste repositorio, clonará su versión, y creará una rama para su código:

    git clone git@github.com:<usuario>/pyDojos
    git checkout -b <dojo>-<grupo>

Durante la sesión, irán cumplimentando los cambios, a medida que consigan los puntos marcados en la kata, si los hubiera, o cuando más les interese:

    git commit -am "<comentario>"

Antes de cada retrospectiva, el grupo subirá sus cambios a su repositorio y solicitará la fusión con su propia rama.

    git push <usuario> <dojo>-<grupo>


Facilitador
===========

Para crear un nuevo dojo, sólo hay que copiar el directorio `base` con el nombre del dojo correspondiente, y actualizar el README.md correspondiente. Por ejemplo, para la sesión del 4 de octubre de 2014:

    cp -r base 20141004

y luego editar el fichero `20141004/README.md` con el enunciado correspondiente a la cata elegida.
Una vez formados los grupos y repasada la kata, poniendo en común los detalles, el facilitador creará una rama por cada grupo.

[pybcn]: http://pybcn.org
