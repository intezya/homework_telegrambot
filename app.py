# layout - row, DataTable

import flet
from flet import Page

from db.DataTable import example


async def main(page: Page) -> None:
    page.title = "Домашнее задание"
    page.theme_mode = flet.ThemeMode.DARK
    page.bgcolor = "#141221"
    page.vertical_alignment = flet.MainAxisAlignment.CENTER
    page.horizontal_alignment = flet.CrossAxisAlignment.CENTER
    page.fonts = {"FulboArgenta": "assets/fonts/FulboArgenta.ttf"}
    page.theme = flet.Theme(font_family="FulboArgenta")

    table = example()

    await page.add_async(
        table
    )


if __name__ == "__main__":
    flet.app(target=main)
