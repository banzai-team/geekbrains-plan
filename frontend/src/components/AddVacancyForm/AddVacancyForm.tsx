import React from 'react';
import { useFormik } from 'formik';
import * as Yup from 'yup';
import { CardContent, CardFooter } from '~/components/ui/card';
import { Input } from '~/components/ui/input';
import { Button } from '~/components/ui/button';
import Dropzone from "~/components/Dropzone";
import {X} from "lucide-react";

const validationSchema = Yup.object({
  link: Yup.string().test(function (value) {
    const { files } = this.parent;
    if (!files) return value !== null;
    return true;
  }),
  files: Yup.string().test(function (value) {
    const { link } = this.parent;
    if (!link) return value !== null;
    return true;
  }),
});

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
          <div className="text-xs text-muted-foreground pb-1">Файл с вакансией (.pdf)</div>
          {
            formik.values.files
                ? (
                    <div>
                      FILE: {formik.values.files[0].name}
                      <Button variant="ghost" size="sm" onClick={() => formik.setFieldValue("files", null)}>
                        <X className="text-destructive h-4 w-4 cursor-pointer hover:opacity-50" />
                      </Button>
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

        <div>
          <div className="text-xs text-muted-foreground pb-1">Ссылка на вакансию</div>
          <Input placeholder="https://..." {...formik.getFieldProps('link')} disabled={!!formik.values.files} />
        </div>
      </CardContent>

      <CardFooter className="justify-end">
        <Button type="submit" disabled={!formik.values.link && !formik.values.files}>
          Добавить
        </Button>
      </CardFooter>
    </form>
  );
};

export default AddVacancyForm;
