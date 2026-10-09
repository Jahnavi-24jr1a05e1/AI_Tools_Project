import streamlit as st
import requests

st.set_page_config(
    page_title="Jahnavi Currency Converter",
    page_icon="💱",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #eef2ff, #fdf2f8);
}

.title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: #4B0082;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #555;
    margin-bottom: 30px;
}

.card {
    background: white;
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0px 5px 20px rgba(0,0,0,0.1);
}

.result {
    padding: 30px;
    border-radius: 20px;
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white;
    text-align: center;
    margin-top: 30px;
    box-shadow: 0px 5px 20px rgba(0,0,0,0.2);
}

.result h1 {
    font-size: 32px;
}

.stButton > button {
    width: 100%;
    height: 50px;
    border-radius: 12px;
    font-size: 18px;
    font-weight: bold;
    background: linear-gradient(90deg, #667eea, #764ba2);
    color: white;
    border: none;
}

.footer {
    text-align: center;
    margin-top: 35px;
    color: #666;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="title">💱 Jahnavi Currency Converter</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Convert currencies quickly using live exchange rates 🌍</div>',
    unsafe_allow_html=True
)

currencies = {
    "🇮🇳 INR - Indian Rupee": "INR",
    "🇺🇸 USD - US Dollar": "USD",
    "🇪🇺 EUR - Euro": "EUR",
    "🇬🇧 GBP - British Pound": "GBP",
    "🇯🇵 JPY - Japanese Yen": "JPY",
    "🇦🇺 AUD - Australian Dollar": "AUD",
    "🇨🇦 CAD - Canadian Dollar": "CAD",
    "🇸🇬 SGD - Singapore Dollar": "SGD",
    "🇦🇪 AED - UAE Dirham": "AED",
    "🇨🇭 CHF - Swiss Franc": "CHF",
    "🇨🇳 CNY - Chinese Yuan": "CNY",
    "🇰🇷 KRW - South Korean Won": "KRW"
}

st.markdown('<div class="card">', unsafe_allow_html=True)

amount = st.number_input(
    "💰 Enter Amount",
    min_value=0.01,
    value=100.0,
    step=1.0
)

col1, col2 = st.columns(2)

with col1:
    from_currency = st.selectbox(
        "🌍 From Currency",
        list(currencies.keys())
    )

with col2:
    to_currency = st.selectbox(
        "🎯 To Currency",
        list(currencies.keys()),
        index=1
    )

st.markdown('</div>', unsafe_allow_html=True)

st.write("")

if st.button("🔄 Convert Currency"):

    from_code = currencies[from_currency]
    to_code = currencies[to_currency]

    if from_code == to_code:
        result = amount

        st.markdown(
            f"""
            <div class="result">
                <h2>💱 Conversion Result</h2>
                <h1>{amount:,.2f} {from_code}</h1>
                <h2>⬇️</h2>
                <h1>{result:,.2f} {to_code}</h1>
            </div>
            """,
            unsafe_allow_html=True
        )

    else:
        url = (
            f"https://api.frankfurter.app/latest"
            f"?amount={amount}"
            f"&from={from_code}"
            f"&to={to_code}"
        )

        try:
            response = requests.get(url, timeout=10)

            if response.status_code == 200:

                data = response.json()

                if "rates" in data and to_code in data["rates"]:

                    result = data["rates"][to_code]

                    rate = result / amount

                    st.markdown(
                        f"""
                        <div class="result">
                            <h2>💱 Conversion Result</h2>
                            <h1>{amount:,.2f} {from_code}</h1>
                            <h2>⬇️</h2>
                            <h1>{result:,.2f} {to_code}</h1>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                    st.success(
                        f"📊 Exchange Rate: 1 {from_code} = "
                        f"{rate:.4f} {to_code}"
                    )

                else:
                    st.error("⚠️ Exchange rate not available.")

            else:
                st.error("⚠️ Unable to fetch exchange rates.")

        except requests.exceptions.RequestException:
            st.error(
                "❌ Internet connection problem. "
                "Please check your connection and try again."
            )

st.markdown(
    """
    <div class="footer">
        💜 Created by Jahnavi | Currency Converter using Streamlit
    </div>
    """,
    unsafe_allow_html=True
)