from citation_map import generate_citation_map
import streamlit as st
import streamlit.components.v1 as components

if __name__ == '__main__':
    st.title("Dash Board")
    User_id=st.text_input("Enter user id","5ZYwOkIAAAAJ")
    button = st.button("Click me")
    button_clear = st.button("Clear")
    if button:

    # This is my Google Scholar ID. Replace this with your ID.
        scholar_id = User_id
        generate_citation_map(scholar_id, output_path='citation_map.html',
                            cache_folder='cache', affiliation_conservative=False, num_processes=16,
                            use_proxy=False, pin_colorful=True, print_citing_affiliations=True)
        
        
        st.success("success")
        # with open("citation_map.html", 'r') as html_file:
        #     html_content = html_file.read()
        with open('citation_map.html', 'r', encoding='utf-8') as file:
            html_content = file.read()


# Display the HTML content in the Streamlit app
        st.title("Citaion Map")
        components.html(html_content, height=600)

# from citation_map import generate_citation_map
# import streamlit as st
# import streamlit.components.v1 as components
# import os


# def add_custom_css():
#     custom_css = """
#     <style>
#         .title {
#             color: #2E86C1;
#             font-size: 36px;
#             font-weight: bold;
#         }
#         .input-box {
#             border: 2px solid #2E86C1;
#             border-radius: 10px;
#             padding: 10px;
#             width: 50%;
#         }
#         .ef3psqc16 {
#             background-color: #28B463;
#             color: white;
#             border-radius: 10px;
#             position : relative;
#         }

#         .stButton>button:hover {
#             background-color: #239B56;
#         }
#         .citation-map {
#             border: 2px solid #A569BD;
#             padding: 10px;
#             border-radius: 10px;
#         }
#     </style>
#     """
#     st.markdown(custom_css, unsafe_allow_html=True)

# if __name__ == '__main__':
 
#     add_custom_css()

#     st.markdown("<div class='title'>Dash Board</div>", unsafe_allow_html=True)
    
#     User_id = st.text_input("Enter Google Scholar ID ", "5ZYwOkIAAAAJ", key='user_id', help="Google Scholar ID")

   
#     button = st.button("Click me")
#     button_clear = st.button("Clear")

#     if button:
       
#         scholar_id = User_id
        
      
#         generate_citation_map(
#             scholar_id,
#             output_path='citation_map.html',
#             cache_folder='cache',
#             affiliation_conservative=False,
#             num_processes=16,
#             use_proxy=False,
#             pin_colorful=True,
#             print_citing_affiliations=True
#         )
        
#         st.success("Citation map generated successfully!")

       
#         with open("citation_map.html", 'r') as html_file:
#             html_content = html_file.read()

        
#         st.markdown("<div class='citation-map'>Citaion Map</div>", unsafe_allow_html=True)
#         components.html(html_content, height=600)

  
#     if button_clear:
#         st.session_state.user_id = "" 
