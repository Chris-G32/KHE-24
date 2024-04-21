import React from 'react';
import logo from './logo.svg';
import './App.css';
import { useState } from 'react';
import { ftruncate } from 'fs';
import { getElementError } from '@testing-library/react';

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
  const parseData=()=>{
    console.log("Description:")
    console.log(parseDescription())
  };
  const onclick = async () => {
    let [tab] = await chrome.tabs.query({ active: true });
    chrome.scripting.executeScript({
      target: { tabId: tab.id! }, 
      func:parseData
    }

    );
  }
  return (
    <div className="App">
      <h1>Title</h1>
      <button onClick={onclick}></button>
    </div>
  );
}

export default App;

