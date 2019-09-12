class Settings():
    def __init__(self):
        # スクリーン
        self.screen_width  = 900
        self.screen_height = 900
        self.bg_color = (230, 230, 230)
        # マップ
        self.map_row = [900, 3]
        self.map_column = [3, 900]
        self.map_row_location = [[0, 300], [0, 600]]
        self.map_column_location = [[300, 0], [600, 0]]
        self.map_color = 60, 60, 60
        # チェスグルプ
        self.group_all = []
        self.group_o = []
        self.group_x = []
        # 結果メッセージ
        self.result_msg = ""
        # X、O判定用フラグ
        self.piece_flag = True
        # 勝負判定用フラグ
        self.win_flag = True
        # AI使うかどうか判定用フラグ
        self.ai_flag = True
        # ダブルクリック判定用フラグ
        self.double_click = False
        # ゲーム開始、終わり判定用フラグ
        self.game_active = False
        # 先手
        self.second = [1, 3, 7, 9]
        # 後手
        self.first = 5
        # チェッカーボード場所記録
        self.checkerboard_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        # チェッカーボードマップロケーション記録
        self.checkerboard_map = [[0, 0], [1, 0], [2, 0],
                                [0, 1], [1, 1], [2, 1],
                                [0, 2], [1, 2], [2, 2]]
        # すべの勝ち状況
        self.win_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9],
                         [1, 4, 7], [2, 5, 8], [3, 6, 9],
                         [1, 5, 9], [3, 5, 7]]

