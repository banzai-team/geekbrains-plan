import React, { lazy, Suspense } from 'react';
import { Outlet, RouteObject, useRoutes, BrowserRouter } from 'react-router-dom';
import MainView from '~/components/MainView';
import { Spinner } from '~/components/ui/spinner';

const Loading = () => (
  <p className="p-4 w-full h-full text-center">
    <Spinner />
  </p>
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
