import React from 'react';
import {useParams} from "react-router";

import {
    Card,
    CardContent,
    CardDescription,
    CardHeader,
    CardTitle,
} from "~/components/ui/card"
import Head from '~/components/Head';
import Breadcrumbs from "~/components/Breadcrumbs";
import {Routes} from "~/pages/Router";

const VacancyPage: React.FC = () => {
    const {id = ""} = useParams();

    return (
        <>
            <Head title={`Вакансия ${id}`} />
            <Breadcrumbs
                path={[
                    {
                        text: "Главная",
                        link: Routes.Root
                    },
                    {
                        text: `Вакансия ${id}`,
                        link: `${Routes.Vacancy}/${id}`
                    },
                ]}
            />
            <Card>
                <CardHeader className="px-7">
                    <CardTitle>Вакансия классная</CardTitle>
                    <CardDescription>VK</CardDescription>
                </CardHeader>
                <CardContent>
                    data
                </CardContent>
            </Card>
        </>
    );
}

export default VacancyPage;
