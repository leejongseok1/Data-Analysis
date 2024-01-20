import pandas as pd
from scipy.stats import chi2_contingency # 카이제곱


def click_abtest(a_click, total_a, b_click, total_b):

    click = [a_click, b_click] # A와 B의 클릭한 유저 수
    no_click = [total_a - a_click, total_b - b_click]  # A와 B의 클릭 안 한 유저 수
    cont_table = pd.DataFrame([click, no_click], columns=['A', 'B'], index=['click', 'no_click'])
    chi2, p_val, d_f, expected = chi2_contingency([click, no_click])

    print("카이제곱 통계량 :", format(chi2, '.5f'))
    print("pvalue :", format(p_val, '.5f'))

# A의 클릭수(13)와 A의 데이터 전체 개수(244)
# B의 클릭수(23)와 A의 데이터 전체 개수(287)를 정의한 클래스에 넣어줌
click_abtest(13, 244, 23, 287)