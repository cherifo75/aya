import flet as ft

def main(page: ft.Page):
    page.title = "IZER NAVIGATOR"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 0
    main_blue = "#00E5FF"

    def build_izer_ui():
        return ft.Stack([
            ft.Container(
                image_src="assets/tuna_izer_bg.jpg",
                image_fit=ft.ImageFit.COVER,
                opacity=0.35,
                expand=True,
            ),
            ft.Container(
                padding=ft.padding.only(top=40, left=20, right=20, bottom=30),
                content=ft.Column([
                    ft.Row([
                        ft.Text("IZER", size=36, weight="bold", color=main_blue, letter_spacing=5),
                        ft.Container(content=ft.Text("NAV", size=12, color="green", weight="bold"), border=ft.border.all(1, "green"), padding=8, border_radius=8)
                    ], alignment="space_between"),
                    ft.Container(height=30),
                    ft.Container(
                        padding=25, bgcolor="#CC000000", border_radius=20, border=ft.border.all(1, "white10"), blur=ft.Blur(10, 10),
                        content=ft.Column([
                            ft.Row([ft.Icon(ft.icons.TARGET, color=main_blue, size=16), ft.Text("TARGET DESTINATION", color="white70", size=14)]),
                            ft.Text("00° 00.00' N", size=58, weight="bold", color="white", letter_spacing=2),
                            ft.Divider(color="white10", height=10),
                            ft.Text("الهدف: خط الاستواء (Deep Water Zone)", size=14, color="white70", weight="bold"),
                        ], horizontal_alignment="center")
                    ),
                    ft.Spacer(),
                    ft.Column([
                        ft.ElevatedButton(content=ft.Row([ft.Icon(ft.icons.RADAR), ft.Text("MARK STRIKE LOCATION", weight="bold")], alignment="center"), style=ft.ButtonStyle(bgcolor=main_blue, color="#000000", shape=ft.RoundedRectangleBorder(radius=15)), height=70, width=500),
                        ft.OutlinedButton(content=ft.Row([ft.Icon(ft.icons.ANCHOR), ft.Text("RETURN TO COAST", weight="bold")], alignment="center"), style=ft.ButtonStyle(color=main_blue, side=ft.border.all(2, main_blue), shape=ft.RoundedRectangleBorder(radius=15)), height=70, width=500),
                    ], spacing=10),
                ])
            )
        ])
    page.add(build_izer_ui())

if __name__ == "__main__":
    ft.app(target=main)
