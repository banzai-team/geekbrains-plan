import './App.css'

let url = "";

// @ts-ignore
chrome.tabs.query({ active: true, lastFocusedWindow: true }, (tabs: any) => {
  url = tabs[0].url;
  // use `url` here inside the callback because it's asynchronous!
});

function App() {

  return (
    <>
      Hello
    </>
  )
}

export default App
