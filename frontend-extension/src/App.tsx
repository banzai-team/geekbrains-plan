import './App.css'
import {Button} from "~/components/ui/button";

let url = "";

// @ts-ignore
const onClick = ()=> {
    chrome.tabs.query({ active: true, lastFocusedWindow: true }, (tabs: any) => {
        url = tabs[0].url;
        console.log(url) // fix for npm run build
        // use `url` here inside the callback because it's asynchronous!
        alert('Successfully added to favorites!');
    });
}

function App() {
    return (
        <>
            <Button variant="outline" onClick={onClick}>
                Like
            </Button>
        </>
    )
}

export default App
