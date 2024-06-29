import streamlit as st
import json
import requests

# Set the base URL for the FastAPI backend
BASE_URL = "http://127.0.0.1:8000"

# Custom CSS for styling
def add_custom_css():
    st.markdown(
        """
        <style>
        body {
            font-family: 'Arial', sans-serif;
            line-height: 1.6;
            background-color: #f9f9f9;
            color: #333;
            margin: 0;
            padding: 0;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 24px;
            text-align: center;
            display: inline-block;
            font-size: 16px;
            border-radius: 8px;
            transition-duration: 0.4s;
            cursor: pointer;
            border: none;
            text-decoration: none;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        .expander-content {
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 8px;
            margin-top: 10px;
            background-color: #fff;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        .expander-content summary::-webkit-details-marker {
            display: none;
        }
        .expander-content summary {
            font-weight: bold;
            cursor: pointer;
        }
        .expander-content summary:hover {
            color: #4CAF50;
        }
        .carousel-item {
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 16px;
            margin: 16px 0;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease-in-out;
        }
        .carousel-item:hover {
            transform: scale(1.05);
        }
        h1, h2, h3, h4, h5 {
            color: #333;
            margin-bottom: 20px;
        }
        h1 {
            font-size: 32px;
            font-weight: bold;
        }
        h2 {
            font-size: 28px;
            font-weight: bold;
        }
        h3 {
            font-size: 24px;
            font-weight: bold;
        }
        h4 {
            font-size: 20px;
            font-weight: bold;
        }
        h5 {
            font-size: 18px;
            font-weight: bold;
        }
        p {
            color: #555;
            margin-bottom: 10px;
        }
        .card {
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            padding: 20px;
            margin-bottom: 20px;
        }
        .card-title {
            font-size: 24px;
            font-weight: bold;
            color: #333;
            margin-bottom: 10px;
        }
        .card-content {
            color: #666;
            line-height: 1.6;
        }
        .card-content p {
            margin-bottom: 5px;
        }
        .form-input {
            margin-bottom: 15px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

add_custom_css()

# Function to fetch data from backend
def fetch_data(endpoint):
    response = requests.get(f"{BASE_URL}/{endpoint}")
    return response.json()

# Function to extract about me data and display
def extract_about_me_and_display(json_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    st.title("About Me")
    
    with st.expander("About Me Details"):
        st.subheader("Name")
        st.write(data.get("name", ""))
        
        st.subheader("Current Designation")
        st.write(data.get("Current Designation", ""))
        
        st.subheader("Contact Details")
        contact_details = data.get("contact details", {})
        st.write(f"- Mobile no: {contact_details.get('Mobile no', '')}")
        st.write(f"- Email: {contact_details.get('Email', '')}")
        st.write(f"- LinkedIn: {contact_details.get('LinkedIn', '')}")
        st.write(f"- Github: {contact_details.get('Github', '')}")
        
        st.subheader("Skills")
        skills = data.get("Skills", [])
        st.write(", ".join(skills))
        
        st.subheader("Summary")
        st.write(data.get("Summary", ""))

# Function to show work experience
def show_work_experience():
    st.title("Work Experience")
    data = fetch_data("work-experience")
    
    for exp in data:
       with st.expander(f"{exp['company_name']} ({exp['from_date']} to {exp['to_date']})"):
            st.markdown(
                f"""
                <div class="carousel-item">
                    <p><strong>Skills Used:</strong> {exp['skills_used']}</p>
                    <div class="expander-content">
                        <details>
                            <summary><strong>Summary:</strong> Click to expand</summary>
                            <p>{exp['summary_of_experience']}</p>
                        </details>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

# Function to show educational background
def show_educational_background():
    st.title("Educational Background")
    data = fetch_data("educational-background")
    for item in data:
        with st.expander(f"{item['name']}"):
            st.write(f"Type: {item['type']}")
            st.write(f"University/Board Name: {item['university_or_board_name']}")
            st.write(f"Year of Completion: {item['year_of_completion']}")
            st.write(f"Ongoing: {item['is_ongoing']}")

# Function to show projects
def show_projects():
    st.title("Projects")
    data = fetch_data("projects")
    for proj in data:
        with st.expander(f"{proj['name_of_project']}"):
            st.write(f"Summary: {proj['summary']}")
            st.write(f"Skills Used: {proj['skills_used']}")
            st.write(f"Duration: {proj['duration']}")
            st.write(f"Year: {proj['year']}")

# Function to show certifications
def show_certifications():
    st.title("Certifications")
    data = fetch_data("certifications")
    for item in data:
        with st.expander(f"{item['name']}"):
            st.write(f"Summary: {item['summary']}")
            st.write(f"Year: {item['year']}")
            # st.write(f"Expiry Date: {item['expiry_date']}")

# Function to show contact form
def show_contact_me():
    st.title("Contact Me")
    with st.expander("Contact Form"):
        with st.form(key='contact_form'):
            name = st.text_input("Name", max_chars=50)
            email = st.text_input("Email", max_chars=50)
            message = st.text_area("Message", max_chars=200)
            submit_button = st.form_submit_button(label='Send')
            if submit_button:
                st.success(f"Thank you {name}! Your message has been sent.")

# Function to show all sections in one page
def show_all():
    st.title("Full CV")
    extract_about_me_and_display("data/about_me.json")
    show_work_experience()
    show_educational_background()
    show_projects()
    show_certifications()
    show_contact_me()

# Main function to initialize and run the app
def main():
    st.sidebar.title("Select Option")
    options = ["About Me", "Work Experience", "Educational Background", "Projects", "Certifications", "Contact Me", "Show All"]
    choice = st.sidebar.selectbox("", options)

    if choice == "About Me":
        extract_about_me_and_display("data/about_me.json")
    elif choice == "Work Experience":
        show_work_experience()
    elif choice == "Educational Background":
        show_educational_background()
    elif choice == "Projects":
        show_projects()
    elif choice == "Certifications":
        show_certifications()
    elif choice == "Contact Me":
        show_contact_me()
    elif choice == "Show All":
        show_all()

if __name__ == "__main__":
    main()
