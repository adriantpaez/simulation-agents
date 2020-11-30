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

## El ambiente

El ambiente de la simulación cumple las siguientes carcterísticas:

- Accesible
- Determinista
- Episódico
- Dinámico
- Discreto

## Agentes

## Agente 1 - Limpiar primero

El primer agente siempre busca la suciedad más cercana para limpiarla, si se encuentra un niño durante el recorrido, entonces lo carga y continua hacia la suciedad. Si al llegar a la suciedad y limpiarla, el robot tiene cargado a un niño entonces inmediatamente se dirige a ponerlo en un corral para contiuar limpiando.

## Agente 2 - Random

El segundo agente realiza todos sus movimientos de forma aleatoria, si se mueve hacia una suciedad la limpia, si se mueve hacia un niño lo carga; si se muve hacia un corral y tiene a un niño cargado, lo pone en el corral.

## Agente 3 - Niño primero

El tercer agente prioriza poner a los niño en el corral, deido a que son la fuente de suciedad. El funcionamiento se basa en buscar el niño más cercano y ponerlo en el corral, si durante el recorrido el agente pasa por una suciedad, la limpia.
