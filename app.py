import streamlit as st

def calculate_monthly_savings(income, fixed_expenses, variable_expenses):
    return income - fixed_expenses - variable_expenses

def calculate_emergency_fund(monthly_expenses):
    return monthly_expenses * 6

def calculate_net_worth(assets, liabilities):
    return assets - liabilities

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
        monthly_savings = calculate_monthly_savings(income, fixed_expenses, variable_expenses)
        monthly_expenses = fixed_expenses + variable_expenses
        emergency_fund = calculate_emergency_fund(monthly_expenses)
        net_worth = calculate_net_worth(assets, liabilities)
        
        st.success("以下是您的個人化理財建議：")
        
        # 緊急預備金建議
        if assets < emergency_fund:
            st.write(f"⚠️ 您的緊急預備金不足。建議至少準備 {emergency_fund:,.0f} 元（6個月支出）的緊急預備金。")
        else:
            st.write("✅ 您的緊急預備金充足，這很好！")
        
        # 儲蓄率建議
        savings_rate = (monthly_savings / income) * 100
        if savings_rate < 20:
            st.write(f"⚠️ 您的月儲蓄率為 {savings_rate:.1f}%，建議至少達到 20% 以上。")
        else:
            st.write(f"✅ 您的月儲蓄率為 {savings_rate:.1f}%，表現很好！")
        
        # 淨資產建議
        if net_worth < 0:
            st.write("⚠️ 您的淨資產為負數，建議優先處理債務問題。")
        else:
            st.write(f"✅ 您的淨資產為 {net_worth:,.0f} 元，繼續保持！")
        
        # 顯示財務摘要
        st.subheader("📊 財務摘要")
        st.write(f"月儲蓄：{monthly_savings:,.0f} 元")
        st.write(f"月儲蓄率：{savings_rate:.1f}%")
        st.write(f"淨資產：{net_worth:,.0f} 元")
        st.write(f"建議緊急預備金：{emergency_fund:,.0f} 元") 