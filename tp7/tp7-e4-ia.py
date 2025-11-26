import numpy as np
import matplotlib.pyplot as plt

def feigenbaum_diagram(r_min=2.4, r_max=4.0, num_r=2000, iterations=1000, last_points=100):
    """
    Genera el diagrama de bifurcación de Feigenbaum.
    
    Args:
        r_min: Valor mínimo del parámetro r
        r_max: Valor máximo del parámetro r
        num_r: Número de valores de r a evaluar
        iterations: Número de iteraciones para cada r
        last_points: Número de últimos puntos a graficar (después del transitorio)
    """
    
    # Array de parámetros r
    r_values = np.linspace(r_min, r_max, num_r)
    
    # Listas para almacenar los datos
    r_plot = []
    x_plot = []
    
    # Condición inicial
    x0 = 0.1
    
    for r in r_values:
        x = x0
        
        # Descartar transitorio
        for i in range(iterations - last_points):
            x = r * x * (1 - x)  # Función logística
        
        # Recolectar puntos en el atractor
        for i in range(last_points):
            x = r * x * (1 - x)
            r_plot.append(r)
            x_plot.append(x)
    
    return r_plot, x_plot

# Generar datos
print("Generando diagrama de bifurcación...")
r_data, x_data = feigenbaum_diagram()

# Crear gráfico
plt.figure(figsize=(14, 8))
plt.plot(r_data, x_data, ',k', markersize=0.5, alpha=0.5)
plt.xlabel('Parámetro r (tasa de crecimiento)', fontsize=12)
plt.ylabel('Población (x)', fontsize=12)
plt.title('Diagrama de Bifurcación de Feigenbaum\nFunción Logística: x(n+1) = r·x(n)·(1-x(n))', fontsize=14)
plt.xlim(2.4, 4.0)
plt.ylim(0, 1)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

print("¡Diagrama completado!")