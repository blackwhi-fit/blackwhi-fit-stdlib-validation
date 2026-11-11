# Inicialización de Git y futura publicación

El instalador puede inicializar este proyecto como Git independiente en la ruta aprobada. `blackwhi-fit-stdlib` permanece como un directorio ordinario. El autor del commit automático será **BlackWhi Engineering <support@blackwhi.com>**, no se suplantará a Mauricio Chara Hurtado.

**GitHub (estado al 2026-11-11):** la licencia Apache-2.0 fue aprobada para el código original y la rama `main` fue publicada en `blackwhi-fit/blackwhi-fit-stdlib-validation`. El comando siguiente se conserva únicamente como referencia histórica de inicialización; **no se debe volver a ejecutar en este repositorio**:

```bash
cd ~/Documentos/ingenieria/proyectos/blackwhi/blackwhi-fit-stdlib/blackwhi-fit-stdlib-validation
gh auth status
gh repo create <propietario>/blackwhi-fit-stdlib-validation --private --source=. --remote=origin --push
```

La cuenta oficial es `blackwhi-fit` y el remoto ya está configurado. Para futuros cambios usar `git status`, revisar el diff, crear un commit explícito y `git push` con autorización. Antes de adjuntar artefactos a GitHub Releases, comprobar el empaquetado real, las licencias incluidas, la integridad, las condiciones de marca y los controles de publicación.
