import { Route, Routes } from 'react-router-dom'

import Home from './pages/Home'
import Summary from './pages/Summary'
import NotFound from './pages/NotFound'
import {Header} from './components/Header'

import './App.css'

function App() {
    return (
        <>
            <Header />
            <Routes>
                <Route path='*' element={<NotFound />} />
                <Route path='/' element={<Home />} />
                <Route path='/summary/:reportId' element={<Summary />} />
            </Routes>
        </>
    )
}

export default App
