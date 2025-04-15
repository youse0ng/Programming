# 최대 몇번 플레이할 수 있는가?
# for문을 돌면서 already_played에 있는 건 플레이에 참여 X
# Y:2,F:3,O:4
N,game = input().split()
plays = 0
already_played = set()
on_game_player = []
for _ in range(int(N)):
    player = input()
    if player in already_played:
        continue
    else:
        on_game_player.append(player)
        already_played.add(player)
    if game == 'Y':
        if len(on_game_player) == 1:
            on_game_player.clear()
            plays += 1
    elif game == 'F':
        if len(on_game_player) == 2:
            on_game_player.clear()
            plays += 1
    elif game == 'O':
        if len(on_game_player) == 3:
            on_game_player.clear()
            plays += 1
    # print(f'대기방: {on_game_player}')
    # print(f'이미 게임을 한 자: {already_played}')
print(plays)