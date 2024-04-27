import React, { lazy, Suspense } from 'react';
import { RouteObject, useRoutes, BrowserRouter } from 'react-router-dom';
import MainView from '~/components/MainView';
import { Spinner } from '~/components/ui/spinner';
import {Card} from "~/components/ui/card";

const Loading = () => (
  <Card className="p-20 w-full h-full text-center mt-10 text-md flex flex-row gap-2 justify-center align-middle text-muted-foreground">
    Загрузка <Spinner />
  </Card>
);

const IndexScreen = lazy(() => import('~/pages/Index'));
const VacancyScreen = lazy(() => import('~/pages/VacancyPage'));
const Page404Screen = lazy(() => import('~/pages/404'));
const AddFormScreen = lazy(() => import('~/pages/AddFormPage'));

export const Routes = {
  Root: '/',
  Vacancy: '/vacancy',
  New: '/new',
};

export const Router = () => {
  return (
    <BrowserRouter>
      <InnerRouter />
    </BrowserRouter>
  );
};

const InnerRouter = () => {
  const routes: RouteObject[] = [
    {
      path: '/',
      element: <MainView />,
      children: [
        {
          index: true,
          element: (
            <Suspense fallback={<Loading />}>
              <IndexScreen />
            </Suspense>
          ),
        },
        {
          path: `${Routes.Vacancy}${Routes.New}`,
          element: (
            <Suspense fallback={<Loading />}>
              <AddFormScreen/>
            </Suspense>
          ),
        },
        {
          path: `${Routes.Vacancy}/:id`,
          element: (
            <Suspense fallback={<Loading />}>
              <VacancyScreen />
            </Suspense>
          ),
        },
        {
          path: '*',
          element: (
            <Suspense fallback={<Loading />}>
              <Page404Screen />
            </Suspense>
          ),
        },
      ],
    },
  ];
  return useRoutes(routes);
};
