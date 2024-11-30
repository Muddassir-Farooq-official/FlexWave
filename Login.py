import flet as ft
import pymysql
from database import config  # Assuming your database connection details are in 'config'


class LoginPage(ft.UserControl):  # Changed from ft.Container to ft.UserControl for better lifecycle handling
    def __init__(self):
        super().__init__()

        self.username = ft.TextField(
            hint_text="User ID",
        )
        self.password = ft.TextField(
            hint_text="Password",
            password=True,
            can_reveal_password=True
        )
        self.btn = ft.FilledButton(
            text="LogIn",
            style=ft.ButtonStyle(
                bgcolor=ft.colors.BLACK, color='White',
                shape=ft.RoundedRectangleBorder(radius=10),
            ), width=500,
            on_click=self.login
        )

    def build(self):
        return ft.Container(
            content=ft.Column(
                [
                    self.username, self.password,
                    self.btn
                ]
            ),
            width=600,
            padding=20
        )

    def login(self, e):
        # Ensure both username and password are filled
        if self.username.value == "" or self.password.value == "":
            self.show_snack_bar("Kindly fill in the required details")
            print("Something Missing")
            return

        # Connect to the database and validate credentials
        connection = pymysql.connect(**config)
        cursor = connection.cursor()

        try:
            # Fetch user details based on email and password
            cursor.execute("SELECT * FROM employee WHERE email = %s AND password = %s", 
                           (self.username.value, self.password.value))
            data = cursor.fetchone()

            print("Data fetched from DB:", data)  # Debugging line

            if data:
                # Credentials matched
                self.show_snack_bar("Login Successful")
                print("Login Successful")
            else:
                # Credentials did not match
                self.show_snack_bar("Invalid Username or Password")
                print("Login Failed")

        except Exception as ex:
            print("Error:", ex)
            self.show_snack_bar(f"An error occurred: {ex}")

        finally:
            cursor.close()
            connection.close()

    def show_snack_bar(self, message):
        # Create and open a snack bar with the message
        self.page.snack_bar = ft.SnackBar(ft.Text(message), open=True)
        self.page.update()  # Ensure page is updated to reflect the SnackBar
        print(f"SnackBar Message: {message}")  # Debugging line

