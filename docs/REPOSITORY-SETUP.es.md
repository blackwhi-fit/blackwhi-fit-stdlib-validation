# Inicialización de Git y futura publicación

El instalador puede inicializar este proyecto como Git independiente en la ruta aprobada. `blackwhi-fit-stdlib` permanece como un directorio ordinario. El autor del commit automático será **BlackWhi Engineering <support@blackwhi.com>**, no se suplantará a Mauricio Chara Hurtado.

**GitHub:** no se debe publicar hasta confirmar titularidad, cuenta autorizada y licencia de código. Cuando se aprueben:

```bash
cd ~/Documentos/ingenieria/proyectos/blackwhi/blackwhi-fit-stdlib/blackwhi-fit-stdlib-validation
gh auth status
gh repo create <propietario>/blackwhi-fit-stdlib-validation --private --source=. --remote=origin --push
```

Sustituye `<propietario>` por la organización/cuenta autorizada. Para visibilidad pública, confirma primero licencia y condiciones de marca. GitHub Releases deben adjuntar únicamente artefactos generados y verificados por el empaquetador real.
