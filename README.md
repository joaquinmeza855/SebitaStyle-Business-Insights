#  Análisis de Datos: SebitaStyle Hair Salon

Este proyecto presenta un análisis detallado de las operaciones de la peluquería SebitaStyle durante un período de 39 semanas (9 meses y 3 semanas). A través del procesamiento de datos, se identificaron patrones de demanda y oportunidades de optimización para mejorar la rentabilidad del negocio.

##  Hallazgos Clave
El análisis revela un negocio sólido con picos de demanda muy marcados:

* **Volumen Total:** 1,114 cortes registrados durante el periodo analizado.
* **Recaudación Total:** Una facturación acumulada de $8,912,000.
* **Días de Alto Rendimiento:** El viernes y sábado generan el 46.2% de la recaudación total.
* **Pico de Demanda Absoluto:** La franja horaria de las 18:00 es el momento de mayor intensidad operativa.
* **Oportunidad Crítica:** El lunes es el día de menor rendimiento, operando a menos de la mitad de la capacidad de un sábado.
  
 <img width="1015" height="583" alt="Frecuencia de cortes por franja horaria" src="https://github.com/user-attachments/assets/726c0fbb-edbc-41af-837d-62c0997ef5be" />


 <img width="918" height="534" alt="Grafico de Recaudacion sumando los dias" src="https://github.com/user-attachments/assets/bb6339d7-1983-4370-a837-8107f430fb31" />

 
 <img width="977" height="688" alt="Grafico mapa de calor por dia y hora" src="https://github.com/user-attachments/assets/41113b6f-7fc6-4165-b27e-aaf9eea3938e" />

 




##  Propuestas Estratégicas
Como resultado del análisis, se proponen las siguientes acciones:
1. **Optimización de Personal:** Reforzar la dotación en el bloque de 17:00 a 18:30, que es el periodo más intenso de la semana.
2. **Incentivos para el Lunes:** Implementar estrategias de descuentos o promociones para distribuir mejor la carga laboral, dado que el lunes promedia solo 2.62 cortes.
3. **Foco Matutino:** Prestar atención a la franja del sábado entre las 11:00 y 12:30, identificado como un pico matutino relevante.

##  Tecnologías y Librerías
* **Lenguaje:** Python
* **Librerías:** Pandas para manipulación de datos, Matplotlib y Seaborn para visualizaciones y matrices de calor.

##  Estructura del Repositorio
* `/data`: Datasets anonimizados.
* `/notebooks`: Procesamiento paso a paso y análisis visual.
* `requirements.txt`: Librerías necesarias para ejecutar el proyecto.

---
**Nota:** Los datos de este análisis cubren 9 meses completos y una fracción del mes 10.
