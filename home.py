import streamlit as st

# Set page config
st.set_page_config(
    page_title="Cat Adoption",
    page_icon="🐱",
    layout="centered",
    initial_sidebar_state="collapsed",
)

tabs_ = ["Home", "Bernard", "Bunny", "Helen", "Plumeria", "Remy", "Wolfie" ]


home, bernard, bunny, helen, plumeria, remy, wolfie = st.tabs(tabs_)

with home:
    st.title("Welcome to Cat Adoption!")
    st.markdown("""
    Are you ready to bring a furry friend into your home? Look no further! We have a wide selection of adorable cats just waiting to be adopted. Whether you're a first-time cat owner or a seasoned pro, we have the perfect companion for you.
    """)

    st.header("Why Adopt a Cat?")
    st.markdown("""
    Adopting a cat is a wonderful way to add joy and companionship to your life. Here are a few reasons why you should consider adopting:
    - Cats make great companions and provide unconditional love.
    - Adopting a cat helps reduce the number of stray and homeless cats.
    - Cats are low-maintenance pets and can fit into any lifestyle.
    - By adopting, you're giving a deserving cat a second chance at a happy life.
    """)

    st.header("How to Adopt")
    st.markdown("""
    Adopting a cat is a simple process. Just follow these steps:
    1. Browse our available cats and find one that steals your heart.
    2. Fill out our adoption application form.
    3. Once your application is approved, schedule a meet and greet with the cat.
    4. If the meet and greet goes well, complete the adoption paperwork and pay the adoption fee.
    5. Take your new furry friend home and enjoy a lifetime of love and happiness!
    """)

    st.header("Contact Us")
    st.markdown("""
    If you have any questions or need assistance, please don't hesitate to reach out to us. We're here to help!
    - Phone: (816)213-2030
    - Email: dawkins.cameron@gmail.com
    """)
    
    with bernard:
        st.header("Bernard")
        st.markdown("""
                    Bernard is a loving, black male kitten with white sprinkles on his back and legs. He is a playful and affectionate kitten who loves to cuddle and play with his toys. Bernard is looking for a forever home where he can be the center of attention and receive lots of love and affection. If you're looking for a sweet and loving companion, Bernard is the perfect cat for you!
                    """)
        pic1, pic2 = st.tabs(["Picture 1", "Picture 2"])
    with bunny:
        st.header("Bunny")
        st.markdown("""
                    Bunny is a beautiful, black and white female tuexedo kittne with bright green eyes. She is an energetic, playful, and sweet kitten. Bunny is looking for a loving home where she can relax, play, and enjoy the company of her humans and other fellow four-legged compantions. If you're looking for an expressive and loving companion, Bunny is the perfect cat for you!
                    """)
        pic1, pic2 = st.tabs(["Picture 1", "Picture 2"])
    with helen:
        st.header("Helen")
        st.markdown("""
                    Helen is a love-y dove-y, black female kitten with the sweetest sounding purr you've ever heard. She likes to stay by your feet and follow you around the house. She loves toys, but plays with them ever so gently and has eyes that you can't help but fall in love with. Helen is looking for a home where she can be loved and cherished for the rest of her days. If you're looking for a sweet and loving companion, Helen is the perfect cat for you!
                    """)
        pic1, pic2 = st.tabs(["Picture 1", "Picture 2"])
    with plumeria:
        st.header("Plumeria")
        st.markdown("""
                    Plumeria is sweet, gentle, and affectionate female kitten. She enjoys being held and will practically melt in your arms. She can be high-energy and loves to play with toys, but she also enjoys lounging around and watching the world go by. Plumeria is looking for a forever home where she can be the center of attention and receive lots of love and affection. If you're looking for a sweet and loving companion, Plumeria is the perfect cat for you!
                    """)
        pic1, pic2 = st.tabs(["Picture 1", "Picture 2"])
    with remy:
        st.header("Remy")
        st.markdown("""
                    Remy is a sweet, black --with sprinkle of white furs-- male kitten with a playful and affectionate personality. He loves to play with toys and chase after anything that moves. Remy is looking for a loving home where he can be the center of attention and receive lots of love and affection. If you're looking for a playful and loving companion, Remy is the perfect cat for you!
                    """)
        pic1, pic2 = st.tabs(["Picture 1", "Picture 2"])
    with wolfie:
        st.header("Wolfie")
        st.markdown("""
                    Wolfie is a loving, sweet, and playful female companion. She has a beautiful coat of black fur with white sprinkles on her back and legs. Wolfie is a playful and affectionate kitten who loves to cuddle and play with her toys. Wolfie is looking for a forever home where she can be the center of attention and receive lots of love and affection. If you're looking for a sweet and loving companion, Wolfie is the perfect cat for you!
                    """)
        pic1, pic2 = st.tabs(["Picture 1", "Picture 2"])