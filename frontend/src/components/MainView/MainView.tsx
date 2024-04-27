import React from 'react';
import { Outlet } from 'react-router-dom';

import Sidebar from '~/components/Sidebar';
import Header from '~/components/Header';

const MainView: React.FC = () => {
  return (
    <div
        className="flex min-h-screen w-full flex-col bg-muted/40 bg-center bg-no-repeat bg-cover"
        style={{backgroundImage: 'url(/public/bg.svg)'}}
    >
      <Sidebar />
      <div className="flex flex-col sm:gap-4 sm:py-4 sm:pl-14">
        <Header />
        <main className="flex-1 items-start gap-4 p-4 sm:px-6 sm:py-0 md:gap-8 lg:grid-cols-3 xl:grid-cols-3">
          <Outlet />
        </main>
      </div>
    </div>
  );
};

export default MainView;
