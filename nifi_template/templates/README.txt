Adjunto la template de nifi inicial y no la final porque tengo problemas con las descargas en el navegador, para transformarla en la final:

1. Borrar abajo a la izquierda el procesador: PUTFILE MONGO FOLDER
2. Conectar una salida del primer funnel (el inmediato el que conecta los 2 GetFiles: Democrata y Republicano) con el procesador PUTMONGO
3. Si hay warnings: entrar en los procesadores y únicamente activar los CONTROLLER SERVICES

Siento no poder proporcionar la final :((
pero estos pasos deberían de ser sencillos y ahorrar bastante tiempo
