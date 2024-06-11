import streamlit as st

with st.form("Adoption Application"):
    st.header("Adoption Application Form")
    
    st.subheader("Personal Information")
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0, max_value=120)
    address = st.text_area("Address")
    email = st.text_input("Email")
    phone = st.text_input("Phone")
    
    st.subheader("Adoption Preferences")
    experience = st.checkbox("Do you have experience with cats?")
    indoor = st.checkbox("Will the cat be kept indoors?")
    other_pets = st.selectbox("Do you have other pets?",
                              ["Yes", "No"], placeholder="Select an option")
    other_pets_ = st.multiselect("What other pets do you have?",
                                 ["Dog", "Cat", "Bird", "Fish", "Other"], placeholder="Select all that apply")
    health = st.selectbox("Are you willing to provide regular veterinary care?",
                          ["Yes", "No", "Not sure"], placeholder="Select an option")
    vet = st.selectbox("Do you have a veterinarian?",
                       ["Yes", "No"], placeholder="Select an option")
        
    
    st.subheader("Additional Information")
    additional_info = st.text_area("Please provide any additional information or comments")
    
    submit_button = st.form_submit_button("Submit Application")
    
    if submit_button:
        # Process the application and save the data
        # You can add your own code here to handle the form submission
        st.success("Application submitted successfully!")