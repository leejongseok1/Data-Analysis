from scipy import stats

# 데이터
design_A = [16.4, 12.6, 17.5, 18.8, 12.1, 13.2, 14.5, 12.4, 17.5, 25.4, 9.3, 10.4]
design_B = [12.1, 11.8, 14.7, 13.1, 13.8, 10.1, 9.1, 13.5, 11.2, 13.7]

# 검정 코드
stats.ttest_ind(design_A,
                design_B,
                equal_var=False)