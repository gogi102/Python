import random

horses = ["말1", "말2", "말3", "말4", "말5"]

def virtual_horse_race():
    print("가상 경마 게임에 오신 것을 환영합니다!")

    # 베팅
    print("베팅할 말의 번호를 선택하세요:")
    for i, horse in enumerate(horses, 1):
        print(f"{i}: {horse}")
    player_bet = int(input("번호를 입력하세요 (1-5): "))
    player_bet -= 1  # 리스트 인덱스와 맞추기 위해 1을 뺍니다

    bet_amount = int(input("베팅할 금액을 입력하세요: "))

    # 경주 시작
    winning_horse = random.choice(horses)

    print("경주 결과:")
    for i, horse in enumerate(horses):
        position = "🐎" if horse == winning_horse else "-"
        print(f"{i + 1}: {horse} {position}")

    # 베팅 결과 결정
    if player_bet == horses.index(winning_horse):
        print(f"축하합니다! {winning_horse}에 베팅한 {bet_amount}원을 얻었습니다!")
        return bet_amount
    else:
        print(f"아쉽지만 {winning_horse}에 베팅한 금액 {bet_amount}원을 잃었습니다.")
        return -bet_amount

if __name__ == "__main__":
   player_money = 5000

   while player_money > 0:
       print(f"남은 돈: {player_money}원")
       result = virtual_horse_race()
       player_money += result

       play_again = input("게임을 더 하시겠습니까? (y/n): ").lower()
       if play_again != "y":
           break

   print("게임 종료. 수고하셨습니다!")
