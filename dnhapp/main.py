import flet as ft

def main(page: ft.Page):
    # Устанавливаем заголовок страницы
    page.title = "DNHTech"
    # Устанавливаем автоматически изменяемую тему в зависимости от системной темы
    page.theme_mode = None
    # Выравниваем элементы по вертикали по центру
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Создаем метку для отображения информации
    user_label = ft.Text("Info")
    # Создаем текстовое поле для ввода пользователя
    user_text = ft.TextField(value="0", width=150, text_align=ft.TextAlign.CENTER)

    # Функция для обработки нажатия кнопки
    def get_info(e):
        # Обновляем значение метки информацией из текстового поля
        user_label.value = user_text.value
        # Обновляем страницу, чтобы отобразить изменения
        page.update()

    # Добавляем элементы на страницу
    page.add(
        ft.Row(
            [
                # Кнопка с иконкой дома, при нажатии вызывается get_info
                ft.IconButton(ft.icons.HOME, on_click=get_info),
                # Иконка в виде руки
                ft.Icon(ft.icons.BACK_HAND),
                # Кнопка с текстом "Click me!", при нажатии вызывается get_info
                ft.ElevatedButton(text="Click me!", on_click=get_info),
                # Кнопка с текстом "Clich meh", при нажатии вызывается get_info
                ft.OutlinedButton(text="Clich meh", on_click=get_info),
                # Чекбокс с вопросом "Вы согласны?", значение по умолчанию - True
                ft.Checkbox(label="Вы согласны?", value=True, on_change=True)
            ],
            # Выравнивание элементов в строке по центру
            alignment=ft.MainAxisAlignment.CENTER
        ),
        # Вторая строка с меткой и текстовым полем
        ft.Row(
            [
                user_label,
                user_text
            ],
            # Выравнивание элементов в строке по центру
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

# Запускаем приложение с целевой функцией main
ft.app(target=main)