import React, { useState } from 'react'
import { createClient } from '@supabase/supabase-js'
import { v4 as uuidv4 } from "uuid";

const supabase = createClient("https://uucjxrxuwtulwesskirt.supabase.co",
"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InV1Y2p4cnh1d3R1bHdlc3NraXJ0Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2ODU2NDU5NTIsImV4cCI6MjAwMTIyMTk1Mn0.5keaiMhPA_Ja45udjBUE1SgT3K5rx_ntvANb2BaYX9g"
);

export default function SupaBase() {
    const [file, setfile] = useState([]);

    const handleSubmit = async (e) => {
        e.preventDefault();
        const filename = `${uuidv4()}-${file.name}`;

        const { data, error } = await supabase.storage
            .from("Images")
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