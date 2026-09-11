## portfolio-hub-main

**Ruta:** D:\Proyectos\portfolio-hub-main
**Estado:** 🟠 Incompleto (aplicación Flask con debug y secrets hardcodeados)
**Evidencia:** Landing page / portfolio hub con Flask. El archivo app.py crea la app Flask con routes para /, /login, /logout, /familia. Tiene templates (base.html, family.html, etc.) y static/. El README no encontrado en la carpeta (solo index.html, index.html.bak). Local modifications: 2 archivos eliminados (hero-bg.mp4, hero-poster.jpg) y archivos nuevos sin commit (.ai/, env.app.py, app.py, etc.). Secret key hardcodeado: "dev-secret-change-in-production". debug=True en app.run(debug=True, port=5000). Último commit aec840a pusheado al remote.
**Stack:**
- Backend: Python/Flask
- Frontend: HTML/CSS/JS (Bootstrap), templates Jinja2
- Base de datos: SQLite (implícito, no configurada explícitamente en app.py)
- Infraestructura: Ninguna definida (Flask dev server)
**Git:** ✅ On branch main, up to date with 'origin/main', pero modifications locales sin commit
**GitHub:** ✅ origin https://github.com/alvaroberrio23242-eng/portfolio-hub.git
**Último commit:** aec840a fix: actualizar demos SalsaQuest y RockQuest a PythonAnywhere
**¿Pusheado?** ⚠️ Parcial — commit aec840a en origin/main, pero modifications locales sin pushear
**Deploy:** Ninguno — tiene requirements.txt (Flask + gunicorn) pero debug=True y secrets hardcodeados bloquean deploy producción
**Production readiness:** REQUIERE TRABAJO
- Puntos fuertes: Estructura de templates completa, login/out system, Bootstrap integrado
- Problemas: debug=True en app.run; secret key hardcodeado "dev-secret-change-in-production"; modifications locales sin commit/push; .env.example existe pero no configurado correctamente

### Próximo paso único
**Quitar debug=True y secret key hardcodeado de app.py; crear .env.example con valores seguros**