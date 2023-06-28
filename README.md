# Creando API REST con DJango y DJango Rest Framework.

**crea una rest API**

Crea un entorno virtual

```bash
pip install virtualenv
```

ejecutando el entorno virtual

```bash
python -m virtualenv _nombreDeLaCarpeta_
#(usualmente ess venv)
```

**ACTIVACION DEL ENTORNO VIRTUAL**

```bash
.\venv\Scripts\activate
```

O tambien precione F1 y seleccione Python: Select Interpreter

#### Intalacion de Django

pip install django
pip install djangorestframework

#### Inicializando el projecto

django-admin startproject django_crud_api .

#### Migrando

Crea los

_python manage.py makemigrations_
_python manage.py migrate_

#### serialicers

### View set

Quien puede ver esto, o si debemos enviar una serie de autenticacion

## Ruta Backend

**Pruebas** https://server-pyme-desk.onrender.com/api/projects/

# Rutas de Backend

- api/Usuarios
- api/productos
- api/pedidos
- api/resumen

- https://server-pyme-desk.onrender.com/api/usuarios/
- https://server-pyme-desk.onrender.com/api/productos/
- https://server-pyme-desk.onrender.com/api/pedidos/
- https://server-pyme-desk.onrender.com/api/resumen/

## Pedidos

- Peticion POST

```json
{
	"cliente": 1,
	"estado": "pendiente",
	"regla_envio": "domicilio",
	"pagado": false,
	"productos": [
		{
			"producto": 5,
			"cantidad": 2
		},
		{
			"producto": 6,
			"cantidad": 1
		}
	]
}
```

- Peticion GET

```json
[
	{
		"id": 1,
		"productos": [
			{
				"id": 1,
				"cantidad": 2,
				"producto": 5
			},
			{
				"id": 2,
				"cantidad": 1,
				"producto": 6
			}
		],
		"fecha": "2023-06-27T14:00:32.852100Z",
		"estado": "pendiente",
		"pagado": false,
		"regla_envio": "domicilio",
		"observaciones": "",
		"cliente": 1
	},
	{
		"id": 2,
		"productos": [
			{
				"id": 3,
				"cantidad": 3,
				"producto": 6
			},
			{
				"id": 4,
				"cantidad": 1,
				"producto": 7
			}
		],
		"fecha": "2023-06-27T14:01:07.155404Z",
		"estado": "pendiente",
		"pagado": false,
		"regla_envio": "domicilio",
		"observaciones": "",
		"cliente": 1
	},
	{
		"id": 4,
		"productos": [
			{
				"id": 7,
				"cantidad": 2,
				"producto": 5
			},
			{
				"id": 8,
				"cantidad": 1,
				"producto": 6
			}
		],
		"fecha": "2023-06-27T14:10:53.701429Z",
		"estado": "pendiente",
		"pagado": false,
		"regla_envio": "domicilio",
		"observaciones": "",
		"cliente": 1
	}
]
```

### Paginacion

http://example.com/api/pedidos/?page=2

#### cambiar el limite

http://example.com/api/mi_endpoint/?page_size=20
