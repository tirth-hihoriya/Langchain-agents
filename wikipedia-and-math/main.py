import langchain_helper as lch
import streamlit as st

st.title('Pet Name Generator')
animal_type = st.sidebar.selectbox('Select the type of animal you have', ['cat', 'dog', 'bird', 'fish'])

if animal_type == 'cat':
    petcolor = st.sidebar.text_area('Enter the color of your cat?', max_chars=15)
elif animal_type == 'dog':
    petcolor = st.sidebar.text_area('Enter the color of your dog?', max_chars=15)
elif animal_type == 'bird':
    petcolor = st.sidebar.text_area('Enter the color of your bird?', max_chars=15)
else:
    petcolor = st.sidebar.text_area('Enter the color of your fish?', max_chars=15)

if st.sidebar.button('Generate'):
    pet_name = lch.generate_pet_name(animal_type, petcolor)
    st.write(f'Here are some cool names for your pet: {pet_name["pet_name"]}')


# st.title('Pet Name Generator')
# animal_type = st.text_input('Enter the type of animal you have')
# petcolor = st.text_input('Enter the color of your pet')
# if st.button('Generate'):
#     pet_name = lch.generate_pet_name(animal_type, petcolor)
#     st.write(f'Here are some cool names for your pet: {pet_name}')
