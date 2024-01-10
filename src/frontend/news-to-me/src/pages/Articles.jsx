import React ,{useEffect, useState} from 'react';
import { BrowserRouter as Router, Routes, Route, useNavigate } from 'react-router-dom';
import { useLocation } from 'react-router-dom';
import altImage from '../imgs/altimg.png'


function ArticlesPage() {
    const [data, setData] = useState([{}]);
    const location = useLocation();
    const title = location.state && location.state.title;
    const navigate = useNavigate();

    const handleListItemClick = (link) => {
        console.log(link);
        window.open(link, '_blank');
    };

    useEffect(() => {
        console.log(`http://127.0.0.1:5000/api/${title}`);
        fetch(`http://127.0.0.1:5000/api/${title}`).then((res) => res.json()).then((data) => setData(data));

    }, []);
    return (
        
        <div className='justify-center flex bg-slate-600 w-screen h-max'>
            <ul className='justify-center text-white font-bold text-xl text-left'>
                {data.map((item, index) => (
                    <li className='text-left' href={item.link}  key={index} onClick={() => handleListItemClick(item.link)}>
                    <div className='flex bg-slate-500 border-r-8 p-10 m-2'>
                        <div className='left-0'>
                        <img
                            src={item.image}
                            alt={altImage}
                            style={{ width: '100%', height: '100%', objectFit: 'cover', flexShrink: 0 }}
                            href={item.image}
                        />
                        </div>
                        <div className='left-0 p-6'>
                        <h1 className='text-left'>{item.title}</h1>
                        </div>
                    </div>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default ArticlesPage;
