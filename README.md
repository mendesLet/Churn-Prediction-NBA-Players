# Churn Prediction of NBA Players
Este projeto foi feito para o trabalho final da diciplina de Pensamento Analítico de Dados para o curso de Inteligência Artificial da UFG, nosso grupo escolheu trabalhar com Predição de Churn, e como pedido pelo professor, o que move esse projeto é a pergunta: 
**É possível entender o que causa "Churn" em jogadores da NBA? E assim prever futuras desistências da carreira?**

## Dataset
Nós iniciamos com um dataset original do Kaggle [NBA Players stats since 1950](https://www.kaggle.com/datasets/drgilermo/nba-players-stats?select=Seasons_Stats.csv), que consiste em dois CSVs separados:
1. **Season_stats.csv**: Um dataset que contém dados das carreiras dos jogadores, como Winrate, Time, Posição, 3 points rate, e outras features
2. **player_data.csv**: Um dataset que contém dados pessoas dos jogadores, como idade de início de carreira, altura, peso, e assim por diante

As principais modificações feitas no dataset além da união de ambos, foi adição de features, como principal foco do projeto é churn, definimos que o Churn do projeto seria jogadores que tiveram uma carreira menor que a média de tempo das carreiras durante a década que o jogador iniciou. Outra modificação foi, como característica do dataset Season_stats.csv um jogador pode ter tido diferentes carreiras, foi decidido pelo grupo unir essas carreiras e gerar uma média dos features durante essas carreiras.
