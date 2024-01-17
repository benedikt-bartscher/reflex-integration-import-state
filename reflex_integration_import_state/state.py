import reflex as rx


class ReuseableAppState(rx.State):
    @rx.var
    def testvar(self) -> int:
        return 0
