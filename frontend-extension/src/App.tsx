import './App.css'
import { Button } from "~/components/ui/button";
import { likeVacancy } from "~/domain/api.tsx";
import { useMutation } from "react-query";

let url = "";

chrome?.tabs?.query({ active: true, lastFocusedWindow: true }, async (tabs: any) => {
  url = tabs[0].url;
});

function App() {
  // @ts-ignore
  const vacancyHandler = async () => likeVacancy(url)

  const likeMutation = useMutation(() => vacancyHandler());

  return (
    <>
      <Button disabled={likeMutation.isLoading} variant="outline" onClick={() => likeMutation.mutateAsync()}>
        Like1:
        {likeMutation.isLoading ? "Loading..." : likeMutation.isSuccess || "not yet called"}
      </Button>
    </>
  )
}

export default App
