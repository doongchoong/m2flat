import pandas as pd


def gen_flat_m2(ixic_file='IXIC.csv', m2_file='M2.csv'):
    m2 = pd.read_csv(m2_file)
    m2.columns = ['Date', 'M2']
    print(m2)

    ixic = pd.read_csv(ixic_file)
    print(ixic)

    # 일봉 기준으로 병합 
    merged = pd.merge(ixic, m2, on='Date', how='left')

    # 결측값은 Nan이므로 보간처리한다.
    merged['M2'] = merged['M2'].interpolate(method='values')

    # 보간 못하는 첫부분 삭제
    merged = merged.dropna(axis=0) # 결측값 있는 행 제거
    merged.reset_index(drop=True, inplace=True)

    # M2 Flatting 
    base_m2 = merged.loc[0]['M2']
    print('base_m2', base_m2)

    merged['Open_1'] = (merged['Open'] * base_m2 / merged['M2']).round(2)
    merged['High_1'] = (merged['High'] * base_m2 / merged['M2']).round(2)
    merged['Low_1' ] = (merged['Low' ] * base_m2 / merged['M2']).round(2)
    merged['Close_1'] = (merged['Close'] * base_m2 / merged['M2']).round(2)

    # 저장 
    print(merged)
    merged.to_csv('./' + ixic_file + '.M2.csv', sep=',', na_rep='NaN', float_format='%.2f', index=False)



if __name__ == "__main__":
    gen_flat_m2('IXIC.csv', 'M2.csv')
    gen_flat_m2('GSPC.csv', 'M2.csv')
    gen_flat_m2('RUT.csv', 'M2.csv')