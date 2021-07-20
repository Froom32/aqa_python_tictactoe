from Pages.GamePage import GameHelper


def test_0_player_should_win_by_horizontal_line_board_3x3(browser):
    game_page = GameHelper(browser)
    game_page.go_to_site()
    game_page.select_board_format("board_3")
    game_page.click("20")
    game_page.click('12')
    game_page.click('01')
    game_page.click('11')
    game_page.click('21')
    game_page.click('10')
    assert game_page.take_game_result() == "0 Won!"


def test_0_player_should_win_by_opposite_diagonal_line_board_4x4(browser):
    game_page = GameHelper(browser)
    game_page.select_board_format("board_4")
    game_page.click("00")
    game_page.click('03')
    game_page.click('11')
    game_page.click('12')
    game_page.click('13')
    game_page.click('21')
    game_page.click('22')
    game_page.click('30')
    assert game_page.take_game_result() == "0 Won!"


def test_0_player_should_win_by_vertical_line_board_5x5(browser):
    game_page = GameHelper(browser)
    game_page.select_board_format("board_5")
    game_page.click("11")
    game_page.click('40')
    game_page.click('12')
    game_page.click('41')
    game_page.click('03')
    game_page.click('42')
    game_page.click('23')
    game_page.click('43')
    game_page.click('30')
    game_page.click('44')
    assert game_page.take_game_result() == "0 Won!"
