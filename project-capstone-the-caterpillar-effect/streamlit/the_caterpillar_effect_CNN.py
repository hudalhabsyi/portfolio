
#----------------------------------------------------------------------------------------------------------
#Importing Libraries
#----------------------------------------------------------------------------------------------------------


#libraries for data processing
import numpy as np
from PIL import Image

#libraries for loading model
from tensorflow.keras.models import load_model # to load model from saved file earlier
from tensorflow.keras.preprocessing import image # to do image processing in the required format for predictions

#libraries for chatbot application and streamlit
from openai import OpenAI
import time
import streamlit as st





# ----------------------------------------------------------------------------------------------------------
# Defining Open AI Assistant

# We are using the OpenAI Assistant API with Knowledge Retrieval function to run the chatbot. The uploaded
# files are used as a knowledge base for the Assistant to answer the questions posed in the prompt. The
# user also has the option to allow the chatbot to access its own base knowledge in the event it is unable
# to find relevant information in the files provided. 

# This chatbot is running on the gpt-3.5-turbo-0125 Assistant model.
# ----------------------------------------------------------------------------------------------------------


# Create an OpenAI client with your API key
client = OpenAI(api_key=st.secrets['OPEN_AI_KEY']['open_ai_key'])

assistant_id = 'asst_2Ll2geL6xFhcqysisEhsHOcP'

# Retrieve the assistant you want to use
assistant = client.beta.assistants.retrieve(assistant_id)

# Upload the files with an "assistants" purpose
pansy_file_1 = client.files.create(
    file=open("../documents/chocolate_pansy/Chocolate_Pansy_Butterflies of Singapore_ Life History of the Chocolate Pansy.html", "rb"),
    purpose='assistants'
)
pansy_file_2 = client.files.create(
    file=open("../documents/chocolate_pansy/Chocolate_Pansy_Nepal_Desk.html", "rb"),
    purpose='assistants'
)
pansy_file_3 = client.files.create(
    file=open("../documents/chocolate_pansy/Chocolate_Pansy_Junonia_iphita_Wikipedia.html", "rb"),
    purpose='assistants'
)

lime_file_1 = client.files.create(
    file=open("../documents/lime_caterpillar/2Lime_Butterfly_Butterflies of Singapore_ Life History of the Lime Butterfly v2.0.html", "rb"),
    purpose='assistants'
)
lime_file_2 = client.files.create(
    file=open("../documents/lime_caterpillar/Lime_Butterfly_Butterflies of Singapore_ Life History of the Lime Butterfly v2.0.html", "rb"),
    purpose='assistants'
)
lime_file_3 = client.files.create(
    file=open("../documents/lime_caterpillar/Papilio demoleus - Wikipedia.html", "rb"),
    purpose='assistants'
)

pj_file_1 = client.files.create(
    file=open("../documents/painted_jezebel/Painted_Jezebel_Butterflies of Singapore_ Butterfly of the Month - December 2010.html", "rb"),
    purpose='assistants'
)
pj_file_2 = client.files.create(
    file=open("../documents/painted_jezebel/Delias hyparete - Wikipedia.html", "rb"),
    purpose='assistants'
)

tiger_file_1 = client.files.create(
    file=open("../documents/plain_tiger/Plain_Tiger_Butterflies of Singapore_ Butterfly of the Month - October 2016.html", "rb"),
    purpose='assistants'
)
tiger_file_2 = client.files.create(
    file=open("../documents/plain_tiger/Danaus chrysippus - Wikipedia.html", "rb"),
    purpose='assistants'
)

#define list of file IDs
uploaded_file_ids = [pansy_file_1.id, pansy_file_2.id, pansy_file_3.id, lime_file_1.id, lime_file_2.id, lime_file_3.id, pj_file_1.id, pj_file_2.id, tiger_file_1.id, tiger_file_2.id]





# ----------------------------------------------------------------------------------------------------------
# Creating Streamlit Platform Introduction Section
# ----------------------------------------------------------------------------------------------------------


# Create the title and subheader for the Streamlit page
st.title("The Caterpillar Effect")
st.subheader("You've got a caterpillar! That's great! :smiling_face_with_3_hearts:")
st.write("This model will be able to answer some questions you may have about your caterpillar.")




# ----------------------------------------------------------------------------------------------------------
# Uploading the file for Modelling and Prediction
# ----------------------------------------------------------------------------------------------------------


# Create a file input for the user to upload an image
st.write("First, upload an image of your caterpillar \U0001F41B")
st.write("Try your best to give a picture  that features your caterpillar clearly.")

