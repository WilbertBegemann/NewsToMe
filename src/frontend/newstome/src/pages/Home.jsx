import React, { useState, useEffect } from 'react';

function Home() {
    const [welcoming, setWelcoming] = useState([]);

    useEffect(() => {
        async function fetchData() {
            try {
                const response = await fetch('http://127.0.0.1:5000/api/home');
                const data = await response.json();
                console.log("Here check this out");
                

                // Check if data.websites is an array before setting the state
                if (Array.isArray(data.websites)) {
                    setWelcoming(data.websites);
                } else {
                    console.error('Invalid API response format. Expected an array.');
                }
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        }

        fetchData();
    }, []);

    return (
        <div className='bg-gray-800 text-white'>
            <h1>Welcome to NewsToMe!</h1>
            <p>Stay up-to-date with the latest news.</p>     
            <div>
                <h1>Articles</h1>
                <ul>
                    {welcoming.map((website, index) => (
                        <li key={index}>
                            <h2>{website}</h2>
                        </li>
                    ))}
                </ul>
            </div>
        </div>
    );
}

export default Home;
