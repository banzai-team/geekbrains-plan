import React from "react";
import Head from "~/components/Head";
import Breadcrumbs from "~/components/Breadcrumbs";
import {Routes} from "~/pages/Router";
import {Card, CardDescription, CardHeader, CardTitle} from "~/components/ui/card";
import AddVacancyForm from "~/components/AddVacancyForm";

const AddFormPage: React.FC = () => {

    // TODO: add submit action
    const onSubmitForm = (data: any) => {
        console.log(data);
    }
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
                <CardHeader className="pb-5">
                    <CardTitle>Форма добавления</CardTitle>
                    <CardDescription>Добавьте файл вакансии или ссылку на вакансию</CardDescription>
                </CardHeader>
                <AddVacancyForm onSubmit={onSubmitForm}/>
            </Card>
        </>
    );
};

export default AddFormPage;
