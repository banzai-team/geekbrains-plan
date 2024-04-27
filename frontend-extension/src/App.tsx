import './App.css'
import { Button } from "~/components/ui/button";
import { likeVacancy } from "~/domain/api.tsx";
import { useMutation } from "react-query";

let url = ""
chrome.tabs.query({ active: true, lastFocusedWindow: true }, async (tabs: any) => {
  url = tabs[0].url;
});

function App() {
  // @ts-ignore
  const vacancyHandler = async () => likeVacancy(url)

  const like = useMutation(() => vacancyHandler());

  return (
    <>
      <Button disabled={like.isLoading} variant="outline" onClick={() => like}>
        Like1:
        {like.isLoading ? "Loading..." : like.isSuccess || "not yet called"}
      </Button>
    </>
  )
}

export default App
