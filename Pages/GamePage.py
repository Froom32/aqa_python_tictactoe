from Pages.BasePage import BasePage


class GameSearchLocators:
    ID_GAME_RESULT_FIELD = "content"
    ID_BUTTON_NEW_GAME = "btn-new-game"


class GameHelper(BasePage):

    def select_board_format(self, board_format):
        self.click(board_format)
        return self.click(GameSearchLocators.ID_BUTTON_NEW_GAME)

    def take_game_result(self):
        return self.find_element(GameSearchLocators.ID_GAME_RESULT_FIELD).text
