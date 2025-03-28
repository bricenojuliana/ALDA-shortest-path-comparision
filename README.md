
# Shortest Path Algorithms Comparison

Este proyecto compara el rendimiento de tres algoritmos clásicos para encontrar caminos más cortos en grafos:

- **Dijkstra** (para pesos no negativos)
- **Bellman-Ford** (permite pesos negativos)
- **A*** (búsqueda heurística)

## Estructura del Proyecto

```
/
├── algorithms/       # Implementaciones de los algoritmos
├── benchmark/       # Pruebas de rendimiento
├── tests/           # Pruebas unitarias
├── config/          # Configuraciones
├── executor.py      # Script principal
└── README.md
```

##  Requisitos

- Python 3.8+
- Librerías: `pip install -r requirements.txt`

##  Cómo Usar

1. Ejecutar pruebas unitarias:
   ```bash
   pytest tests/
   ```

2. Correr el benchmark:
   ```bash
   python executor.py
   ```

3. Ver resultados en:
   ```
   /benchmark/results/performance_comparison.png
   ```

## Resultados Esperados

El benchmark generará gráficas comparando:
- Tiempo de ejecución vs tamaño del grafo
- Comportamiento de cada algoritmo
- Análisis de complejidad

## Notas

- Los algoritmos están optimizados para claridad, no para máximo rendimiento
- Configura los parámetros en `config/settings.py`

