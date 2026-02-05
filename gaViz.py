import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'MS Gothic'

# CSVファイルの読み込み
# ファイル名は適宜変更してください
file_path = '100_0.05_5_false.csv'
df = pd.read_csv(file_path)

# プロットの作成
plt.figure(figsize=(10, 6))
plt.plot(df['generation'], df['best_distance'], label='ベスト距離(Best Distance)')

# ラベルとタイトルの設定
plt.xlabel('世代(Generation)')
plt.ylabel('ベスト距離(Best Distance)')
plt.title('')

# グリッドと凡例の表示
plt.grid(True)
plt.legend()

# レイアウトの調整と保存（または表示）
plt.tight_layout()
plt.savefig(file_path[:-3] + 'png')
plt.show()