img = st.file_uploader(
    label = "First, upload an image of your caterpillar. Try your best to give a picture that features your caterpillar clearly.", 
    type = ['jpg','jpeg','png','bmp'], 
    label_visibility="collapsed"
)

# Check if an image has been uploaded
while img is None:
    
    # Create a status indicator to show the user the assistant is working
    with st.status("Quick! Upload your image before your caterpillar pupates...", expanded=False) as status_box:

        time.sleep(15)
        status_box.update(label=f"Waiting for image upload...", state="running")
        
        # Display a message to upload an image
        st.write("Please upload an image.")

# Display the uploaded image
st.image(img, caption='What a cute little guy! \U0001F929', use_column_width=True)
# Perform further processing with the uploaded image
# Add your code here to process the uploaded image


# ----------------------------------------
# Preprocessing the image before modelling
# ----------------------------------------

# Open the uploaded image using PIL
img = Image.open(img)

#resize image
img = img.resize((256,256))

#convert the image to a matrix of numbers
img = np.array(img)
img = np.expand_dims(img,axis=0)

#Scaling X_train to between 0 and 1
img = img / 255

# ----------------------------------------
# Loading the existing model
# ----------------------------------------

model = load_model('the_caterpillar_effect_CNN.keras')

# ----------------------------------------
# Running the model and saving predicted class
# ----------------------------------------

# Define function: generate predicted classes as a numpy array

def pred_class(pred_prob_varname):

    pred_class_all = np.array([])
    for pred_prob_array in pred_prob_varname:
        pred_class = np.argmax(pred_prob_array)
        pred_class_all = np.append(pred_class_all, pred_class)
    
    return pred_class_all


# Predict the outcome
pred = model.predict(img)
result = pred_class(pred)

if result == 0:
    caterpillar_name = 'Chocolate Pansy Caterpillar'

elif result == 1:
    caterpillar_name = 'Lime Caterpillar'

elif result == 2: 
    caterpillar_name = 'Painted Jezebel Caterpillar'

else:
    caterpillar_name = 'Plain Tiger Caterpillar'

st.write("Image processing completed.")
st.write(f"Your caterpillar is the {caterpillar_name}!")


# ----------------------------------------------------------------------------------------------------------
# Entering Age for Chatbot Output
# ----------------------------------------------------------------------------------------------------------

#Enter your age
st.write("Next, we need to know how old you are.")
age = st.number_input(
    label = 'Enter your age (4-100): ',
    min_value = 4,
    max_value = 100,
    placeholder = 'How old are you?')

# Confirm age
st.write(f'You are {age} years old.')



# ----------------------------------------------------------------------------------------------------------
# Chatbot to Answer Questions on the Predicted Caterpillar Class
# ----------------------------------------------------------------------------------------------------------


st.subheader(f"Ask a question about the {caterpillar_name}!")
st.write("Here, you can ask questions about your caterpillar \U0001F41B")

if prompt := st.chat_input(f'What would you like to know about {caterpillar_name}s?'):
    
    # Create a status indicator to show the user the assistant is working
    with st.status("While we're working, did you hear how the caterpillar \U0001F41B got 100 feet \U0001F463 into the air? He rolled onto his back!", expanded=False) as status_box:

        # st.session_state.messages.append({'role': 'user', 'content': prompt})
        with st.chat_message('user'):
            st.markdown(prompt)

        with st.chat_message('assistant'):
            message_placeholder = st.empty()
            full_response = ''
            
            thread = client.beta.threads.create(
                    messages=[
                        {
                            "role": "user",
                            "content": f"Answer the {prompt} as you would to someone who is {age} years old, using only the information about the {caterpillar_name} in the uploaded files. If questions are asked about anything other than {caterpillar_name}, give the following answer: 'I can only answer questions based on the identified caterpillar. Please ask a different question related to {caterpillar_name} only.'",
                            "file_ids": uploaded_file_ids,
                        }
                    ]
            )

            # Create a run with the new thread
            run = client.beta.threads.runs.create(
                thread_id=thread.id,
                assistant_id=assistant.id,
            )

            # Check periodically whether the run is done, and update the status
            while run.status != "completed":
                time.sleep(5)
                status_box.update(label=f"{run.status}\U0001F343...", state="running")
                run = client.beta.threads.runs.retrieve(
                    thread_id=thread.id, run_id=run.id
                )

            # Once the run is complete, update the status box and show the content
            status_box.update(label="We're done! Here's the information you wanted! Ask another question if you wish \U0001F331", state="complete", expanded=True)
            messages = client.beta.threads.messages.list(
                thread_id=thread.id
            )
            st.markdown(messages.data[0].content[0].text.value)
