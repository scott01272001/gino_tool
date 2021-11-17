import pandas as pd
from pandas.core.frame import DataFrame

class VoReport:

    # 營業費用
    operating_expenses: DataFrame
    eps: DataFrame

    # 稅率
    pre_tax_income: DataFrame
    tax: DataFrame
    tax_rate: float

    # 業外收入
    total_non_operating: DataFrame

    # 毛利率
    gross_profit: DataFrame
    revenue: DataFrame
    gross_margin: float

    # 月營收
    month_revenue: DataFrame

    # 稅後淨利
    income_after_taxes: DataFrame

    
