import React from 'react';
import { useParams } from 'react-router';

import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '~/components/ui/card';
import Head from '~/components/Head';
import Breadcrumbs from '~/components/Breadcrumbs';
import { Routes } from '~/pages/Router';
import { getRequest } from "~/domain/api";
import { useQuery } from "react-query";
import {Clock, Wallet, BookHeart, MoveRight, BadgeCheck, Badge as BadgeIcon, BadgeX} from "lucide-react";
import Progress from '~/components/Progress';
import {Spinner} from "~/components/ui/spinner";
import {Badge} from "~/components/ui/badge";

const VacancyPage: React.FC = () => {
  const { id = '' } = useParams();

  const request = useQuery(["request", id], () => getRequest(id), { refetchInterval: 3000 });

  if (!request.isFetched) {
    return (
        <Card className="p-20 w-full h-full text-center mt-10 text-md flex flex-row gap-2 justify-center align-middle text-muted-foreground">
          Загрузка <Spinner />
        </Card>
    )
  }

  const mainCourse = request.data?.response?.eduCourses[0]?.program;
  const simularCourses = request.data.response.simularCourses.slice(0, 3);
  const metaCourse = JSON.parse(request.data.response.meta);

  const renderSkill = (item: any, key:any) => (
      <div key={`skill-${key}`} className="flex flex-row gap-3 text-muted-foreground py-1 text-sm">
        {
          item.requirement === 1
              ? <BadgeCheck className="h-5 w-5 min-w-5 text-green-500" />
              : item.requirement === 0
                  ? <BadgeIcon className="h-5 w-5 min-w-5 text-gray-700" />
                  : <BadgeX className="h-5 w-5 min-w-5 text-destructive" />
        }
        {item.skill_name}
      </div>
  )

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
        <div className="grid gap-4 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-5 xl:grid-cols-5">
          <div className="row-start-1 row-end-6 sm:col-span-3 md:col-span-3 lg:col-span-2 xl:col-span-2">
            <Card className="" x-chunk="vacancy-chunk-0">
              <CardHeader className="pb-2">
              <CardTitle>Описание вакансии</CardTitle>
              {/* <CardDescription>VK</CardDescription> */}
            </CardHeader>
            <CardContent>data</CardContent>
          </Card>
        </div>

        <Card className="sm:col-span-3" x-chunk="vacancy-chunk-11">
          <CardHeader className="pb-2">
            <CardTitle>Оценка совпадений навыков</CardTitle>
          </CardHeader>
          <CardContent className="grid grid-cols-1 gap-0 sm:grid-cols-3 sm:gap-2">
              {
                  metaCourse ? (
                      <>
                          <div>
                              {metaCourse?.skills_need.filter((item: any, key: any) => item.requirement === 1).map(renderSkill)}
                          </div>
                          <div>
                              {metaCourse?.skills_need.filter((item: any, key: any) => item.requirement === 0).map(renderSkill)}
                          </div>
                          <div>
                              {metaCourse?.skills_need.filter((item: any, key: any) => item.requirement === -1).map(renderSkill)}
                          </div>
                      </>
                  ) : <div className="my-12 col-span-4"><Spinner  /></div>
              }

          </CardContent>
        </Card>
            <Card className="sm:col-span-3" x-chunk="vacancy-chunk-1">
                {
                    mainCourse ? (
                        <>
                            <CardHeader className="pb-2">
                                <CardTitle>
                                    <a target="_blank" href={mainCourse.url}
                                       className="flex flex-row gap-2 items-center hover:text-primary"
                                   rel="noreferrer">
                                    {mainCourse.name}
                                    <MoveRight className="h-4 w-4" />
                                </a>

                            </CardTitle>
                            <CardDescription>
                                <Badge className="mr-3" variant="secondary">#{mainCourse.difficulty}</Badge>
                                <Badge variant="secondary">#{mainCourse.tag}</Badge>
                            </CardDescription>
                        </CardHeader>
                        <CardContent>{mainCourse.speciality}</CardContent>
                    </>
                ) : <Spinner className="my-12" />
            }
        </Card>
        <Card x-chunk="vacancy-chunk-2">
          <CardHeader className="pb-2">
            <CardDescription className="flex flex-row items-center justify-between space-y-0 pb-0">
              Стоимость
              <Wallet className="h-6 w-6 text-muted-foreground" />
            </CardDescription>
              {
                  mainCourse ? (
                      <CardTitle className="text-4xl text-primary">{mainCourse.price} &#8381;</CardTitle>
                  ) : <Spinner className="my-5" />
              }
          </CardHeader>
          {/* <CardContent> */}
          {/*   <div className="text-xs text-muted-foreground">* ? доп текст ? *</div> */}
          {/* </CardContent> */}
        </Card>
        <Card x-chunk="vacancy-chunk-3">
          <CardHeader className="pb-2">
            <CardDescription className="flex flex-row items-center justify-between space-y-0 pb-0">
              Длительность
              <Clock className="h-6 w-6 text-muted-foreground" />
            </CardDescription>
              {
                  mainCourse ? (
                      <CardTitle className="text-4xl text-primary">{mainCourse.daysAmount}</CardTitle>
                  ) : <Spinner className="my-5" />
              }
          </CardHeader>
          {/* <CardContent> */}
          {/*   <div className="text-xs text-muted-foreground">* ? доп текст ? *</div> */}
          {/* </CardContent> */}
        </Card>
        <Card x-chunk="vacancy-chunk-4">
          <CardHeader className="pb-0">
            <CardDescription className="flex flex-row items-center justify-between space-y-0 pb-0">
              Совместимость
              <BookHeart className="h-6 w-6 text-muted-foreground" />
            </CardDescription>
          </CardHeader>
            {
                mainCourse ? (
                    <CardContent className="pb-4 pt-2"><Progress progress={0.90} /></CardContent>
                ) : <Spinner className="my-5" />
            }
        </Card>
            {
                simularCourses && simularCourses.length ? (
                    <Card className="sm:col-span-3" x-chunk="vacancy-chunk-1">
                        <CardHeader className="pb-2">
                            <CardTitle>Обратите внимание</CardTitle>
                            <CardDescription>Курсы, которые так же могут пригодиться</CardDescription>
                        </CardHeader>
                        <CardContent>
                            {
                                simularCourses.map((item: any) => (
                                    <div key={`course-${item.program.id}`} className="py-1">
                                        <a rel="noreferrer" href={item.program.url} className="hover:text-primary" target="_blank">
                                            {item.program.name}
                                        </a>
                                        <Badge className="ml-3" variant="secondary">#{item.program.tag}</Badge>
                                    </div>
                                ))
                            }
                        </CardContent>
                    </Card>
                ) : null
            }
      </div>
    </>
  );
};

export default VacancyPage;
