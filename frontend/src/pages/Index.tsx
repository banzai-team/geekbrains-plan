import React from 'react';

import {
    Card,
    CardContent,
    CardDescription,
    CardHeader,
    CardTitle,
} from "~/components/ui/card"
import Head from '~/components/Head';
import Table from "~/components/Table";
import Empty from "~/components/Empty";

function Index() {
    {/*TODO: add real data*/}
    const data = [
        // {
        //     vacancy: "Паграмист",
        //     vacancyLink: "https://google.com",
        //     price: "5000",
        //     status: "Done"
        // }, {
        //     vacancy: "Клининг мастер",
        //     vacancyLink: "https://google.com",
        //     price: "1000000",
        //     status: "Done"
        // }, {
        //     vacancy: "Дизайнер обоев",
        //     vacancyLink: "https://google.com",
        //     price: "",
        //     status: "Progress"
        // }
    ];

  return (
    <>
      <Head title="Главная" />
      <Card>
        <CardHeader className="px-7">
          <CardTitle>Таблица с данными</CardTitle>
          <CardDescription>Отображение вакансия - курсы</CardDescription>
        </CardHeader>
        <CardContent>
            {
                data && data.length
                    ? (<Table data={data}/>)
                    : (<Empty text="Ой! Кажется еще ничего нет"/>)
            }

        </CardContent>
      </Card>
    </>
  );
}

export default Index;
