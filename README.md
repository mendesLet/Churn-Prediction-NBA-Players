# Modelo de Predição de "Churn" de Atletas na NBA League 
Este repositório contém o código e informações relacionadas à predição de atletas que abandonarão precocemente a NBA League, permitindo que a liga tome medidas proativas para mitigar o "churn".

## Processos:
**Limpeza e Transformação de Dados**: Foram removidas colunas dos dados originais que poderião causar overfitting do modelo. Também foi realiza a normalização dos dados e aplicação do one-hot encoding em variáveis categóricas. Isso garante que os dados estejam prontos para serem usados pelos modelos de machine learning.

## Modelos de Machine Learning:

**Logistic Regression**: Um modelo de regressão logística é treinado usando os dados pré-processados. Ele serve como um baseline para comparação com os outros modelos.

**Gradient Boosting Classifier**: O modelo Gradient Boosting é implementado e treinado usando o FMF para realizar a previsão de churn. Ele é escolhido como o modelo principal devido ao seu desempenho superior.

**Support Vector Machine Classifier**: Um modelo de Support Vector Machine é implementado e treinado para fins de comparação de desempenho.

## Avaliação de Modelos: 
Os modelos são avaliados usando métricas relevantes, como precisão, recall, F1-score e ROC AUC. 

## Escolha do Modelo: 
Com base principalmente no balanço entre recall e precision, o Gradient Boosting Classifier é escolhido como o modelo preferido de previsão de "churn" para atletas na NBA League.

## Referência:
Este código utilizará como referência o FMF, principalmente o que tange à transformação de dados: https://www.kaggle.com/code/kmalit/bank-customer-churn-prediction/notebook
