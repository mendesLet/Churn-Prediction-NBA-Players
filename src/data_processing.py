### This is a script for cleaning data and feature adding 
### The features for the dataset will be
### From season_stats: G, GS, MP, PER, TS%, OWS, DWS, WS, BPM, FG%, 2P%, 3P%
### From player_stats: name, year_start, year_end,postion, height, weight, birth_date
### To add: age_start, age_end, time_active, is_churn

# -----------------------------------------------

import pandas as pd

# Remover features não necessários e remover jogadores de 1950 a 1979 do csv Seasons_Stats

def Season_dropcol(csv, expname): #csv: input csv path, expname: exported csv name
    df = pd.read_csv(csv)
    drop_col = ['Age', '3PAr', 'FTr', 'ORB%', 'DRB%', 'TRB%',
                 'AST%', 'STL%', 'BLK%', 'TOV%', 'USG%', 'blanl', 'WS/48',
                 'blank2', 'OBPM', 'DBPM', 'VORP', 'FG', 'FGA', '3P',
                 '3PA', '2P', '2PA', 'eFG%', 'FT', 'FTA', 'FT%', 'ORB',
                 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']
    df = df.drop(drop_col, axis=1)
    
    df = df.iloc[6449:]
    df = df.dropna()
    
    df['Year'] = df['Year'].round().astype(int)
    df['G'] = df['G'].round().astype(int)
    df['GS'] = df['GS'].round().astype(int)
    df['MP'] = df['MP'].round().astype(int)

    df.to_csv(expname, index=False)


# Calcular idade (age_start, age_end) e tempo ativo (time_active) adicionar colunas
# Calcular média de year_end para intervalos de anos 

def Player_newFeatures(csv):
    df = pd.read_csv(csv)
    
    df = df.drop(columns=['college'])
    df = df.dropna(subset=['position', 'height', 'weight', 'birth_date'])
    
    df['birth_date'] = pd.to_datetime(df['birth_date'])
    df['birth_date'] = df['birth_date'].dt.year
    df['birth_date'] = df['birth_date'].round().astype(int)
    df['weight'] = df['weight'].round().astype(int)
    df['year_active'] = (df['year_end'] - df['year_start'] + 1)
    df['age_start'] = (df['year_start'] - df['birth_date'])
    df['age_end'] = (df['year_end'] - df['birth_date'])
    df = df.sort_values(by='year_start')
    df = df.reset_index()
    df = df.drop(columns=['index'])
    mean = df['year_active'].mean()
    df['churn'] = (df['year_active'] > mean).astype(int)

    dec1 = df.loc[0:594]
    dec2 = df.loc[595:848]
    dec3 = df.loc[849:1653]
    dec4 = df.loc[1654:2241]
    dec5 = df.loc[2242:2927]
    dec6 = df.loc[2928:3612]
    dec7 = df.loc[3613:4337]
    dec8 = df.loc[4338:]
    
    subsets = [dec1, dec2, dec3, dec4, dec5, dec6, dec7, dec8]
    
    for i, subset in enumerate(subsets, start=1):
        subset.to_csv(f'dec_subset_{i}.csv', index=False)


# Medir se é churn e criar coluna churn

def Player_churnMaker(expname): 
    df = pd.read_csv()
    subset_filenames = ['dec_subset_1.csv', 'dec_subset_2.csv', 'dec_subset_3.csv', 'dec_subset_4.csv',
                        'dec_subset_5.csv', 'dec_subset_6.csv', 'dec_subset_7.csv', 'dec_subset_8.csv']
    combined_df = pd.DataFrame()
    for subset_filename in subset_filenames:
        df = pd.read_csv(subset_filename)
        mean_year_active = df['year_active'].mean()
        df['churn'] = (df['year_active'] < mean_year_active).astype(int)
        combined_df = combined_df.append(df, ignore_index=True)
    combined_df.to_csv(expname, index=False)

def Season_groupBy(csv, expname):
    df = pd.read_csv(csv)
    df.drop(columns=['Unnamed: 0', 'Year', 'Tm'], inplace=True)
    df['group_id'] = (df['Player'] != df['Player'].shift(1)).cumsum()
    
    df['careers'] = df.groupby(['group_id', 'Player']).cumcount() + 1
    
    unique_combinations = pd.DataFrame({
        'group_id': df['group_id'].values,
        'Player': df['Player'].values,
        'Pos': df['Pos'].values
    })
    
    # Merge the unique_combinations DataFrame with the original DataFrame to ensure all names are included
    merged_df = unique_combinations.merge(df, on=['group_id', 'Player', 'Pos'], how='left')
    
    # Group by 'group_id', 'names', and 'gender', sum 'goals', calculate mean of 'score', and get the max 'career'
    transformed_df = merged_df.groupby(['group_id', 'Player', 'Pos'], as_index=False).agg({'G': 'sum', 'PER': lambda x: round(x.mean(), 1), 'careers': 'max',
                                                                                           'GS': 'sum', 'MP': 'sum', 'TS%': lambda x: round(x.mean(), 1), 'OWS': lambda x: round(x.mean(), 1),
                                                                                           'DWS': lambda x: round(x.mean(), 1), 'WS': lambda x: round(x.mean(), 1), 'BPM': lambda x: round(x.mean(), 1), 'FG%': lambda x: round(x.mean(), 1),
                                                                                           '2P%': lambda x: round(x.mean(), 1), '3P%': lambda x: round(x.mean(), 1)})
    transformed_df.to_csv(expname, index=False)
    
# Unir ambos csv

def JoinCsv(csv1, csv2, expname):
    Season_Stats = pd.read_csv(csv1) # 'Season_Stats.csv'
    Player_Data = pd.read_csv(csv2) # 'Player_Data.csv'
    
    # Agroupar DataFrames 
    groups_csv1 = Season_Stats.groupby('Player_Season').groups
    groups_csv2 = Player_Data.groupby('Player_Data').groups
    
    # Criando um df vazio para o resultado da concatenação
    combined_df = pd.DataFrame(columns=Season_Stats.columns)
    
    # Iterar pelos dfs e combinar eles
    for name, idx_list_csv1 in groups_csv1.items():
        idx_list_csv2 = groups_csv2.get(name)
        
        if idx_list_csv2 is not None:
            for idx_csv1, idx_csv2 in zip(idx_list_csv1, idx_list_csv2):
                combined_row = pd.concat([Season_Stats.iloc[[idx_csv1]], Player_Data.iloc[[idx_csv2]]], axis=1)
                combined_df = combined_df.append(combined_row, ignore_index=True)
    
    # Ajustes nas linhas 
    columns_to_shift = ['Player_Data', 'year_start', 'year_end', 'height',
                        'weight', 'birth_date', 'year_active', 'age_start',
                        'age_end', 'churn']
    
    # Shift the values in the specified columns up by one line
    for column in columns_to_shift:
        combined_df[column] = combined_df[column].shift(-1)
    
    # Ajustes finais
    combined_df = combined_df.iloc[::2].reset_index(drop=True)
    
    int_columns = ['G', 'careers', 'GS', 'MP', 'year_start', 'year_end',
                   'weight', 'birth_date', 'year_active', 'age_start', 'age_end',
                   'churn']
    for columns in int_columns:
      combined_df[columns] = combined_df[columns].round().astype(int)
    
    combined_df = combined_df.drop(columns=['group_id', 'Player_Data'])
    combined_df.to_csv(expname, index=False)

    
def main():
    # Add names of input csvs and output csvs
    csv_Season_dropcol = ''
    expname_Season_dropcol = ''
    Season_dropcol(csv_Season_dropcol, expname_Season_dropcol)
    
    csv_Player_newFeatures = ''
    Player_newFeatures(csv_Player_newFeatures)

    expname_Player_churnMaker = ''
    Player_churnMaker(expname_Player_churnMaker) # Deve ter os arquivos criados pelo Player_newFeatures com os mesmos nomes que quando gerados

    csv_Season_groupBy = ''
    expname_Season_groupBy = ''
    Season_groupBy(csv_Season_groupBy, expname_Season_groupBy)

    csv1_JoinCsv = ''
    csv2_JoinCsv = ''
    expname_JoinCsv = ''
    JoinCsv(csv1_JoinCsv, csv2_JoinCsv, expname_JoinCsv)
    

if __name__ == '__main__':
    main()
