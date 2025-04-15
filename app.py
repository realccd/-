import streamlit as st
import pandas as pd
import numpy as np

def calculate_monthly_savings(income, fixed_expenses, variable_expenses):
    return income - fixed_expenses - variable_expenses

def calculate_emergency_fund(monthly_expenses):
    return monthly_expenses * 6

def calculate_debt_to_income_ratio(monthly_debt_payments, monthly_income):
    return (monthly_debt_payments / monthly_income) * 100

def calculate_net_worth(assets, liabilities):
    return assets - liabilities

def generate_financial_advice(income, fixed_expenses, variable_expenses, assets, liabilities, goals):
    monthly_savings = calculate_monthly_savings(income, fixed_expenses, variable_expenses)
    monthly_expenses = fixed_expenses + variable_expenses
    emergency_fund = calculate_emergency_fund(monthly_expenses)
    net_worth = calculate_net_worth(assets, liabilities)
    
    advice = []
    
    # 緊急預備金建議
    if assets < emergency_fund:
        advice.append(f"⚠️ 您的緊急預備金不足。建議至少準備 {emergency_fund:,.0f} 元（6個月支出）的緊急預備金。")
    else:
        advice.append("✅ 您的緊急預備金充足，這很好！")
    
    # 儲蓄率建議
    savings_rate = (monthly_savings / income) * 100
    if savings_rate < 20:
        advice.append(f"⚠️ 您的月儲蓄率為 {savings_rate:.1f}%，建議至少達到 20% 以上。")
    else:
        advice.append(f"✅ 您的月儲蓄率為 {savings_rate:.1f}%，表現很好！")
    
    # 淨資產建議
    if net_worth < 0:
        advice.append("⚠️ 您的淨資產為負數，建議優先處理債務問題。")
    else:
        advice.append(f"✅ 您的淨資產為 {net_worth:,.0f} 元，繼續保持！")
    
    # 理財目標建議
    if "退休" in goals:
        advice.append("💡 針對退休規劃，建議：\n- 每月至少投資收入的 15%\n- 考慮開立退休金帳戶\n- 分散投資組合")
    if "買房" in goals:
        advice.append("💡 針對購屋規劃，建議：\n- 準備至少 20% 的首付款\n- 確保月供不超過月收入的 30%\n- 考慮額外的裝修和家具預算")
    
    return "\n\n".join(advice)

st.title("💰 個人理財規劃助手")

st.write("請輸入您的財務資訊，我們將為您提供專業的理財建議。")

# 輸入表單
with st.form("financial_info"):
    income = st.number_input("月收入（元）", min_value=0, step=1000)
    fixed_expenses = st.number_input("固定支出（元）", min_value=0, step=1000)
    variable_expenses = st.number_input("變動支出（元）", min_value=0, step=1000)
    assets = st.number_input("總資產（元）", min_value=0, step=10000)
    liabilities = st.number_input("總負債（元）", min_value=0, step=10000)
    
    goals = st.multiselect(
        "理財目標",
        ["退休", "買房", "子女教育", "創業", "旅遊", "其他"],
        default=[]
    )
    
    submitted = st.form_submit_button("獲取理財建議")

if submitted:
    if income == 0:
        st.error("請輸入有效的月收入！")
    else:
        advice = generate_financial_advice(
            income, fixed_expenses, variable_expenses,
            assets, liabilities, goals
        )
        st.success("以下是您的個人化理財建議：")
        st.write(advice)
        
        # 顯示財務摘要
        st.subheader("📊 財務摘要")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("月儲蓄", f"{calculate_monthly_savings(income, fixed_expenses, variable_expenses):,.0f} 元")
            st.metric("月儲蓄率", f"{(calculate_monthly_savings(income, fixed_expenses, variable_expenses) / income * 100):.1f}%")
        with col2:
            st.metric("淨資產", f"{calculate_net_worth(assets, liabilities):,.0f} 元")
            st.metric("建議緊急預備金", f"{calculate_emergency_fund(fixed_expenses + variable_expenses):,.0f} 元") 