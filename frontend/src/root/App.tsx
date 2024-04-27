import { HelmetProvider } from 'react-helmet-async';
import { Router } from '~/pages/Router';
import {QueryClient, QueryClientProvider} from "react-query";

const queryClient = new QueryClient();

export const App = () => {
  return (
      <QueryClientProvider client={queryClient}>
          <HelmetProvider>
          <main>
            <Router />
          </main>
        </HelmetProvider>
      </QueryClientProvider>
  );
};
