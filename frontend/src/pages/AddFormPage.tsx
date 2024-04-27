import React from "react";
import Head from "~/components/Head";
import Breadcrumbs from "~/components/Breadcrumbs";
import {Routes} from "~/pages/Router";
import {Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle} from "~/components/ui/card";
import {Input} from "~/components/ui/input";
import {Button} from "~/components/ui/button";

const AddFormPage: React.FC = () => {
    return (
        <>
            <Head title="Добавление вакансии" />
            <Breadcrumbs
                path={[
                    {
                        text: 'Главная',
                        link: Routes.Root,
                    },
                    {
                        text: `Добавление вакансии`,
                        link: `${Routes.Root}${Routes.New}`,
                    },
                ]}
            />
            <Card>
                <CardHeader className="pb-2">
                    <CardTitle>Ссылка</CardTitle>
                    <CardDescription></CardDescription>
                </CardHeader>
                <CardContent>
                    <Input></Input>
                </CardContent>
                <CardFooter>
                    <Button>Добавить</Button>
                </CardFooter>
            </Card>
        </>
    );
};

export default AddFormPage;