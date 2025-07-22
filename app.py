import streamlit as st
import pandas as pd
import csv

st.title('売上予測アプリ')

# 入力フォーム
youbi = st.selectbox('曜日区分を選択してください', ['平日', '休日', '祝祭日'])
tenki = st.selectbox('天気を選択してください', ['晴れ', '雨', '曇り'])

# 予測ボタン
if st.button('売上を予測'):
    # CSVファイルを読み込む
    df = pd.read_csv('売り上げ.csv', encoding='shift_jis')
    # 条件に合うデータを抽出
    data = df[(df['曜日区分'] == youbi) & (df['天気'] == tenki)]
    if len(data) == 0:
        st.warning('該当するデータがありません。サンプルデータから予測します。')
        yoso = 10000  # データがない場合の仮の予測値
    else:
        yoso = data['売上'].mean()
        st.success(f'{youbi}・{tenki}の予測売上は {int(yoso)} 円です。')
    # 予測値をファイルに追記
    with open('売り上げ.csv', 'a', encoding='shift_jis', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([youbi, tenki, int(yoso)])
        st.info(f'予測値 {int(yoso)} 円 を売り上げ.csvに追加しました。') 