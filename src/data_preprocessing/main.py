import requests
import pandas as pd

# ANTES DE RODAR O CODIGO MUDE O NOME DO CSV QUE SERÁ GERADO NO FINAL!!!

MatchIDArr = []
AccountIDArr = []
AllAccountIDs = []
MIDNUM = 0
AIDNUM = 0
getIDRecursionCounter = 0
callCounter = 0
# MatchIDArr: Pega os IDs das partidas recentes de um jogador especifico
# AccountIDArr: Pega os IDs dos jogadores dentro de uma partida especifica
# AllAccountIDs: É a lista que vai pegar todos os IDs de usuário que a gente precisa
# callCounter: Conta a quantidade de chamadas feitas para o API
# getIDRecursionCounter: Conta a quantidade de recursões em getAccount
# AIDNUM e MIDNUM: Pega o primeiro Account ID e Match ID da lista. Isso é feito para
# evitar possiveis falhas relacionada a possibilidade dos jogadores esconderem certas
# coisas sobre os seus dados.


#--------------------------------------------

def getAccount(MIDNUM):
  global callCounter
  AccountIDArr.clear()
  MatchID = MatchIDArr[MIDNUM]

  url2 = f'https://api.opendota.com/api/matches/{MatchID}'
  MatchData = requests.get(url2)
  callCounter += 1
  MatchData = MatchData.json()
  players = MatchData.get('players', [])

  for player in players:
    account_id = player.get('account_id')
    if account_id is not None:
      AccountIDArr.append(account_id)
      AllAccountIDs.append(account_id)
      #if account_id not in AllAccountIDs:
        #AllAccountIDs.append(account_id)


  if len(AccountIDArr) == 0:
    getMatchRecursionCounter += 1
    if callCounter > 58:
      return
    if getIDRecursionCounter > 9:
      getIDRecursionCounter = 0
    else:
      getAccount(MIDNUM+1)


def getMatch(AIDNUM):
  global callCounter
  MatchIDArr.clear()
  AccountID = AccountIDArr[AIDNUM]

  url3 = f'https://api.opendota.com/api/players/{AccountID}/recentMatches'
  rMatch = requests.get(url3)
  callCounter += 1
  rMatch = rMatch.json()

  for item in rMatch:
    # MatchIDArr.append(item['match_id'])
    for key, value in item.items():
      if key == "match_id":
        MatchIDArr.append(value)


#---------------------------------------------


if __name__ == "__main__":
  # Pacient_zero is a AccountID
  pacient_zero = 72253508

  url1 = f'https://api.opendota.com/api/players/{pacient_zero}/recentMatches'
  rMatch = requests.get(url1)
  rMatch = rMatch.json()

  for item in rMatch:
    # MatchIDArr.append(item['match_id'])
    for key, value in item.items():
      if key == "match_id":
        MatchIDArr.append(value)


  while callCounter < 55:
    getAccount(AIDNUM)
    getMatch(MIDNUM)

  # print(AllAccountIDs)
  # print(len(AllAccountIDs))

  df = pd.DataFrame(AllAccountIDs, columns=['Account_ID'])

  df = df.drop_duplicates()

  file_path = './data/raw_data/MatchIDs_2.csv'
  df.to_csv(file_path)