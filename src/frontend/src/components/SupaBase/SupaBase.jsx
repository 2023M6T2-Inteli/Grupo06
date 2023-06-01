import React, {useState} from 'react'
import { createClient } from '@supabase/supabase-js'

export const supabase = createClient(
    process.env.SUPABASE_PROJECT_URL,
    process.env.SUPABASE_ANON_KEY
  );

export default function SupaBase() {
    const [file, setfile] = useState([]);
  
    const handleSubmit = async (e) => {
        e.preventDefault();
        const filename = `${uuidv4()}-${file.name}`;
    
        const { data, error } = await supabase.storage
          .from("images")
          .upload(filename, file, {
            cacheControl: "3600",
            upsert: false,
          });
    
        const filepath = data.path;
        // save filepath in database
      };
  
    const handleFileSelected = (e) => {
      setfile(e.target.files[0]);
    };
  
    return (
      <form onSubmit={handleSubmit}>
        <input type="file" name="image" onChange={handleFileSelected} />
        <button type="submit">Upload image</button>
      </form>
    );
  }