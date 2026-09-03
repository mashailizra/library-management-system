import streamlit as st
import requests
import pandas as pd

API_URL = "http://127.0.0.1:8000"


st.title("Library Member Management System")

st.write("Connecting to FastAPI backend...")

try:
    response = requests.get(f"{API_URL}/members")

    if response.status_code == 200:
        st.success("Connected to FastAPI successfully!")
    else:
        st.error(f"API returned an error: {response.status_code}")

except requests.exceptions.RequestException:
    st.error(
        "Could not connect to the FastAPI backend. "
        "Make sure the FastAPI server is running on port 8000."
    )
st.header("Add New Member")

with st.form("add_member_form"):
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=1, max_value=120, value=18)
    member_id = st.text_input("Member ID")
    membership_type = st.selectbox(
        "Membership Type",
        ["Basic", "Premium"]
    )

    submitted = st.form_submit_button("Add Member")

    if submitted:
        member_data = {
            "name": name,
            "age": age,
            "member_id": member_id,
            "membership_type": membership_type
        }

        try:
            response = requests.post(
                f"{API_URL}/members",
                json=member_data
            )

            if response.status_code == 200:
                st.success("Member added successfully!")

            elif response.status_code == 409:
                st.error(response.json()["detail"])

            else:
                st.error(
                    f"API returned an error: {response.status_code}"
                )

        except requests.exceptions.RequestException:
            st.error(
                "Could not connect to the FastAPI backend. "
                "Make sure the FastAPI server is running on port 8000."
            )
st.header("All Members")

search = st.text_input("Search members")

sort_by = st.selectbox(
    "Sort by",
    ["None", "name", "age", "member_id", "membership_type"]
)

try:
    response = requests.get(f"{API_URL}/members")

    if response.status_code == 200:
        members = response.json()

        if members:
            df = pd.DataFrame(members)

            if search:
                df = df[
                    df["name"].str.contains(search, case=False, na=False)
                    | df["member_id"].str.contains(search, case=False, na=False)
                    | df["membership_type"].str.contains(
                        search, case=False, na=False
                    )
                ]

            if sort_by != "None":
                df = df.sort_values(by=sort_by)

            st.dataframe(df, use_container_width=True)

        else:
            st.info("No members found.")

    else:
        st.error(f"API returned an error: {response.status_code}")

except requests.exceptions.RequestException:
    st.error(
        "Could not connect to the FastAPI backend. "
        "Make sure the FastAPI server is running on port 8000."
    )