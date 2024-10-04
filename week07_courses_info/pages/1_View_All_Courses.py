import pandas as pd
import streamlit as st
import json

st.set_page_config(page_title="View all courses")

def load_courses():
    with open('./data/courses-full.json', 'r') as f:
        #/Users/vins/Documents/project folder/data/courses-full.json
        courses = json.load(f)
    return courses

def convert_to_dataframe(courses_data):
    courses_list = []
    for course_name, course_info in courses_data.items():
        courses_list.append({
            'Name' : course_info['name'],
            'Category' : course_info['category'],
            'Provider': course_info['provider'],
            'Course Code': course_info['course_code'],
            'Duration': course_info['duration'],
            'Rating': course_info['rating'],
            'Price' : f"${course_info['price']:.2f}",
            'Skills Covered': ', '.join(course_info['skills_covered']),
            'Description' : course_info['description']
        })
    return pd.DataFrame(courses_list)

# Main App
def main():
    st.title("View All Courses")

# Load Courses

    courses_data = load_courses()
    courses_df = convert_to_dataframe(courses_data)

    st.write("Here are all the courses available: ")
    st.dataframe(courses_df,use_container_width=True)

if __name__ == "__main__":
    main()

    
