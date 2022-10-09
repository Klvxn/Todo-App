from django.http import HttpResponse


class HtmxRedirect(HttpResponse):

    def __init__(self, redirect_to: str, status_code: int=200) -> None:
        super().__init__()
        self["HX-Location"] = redirect_to
        self.status_code = status_code
