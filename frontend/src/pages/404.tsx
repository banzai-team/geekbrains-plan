import Head from '~/components/Head';
import { Card, CardContent } from '~/components/ui/card';
import Table from '~/components/Table';
import Empty from '~/components/Empty';
import React from 'react';
import {Link} from "react-router-dom";
import {Routes} from "~/pages/Router";
import {MoveLeft} from "lucide-react";
import Breadcrumbs from "~/components/Breadcrumbs";

const Page404: React.FC = () => {
  return (
    <>
      <Head title="The page is not found" />
        <Breadcrumbs
            path={[
                {
                    text: "Главная",
                    link: Routes.Root
                },
                {
                    text: "404",
                    link: Routes.Root
                },
            ]}
        />
      <Card>
        <CardContent>
          <Empty text="Такой страницы не существует">
              <Link to={Routes.Root} className="pt-10 font-medium hover:text-primary">
                  <MoveLeft className="inline pr-2"/>вернуться на главную
              </Link>
          </Empty>
        </CardContent>
      </Card>
    </>
  );
}

export default Page404;
