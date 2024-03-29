import React, { useEffect, useState, useContext } from 'react';
import { useNavigate } from 'react-router-dom';
import Navbar from '../components/Navbar';

function Home() {
  // Define state variables and their initial values
  const [data, setData] = useState([{}]);
  const [title, setTitle] = useState('');
  const navigate = useNavigate();
  /**S
   * Fetch backend data when the page is rendered
   */
  useEffect(() => {
    fetch('http://127.0.0.1:5000/api/getWebsites')
      .then((res) => res.json())
      .then((data) => setData(data));

    // Fetch data here
  }, []);

  // Function to handle click on list item
  const handleListItemClick = (clickedTitle) => {
    setTitle(clickedTitle);
    navigate('/articles', { state: { title: clickedTitle } });
  };

  return (
    <div className=' bg-slate-600 w-screen max-h-full'>
      <Navbar/>
      <div className=' bg-slate-600 w-screen max-h-full'>
        <h1 className='text-center text-white font-bold text-6xl p-6'>List of available websites</h1>

        <div className='justify-center'>
          <ul className='flex flex-col items-center justify-center text-white font-bold text-xl'>
            {data.map((item, index) => (
              <li className='' key={index} onClick={() => handleListItemClick(item.title)}>
                <div
                  style={{
                    background: '#6b7280',
                    borderRadius: '8px',
                    padding: '10px',
                    margin: '5px',
                    width: '60em', // Adjust the width as needed
                    height: '13em', // Adjust the height as needed
                  }}
                >
                  <h1 className='text-center text-xl'>{item.title}</h1>
                  <div className='p-4 h-40'>
                    <img
                    src={item.img}
                    alt=''
                    className='mx-auto'
                    style={{ borderRadius: '8px', marginTop: '5px', maxWidth: '100%', maxHeight: '100%',borderRadius: '8px' }}
                  />
                  </div>
                  
                </div>
              </li>
            ))}
          </ul>
        </div>
        
      </div>
    </div>
  );
}

export default Home;