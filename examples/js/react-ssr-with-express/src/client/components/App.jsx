import {Routes, Route} from 'react-router-dom';
import Home from './Home';
import About from './About';
import Navbar from './Navbar';

const App = () => {
    return (
        <main>
            <Navbar/>
            <Routes>
                <Route path="/" element={<Home/>}/>
                <Route path="/about" element={<About/>}/>
            </Routes>
        </main>
    );
};

export default App;
