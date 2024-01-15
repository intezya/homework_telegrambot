import flet as ft

from db.interaction import DataBase

DB = DataBase('main.db')

info = DB.get_info()


def example():
    return ft.DataTable(
        width=700,
        bgcolor="#141221",
        border=ft.border.all(2, "red"),
        border_radius=10,
        vertical_lines=ft.border.BorderSide(3, "blue"),
        horizontal_lines=ft.border.BorderSide(1, "green"),
        sort_column_index=0,
        sort_ascending=True,
        heading_row_color=ft.colors.BLACK12,
        heading_row_height=100,
        data_row_color={"hovered": "0x30FF0000"},
        show_checkbox_column=True,
        divider_thickness=0,
        column_spacing=200,
        columns=[
            ft.DataColumn(
                ft.Text("Column 1")
            ),
            ft.DataColumn(
                ft.Text("Column 2"),
                tooltip="This is a second column"
            ),
        ],
        rows=[
            ft.DataRow(
                [ft.DataCell(ft.Text("A")), ft.DataCell(ft.Text("1"))]
            ),
            ft.DataRow([ft.DataCell(ft.Text("B")), ft.DataCell(ft.Text("2"))]),
        ],
    )
