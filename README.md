TruequeApp es un marketplace sencillo de productos usados construido con Django. 

Al iniciar sesión, el usuario entra a “Mis productos”, donde se listan únicamente las publicaciones del usuario autenticado. Si ese usuario pertenece al rol de vendedor, verá el botón para crear un nuevo producto; además, en cada fila aparecerán los botones para editar y borrar únicamente cuando el producto le pertenece. Los compradores, por el contrario, solo pueden navegar y ver detalles. En la página de detalle se muestra la información del producto y, si quien está mirando no es el vendedor, aparece un formulario para contactar al vendedor. Los mensajes enviados quedan guardados en la base de datos y el vendedor los ve resumidos al final de su página de “Mis productos”, de forma que puede revisar todas las consultas que le hacen sobre sus publicaciones sin salir del flujo principal.

Configuración de permisos:
El grupo vendedor posee los permisos de agregar, cambiar, eliminar y ver sobre el modelo Producto, mientras que el comprador únicamente tiene permiso de ver. En las plantillas se usa el objeto perms de Django para decidir qué botones mostrar y, además, se valida la propiedad del recurso antes de permitir ediciones o eliminaciones. De esta manera, la interfaz guía al usuario y la capa de vistas asegura que no se puedan forzar acciones desde la URL.

La instalación del proyecto se hace de forma habitual: crear y activar un entorno virtual, instalar dependencias con pip install -r requirements.txt, ejecutar migraciones y levantar el servidor. El repositorio incluye scripts de carga para crear grupos, usuarios de prueba y un conjunto de productos iniciales; tras ejecutar esas semillas se puede navegar con credenciales de vendedor y de comprador para observar el comportamiento de cada rol. Si se desea acceso al panel de administración, basta con crear un superusuario; en el navbar aparecerá un enlace “Administrar” solo para usuarios con permisos de staff o superusuario.

En cuanto al modelo de datos, Producto contiene título, descripción, precio, estado y un ForeignKey al usuario vendedor. Para el contacto se define un modelo Mensaje que relaciona producto, remitente y el contenido del mensaje, con marca de tiempo automática. El flujo está pensado para ser didáctico: el vendedor publica, el comprador consulta y contacta, y el vendedor recibe el mensaje en su propia vista. 



