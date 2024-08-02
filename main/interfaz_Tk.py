import tkinter as tk
from tkinter import messagebox
from clases.usuarios import Usuarios


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Gestión de Usuarios")
        self.geometry("300x200")
        self.init_ui()

    def init_ui(self):
        self.frames = {}

        for F in (StartPage, LoginPage, RegisterPage, UserManagementPage):
            page_name = F.__name__
            frame = F(parent=self, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        tk.Label(self, text="Bienvenido al sistema", font=("Arial", 16)).pack(pady=10)
        tk.Button(self, text="Iniciar sesión", command=lambda: controller.show_frame("LoginPage")).pack(pady=5)
        tk.Button(self, text="Registrarse", command=lambda: controller.show_frame("RegisterPage")).pack(pady=5)


class RegisterPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        tk.Label(self, text="Registro de Usuario", font=("Arial", 16)).pack(pady=10)

        tk.Label(self, text="Nombre:").pack()
        self.name_entry = tk.Entry(self)
        self.name_entry.pack()

        tk.Label(self, text="Apellido:").pack()
        self.last_name_entry = tk.Entry(self)
        self.last_name_entry.pack()

        tk.Label(self, text="Email:").pack()
        self.email_entry = tk.Entry(self)
        self.email_entry.pack()

        tk.Label(self, text="Contraseña:").pack()
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        tk.Button(self, text="Registrar", command=self.register).pack(pady=10)
        tk.Button(self, text="Volver", command=lambda: controller.show_frame("StartPage")).pack()

    def register(self):
        name = self.name_entry.get()
        last_name = self.last_name_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()

        if not (name and last_name and email and password):
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")
            return

        user = Usuarios(None, name, last_name, email, password)
        user.register_user()
        messagebox.showinfo("Éxito", "Usuario registrado exitosamente")
        self.controller.show_frame("StartPage")


class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        tk.Label(self, text="Inicio de sesión", font=("Arial", 16)).pack(pady=10)

        tk.Label(self, text="Email:").pack()
        self.email_entry = tk.Entry(self)
        self.email_entry.pack()

        tk.Label(self, text="Contraseña:").pack()
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        tk.Button(self, text="Iniciar sesión", command=self.login).pack(pady=10)
        tk.Button(self, text="Volver", command=lambda: controller.show_frame("StartPage")).pack()

    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()

        # Aquí puedes implementar la lógica de autenticación real
        # Para simplicidad, asumo que la autenticación siempre es exitosa
        if email and password:
            self.controller.show_frame("UserManagementPage")
        else:
            messagebox.showwarning("Advertencia", "Email y contraseña son necesarios")


class UserManagementPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        tk.Label(self, text="Gestión de Usuarios", font=("Arial", 16)).pack(pady=10)
        tk.Button(self, text="Mostrar todos los usuarios", command=self.show_users).pack(pady=5)
        tk.Button(self, text="Volver", command=lambda: controller.show_frame("StartPage")).pack()

    def show_users(self):
        Usuarios.show_all_users()


if __name__ == "__main__":
    app = Application()
    app.mainloop()

