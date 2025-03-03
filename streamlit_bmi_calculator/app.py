import streamlit as st

def calculate_bmi(weight, height):
    return weight / (height * height)

def get_bmi_status(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    st.title("BMI Calculator")
    
    st.write("Enter your details to calculate BMI:")
    
    weight = st.number_input("Weight (kg)", min_value=1.0, max_value=300.0, value=70.0)
    height = st.number_input("Height (meters)", min_value=0.1, max_value=3.0, value=1.7)
    
    if st.button("Calculate BMI"):
        bmi = calculate_bmi(weight, height)
        status = get_bmi_status(bmi)
        
        st.write(f"Your BMI is: {bmi:.2f}")
        st.write(f"Status: {status}")
        
        # Add color-coded status
        if status == "Underweight":
            st.warning(f"You are {status}")
        elif status == "Normal weight":
            st.success(f"You are at a {status}")
        else:
            st.error(f"You are {status}")

if __name__ == "__main__":
    main() 