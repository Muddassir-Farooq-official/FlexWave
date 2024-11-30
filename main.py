import flet as ft
from Views import *

def route_change(route_event, page):
    route = route_event.route
    print("Route change:", route)
    if route == "/":
        print("Hello")
        Home_call(page)
    
    elif route == "/dashboard":
        pass

    print("Current views:", page.views)
    page.update()


def view_pop(view, page):
    page.views.pop()
    top_view = page.views[-1]
    page.go(top_view.route)


def main(page: ft.Page):
    page.title = "Routes Example"
    page.on_route_change = lambda route: route_change(route, page)
    page.on_view_pop = lambda view: view_pop(view, page)
    page.go(page.route)
    page.theme_mode = 'light'
    page.window_width = 370
    page.auto_scroll = True
    page.window_always_on_top = True


ft.app(target=main)