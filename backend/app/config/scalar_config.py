from scalar_fastapi import get_scalar_api_reference, Layout  # type: ignore


def setup_scalar(app):
    """
    Configura la documentación Scalar para FastAPI.
    """
    app.mount(
        "/scalar",
        get_scalar_api_reference(
            openapi_url=app.openapi_url,
            title=app.title,
            layout=Layout.MODERN,         # Diseño moderno (default)
            show_sidebar=True,            # Mostrar el sidebar
            hide_download_button=False,   # Permitir descargar el esquema
            hide_models=False,            # Mostrar los modelos
            dark_mode=True,               # Activar modo oscuro
            default_open_all_tags=False,  # No expandir todos los tags por defecto
        )
    )
