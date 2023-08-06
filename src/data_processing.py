### This is a script for cleaning data and feature adding 
### The features for the dataset will be
### From season_stats: G, GS, MP, PER, TS%, OWS, DWS, WS, BPM, FG%, 2P%, 3P%
### From player_stats: name, year_start, year_end,postion, height, weight, birth_date
### To add: age_start, age_end, time_active, is_churn

# -----------------------------------------------

import pandas as pd

# Remover features não necessários e remover jogadores de 1950 a 1979 do csv Seasons_Stats

def Season_dropcol(csv, expname):
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

def ChurnMaker(csv):
    df = pd.read_csv(csv)
    subset_filenames = ['dec_subset_1.csv', 'dec_subset_2.csv', 'dec_subset_3.csv', 'dec_subset_4.csv',
                        'dec_subset_5.csv', 'dec_subset_6.csv', 'dec_subset_7.csv', 'dec_subset_8.csv']
    combined_df = pd.DataFrame()
    for subset_filename in subset_filenames:
        df = pd.read_csv(subset_filename)
        mean_year_active = df['year_active'].mean()
        df['churn'] = (df['year_active'] < mean_year_active).astype(int)
        combined_df = combined_df.append(df, ignore_index=True)
    combined_df.to_csv('Player_Data_Almost_Done.csv', index=False)

# Unir ambos csv

def main():
    pass

if __name__ == '__main__':
    main()
