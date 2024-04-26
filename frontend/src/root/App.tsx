import { HelmetProvider } from 'react-helmet-async';
import { Router } from '~/pages/Router';

export const App = () => {
  return (
    <HelmetProvider>
      <main>
        <Router />
      </main>
    </HelmetProvider>
  );
};
