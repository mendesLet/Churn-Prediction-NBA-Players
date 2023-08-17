# Churn Prediction of NBA Players
Este projeto foi feito para o trabalho final da diciplina de Pensamento Analítico de Dados para o curso de Inteligência Artificial da UFG, nosso grupo escolheu trabalhar com Predição de Churn, e como pedido pelo professor, o que move esse projeto é a pergunta: 
**É possível entender o que causa "Churn" em jogadores da NBA? E assim prever futuras desistências da carreira?**

## Dataset
Nós iniciamos com um dataset original do Kaggle [NBA Players stats since 1950](https://www.kaggle.com/datasets/drgilermo/nba-players-stats?select=Seasons_Stats.csv), que consiste em dois CSVs separados:
1. **Season_stats.csv**: Um dataset que contém dados das carreiras dos jogadores, como Winrate, Time, Posição, 3 points rate, e outras features
2. **player_data.csv**: Um dataset que contém dados pessoas dos jogadores, como idade de início de carreira, altura, peso, e assim por diante

As principais modificações feitas no dataset além da união de ambos, foi adição de features, como principal foco do projeto é churn, definimos que o Churn do projeto seria jogadores que tiveram uma carreira menor que a média de tempo das carreiras durante a década que o jogador iniciou. Outra modificação foi, como característica do dataset Season_stats.csv um jogador pode ter tido diferentes carreiras, foi decidido pelo grupo unir essas carreiras e gerar uma média dos features durante essas carreiras.

## Exploração de Métricas
A análise exploratória envolveu a exploração das seguintes métricas:

Taxa de vitória (Winning Percentage);

Índice de Eficiência (PER);

Posição dos jogadores (Pos);

Outras métricas relevantes, como idade, altura, peso, entre outras
Gráficos e visualizações foram utilizados para identificar padrões, tendências e relações entre as métricas. 
Isso incluiu gráficos de dispersão, gráficos de barras e matrizes de correlação.

## Resultados e Insights
A análise exploratória revelou insights interessantes sobre a relação entre diferentes métricas e a possibilidade de "churn" (desistência) de jogadores da NBA. 
Foram identificados padrões de desempenho e características pessoais que podem estar relacionados a maiores taxas de churn.

## Processos:
**Limpeza e Transformação de Dados**: foram removidas colunas dos dados originais que poderiam causar overfitting do modelo. 
Também foi realizada a normalização dos dados e aplicação do one-hot encoding em variáveis categóricas. 
Isso garante que os dados estejam prontos para serem utilizados pelos modelos de machine learning.

## Modelos de Machine Learning:

**Logistic Regression**

**Gradient Boosting**

**Random Forest Classifier**

## Avaliação de Modelos: 
Os modelos foram avaliados utilizando métricas relevantes, como precisão, recall, F1-score e ROC AUC. 

## Comparações 

*Conjunto FMF:*

Logistic Regression:
Acurácia: 0.84
Precision (Precisão): 0.84
Recall (Revocação): 0.82
F1-score: 0.83

Random Forest Classifier:
Acurácia: 0.83
Precision (Precisão): 0.83
Recall (Revocação): 0.82
F1-score: 0.83

Gradient Boost Classifier:
Acurácia: 0.85
Precision (Precisão): 0.85
Recall (Revocação): 0.81
F1-score: 0.85

*Conjunto MEDIUM:*

Logistic Regression:
Acurácia: 0.84
Precision (Precisão): 0.84
Recall (Revocação): 0.80
F1-score: 0.83

Random Forest Classifier:
Acurácia: 0.84
Precision (Precisão): 0.84
Recall (Revocação): 0.81
F1-score: 0.83

Gradient Boost Classifier:
Acurácia: 0.85
Precision (Precisão): 0.85
Recall (Revocação): 0.81
F1-score: 0.85


## Resultados
Ao comparar os resultados dos modelos nos conjuntos de métricas FMF e MEDIUM, observamos que os modelos Gradient Boost Classifier tendem a ter melhor desempenho em termos de acurácia, precisão, F1-score e recall em comparação com os outros dois modelos (Logistic Regression e Random Forest Classifier). O Gradient Boost Classifier também apresenta consistência entre os dois conjuntos de métricas. E entre os modelos a diferença é miníma se distinguindo na preparação dos dados e na métrica de escolha para determinar o desempenho do modelo.
