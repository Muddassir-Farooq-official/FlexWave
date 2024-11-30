import flet as ft
from Login import *

login = LoginPage()


def Home_call(page):
    print("Adding home view", flush=True)
    page.views.append(
        ft.View(
            "/",
            [
                login
                                           
            ],
                padding=0,horizontal_alignment='center',
                vertical_alignment="center",
                bgcolor=ft.colors.YELLOW_100


        )
    )
    page.update()
    return page.views

def Dashboard_call(page):
    print("Adding home view", flush=True)
    page.views.append(
        ft.View(
            "/dashboard",
            [
                    ft.AppBar(
                        leading=ft.IconButton(icon=ft.icons.ARROW_BACK,icon_color='white',on_click= lambda _: page.go("/")),
                        title=ft.Text("Quiclkli Merchant",size=16,color='white'), bgcolor='red'),
                        ft.Row(
                        [
                            ft.Container(content=ft.Row(
                                [
                                    ft.Text("Dashboard",color='white',size=20),ft.IconButton(icon=ft.icons.MENU,icon_color='white'),
                                ],alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                                ),
                                bgcolor='red',expand=True,padding=10 
                            ),
                        ]
                    ),
                                           
            ],
                padding=0,horizontal_alignment='center',
                scroll=True,
                #bgcolor='white'

        )
    )
    page.update()
    return page.views