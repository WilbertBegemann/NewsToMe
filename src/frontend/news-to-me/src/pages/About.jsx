import React from 'react';
import Navbar from '../components/Navbar';

const About = () => {
    return (
        <div className='bg-slate-600 min-h-screen'>
            <Navbar/>
            <div className='content-center'>
                <h1 className='text-6xl text-white text-center p-5'>About Page</h1>
                <p className='text-white text-center text-xl m-4 p-5'>This is a little project just to learn about some front-end javascript using react, tailwind and python flask for the back-end.
                    To be honest, I'm not sure how far i will be going with this, but I'm having fun so far.
                </p>
            </div>
        </div>
    );
};

export default About;
