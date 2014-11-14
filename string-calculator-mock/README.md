Kata String Calculator
======================

Introducción
------------

En esta kata, partiremos de otra kata ya resuelta sobre la que desarrollaremos algunas funcionalidades nuevas que nos obligarán a utilizar *mocking* para que los tests puedan comprobarlo.

Dado que *mocking* es un concepto un poco confuso, la kata consistirá de tres fases. En la primera se hará un ejemplo del uso de `mock` para crear un falso recurso a utilizar.

Requerimientos
--------------

En este caso, para la realización de la kata, será necesario disponer de la librería `mock` instalada. Para instalaros la librería, debería bastar en ejecutar el siguiente comando, estando conectados a Internet: ::

    pip install mock

Primera fase
------------

El objetivo de esta primera fase es crear un nuevo programa que, utilizando la clase StringCalculator, permitirá al usuario invocarlo con los dígitos desde la línea de comandos.

Segunda fase
------------

En la segunda fase, el programa responderá al usuario imprimiendo la suma, el resultado, por la pantalla.

Tercera fase
------------

Una vez impreso el resultado, el programa imprimirá la pregunta `Otra entrada, por favor` y esperará otra lista de usuarios que el usuario deberá entrar. Si el usuario pulsa Enter sin ninguna entrada, el programa saldrá.
