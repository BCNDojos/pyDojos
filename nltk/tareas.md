## Pasos para hacer Naive Bayes

    1. tokenización
    2. filtrado
    3. normalización
        - stemming/lemmatization
    4. entrenamiento
    5. evaluación

## Tareas

1. [COMPLETADA] Extraer corpus a json.
2. Explicación Naive Bayes, pasos, ejemplo keyword-corpus de Devex.
3. Primer pomodoro: Ejemplo propio con código básico:
    - Código
        - Carga del corpus.
        - Función para tokenizar.
        - Función para preprocesar. (inicialmente, que no haga nada)
        - Clasificador.

    - "Test":
         - Input
            - texto (ya tokenizado?)
            - función para preprocesado:
                - normalización (stemming/lemmatization)
                - filtrado
            - clasificador
         - Proceso: 
            1. training
            2. testing

        - Output: porcentaje de acierto
4. Segundo pomodoro: Añadir variabilidad en las funciones de preprocesado.
    - ¿Qué otros preprocesados se pueden hacer?
        - Tokenizar de forma diferente?
        - Stemming, lemmatization?
        - Diferentes filtrados
5. Tercer pomodoro: Añadir variabilidad en la elección del clasificador.
    - ¿Qué más clasificadores hay (aparte de NB)?
6. Cuarto pomodoro: Obtener el mejor resultado.
