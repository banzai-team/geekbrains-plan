import './App.css'
import {Button} from "~/components/ui/button";

let url = "";

// @ts-ignore
chrome.tabs.query({ active: true, lastFocusedWindow: true }, (tabs: any) => {
  url = tabs[0].url;
  console.log(url) // fix for npm run build
  // use `url` here inside the callback because it's asynchronous!
});

function App() {
  return (
    <>
      <Button size="icon" variant="outline" className="sm:hidden">
        Like
      </Button>
    </>
  )
}

export default App
