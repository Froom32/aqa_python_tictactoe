from Pages.GamePage import GameHelper


def test_x_player_should_win_by_vertical_line_board_3x3(browser):
    game_page = GameHelper(browser)
    game_page.go_to_site()
    game_page.select_board_format("board_3")
    game_page.click("00")
    game_page.click('00')
    assert game_page.find_element('00').text == "X"
