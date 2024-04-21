import React from 'react';
import logo from './logo.svg';
import './App.css';
import { useState } from 'react';
import { ftruncate } from 'fs';

function App() {
  const onclick = async () => {
    let [tab] = await chrome.tabs.query({ active: true });
    chrome.scripting.executeScript({
      target: { tabId: tab.id! }, 
      func: () => {
        console.log("posos");
      }
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

