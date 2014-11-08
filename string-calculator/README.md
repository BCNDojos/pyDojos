Kata String Calculator
======================

Introducción
------------

Esta kata es una kata de iniciación, en la que se plantea el desarrollo de una calculadora que sumará operandos recibidos en una cadena de carácteres.

**El desarrollo de la kata está contemplado para practicar el desarrollo guiado por tests e incremental, por lo que es conveniento no saltarse ninguna tarea sin antes haberla completado, ni tampoco leer el contenido de las tareas posteriores.**

**No es necesario en ningún caso para esta kata comprovar entradas erróneas.**

Requerimientos
--------------

Para la realización de esta kata sólo es necesario disponer de un python 2.7.x o 3.x sin ningún otro paquete adicional.

Primera fase
------------

El objetivo es conseguir una clase `StringCalculator` que dispondrá de un método `int Add(string)` el cual recibirá una cadena de carácteres con una lista de hasta dos números separados por `,` y devolverá la suma de dichos números. Se debe esperar que la cadena esté vacía, devolviendo la suma 0.

En esta primera fase es recomendable empezar por el test en el que la cadena está vacía, e ir añadiendo los casos en los que hay uno, y luego dos.

Segunda fase
------------

En esta fase, el objetivo es que el método `Add` pueda recibir más de un número.

Tercera fase
------------

La siguiente funcionalidad que se añadirá, consistirá en permitir el salto de línea, `\n`, como separador alternativo. Así, en esta fase:

  * La entrada `"1\n2,3"` se considerará correcto.
  * En cambio, la entrada `"1,\n"` se considerará incorrecta.

Cuarta fase
-----------

En esta fase, añadiremos la posibilidad de determinar el separador en la primera línea de la entrada, indicándolo con `"//"`. Por ejemplo, si queremos que el nuevo separador sea `;`, la entrada sería `"//;\n1;2"`.
