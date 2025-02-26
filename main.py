import openai
import streamlit as st

# Function to perform the unit conversion
def convert_units(value, from_unit, to_unit):
    conversion_dict = {
        'Length': {
            'meters': 1, 'kilometers': 0.001, 'centimeters': 100, 'millimeters': 1000, 'miles': 0.000621371
        },
        'Weight': {
            'kilograms': 1, 'grams': 1000, 'milligrams': 1000000, 'pounds': 2.20462, 'ounces': 35.274
        }
    }

    if from_unit in conversion_dict['Length']:
        conversion_type = 'Length'
    elif from_unit in conversion_dict['Weight']:
        conversion_type = 'Weight'
    else:
        return "Invalid unit"

    if conversion_type == 'Length' or conversion_type == 'Weight':
        result = value * conversion_dict[conversion_type][to_unit] / conversion_dict[conversion_type][from_unit]
        return result

# Create the Streamlit app
def app():
    # Set page configuration for the app
    st.set_page_config(page_title="Unit Converter", )

    # Title and description
    st.title('Unit Converter')
    st.write('This app allows you to convert between different units of measurement.')

    # Choose category of conversion
    conversion_type = st.selectbox('Choose conversion category', ['Length', 'Weight'])

    if conversion_type == 'Length':
        units = ['meters', 'kilometers', 'centimeters', 'millimeters', 'miles']
    elif conversion_type == 'Weight':
        units = ['kilograms', 'grams', 'milligrams', 'pounds', 'ounces']
    
    # Select from and to units
    from_unit = st.selectbox('From unit', units)
    to_unit = st.selectbox('To unit', units)

    # Input value to convert
    value = st.number_input('Enter the value to convert', value=0)

    # Convert button
    if st.button('Convert'):
        # Perform the conversion
        result = convert_units(value, from_unit, to_unit)
        
        # Display the result
        if result:
            st.write(f'{value} {from_unit} is equal to {result:.2f} {to_unit}')
        else:
            st.error("Invalid conversion. Please check the units or the value entered.")

if __name__ == '__main__':
    app()
