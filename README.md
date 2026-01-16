# 🎵 RetroVibes - E-commerce de Vinilos

[![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)

> Plataforma e-commerce completa para la compra y venta de vinilos vintage y modernos. Proyecto universitario desarrollado con Django y metodologías ágiles.
## Video Demo

<div align="center">
  
  [![Video Demo RetroVibes](https://img.shields.io/badge/▶️_Ver_Video_Demo-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://youtu.be/uS4ljAZ9Rtk)
  
  *Haz clic en el botón para ver la demostración completa del proyecto*

</div>

## Descripción

RetroVibes es una aplicación web de comercio electrónico desarrollada en Django que permite a los usuarios explorar, buscar y comprar vinilos de música. La plataforma cuenta con un catálogo completo de productos, sistema de carrito de compras, gestión de perfiles de usuario y proceso de checkout integrado.

## Características

### Funcionalidades E-commerce
- **Catálogo de Productos**: Exploración completa de vinilos vintage y modernos
- **Búsqueda y Filtros**: Sistema de búsqueda avanzada y filtrado por categorías
- **Carrito de Compras**: Gestión de productos seleccionados con actualización en tiempo real
- **Proceso de Checkout**: Flujo completo de compra con validación de datos
- **Gestión de Inventario**: Control de stock y disponibilidad de productos

### Gestión de Usuarios
- **Autenticación**: Sistema de registro e inicio de sesión
- **Perfil de Usuario**: Gestión de información personal y preferencias
- **Historial de Compras**: Seguimiento de pedidos realizados
- **Lista de Deseos**: Guardado de productos favoritos

### Interfaz de Usuario
- **Diseño Responsivo**: Adaptado para dispositivos móviles, tablets y escritorio
- **Estética Retro**: Diseño visual inspirado en la época dorada del vinilo
- **Navegación Intuitiva**: UX/UI optimizada para facilitar la experiencia de compra
- **Imágenes de Alta Calidad**: Galería visual de productos con detalles

## Tecnologías Utilizadas

### Backend
- **Django**: Framework web principal de Python
- **SQLite**: Base de datos para desarrollo
- **Python**: Lógica del servidor y modelos de datos

### Frontend
- **JavaScript**: Interactividad y funcionalidades dinámicas
- **CSS3**: Estilos y diseño visual
- **HTML5**: Estructura de las páginas
- **Bootstrap**: Framework CSS para diseño responsivo

### Herramientas de Desarrollo
- **Git**: Control de versiones
- **Metodologías Ágiles**: Scrum y Kanban para gestión del proyecto

## Estructura del Proyecto

```
TEIS-RetroVibes/
├── RetroVibes/              # Configuración principal de Django
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── pages/                   # Aplicación principal de páginas
│   ├── models.py           # Modelos de datos
│   ├── views.py            # Vistas y lógica
│   ├── urls.py             # Rutas de la aplicación
│   └── templates/          # Plantillas HTML
├── staticfiles/            # Archivos estáticos (CSS, JS, imágenes)
│   ├── admin/
│   └── pages/
├── db.sqlite3              # Base de datos SQLite
├── db_backup.sqlite3       # Respaldo de base de datos
├── manage.py               # Script de gestión de Django
└── README.md
```

## 🚀 Instalación y Configuración

### Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Git

### Instalación

1. **Clonar el repositorio**
```bash
git clone https://github.com/aristcub/TEIS-RetroVibes.git
cd TEIS-RetroVibes
```

2. **Crear y activar entorno virtual**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Instalar dependencias**
```bash
pip install django
pip install pillow  # Para manejo de imágenes
# Instalar otras dependencias según requirements.txt si existe
```

4. **Configurar la base de datos**
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Crear superusuario (administrador)**
```bash
python manage.py createsuperuser
```

6. **Recolectar archivos estáticos**
```bash
python manage.py collectstatic
```

7. **Ejecutar el servidor de desarrollo**
```bash
python manage.py runserver
```

8. **Acceder a la aplicación**
- Aplicación web: `http://localhost:8000`
- Panel de administración: `http://localhost:8000/admin`

## Uso de la Aplicación

### Para Usuarios
1. **Registro**: Crea una cuenta nueva con tus datos
2. **Explorar**: Navega por el catálogo de vinilos
3. **Buscar**: Utiliza los filtros para encontrar tu música favorita
4. **Comprar**: Agrega productos al carrito y completa el checkout
5. **Perfil**: Gestiona tus datos y revisa tu historial de compras

### Para Administradores
1. Accede al panel de administración en `/admin`
2. Gestiona productos, categorías y usuarios
3. Revisa y procesa pedidos
4. Actualiza el inventario
5. Genera reportes de ventas

## Funcionalidades Destacadas

### Catálogo de Productos
```python
# Modelo de Producto (ejemplo simplificado)
class Vinyl(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    image = models.ImageField(upload_to='vinyls/')
    description = models.TextField()
    release_year = models.IntegerField()
    condition = models.CharField(max_length=50)
```

### Sistema de Carrito
- Agregar/eliminar productos
- Actualizar cantidades
- Cálculo automático de totales
- Persistencia de datos

### Checkout
- Validación de formularios
- Cálculo de envío
- Confirmación de pedido
- Notificaciones por email

## Equipo de Desarrollo

Proyecto desarrollado por estudiantes de Ingeniería de Sistemas de la Universidad EAFIT aplicando metodologías ágiles y trabajo en equipo.

### Roles del Proyecto
- **Desarrolladora Frontend**: Manuela Caro Villada
  - Implementación de toda la interfaz de usuario
  - Desarrollo con HTML, CSS, Python y Bootstrap
  - Diseño de experiencia de usuario
- **Desarrolladores Backend**: Katherin Natalia Allín y Dixon Calderón 
  - Arquitectura de base de datos
  - Lógica de negocio
  - APIs y servicios

## Metodología de Desarrollo

El proyecto fue desarrollado siguiendo principios ágiles:

- **Sprints de 2 semanas**: Entregas incrementales de funcionalidad
- **Reuniones Diarias**: Sincronización del equipo
- **Revisiones de Sprint**: Validación de avances
- **Retrospectivas**: Mejora continua del proceso

## Solución de Problemas

### Error: Port already in use
```bash
# Usar un puerto diferente
python manage.py runserver 8080
```

### Error: No module named 'django'
```bash
# Asegurarse de que el entorno virtual esté activado
# Reinstalar Django
pip install django
```

### Error en migraciones
```bash
# Resetear migraciones (solo en desarrollo)
python manage.py migrate --run-syncdb
```

## Roadmap y Mejoras Futuras

- [ ] Implementar pasarela de pagos real (PayPal, Stripe)
- [ ] Sistema de reseñas y calificaciones de productos
- [ ] Recomendaciones personalizadas con ML
- [ ] Chat en vivo para atención al cliente
- [ ] Aplicación móvil nativa
- [ ] Integración con redes sociales
- [ ] Sistema de cupones y descuentos
- [ ] Programa de fidelización de clientes

## Licencia

Este es un proyecto académico desarrollado con fines educativos en la Universidad EAFIT.

## Contribuciones

Este proyecto fue desarrollado como parte de un curso universitario. Para consultas o sugerencias, contacta al equipo de desarrollo.


