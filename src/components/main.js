import React from "react";

export default function Main(prop){
    


    //  .then(res=> console.log(res.text)))

    // fetch (link)
    // .then((response) => response.text().then(createhtmlsite));

    // console.log(prop.choice);
    function Choices(){
        const btns = prop.content[prop.choice].versions.map(e => 
        <p 
            className="buttons"
            id={e + "btn"}
            onClick = {prop.clickevent}
        >{e}</p>)
        return btns
    }
    function Version(){
        if (prop.version === "pagebtn"){
        return <iframe className="main-content" src= {prop.htmllink} title="description"></iframe>
        }else if (prop.version === "htmlbtn"){
            return <textarea readOnly className="main-content" >{prop.htmltext}</textarea>
        } else if (prop.version === "cssbtn"){
           return <textarea readOnly className="main-content" >{prop.csstext}</textarea>
        } else if (prop.version === "javascriptbtn"){
            return <textarea readOnly className="main-content" >{prop.JStext}</textarea>
        }else if (prop.version === "pythonbtn"){
            return <textarea readOnly className="main-content" >{prop.pythontext}</textarea>
        }
    }
    
    return(
        <div className="main">
            <div className="button-container"> <Choices/> </div>
            <Version/>
        </div>

    )
}