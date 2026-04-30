import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

# ─────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────
st.set_page_config(
    page_title="Mama Tee's Provisions — Dashboard",
    page_icon="🛒",
    layout="wide"
)

# ─────────────────────────────────────────
# STYLING
# ─────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=DM+Sans:wght@300;400;500&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    background-color: #faf7f2;
    color: #1a1a1a;
}
.stApp { background-color: #faf7f2; }

.header {
    background: linear-gradient(135deg, #1a1a1a, #2d2d2d);
    padding: 2.5rem 3rem;
    border-radius: 16px;
    margin-bottom: 2rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.header h1 {
    font-family: 'Playfair Display', serif;
    font-size: 2.2rem;
    color: #f5c842;
    margin: 0;
}
.header p {
    color: #888;
    font-size: 0.85rem;
    margin: 0.3rem 0 0 0;
    font-family: 'DM Sans', sans-serif;
}

.metric-card {
    background: white;
    border-radius: 12px;
    padding: 1.5rem;
    border-left: 4px solid #f5c842;
    box-shadow: 0 2px 12px rgba(0,0,0,0.06);
    height: 100%;
}
.metric-label {
    font-size: 0.75rem;
    color: #888;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    margin-bottom: 0.5rem;
}
.metric-value {
    font-family: 'Playfair Display', serif;
    font-size: 1.6rem;
    font-weight: 700;
    color: #1a1a1a;
}

.section-title {
    font-family: 'Playfair Display', serif;
    font-size: 1.3rem;
    color: #1a1a1a;
    margin: 2rem 0 1rem 0;
    padding-bottom: 0.5rem;
    border-bottom: 2px solid #f5c842;
}

.insight-card {
    background: white;
    border-radius: 12px;
    padding: 1.5rem;
    box-shadow: 0 2px 12px rgba(0,0,0,0.06);
    margin-bottom: 1rem;
}
.insight-card h4 {
    font-family: 'Playfair Display', serif;
    color: #1a1a1a;
    margin: 0 0 0.8rem 0;
}
.insight-item {
    font-size: 0.88rem;
    color: #444;
    padding: 0.4rem 0;
    border-bottom: 1px solid #f5f5f5;
    line-height: 1.6;
}

.rec-card {
    background: #1a1a1a;
    border-radius: 12px;
    padding: 1.5rem;
    color: white;
}
.rec-card h4 {
    font-family: 'Playfair Display', serif;
    color: #f5c842;
    margin: 0 0 1rem 0;
}
.rec-item {
    font-size: 0.88rem;
    color: #ccc;
    padding: 0.4rem 0;
    border-bottom: 1px solid #333;
    line-height: 1.6;
}

.note-card {
    background: #fff8e6;
    border: 1px solid #f5c842;
    border-radius: 8px;
    padding: 1rem 1.5rem;
    font-size: 0.83rem;
    color: #666;
    margin-top: 1rem;
}

.footer {
    text-align: center;
    font-size: 0.75rem;
    color: #aaa;
    margin-top: 3rem;
    padding-top: 1.5rem;
    border-top: 1px solid #eee;
    font-family: 'DM Sans', sans-serif;
}
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────
# LOAD DATA
# ─────────────────────────────────────────
@st.cache_data
def load_data():
    df = pd.read_csv('surulere_provision_store.csv')
    df['date'] = pd.to_datetime(df['date'])
    df['month_year'] = df['date'].dt.strftime('%B %Y')
    df['month'] = df['date'].dt.strftime('%B')
    df['year'] = df['date'].dt.year
    df['day_of_week'] = df['date'].dt.strftime('%A')
    return df

df = load_data()

# ─────────────────────────────────────────
# KEY METRICS
# ─────────────────────────────────────────
total_revenue = df['revenue'].sum()
best_month = df.groupby('month_year')['revenue'].sum().idxmax()
best_product = df.groupby('product')['revenue'].sum().idxmax()
total_products = df['product'].nunique()
total_transactions = len(df)

# ─────────────────────────────────────────
# HEADER
# ─────────────────────────────────────────
st.markdown("""
<div class="header">
    <div>
        <h1>🛒 TeeJay Provisions</h1>
        <p>Surulere, Lagos &nbsp;•&nbsp; Sales Dashboard &nbsp;•&nbsp; January 2023 — December 2024</p>
    </div>
    <div style="text-align:right;">
        <div style="color:#f5c842; font-size:0.75rem; letter-spacing:0.1em;">POWERED BY</div>
        <div style="color:white; font-family:'Playfair Display',serif; font-size:1.1rem;">NexusMind 🧠</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────
# KEY METRICS ROW
# ─────────────────────────────────────────
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">💰 Total Revenue</div>
        <div class="metric-value">₦{total_revenue:,.0f}</div>
    </div>""", unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">🏆 Best Month</div>
        <div class="metric-value">{best_month}</div>
    </div>""", unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">⭐ Best Product</div>
        <div class="metric-value">{best_product}</div>
    </div>""", unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">📦 Total Products</div>
        <div class="metric-value">{total_products}</div>
    </div>""", unsafe_allow_html=True)

# ─────────────────────────────────────────
# CHARTS
# ─────────────────────────────────────────
st.markdown('<div class="section-title">📈 Revenue Trends</div>', unsafe_allow_html=True)

# Monthly revenue — 2023 vs 2024
month_order = ['January','February','March','April','May','June',
               'July','August','September','October','November','December']

df_2023 = df[df['year'] == 2023].groupby('month')['revenue'].sum().reset_index()
df_2024 = df[df['year'] == 2024].groupby('month')['revenue'].sum().reset_index()

for d in [df_2023, df_2024]:
    d['month'] = pd.Categorical(d['month'], categories=month_order, ordered=True)

df_2023 = df_2023.sort_values('month')
df_2024 = df_2024.sort_values('month')

fig1, ax1 = plt.subplots(figsize=(14, 4))
fig1.patch.set_facecolor('#ffffff')
ax1.set_facecolor('#fafafa')
ax1.plot(df_2023['month'], df_2023['revenue'], marker='o', color='#1a1a1a', linewidth=2, label='2023')
ax1.plot(df_2024['month'], df_2024['revenue'], marker='o', color='#f5c842', linewidth=2, label='2024')
ax1.set_xlabel('Month', fontsize=10, labelpad=8)
ax1.set_ylabel('Revenue (₦)', fontsize=10, labelpad=8)
ax1.tick_params(axis='x', rotation=45, labelsize=8)
ax1.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, p: f'₦{x:,.0f}'))
ax1.legend()
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.grid(axis='y', alpha=0.3)
plt.tight_layout()
st.pyplot(fig1)
plt.close()

# Category and Top 10 side by side
col_a, col_b = st.columns(2)

with col_a:
    st.markdown('<div class="section-title">🏷️ Revenue by Category</div>', unsafe_allow_html=True)
    cat_rev = df.groupby('category')['revenue'].sum().reset_index()
    fig2, ax2 = plt.subplots(figsize=(6, 4))
    fig2.patch.set_facecolor('#ffffff')
    ax2.set_facecolor('#fafafa')
    bars = ax2.bar(cat_rev['category'], cat_rev['revenue'],
                   color=['#1a1a1a', '#f5c842', '#888'], width=0.5)
    for bar in bars:
        h = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., h,
                 f'₦{h:,.0f}', ha='center', va='bottom', fontsize=8, fontweight='bold')
    ax2.set_xlabel('Category', fontsize=9, labelpad=8)
    ax2.set_ylabel('Revenue (₦)', fontsize=9)
    ax2.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, p: f'₦{x:,.0f}'))
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    ax2.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    st.pyplot(fig2)
    plt.close()

with col_b:
    st.markdown('<div class="section-title">🥇 Top 10 Products</div>', unsafe_allow_html=True)
    prod_rev = df.groupby('product')['revenue'].sum().reset_index()
    top10 = prod_rev.sort_values('revenue', ascending=False).head(10)
    fig3, ax3 = plt.subplots(figsize=(6, 4))
    fig3.patch.set_facecolor('#ffffff')
    ax3.set_facecolor('#fafafa')
    ax3.barh(top10['product'], top10['revenue'], color='#1a1a1a')
    ax3.set_xlabel('Revenue (₦)', fontsize=9, labelpad=8)
    ax3.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, p: f'₦{x:,.0f}'))
    ax3.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, p: f'₦{x/1000000:.1f}M'))
    ax3.tick_params(axis='y', labelsize=8)
    ax3.spines['top'].set_visible(False)
    ax3.spines['right'].set_visible(False)
    ax3.grid(axis='x', alpha=0.3)
    plt.tight_layout()
    st.pyplot(fig3)
    plt.close()

# Bottom 5
st.markdown('<div class="section-title">⚠️ Lowest Performing Products</div>', unsafe_allow_html=True)
bottom5 = prod_rev.sort_values('revenue', ascending=True).head(5)
fig4, ax4 = plt.subplots(figsize=(14, 3))
fig4.patch.set_facecolor('#ffffff')
ax4.set_facecolor('#fafafa')
ax4.barh(bottom5['product'], bottom5['revenue'], color='#e74c3c')
ax4.set_xlabel('Revenue (₦)', fontsize=9, labelpad=8)
ax4.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, p: f'₦{x:,.0f}'))
ax4.tick_params(axis='y', labelsize=9)
ax4.spines['top'].set_visible(False)
ax4.spines['right'].set_visible(False)
ax4.grid(axis='x', alpha=0.3)
plt.tight_layout()
st.pyplot(fig4)
plt.close()

# ─────────────────────────────────────────
# INSIGHTS & RECOMMENDATIONS
# ─────────────────────────────────────────
st.markdown('<div class="section-title">💡 Insights & Recommendations</div>', unsafe_allow_html=True)

col_i, col_r = st.columns(2)

food_rev = df[df['category']=='Food']['revenue'].sum()
food_pct = (food_rev / total_revenue) * 100
rev_2023 = df[df['year']==2023]['revenue'].sum()
rev_2024 = df[df['year']==2024]['revenue'].sum()
growth = ((rev_2024 - rev_2023) / rev_2023) * 100
worst_product = bottom5.iloc[0]['product']

with col_i:
    st.markdown(f"""
    <div class="insight-card">
        <h4>📊 What the Data Says</h4>
        <div class="insight-item">🏆 <b>{best_product}</b> is your highest revenue product — stock it consistently</div>
        <div class="insight-item">🍎 Food drives <b>{food_pct:.0f}%</b> of total revenue — your most important category</div>
        <div class="insight-item">📅 <b>{best_month}</b> was your best month across 2 years</div>
        <div class="insight-item">📉 January is consistently your slowest month every year</div>
        <div class="insight-item">🎄 December always spikes — festive season and school resumption boost sales</div>
        <div class="insight-item">📈 Revenue {'grew' if growth > 0 else 'declined'} by <b>{abs(growth):.1f}%</b> from 2023 to 2024</div>
    </div>
    """, unsafe_allow_html=True)

with col_r:
    st.markdown(f"""
    <div class="rec-card">
        <h4>✅ Recommendations</h4>
        <div class="rec-item">📦 Always maintain high stock of <b>{best_product}</b> — especially in Q4</div>
        <div class="rec-item">🎯 Focus on Food category — it generates over half your revenue</div>
        <div class="rec-item">🔔 Prepare extra stock in <b>November</b> before the December rush</div>
        <div class="rec-item">💡 Run promotions or discounts in <b>January</b> to boost slow month sales</div>
        <div class="rec-item">⚠️ Review <b>{worst_product}</b> — lowest revenue product, consider reducing stock</div>
        <div class="rec-item">📊 Provide cost price data for a deeper profitability analysis</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="note-card">
    ⚠️ <b>Important Note:</b> This analysis is based on sales revenue only.
    To identify which products are truly profitable, kindly provide cost price per product
    for a complete profit and loss analysis.
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────
# FOOTER
# ─────────────────────────────────────────
st.markdown("""
<div class="footer">
    Prepared by Ajibola Akinbode &nbsp;•&nbsp; Data Analysis Report &nbsp;•&nbsp; NexusMind 🧠
</div>
""", unsafe_allow_html=True)