import React from "react";
import Head from "~/components/Head";
import Breadcrumbs from "~/components/Breadcrumbs";
import {Card, CardDescription, CardHeader, CardTitle} from "~/components/ui/card";
import AddVacancyForm from "~/components/AddVacancyForm";
import {uploadFile, uploadLink} from "~/domain/api";
import {useMutation} from "react-query";
import { Routes } from '~/pages/Router';
import { useNavigate } from "react-router-dom";


const AddFormPage: React.FC = () => {
    const navigate = useNavigate();
    const sendFile = useMutation(uploadFile, {
        onSuccess: (data) => {
            setTimeout(() => {
                navigate(`${Routes.Vacancy}/${data.data.requestId}`);
            }, 1500);

        }
    });
    const sendLink = useMutation(uploadLink, {
        onSuccess: (data) => {
            setTimeout(() => {
                navigate(`${Routes.Vacancy}/${data.data.requestId}`);
            }, 1500);
        }
    });

    const onSubmitForm = async (data: { files?: any[], link?: string }) => {
        if (data.files) {
            await sendFile.mutateAsync({ file: data.files[0] });
        } else {
            await sendLink.mutateAsync(data)
        }

        // await new Promise((resolve) => setTimeout(() => {
        //     console.log("yessss");
        //     resolve(0);
        // }, 1500));
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
                    <CardDescription>Добавьте ссылку на вакансию или файл вакансии</CardDescription>
                </CardHeader>
                <AddVacancyForm onSubmit={onSubmitForm}  />
            </Card>
        </>
    );
};

export default AddFormPage;
