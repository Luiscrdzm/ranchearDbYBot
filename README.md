Bot de discord que proyecta una terminal de mysql lleno de datos de stardew valley



La terminal tiene permisos de SELECT en toda la base de datos y puede ejecutar funciones dentro de sus querys, los procedures aun se estan trabajando, lo mas probable es que sean incluidos como slash_commands.

Para ejecutar el proyecto desde tu entorno necesitas un token para el bot de discord que puedes conseguir en https://discord.com/developers/applications y tu id de usuario de discord, este ultimo es opcional y puedes editar el codigo que lo referencia para eliminarlo. Estos dos elementos se planea esten incluidos en las variables de tu entorno con ranchear="Token del bot" y owner_id="Tu id de discord", si prefieres no añadir estos a tus variables del entorno los puedes añadir temporalmente desde la terminal con $Env: en Windows y export en Linux, alternativamente pegalos directamente en el codigo y ahorrate los problemas.

Dentro del codigo se incluyen los comandos para descargar las dependencias, en caso de que no las tengas, y la documentacion de la libreria para que puedas entender modificar y exportar cualquier cosa que aqui encuentres.