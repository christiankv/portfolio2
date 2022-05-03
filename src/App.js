import React from "react";
import Nav from "./components/nav";
import Info from "./components/info";
import Main from "./components/main";


export default function App(){
const [choices, setChoices]= React.useState(0)
const [version, setversion]= React.useState("pagebtn")
    const info = [
        {
            versions : ["html","page","css"],
            
            link: "/html/task22.11/" ,
            id: "html",
            language : "html",
            title: "List",
            info: "task about making lists"
        },
        {
            versions : ["javascript"],
            link: "/javascript/oppg1/",
            id: "javascript",
            language : "javascript",
            title: "03.12",
            info: "iframe"
        },        
        {
            versions: ["python"],
            link: "/python/",
            id: "python",
            language : "python",
            title: "03.12",
            info: "how to make an if setting that works"
            }

    ]

    const htmllink = "https://christiankv.github.io/portfolio"+ info[choices].link + "index.html"
    const csslink = "https://christiankv.github.io/portfolio"+ info[choices].link + "css/style.css"
    const JSlink = "https://christiankv.github.io/portfolio"+ info[choices].link + "index.js"
    const pythonlink = "https://christiankv.github.io/portfolio"+ info[choices].link + "index.py"
    // console.log(prop.content[prop.choice].versions);
    const [htmltext, sethtmltext] = React.useState("")
    const [csstext, setcsstext] = React.useState("")
    const [JStext, setJStext] = React.useState("")
    const [pythontext, setpythontext] = React.useState("")

    React.useEffect(()=>{
        fetch(htmllink)
        .then (res => res.text().then(sethtmltext))
    }, [choices])
    React.useEffect(()=>{
        fetch(csslink)
        .then (res => res.text().then(setcsstext))
    }, [choices])
    React.useEffect(()=>{
        fetch(JSlink)
        .then (res => res.text().then(setJStext))
    }, [choices])
    React.useEffect(()=>{
        fetch(pythonlink)
        .then (res => res.text().then(setpythontext))
    }, [choices])

    console.log(choices);




// console.log(version);

function clickEvent(className,index){
    if (className === "card html"){
        setversion(()=> "pagebtn")
    } else if (className === "card javascript"){
        setversion(()=> "javascriptbtn")
    }else if (className === "card python"){
        setversion(()=> "pythonbtn")
    }
    
    console.log(className);

    setChoices(()=>  index)

    console.log(choices);
    
}


function choiceclick(id){
    setversion(e=>id.target.id )
}
    return(
        <div className="container">
        <Nav
            clickevent = {clickEvent}
            content = {info}

/>
            <Info/>
            <Main
            htmllink = {htmllink}
            htmltext={htmltext}
            csstext ={csstext}
            JStext ={JStext}
            pythontext = {pythontext}
            content = {info}
            choice = {choices}
            clickevent = {choiceclick}
            version = {version}
            
            />
        </div>

    )
}