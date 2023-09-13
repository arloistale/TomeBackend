import os
from supabase import create_client, Client

supabaseUrl = os.environ.get("SUPABASE_URL")
supabaseKey = os.environ.get("SUPABASE_KEY")

client: Client = create_client(supabaseUrl, supabaseKey);