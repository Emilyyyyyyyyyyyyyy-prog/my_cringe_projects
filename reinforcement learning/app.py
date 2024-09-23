import flet as ft
from code import WorldOptions
from code import GridWorld
from code import Agent
from code import Agent_V


def main(page: ft.Page):
    options = WorldOptions()
    options.board_rows = 3
    options.board_cols = 4
    options.win_state = (2, 3)
    options.lose_state = (1, 3)
    options.start_state = (0, 0)
    options.obstacles = [(1, 1), (1, 2)]

    options.deterministic = True

    page.title = "Agent"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def btn_click(e):
        if not txt_name.value:
            txt_name.error_text = "Please enter count of rounds!!"
            page.update()
        else:
            count_rounds = txt_name.value
            page.clean()
            ag = Agent_V(options)
            ag.play(int(count_rounds))
            ag.show_values()

    txt_name = ft.TextField(label="roundsCount")

    page.add(txt_name, ft.ElevatedButton("Play!", on_click=btn_click))


ft.app(main)
