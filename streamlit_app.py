import streamlit as st
import requests
import pandas as pd

API_URL = "http://127.0.0.1:8000"

st.title("Library Member Management System")

st.write("Connecting to FastAPI backend...")

# Check connection to FastAPI
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


# --------------------------------------------------
# Add New Member
# --------------------------------------------------

st.header("Add New Member")

with st.form("add_member_form"):
    name = st.text_input("Name")

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=120,
        value=18
    )

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


# --------------------------------------------------
# All Members
# --------------------------------------------------

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

            # Search
            if search:
                df = df[
                    df["name"].str.contains(
                        search,
                        case=False,
                        na=False
                    )
                    | df["member_id"].str.contains(
                        search,
                        case=False,
                        na=False
                    )
                    | df["membership_type"].str.contains(
                        search,
                        case=False,
                        na=False
                    )
                ]

            # Sort
            if sort_by != "None":
                df = df.sort_values(by=sort_by)

            # Display table
            st.dataframe(
                df,
                use_container_width=True
            )

            # --------------------------------------------------
            # Delete Members
            # --------------------------------------------------

            st.subheader("Delete Members")

            for row in df.to_dict("records"):
                col1, col2 = st.columns([4, 1])

                with col1:
                    st.write(
                        f"{row['member_id']} - {row['name']}"
                    )

                with col2:
                    if st.button(
                        "Delete",
                        key=f"delete_{row['member_id']}"
                    ):
                        st.session_state["confirm_delete"] = (
                            row["member_id"]
                        )

            # Confirmation
            if "confirm_delete" in st.session_state:
                delete_id = st.session_state["confirm_delete"]

                st.warning(
                    f"Are you sure you want to delete member "
                    f"{delete_id}?"
                )

                confirm_col, cancel_col = st.columns(2)

                with confirm_col:
                    if st.button(
                        "Yes, Delete",
                        key="confirm_delete_button"
                    ):
                        try:
                            response = requests.delete(
                                f"{API_URL}/members/{delete_id}"
                            )

                            if response.status_code == 200:
                                st.success(
                                    "Member deleted successfully!"
                                )

                                del st.session_state[
                                    "confirm_delete"
                                ]

                                st.rerun()

                            elif response.status_code == 404:
                                st.error(
                                    response.json()["detail"]
                                )

                                del st.session_state[
                                    "confirm_delete"
                                ]

                            else:
                                st.error(
                                    f"API returned an error: "
                                    f"{response.status_code}"
                                )

                        except requests.exceptions.RequestException:
                            st.error(
                                "Could not connect to the FastAPI "
                                "backend. Make sure the FastAPI "
                                "server is running on port 8000."
                            )

                with cancel_col:
                    if st.button(
                        "Cancel",
                        key="cancel_delete"
                    ):
                        del st.session_state[
                            "confirm_delete"
                        ]

                        st.rerun()

        else:
            st.info("No members found.")

    else:
        st.error(
            f"API returned an error: {response.status_code}"
        )

except requests.exceptions.RequestException:
    st.error(
        "Could not connect to the FastAPI backend. "
        "Make sure the FastAPI server is running on port 8000."
    )


# --------------------------------------------------
# Update Member
# --------------------------------------------------

st.header("Update Member")

with st.form("update_member_form"):
    update_id = st.selectbox(
     "Member ID to update",
    [member["member_id"] for member in members]
)

    new_name = st.text_input("New Name")

    new_age = st.number_input(
        "New Age",
        min_value=1,
        max_value=120,
        value=18
    )

    new_membership_type = st.selectbox(
        "New Membership Type",
        ["Basic", "Premium"]
    )

    update_submitted = st.form_submit_button(
        "Update Member"
    )

    if update_submitted:
        update_data = {
            "name": new_name,
            "age": new_age,
            "membership_type": new_membership_type
        }

        try:
            response = requests.put(
                f"{API_URL}/members/{update_id}",
                json=update_data
            )

            if response.status_code == 200:
                st.success(
                    "Member updated successfully!"
                )
                st.rerun()
                
            elif response.status_code == 404:
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