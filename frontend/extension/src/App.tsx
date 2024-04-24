import './App.css'
import { useState } from 'react'
import CompareIcon from '@mui/icons-material/Compare';
import LoadingAnimation from './components/Loading';
import Report from './components/Report';
import { wait } from '@testing-library/user-event/dist/utils';
import { assert } from 'console';

function App() {

    const [status, setStatus] = useState('ready')
    const [report, setReport] = useState(null)

    const foo = async () => {
        const [tab] = await chrome.tabs.query({ active: true, lastFocusedWindow: true });
        var tabid = Number(tab.id);
        chrome.tabs.sendMessage(tabid, { type: "scan" }, async (data) => {
            setReport(data);
        })
    };
    const onclick = async () => {
        setStatus('loading')
        setTimeout(() => {
            setStatus('report')
        }, 3000)
        await foo();

    }

    return (
        <>

            {status == 'ready' && (
                <div className="App">
                    <h2>Secure Your Career!</h2>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
                    <button onClick={onclick}><CompareIcon style={{ width: '100%', height: '100%' }} /></button>
                </div>
            )}
            {status == 'loading' && (
                <div className="App">
                    <LoadingAnimation />
                </div>

            )}
            {status == 'report' && (
                <>
                    <Report item={report} />
                </>
            )}
        </>

    );
}

export default App;

