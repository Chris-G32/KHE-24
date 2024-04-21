import './App.css'
import { useState } from 'react'
import CompareIcon from '@mui/icons-material/Compare';
import LoadingAnimation from './components/Loading';
import { wait } from '@testing-library/user-event/dist/utils';

function elementToPlainText(element: HTMLElement|Element|undefined|null): string {
    let text = element?.textContent || '';
    text = text.trim().replace(/\s+/g, ' '); // Remove extra whitespace
    return text;
}

function removeHtmlTags(html: string): string {
    const div = document.createElement('div');
    div.innerHTML = html;
    return div.innerText || div.textContent || '';
}

function parseDescription(){
    let url=window.location.href
    let element;
    if(url.includes("indeed")){
        element=document.getElementById("jobDescriptionText")
    }
    else if(url.includes("linked")){
        element=document.getElementById("job-details")
        element=element?.getElementsByClassName("mt4").item(0)
    }

    // Select elements with class names containing the keyword
    // const elements = document.querySelectorAll(`[class*="j${keyword}"]`);
    return removeHtmlTags(elementToPlainText(element));
}


function App() {

    const [status, setStatus] = useState('ready')
    const [report, setReport] = useState(null)

    const parseData=()=>{
        console.log("Description:")
        console.log(parseDescription())
    };

    const onclick = async () => {
        setStatus('loading')
        setTimeout(() => {
            setStatus('report')
        }, 3000)
        let [tab] = await chrome.tabs.query({ active: true });
        chrome.scripting.executeScript({
            target: { tabId: tab.id! }, 
            func:parseData
        });
    }

    return (
        <div className="App">
            {status == 'ready' && (
                <>
                    <h2>Secure Your Career!</h2>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
                    <button onClick={onclick}><CompareIcon style={{width: '100%', height: '100%'}} /></button>
                </>
            )}
            {status == 'loading' && (
                <LoadingAnimation />
            )}
            {status == 'report' && (
                <>
                    <h2>Position</h2>
                    <p>volutpat commodo sed egestas egestas fringilla phasellus faucibus scelerisque eleifend donec pretium vulputate sapien nec sagittis aliquam malesuada bibendum arcu vitae elementum curabitur vitae nunc sed velit dignissim sodales ut eu sem integer vitae justo eget magna fermentum iaculis eu non diam phasellus vestibulum lorem sed risus ultricies tristique nulla aliquet enim tortor at auctor urna nunc id cursus metus aliquam eleifend mi in nulla posuere sollicitudin aliquam ultrices sagittis orci a scelerisque purus semper eget duis at tellus at urna condimentum mattis pellentesque id nibh tortor id aliquet lectus proin nibh nisl condimentum id venenatis a condimentum vitae sapien pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas sed tempus urna et pharetra pharetra massa massa ultricies mi quis hendrerit</p>
                    <hr />
                    
                </>
            )}
        </div>
    );
}

export default App;

