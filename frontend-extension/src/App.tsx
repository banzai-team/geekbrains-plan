import './App.css'
import { Button } from "~/components/ui/button";
import { likeVacancy } from "~/domain/api.tsx";
import { useMutation } from "react-query";
import {Label} from "~/components/ui/label.tsx";
import {Spinner} from "~/components/ui/spinner.tsx";
import {Heart} from "lucide-react";

let url = "";

chrome?.tabs?.query({ active: true, lastFocusedWindow: true }, async (tabs: any) => {
  url = tabs[0].url;
});

function App() {
  // @ts-ignore
  const vacancyHandler = async () => likeVacancy(url)

  const likeMutation = useMutation(() => vacancyHandler());

  return (
      <div className="w-80 h-60 bg-cover bg-center bg-no-repeat flex items-center justify-center text-base" style={{backgroundImage: 'url(/bg.svg)'}}>
          <div className="flex flex-col gap-3 items-center justify-center p-5 h-full">
              <Label className="py-1.5 text-lg">Вы можете добавить эту вакансию в избранные</Label>
              <Button
                  disabled={likeMutation.isLoading}
                  variant="ghost"
                  size="lg"
                  onClick={() => likeMutation.mutateAsync()}
                  className="text-primary font-medium rounded-full text-sm p-2.5 text-center
                   inline-flex items-center text hover:bg-transparent hover:text-purple-400 focus:text-purple-500"
              >
                  {likeMutation.isLoading
                      ? <Spinner size="small"/>
                      : <Heart
                          className="w-12 h-12 md:h-9 md:w-9 p-0"
                          aria-hidden="true"
                          xmlns="http://www.w3.org/2000/svg"
                          fill={likeMutation.isSuccess ? 'currentColor' : 'none'}
                      />
                  }
              </Button>
          </div>
      </div>
  )
}

export default App
