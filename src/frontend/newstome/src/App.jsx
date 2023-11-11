import { React } from "react";
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import Home from './pages/Home';
import Articles from './pages/Articles';



function App() {
  return (
    <Router>
    <Routes>
      {/* Set the default route as '/notes' */}
      <Route path='/' element={<Navigate to="/Home" />} />
      <Route path='/Home' element={<Home />} />
      <Route path='/Articles' element={<Articles/>}/>
    </Routes >
  </Router >

  );
}

export default App;
