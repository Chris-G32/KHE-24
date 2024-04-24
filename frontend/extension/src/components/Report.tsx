import React from 'react';

interface EntryItems {
    title: string;
    body: string;
}



const Entry: React.FC<EntryItems> = ({ title, body }) => {
    return (
        <div>
            <h2> {title}</h2>
            <p>{body}</p>
            <hr />
        </div>

    );
};
const Report: React.FC<any> = ({item}) => {
    var entries=[];
    console.log("Creating res ob")
    console.log(item);
    for (const [key, value] of Object.entries(item)) {
        var titleString=key;
        //Format string to capitalize first letter
        if(key.length>0){
            titleString=key.at(0)?.toLocaleUpperCase()+key.substring(1);
        }
        
        // console.log(`Key: ${key}, Value: ${value}`);
        entries.push(<Entry title={titleString} body={String(value)} />)
    }
    
    return (
        <div style={{ top: "1rem" }}>
            <h1>Report</h1>
            {entries}
        </div>
    )
};

export default Report