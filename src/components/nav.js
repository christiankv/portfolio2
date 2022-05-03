import React from "react";


export default function Nav(prop){
    const info = prop.content

    // console.log(info);

    const card = info.map((element, index)=> {   
                    // console.log(index);
                    const theclass = "card " + element.id
                    return(
                 <div className={theclass} 
                    
                    onClick={()=>prop.clickevent(theclass, index)}>
                    <small className="c-languange">{element.language}</small> <h3 className="c-title">{element.title}</h3> 
                    
                    <p className="c-info">{element.info}</p>
            
                </div>)})
    





    
        
    return(
        <div className="navbar">
            <div className="title">
            <small>welcome to</small>
            <h1>my portfolio</h1>
            </div>
            {card}

        </div>
    )
}