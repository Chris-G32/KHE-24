import { useState } from 'react'
import { useAuth } from '@clerk/clerk-react'

import './Home.css'

import { SearchBar } from '../components/Inputs'
import { PrimaryButton } from '../components/Buttons'

function Home() {
    const [searchVal, setSearchVal] = useState('')

    function handleSearch(event) {
        event.preventDefault()
    }

    const { getToken } = useAuth();
 
    const authenticatedFetch = async (...args) => {
      return fetch(...args, {
        headers: { Authorization: `Bearer ${await getToken()}` }
      }).then(res => res.json());
    };

    async function makeRequest() {
        console.log(await authenticatedFetch("http://localhost:5000/test"))
    }

    return (
        <div id='Home'>
            <h1>Secure Your Career Path!</h1>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
            <SearchBar placeholder='Link to a job posting' value={searchVal} onChange={e => setSearchVal(e.target.value)} onSubmit={handleSearch} style={{width: '80%'}} />
            <PrimaryButton onClick={makeRequest} />
        </div>
    )
}

export default Home