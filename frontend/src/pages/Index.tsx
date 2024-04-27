import React from 'react';

import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '~/components/ui/card';
import Head from '~/components/Head';
import Table from '~/components/Table';
import Empty from '~/components/Empty';
import Breadcrumbs from '~/components/Breadcrumbs';
import { Routes } from "~/pages/Router";
import { Button } from "~/components/ui/button";
import { Plus } from "lucide-react";
import { useNavigate } from "react-router";
import { useQuery } from "react-query";
import { getRequests } from "~/domain/api";

function Index() {
  const navigate = useNavigate();

  const onAddClick = () => {
    navigate(`${Routes.Vacancy}${Routes.New}`);
  };

  const requests = useQuery(["requests"], getRequests);
  const data = requests.data;

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
        <CardHeader className="flex flex-row items-center justify-between px-7">
          <div className="space-y-1.5">
            <CardTitle>Ваши вакансии</CardTitle>
            <CardDescription>Вакансии и подходящие к ним курсы</CardDescription>
          </div>
          <Button size="sm" onClick={onAddClick}>
            <Plus className="h-4 w-4 mr-2"/>
            Добавить
          </Button>
        </CardHeader>
        <CardContent className="p-0">
          {data && data.length ? <Table data={data}/> : <Empty text="Ой! Кажется еще ничего нет"/>}
        </CardContent>
      </Card>
    </>
  );
}

export default Index;
