import React from 'react';
import { useParams } from 'react-router';

import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '~/components/ui/card';
import Head from '~/components/Head';
import Breadcrumbs from '~/components/Breadcrumbs';
import { Routes } from '~/pages/Router';
import {Clock, Wallet} from "lucide-react";

const VacancyPage: React.FC = () => {
  const { id = '' } = useParams();

  return (
    <>
      <Head title={`Вакансия ${id}`} />
      <Breadcrumbs
        path={[
          {
            text: 'Главная',
            link: Routes.Root,
          },
          {
            text: `Вакансия ${id}`,
            link: `${Routes.Vacancy}/${id}`,
          },
        ]}
      />
      <div className="grid gap-4 sm:grid-cols-2 md:grid-cols-2 lg:grid-cols-4 xl:grid-cols-4">
        <Card className="row-start-1 row-end-3 sm:col-span-2" x-chunk="vacancy-chunk-0">
          <CardHeader className="pb-2">
            <CardTitle>Вакансия классная</CardTitle>
            <CardDescription>VK</CardDescription>
          </CardHeader>
          <CardContent>data</CardContent>
        </Card>
        <Card className="sm:col-span-2" x-chunk="vacancy-chunk-1">
          <CardHeader className="pb-2">
            <CardTitle>Курс самый прекрасный</CardTitle>
            <CardDescription>обязательно пройдите!</CardDescription>
          </CardHeader>
          <CardContent>data</CardContent>
        </Card>
        <Card x-chunk="vacancy-chunk-2">
          <CardHeader className="pb-2">
            <CardDescription className="flex flex-row items-center justify-between space-y-0 pb-0">
              Стоимость
              <Wallet className="h-6 w-6 text-muted-foreground" />
            </CardDescription>
            <CardTitle className="text-4xl text-primary">2000 &#8381;</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="text-xs text-muted-foreground">* ? доп текст ? *</div>
          </CardContent>
        </Card>
        <Card x-chunk="vacancy-chunk-3">
          <CardHeader className="pb-2">
            <CardDescription className="flex flex-row items-center justify-between space-y-0 pb-0">
              Длительность
              <Clock className="h-6 w-6 text-muted-foreground" />
            </CardDescription>
            <CardTitle className="text-4xl text-primary">4 месяца</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="text-xs text-muted-foreground">* ? доп текст ? *</div>
          </CardContent>
        </Card>
      </div>
    </>
  );
};

export default VacancyPage;
