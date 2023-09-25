import reflex as rx

class KakaosyncbotConfig(rx.Config):
    pass

config = KakaosyncbotConfig(
    app_name="kakaosync_bot",
    db_url="sqlite:///reflex.db",
    env=rx.Env.DEV,
)