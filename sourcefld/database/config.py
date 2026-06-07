import streamlit as sl
from supabase import create_client, Client

supabase: Client = create_client(
    sl.secrets["supabase_url"],
    sl.secrets["key"]
)