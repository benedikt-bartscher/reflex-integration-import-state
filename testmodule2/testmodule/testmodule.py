"""App using a fully controlled input with implicit debounce wrapper."""
import reflex as rx

from reflex_integration_import_state.state import ReuseableAppState


class State2(ReuseableAppState):
    text: str = "initial"


#  class State2(rx.State):
#      text: str = "initial"


app = rx.App(state=rx.State)


@app.add_page
def index():
    return rx.fragment(
        rx.input(
            value=State2.router.session.client_token, is_read_only=True, id="token"
        ),
        rx.input(
            id="debounce_input_input",
            on_change=State2.set_text,  # type: ignore
            value=State2.text,
        ),
        rx.input(value=State2.text, id="value_input", is_read_only=True),
        rx.input(on_change=State2.set_text, id="on_change_input"),  # type: ignore
        rx.el.input(
            value=State2.text,
            id="plain_value_input",
            disabled=True,
            _disabled={"background_color": "#EEE"},
        ),
        rx.button("CLEAR", on_click=rx.set_value("on_change_input", "")),
    )
