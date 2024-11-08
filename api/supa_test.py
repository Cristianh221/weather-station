import hashlib
from supabase import create_client, Client

#supabase data connection: URL,KEY 
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InZwZmR3cWVkc21kZHZ3a2xpZXBsIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzAxNjY3NjYsImV4cCI6MjA0NTc0Mjc2Nn0.LDvk-XTYTVHuWPU8mBi-O7_YNp1iEMdOvo0u8y8gWsk"
SUPABASE_URL = "https://vpfdwqedsmddvwkliepl.supabase.co"
    
#Connect to Supabase Client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

#Get and save data function
def  save_data(e, p):
    # Insert into users model
    enc_pass = hashlib.sha256(p.encode()).hexdigest()
    
    response = supabase.table('users').insert({"email": e, "password": enc_pass}).execute()
    
    if response.data:
        print(f"user has been save succesfully {response.data}")
    elif response.error:
        print(f"Error saving user: {response.error}")
    
#Main
email = input("User e-mail:")
passwd =input("User password:")
save_data(email, passwd)