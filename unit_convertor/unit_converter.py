import streamlit as st
import pandas as pd
from datetime import datetime

def apply_custom_css():
    st.markdown("""
        <style>
        .main {
            padding: 2rem;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            padding: 0.5rem 1rem;
            border-radius: 10px;
            border: none;
            box-shadow: 0 2px 5px rgba(0,0,0,0.2);
            transition: all 0.3s;
        }
        .stButton>button:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }
        .unit-card {
            background-color: #f8f9fa;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            margin-bottom: 20px;
        }
        h1 {
            color: #1e88e5;
            text-align: center;
            margin-bottom: 2rem;
        }
        .stSelectbox {
            margin-bottom: 1rem;
        }
        </style>
    """, unsafe_allow_html=True)

def length_conversion(value, from_unit, to_unit):
    # Length conversion factors to meters
    length_units = {
        'Meter': 1,
        'Kilometer': 1000,
        'Centimeter': 0.01,
        'Millimeter': 0.001,
        'Mile': 1609.34,
        'Foot': 0.3048,
        'Inch': 0.0254,
        'Yard': 0.9144,
        'Nautical Mile': 1852
    }
    
    # Convert to meters first, then to target unit
    meters = value * length_units[from_unit]
    return meters / length_units[to_unit]

def weight_conversion(value, from_unit, to_unit):
    # Weight conversion factors to kilograms
    weight_units = {
        'Kilogram': 1,
        'Gram': 0.001,
        'Pound': 0.453592,
        'Ounce': 0.0283495,
        'Metric Ton': 1000,
        'Stone': 6.35029
    }
    
    kilos = value * weight_units[from_unit]
    return kilos / weight_units[to_unit]

def temperature_conversion(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == 'Celsius':
        if to_unit == 'Fahrenheit':
            return (value * 9/5) + 32
        elif to_unit == 'Kelvin':
            return value + 273.15
    elif from_unit == 'Fahrenheit':
        if to_unit == 'Celsius':
            return (value - 32) * 5/9
        elif to_unit == 'Kelvin':
            return (value - 32) * 5/9 + 273.15
    elif from_unit == 'Kelvin':
        if to_unit == 'Celsius':
            return value - 273.15
        elif to_unit == 'Fahrenheit':
            return (value - 273.15) * 9/5 + 32
    return value

def digital_conversion(value, from_unit, to_unit):
    digital_units = {
        'Byte': 1,
        'Kilobyte': 1024,
        'Megabyte': 1024**2,
        'Gigabyte': 1024**3,
        'Terabyte': 1024**4
    }
    bytes_val = value * digital_units[from_unit]
    return bytes_val / digital_units[to_unit]

def main():
    st.set_page_config(
        page_title="Unit Converter",
        page_icon="🔄",
        layout="wide"
    )
    
    apply_custom_css()
    
    st.title('🔄 Unit Converter')
    
    # Create columns for better layout
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("### 📊 Conversion Type")
        conversion_type = st.selectbox(
            'Select what you want to convert',
            ['Length', 'Weight', 'Temperature', 'Digital Storage']
        )
        
        value = st.number_input('Enter Value', value=0.0, format="%.6f")
        
    with col2:
        st.markdown("### 🔄 Units")
        if conversion_type == 'Length':
            units = ['Meter', 'Kilometer', 'Centimeter', 'Millimeter', 'Mile', 'Foot', 'Inch', 'Yard', 'Nautical Mile']
            convert_func = length_conversion
        elif conversion_type == 'Weight':
            units = ['Kilogram', 'Gram', 'Pound', 'Ounce', 'Metric Ton', 'Stone']
            convert_func = weight_conversion
        elif conversion_type == 'Temperature':
            units = ['Celsius', 'Fahrenheit', 'Kelvin']
            convert_func = temperature_conversion
        else:
            units = ['Byte', 'Kilobyte', 'Megabyte', 'Gigabyte', 'Terabyte']
            convert_func = digital_conversion

        col2_1, col2_2 = st.columns(2)
        with col2_1:
            from_unit = st.selectbox('From Unit', units)
        with col2_2:
            to_unit = st.selectbox('To Unit', units)

    # Convert button
    if st.button('Convert', key='convert'):
        result = convert_func(value, from_unit, to_unit)
        
        # Create a nice result card
        st.markdown("""
            <div class="unit-card">
                <h3 style="color: #1e88e5; text-align: center;">Result</h3>
                <h2 style="text-align: center; color: #4CAF50;">
                    {:.4f} {} = {:.4f} {}
                </h2>
            </div>
        """.format(value, from_unit, result, to_unit), unsafe_allow_html=True)
        
        # Add to history
        if 'conversion_history' not in st.session_state:
            st.session_state.conversion_history = []
            
        st.session_state.conversion_history.append({
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'from_value': value,
            'from_unit': from_unit,
            'to_value': result,
            'to_unit': to_unit,
            'type': conversion_type
        })

    # Show conversion history
    if st.checkbox('Show Conversion History'):
        if 'conversion_history' in st.session_state and st.session_state.conversion_history:
            history_df = pd.DataFrame(st.session_state.conversion_history)
            st.markdown("### 📜 Conversion History")
            st.dataframe(history_df, use_container_width=True)
            
            if st.button('Clear History'):
                st.session_state.conversion_history = []
                st.experimental_rerun()

if __name__ == '__main__':
    main()
