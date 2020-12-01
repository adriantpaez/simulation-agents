# Proyecto de Simulacion Agentes

## Generales del estudiante

- **Nombre**: Adrian Tubal Paez Ruiz
- **Grupo**: C-412

## Contenido

- [Proyecto de Simulacion Agentes](#proyecto-de-simulacion-agentes)
  - [Generales del estudiante](#generales-del-estudiante)
  - [Contenido](#contenido)
  - [El ambiente](#el-ambiente)
  - [Agentes](#agentes)
  - [Agente 1 - Limpiar primero](#agente-1---limpiar-primero)
  - [Agente 2 - Random](#agente-2---random)
  - [Agente 3 - Niño primero](#agente-3---niño-primero)
  - [Observaciones generales](#observaciones-generales)

## El ambiente

El ambiente de la simulación cumple las siguientes carcterísticas:

- Accesible
- Determinista
- Episódico
- Dinámico
- Discreto

## Agentes

> **Nota:** todas las simulaciones se realizaron con 10 niños y *t = 5*.

## Agente 1 - Limpiar primero

***Cracteristicas***

Es una agente inteligente, puesto que cumple con lo siguientes objetivos fundamentales:

- Reactivo: ya que percibe el ambiente y responde de forma oportuna.
- Pro-activo: su comportamiento está orientado unicamente al cumplimiento de su objetivo.

***Comportamiento esperado***

Tiene com objetivo final mantener la limpieza de la casa (ambiente), por debajo del 60%. Para alcanzar el objetivo principal, se  basa en limpiar siempre la suciedad más cercanas, si durante el recorrido a una suciedad alcanza a un niño, entonces lo lleva al corral; eliminando de esta forma la fuente principal de suciedad.

***Resultados***

| #   | Promedio Limpio | Veces Despedido | Veces Limpio | X   | Y   | Suciedad Inicial | Obstaculos |
| --- | --------------- | --------------- | ------------ | --- | --- | ---------------- | ---------- |
| 1   | 20.650000       | 0               | 0            | 20  | 20  | 29               | 11         |
| 2   | 15.470000       | 0               | 0            | 20  | 20  | 12               | 26         |
| 3   | 12.220000       | 0               | 0            | 20  | 20  | 10               | 17         |
| 4   | 3.970000        | 0               | 14           | 10  | 10  | 39               | 10         |
| 5   | 6.000000        | 0               | 12           | 10  | 10  | 30               | 16         |
| 6   | 15.350000       | 0               | 0            | 30  | 30  | 11               | 22         |
| 7   | 20.400000       | 0               | 0            | 30  | 30  | 23               | 21         |
| 8   | 25.520000       | 0               | 0            | 30  | 30  | 33               | 25         |
| 9   | 16.440000       | 0               | 0            | 40  | 40  | 16               | 24         |
| 10  | 19.390000       | 0               | 0            | 40  | 40  | 21               | 29         |

Observaciones:

- El agente nunca fue despedido.
- Logró limpiar el ambiente completamente en 36 ocaciones.
- En la mayoría de los casos deja el ambiente más limpio de como inició.

## Agente 2 - Random

***Caracteristicas***

No es un agente inteligente, no posee objetivos, sus son aleatorios.

***Comportamiento esperado***

Realiza todos sus movimientos de forma aleatoria, si se mueve hacia una suciedad la limpia, si se mueve hacia un niño lo carga; si se muve hacia un corral y tiene a un niño cargado, lo pone en el corral.

***Resultados***

| #   | Promedio Limpio | Veces Despedido | Veces Limpio | X   | Y   | Suciedad Inicial | Obstaculos |
| --- | --------------- | --------------- | ------------ | --- | --- | ---------------- | ---------- |
| 1   | 36.100000       | 0               | 0            | 20  | 20  | 12               | 19         |
| 2   | 35.340000       | 0               | 0            | 20  | 20  | 15               | 29         |
| 3   | 38.280000       | 0               | 0            | 20  | 20  | 22               | 28         |
| 4   | 52.770000       | 0               | 0            | 10  | 10  | 35               | 13         |
| 5   | 55.000000       | 1               | 0            | 10  | 10  | 40               | 10         |
| 6   | 31.620000       | 0               | 0            | 30  | 30  | 21               | 16         |
| 7   | 28.450000       | 0               | 0            | 30  | 30  | 16               | 12         |
| 8   | 44.790000       | 0               | 0            | 30  | 30  | 39               | 18         |
| 9   | 26.230000       | 0               | 0            | 40  | 40  | 19               | 15         |
| 10  | 20.040000       | 0               | 0            | 40  | 40  | 10               | 20         |

Observaciones:

- Nunca logró limpiar completamente el ambiente.
- Fue despedido 1 vez.
- La mayoría de las ocaciones deja el ambiente con más suciedad que la inicial.

## Agente 3 - Niño primero

***Caracteristicas***

Es una agente inteligente, puesto que cumple con lo siguientes objetivos fundamentales:

- Reactivo: ya que percibe el ambiente y responde de forma oportuna.
- Pro-activo: su comportamiento esta orientado unicamente al cumplimiento de su objetivo.

***Comportamiento esperado***

Para alcanzar el objetivo final de mantener el ambiente limpio, prioriza poner a los niños en el corral, deido a que son la fuente de suciedad. El funcionamiento se basa en buscar el niño más cercano y ponerlo en el corral, si durante el recorrido el agente pasa por una suciedad, la limpia. Una vez que todos los niños sean puestos en el corral, el agente comienza a limpiar las suciedades restantes.

***Resultados***

| #   | Promedio Limpio | Veces Despedido | Veces Limpio | X   | Y   | Suciedad Inicial | Obstaculos |
| --- | --------------- | --------------- | ------------ | --- | --- | ---------------- | ---------- |
| 1   | 6.920000        | 0               | 1            | 20  | 20  | 15               | 18         |
| 2   | 27.270000       | 0               | 0            | 20  | 20  | 40               | 25         |
| 3   | 6.490000        | 0               | 1            | 20  | 20  | 14               | 12         |
| 4   | 21.530000       | 0               | 2            | 10  | 10  | 25               | 27         |
| 5   | 3.270000        | 0               | 22           | 10  | 10  | 32               | 14         |
| 6   | 19.110000       | 0               | 0            | 30  | 30  | 19               | 29         |
| 7   | 15.340000       | 0               | 0            | 30  | 30  | 11               | 26         |
| 8   | 18.340000       | 0               | 0            | 30  | 30  | 17               | 23         |
| 9   | 13.400000       | 0               | 0            | 40  | 40  | 10               | 13         |
| 10  | 34.290000       | 0               | 0            | 40  | 40  | 38               | 19         |

Observaciones:

- El agente nunca fue despedido.
- Logró limpiar completamente el ambiente en 25 ocaciones.
- En la mayoría de las ocaciones deja el ambiente con menos suciedad que la inicial.

## Observaciones generales

Se puede llegar a la conclusión de que los agentes 1 y 3 son superiores al 2 en la busqueda del objetivo principal, mantener el ambiente limpio.
