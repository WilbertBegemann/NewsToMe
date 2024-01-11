// In your App component or main application file
import Home from './pages/Home';
import ArticlesPage from './pages/articles';
import AboutPage from './pages/About';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';

function App() {
  return (
  <Router>
    <Routes>
      {/* Set the default route as '/notes' */}
      <Route path='/' element={<Home />} />
      <Route path='/articles' element={<ArticlesPage />} />
      <Route path='/about' element={<AboutPage/>}/>
    </Routes >
  </Router >
  );
}
export default App;