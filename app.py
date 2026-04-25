import streamlit as st
from PIL import Image
from api_calling import hint_generator
from api_calling import solution_generator

from google.genai import errors


# ------------------------- Title -----------------------
st.title("AI Code Debugger App", anchor=False)
st.markdown("Upload the images of your code")
st.divider()


# ------------------------- Working with sidebar -------------
with st.sidebar:
    st.header("Controls", anchor=False)
    

    # ------------------ file uploader ----------------
    images = st.file_uploader("Upload the photos :red[(at max 3)] of your code",
                     type=['jpg', 'jpeg', 'png'],
                     accept_multiple_files=True)
    
    
    pil_images = []

    for img in images:
        pil_img = Image.open(img)
        pil_images.append(pil_img)

    if images:
        if len(images)>3:
            st.error("Upload at max 3 images")
        else:
            st.success("Successfully uploaded")
        
        cols = st.columns(len(images))
        for i,img in enumerate(images):
            with cols[i]:
                st.image(img)
                
    # ------------- Solving method -> hint/solution -----------
    method = st.selectbox("What do you want from the AI",
                          ("Hint", "Solve"),
                          index=None)
    
    # ---------------- Button ----------------
    pressed = st.button("Initiate", type="primary")
    


    
# ------------- Main body ----------------
if pressed:
        if not images:
            st.error("Image is required")
        if not method:
            st.error("Select Hint/Solve")
        
        if images and method:
            with st.container(border=True):
                st.subheader(f"Here is your {method}", anchor=False)
                with st.spinner("Initializing..."):
                    try:
                        if method=="Hint":
                            hints = hint_generator(pil_images)
                            st.markdown(hints)
                        else:
                            solution = solution_generator(pil_images)
                            st.markdown(solution)
                    except errors.ServerError:
                        st.error("The server is busy right now. Please wait a moment and try again later.")
                    except Exception as e:
                        st.error(f"An unexpected error occurred: {e}")
                        