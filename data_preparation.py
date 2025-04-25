# data_preparation.py

import pandas as pd

def load_and_clean_matches():
    # 1) MATCHES.csv oku
    df = pd.read_csv("Matches.csv")
    # 2) Tarih sütununu 'Date' olarak ayarla
    df['Date'] = pd.to_datetime(df['MatchDate'], dayfirst=True, errors='coerce')
    # 3) Gerekli sütunları seç ve yeniden adlandır
    df = df[['Date', 'HomeTeam', 'AwayTeam', 'FTHome', 'FTAway', 'FTResult',
             'OddHome', 'OddDraw', 'OddAway']]
    df = df.rename(columns={
        'FTHome': 'FTHG', 'FTAway': 'FTAG', 'FTResult': 'FTR',
        'OddHome': 'B365H', 'OddDraw': 'B365D', 'OddAway': 'B365A'
    })
    # 4) Oranları float yap ve eksikleri çıkar
    df[['B365H','B365D','B365A']] = df[['B365H','B365D','B365A']].apply(pd.to_numeric, errors='coerce')
    df = df.dropna(subset=['Date','HomeTeam','AwayTeam','FTR','B365H','B365D','B365A'])
    return df


def load_and_merge_elo(df_matches):
    # 1) EloRatings.csv dosyasını oku (küçük harfli 'date')
    elo = pd.read_csv("EloRatings.csv")
    elo['date'] = pd.to_datetime(elo['date'], dayfirst=True, errors='coerce')
    elo = elo.dropna(subset=['date','club','elo'])

    # 2) Kolon adlarını projedekilere uyarlayarak yeniden adlandır
    elo_home = elo.rename(columns={'club':'HomeTeam', 'elo':'HomeElo', 'date':'Date'})
    elo_away = elo.rename(columns={'club':'AwayTeam', 'elo':'AwayElo', 'date':'Date'})

    # 3) Merge işlemleri
    df = pd.merge(df_matches, elo_home[['Date','HomeTeam','HomeElo']],
                  on=['Date','HomeTeam'], how='left')
    df = pd.merge(df, elo_away[['Date','AwayTeam','AwayElo']],
                  on=['Date','AwayTeam'], how='left')

    df = df.dropna(subset=['HomeElo','AwayElo'])  # eksik elo'lu maçları at
    return df


def engineer_features(df):
    # 1) Bahis marketinin implied probability’si
    for col, new in [('B365H','ProbH'),('B365D','ProbD'),('B365A','ProbA')]:
        df[new] = 1.0 / df[col]
    # 2) Piyasa marjini
    df['BookmakerMargin'] = df['ProbH'] + df['ProbD'] + df['ProbA'] - 1.0
    # 3) Elo farkı
    df['EloDiff'] = df['HomeElo'] - df['AwayElo']
    # 4) Sonuç etiketini sayısal yap (Home=1, Draw=0, Away=-1)
    df['ResultLabel'] = df['FTR'].map({'H':1,'D':0,'A':-1})
    return df

def main():
    print("1) Maç verisi yükleniyor ve temizleniyor…")
    matches = load_and_clean_matches()
    print(f"  → Matches: {len(matches)} satır")

    print("2) Elo verisi ile birleştiriliyor…")
    merged = load_and_merge_elo(matches)
    print(f"  → Merged: {len(merged)} satır")

    print("3) Özellik mühendisliği yapılıyor…")
    final = engineer_features(merged)

    # Temizlenmiş veriyi kaydet
    final.to_csv("cleaned_data.csv", index=False)
    print("✅ cleaned_data.csv oluşturuldu. Toplam sütun sayısı:", len(final.columns))

if __name__ == "__main__":
    main()
