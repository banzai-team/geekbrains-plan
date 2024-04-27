import React from 'react';
import { useFormik } from 'formik';
import { CardContent, CardFooter } from '~/components/ui/card';
import { Input } from '~/components/ui/input';
import { Button } from '~/components/ui/button';
import Dropzone from "~/components/Dropzone";
import {FileCheck2, X} from "lucide-react";

type AddVacancyFormProps = {
  onSubmit: (values: { link?: string; files?: any }) => void;
};

const AddVacancyForm: React.FC<AddVacancyFormProps> = ({ onSubmit }) => {
  const formik = useFormik<{
    link: string;
    files: {
      path: string;
      type: "file" | "folder";
      name: string;
      mimeType: string;
      data: string;
      size: number;
    }[] | null
  }>({
    initialValues: {
      link: '',
      files: null,
    },
    onSubmit: async (values) => onSubmit(values),
    // validationSchema,
  });

  return (
    <form onSubmit={formik.handleSubmit}>
      <CardContent className="grid gap-4 sm:grid-cols-1 md:grid-cols-2">
        <div>
          <div className="text-xs text-muted-foreground pb-1">Ссылка на вакансию</div>
          <Input placeholder="https://..." {...formik.getFieldProps('link')} disabled={!!formik.values.files} />
        </div>

        <div className="flex flex-col md:flex-row">
          <div className="py-5 gap-4 text-md text-muted-foreground/50 flex flex-row items-center md:py-0 md:pr-10 md:flex-col md:gap-2">
            <div className="w-full h-px bg-muted-foreground/20 md:w-px md:h-full" />
            или
            <div className="w-full h-px bg-muted-foreground/20 md:w-px md:h-full" />
          </div>
          <div>
            <div className="text-xs text-muted-foreground pb-1">Файл с вакансией (.pdf)</div>
            {
              formik.values.files
                  ? (
                      <div className="flex flex-row gap-4">
                        <div
                            style={{backgroundImage: 'url(/round.svg)'}}
                            className="bg-center bg-no-repeat bg-cover relative p-4 flex h-36 w-40 flex-col items-center justify-center rounded-md bg-zinc-100 md:p-10 md:h-48"
                        >
                          <Button className="absolute top-1 right-0" variant="ghost" size="sm"
                                  onClick={() => formik.setFieldValue("files", null)}>
                            <X className="text-destructive h-6 w-6 cursor-pointer hover:opacity-50" />
                          </Button>
                          <FileCheck2 className="h-8 w-8 text-primary" />
                        </div>
                        <div>
                          <div className="font-medium pt-2 whitespace-nowrap overflow-hidden overflow-ellipsis max-w-24 md:max-w-32 lg:max-w-52 xl:max-w-80">{formik.values.files[0].name}</div>
                          <div
                              className="text-xs text-muted-foreground pt-1">{(formik.values.files[0].size / 1024 / 1024).toFixed(2)}Мб
                          </div>
                        </div>
                      </div>
                  )
                  : (
                      <Dropzone onDrop={(acceptedFiles: any[]) => {
                        acceptedFiles.forEach((file) => {
                          const reader = new FileReader()

                          reader.onabort = () => console.log('file reading was aborted')
                          reader.onerror = () => console.log('file reading has failed')
                          reader.onload = () => {
                            // Do whatever you want with the file contents
                            // const binaryStr = reader.result
                            formik.setFieldValue("files", [file]);
                          }
                          reader.readAsArrayBuffer(file)
                        })
                      }} disabled={!!formik.values.link} acceptTypes={{'application/pdf': ['.pdf']}} />
                  )
            }
          </div>
        </div>
      </CardContent>

      <CardFooter className="justify-end">
        <Button type="submit" disabled={(!formik.values.link && !formik.values.files) || formik.isSubmitting}>
          Добавить {formik.isSubmitting}
        </Button>
      </CardFooter>
    </form>
  );
};

export default AddVacancyForm;
