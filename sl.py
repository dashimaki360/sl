#!/usr/bin/env python3

import os
import sys
import argparse
import time

# 簡単な列車のアニメーションの定義
frames = [
"""
       　　　　　　　　　　　　＿⊂三ニニ⊃＿＿_＿　パーーーポーーーーーーーーーーーーーー！！！！
　　　　　　　　　　　, -'＿＿＿＿ ,-'＿＿　　　 ''-,,
　　　　　　　　　 ／_,,''⌒'',,.　　７/''⌒'',,;|;''ヽ,ヽ,
　　　　　　　　／　（・∀・) ）　.//￣,_√）|;|;| 　　　|ヽ,ヽ,
　　　　　　[／＿_⊆⊇_ヽ__）_/[;;;]y＿つ_|;|;|.＿＿.|__ヽ, ''―-,,,
　 _,,,.-'￣'￣'￣'￣/;,,.-―''''"_ |＿＿警_=.|視＿庁__=_|＿＿_|]
._/二ゝo=*=o/二ソ;;/⌒ヽ ;;;;;; |;;;;|;;;;;;;;;/⌒ヽ;;;;;;;;;〕
ヽロ＝[ニ]＝ロヽ.:: ０ i|; ;;;;;|;;;;;;;i:: ０ i|;;;;ノ　≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡3
　 ￣ゞ;三ノ￣￣￣ゞ___ノ￣￣￣ゞ;三ノ￣￣￣￣ゞ___ノ
￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣
""",
"""
       　　　　　　　　　　　　＿⊂三ニニ⊃＿＿_＿　
　　　　　　　　　　　, -'＿＿＿＿ ,-'＿＿　　　 ''-,,
　　　　　　　　　 ／_,,''⌒'',,.　　７/''⌒'',,;|;''ヽ,ヽ,
　　　　　　　　／　（・∀・) ）　.//￣,_√）|;|;| 　　　|ヽ,ヽ,
　　　　　　[／＿_⊆⊇_ヽ__）_/[;;;]y＿つ_|;|;|.＿＿.|__ヽ, ''―-,,,
　 _,,,.-'￣'￣'￣'￣/;,,.-―''''"_ |＿＿警_=.|視＿庁__=_|＿＿_|]
._/二ゝo=*=o/二ソ;;/⌒ヽ ;;;;;; |;;;;|;;;;;;;;;/⌒ヽ;;;;;;;;;〕
ヽロ＝[ニ]＝ロヽ.:: ０ i|; ;;;;;|;;;;;;;i:: ０ i|;;;;ノ　
　 ￣ゞ;三ノ￣￣￣ゞ___ノ￣￣￣ゞ;三ノ￣￣￣￣ゞ___ノ
￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣
"""
]

def animate(frames, speed=0.03, anima_speed = 8):
    terminal_width = os.get_terminal_size().columns
    terminal_width -= 100
    anima_idx = 0
    for space in range(terminal_width*2):
        if space % anima_speed == 0:
            anima_idx += 1
            anima_idx %= len(frames)
        frame = frames[anima_idx]

        # 前のフレームを消すためにコンソールをクリアします
        os.system('cls' if os.name == 'nt' else 'clear')

        # スペースを各行に追加し、ターミナル幅を超えないように調整します
        frame_lines = frame.split('\n')
        for i in range(len(frame_lines)):
            line = " " * terminal_width + frame_lines[i] + " " * terminal_width
            line = line[space:space + terminal_width]  # ターミナルの幅を超えないように調整
            print(line)

        time.sleep(speed)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='パトカー版SLコマンド')
    parser.add_argument('-r', '--repeat', action='store_true')
    parser.add_argument('--speed',default=0.03, type=float, help="move speed. default=0.03")
    parser.add_argument('--animation_speed', default=8, type=int, help="animation speed.How many frame keep same frame. default=8")
    args = parser.parse_args()

    # アニメーションを開始します
    while True:
       animate(frames, args.speed, args.animation_speed)
       if not args.repeat:
           break