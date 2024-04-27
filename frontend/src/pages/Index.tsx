import React from 'react';

import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '~/components/ui/card';
import Head from '~/components/Head';
import Table from '~/components/Table';
import Empty from '~/components/Empty';
import Breadcrumbs from '~/components/Breadcrumbs';
import {Routes} from "~/pages/Router";

function Index() {
  {
    /*TODO: add real data*/
  }
  const data = [
    {
      id: 'pro-1',
      vacancy: 'Паграмист',
      vacancyLink: 'https://google.com',
      price: '5000',
      status: 'Done',
    },
    {
      id: 'fu-15',
      vacancy: 'Клининг мастер',
      vacancyLink: 'https://google.com',
      price: '1000000',
      status: 'Done',
    },
    {
      id: 'like-2345',
      vacancy: 'Дизайнер обоев',
      vacancyLink: 'https://google.com',
      price: '',
      status: 'Progress',
    },
  ];

  return (
    <>
      <Head title="Главная" />
      <Breadcrumbs
          path={[
            {
              text: "Главная",
              link: Routes.Root
            }
          ]}
      />
      <Card>
        <CardHeader className="px-7">
          <CardTitle>Таблица с данными</CardTitle>
          <CardDescription>Отображение вакансия - курсы</CardDescription>
        </CardHeader>
        <CardContent className="p-0">
          {data && data.length ? <Table data={data} /> : <Empty text="Ой! Кажется еще ничего нет" />}
        </CardContent>
      </Card>
    </>
  );
}

export default Index;
